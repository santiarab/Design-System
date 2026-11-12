import os
import sys
import time
import json
import subprocess
from datetime import timedelta
from faster_whisper import WhisperModel

FFMPEG_PATH = r"C:\Users\santi\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
INPUT_DIR = "OneDrive_1_11-11-2026"
OUTPUT_DIR = "transcripciones"

# Class recordings in chronological order (excluding the duplicate copy)
RECORDINGS = [
    {
        "id": "01_20260820_082357",
        "class_label": "Clase 01 - Parte 1",
        "date": "2026-08-20",
        "file": "Clase 01-20260820_082357-Grabación de la reunión.mp4"
    },
    {
        "id": "01_20260820_102934",
        "class_label": "Clase 01 - Parte 2",
        "date": "2026-08-20",
        "file": "Clase 01-20260820_102934-Grabación de la reunión.mp4"
    },
    {
        "id": "02_20260827_081937",
        "class_label": "Clase 02 - Completa",
        "date": "2026-08-27",
        "file": "Teams meeting-20260827_081937-Grabación de la reunión.mp4"
    },
    {
        "id": "03_20260903_081406",
        "class_label": "Clase 03 - Parte 1",
        "date": "2026-09-03",
        "file": "Clase 03-20260903_081406-Grabación de la reunión 1.mp4"
    },
    {
        "id": "03_20260903_101348",
        "class_label": "Clase 03 - Parte 2",
        "date": "2026-09-03",
        "file": "Clase 03-20260903_101348-Grabación de la reunión.mp4"
    },
    {
        "id": "05_20260917_081823",
        "class_label": "Clase 05 - Parte 1",
        "date": "2026-09-17",
        "file": "Clase 05-20260917_081823-Meeting Recording.mp4"
    },
    {
        "id": "05_20260917_101702",
        "class_label": "Clase 05 - Parte 2",
        "date": "2026-09-17",
        "file": "Clase 05-20260917_101702-Grabación de la reunión.mp4"
    },
    {
        "id": "06_20260924_082126",
        "class_label": "Clase 06 - Parte 1",
        "date": "2026-09-24",
        "file": "Clase 06-20260924_082126-Grabación de la reunión.mp4"
    },
    {
        "id": "06_20260924_114136",
        "class_label": "Clase 06 - Parte 2",
        "date": "2026-09-24",
        "file": "Clase 06-20260924_114136-Grabación de la reunión.mp4"
    },
    {
        "id": "07_20261001_082247",
        "class_label": "Clase 07 - Parte 1",
        "date": "2026-10-01",
        "file": "Clase Diseño-20261001_082247-Grabación de la reunión.mp4"
    },
    {
        "id": "07_20261001_103650",
        "class_label": "Clase 07 - Parte 2",
        "date": "2026-10-01",
        "file": "Clase Diseño-20261001_103650-Grabación de la reunión.mp4"
    },
    {
        "id": "08_20261008_082230",
        "class_label": "Clase 08 - Completa",
        "date": "2026-10-08",
        "file": "Clase-20261008_082230-Grabación de la reunión.mp4"
    },
    {
        "id": "09_20261015_082342",
        "class_label": "Clase 09 - Completa",
        "date": "2026-10-15",
        "file": "Clase 1510-20261015_082342-Grabación de la reunión.mp4"
    },
    {
        "id": "11_20261029_082145",
        "class_label": "Clase 11 - Completa",
        "date": "2026-10-29",
        "file": "Clase 11-20261029_082145-Grabación de la reunión.mp4"
    }
]

INITIAL_PROMPT = (
    "Clase universitaria de Diseño de Sistemas. "
    "Temas tratados: análisis y diseño de sistemas de software, diagramas UML, "
    "casos de uso, diagramas de clases, diagramas de secuencia, diagramas de estados, "
    "diagramas de actividades, arquitectura de software, patrones de diseño GoF, "
    "principios SOLID, GRASP, acoplamiento, cohesión, interfaces, herencia, polimorfismo, "
    "parcial, ejercicios prácticos, modelos de dominio, capa de presentación, negocio y datos."
)

def format_timestamp(seconds: float) -> str:
    td = timedelta(seconds=int(seconds))
    total_sec = int(seconds)
    hours = total_sec // 3600
    minutes = (total_sec % 3600) // 60
    secs = total_sec % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def log(msg: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] {msg}"
    print(full_msg, flush=True)
    with open("transcription_progress.log", "a", encoding="utf-8") as f:
        f.write(full_msg + "\n")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    log("=== INICIANDO PIPELINE DE TRANSCRIPCIÓN ===")
    log(f"Total grabaciones a procesar: {len(RECORDINGS)}")

    # Check pending files
    pending = []
    for rec in RECORDINGS:
        json_file = os.path.join(OUTPUT_DIR, f"{rec['id']}.json")
        txt_file = os.path.join(OUTPUT_DIR, f"{rec['id']}.txt")
        if os.path.exists(json_file) and os.path.exists(txt_file) and os.path.getsize(json_file) > 100:
            log(f"Ya transcrito: {rec['class_label']} ({rec['id']}) - OMITIENDO")
        else:
            pending.append(rec)

    if not pending:
        log("¡Todas las grabaciones ya han sido transcritas!")
        return

    log(f"Grabaciones pendientes: {len(pending)}")
    log("Cargando modelo Whisper 'base' en CPU (int8, 8 threads)...")
    t_load = time.time()
    model = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=8)
    log(f"Modelo cargado en {time.time() - t_load:.2f}s")

    for idx, rec in enumerate(pending, 1):
        rec_id = rec["id"]
        label = rec["class_label"]
        mp4_path = os.path.join(INPUT_DIR, rec["file"])
        wav_path = os.path.join(OUTPUT_DIR, f"temp_{rec_id}.wav")
        json_path = os.path.join(OUTPUT_DIR, f"{rec_id}.json")
        txt_path = os.path.join(OUTPUT_DIR, f"{rec_id}.txt")

        log(f"\n--- [{idx}/{len(pending)}] Procesando: {label} ({rec['file']}) ---")
        t_start = time.time()

        # Step 1: Extract 16kHz mono audio via ffmpeg
        log(f"Extrayendo audio a {wav_path}...")
        cmd = [
            FFMPEG_PATH, "-y",
            "-i", mp4_path,
            "-vn", "-ac", "1", "-ar", "16000",
            "-c:a", "pcm_s16le",
            wav_path
        ]
        ret = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ret.returncode != 0 or not os.path.exists(wav_path):
            log(f"ERROR: Falló extracción de audio para {rec['file']}")
            continue

        wav_size_mb = os.path.getsize(wav_path) / (1024 * 1024)
        log(f"Audio extraído ({wav_size_mb:.1f} MB). Iniciando transcripción Whisper...")

        # Step 2: Transcribe
        segments, info = model.transcribe(
            wav_path,
            language="es",
            beam_size=1,
            initial_prompt=INITIAL_PROMPT,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500)
        )

        all_segments = []
        txt_lines = []
        txt_lines.append(f"# {label} - {rec['date']}")
        txt_lines.append(f"Archivo de origen: {rec['file']}")
        txt_lines.append(f"Idioma detectado: {info.language} (probabilidad: {info.language_probability:.2f})")
        txt_lines.append(f"Duración estimada del audio: {format_timestamp(info.duration)}")
        txt_lines.append("\n---\n")

        seg_count = 0
        last_log_time = time.time()

        for seg in segments:
            seg_data = {
                "start": round(seg.start, 2),
                "end": round(seg.end, 2),
                "text": seg.text.strip()
            }
            all_segments.append(seg_data)
            time_str = f"[{format_timestamp(seg.start)} - {format_timestamp(seg.end)}]"
            txt_lines.append(f"{time_str} {seg.text.strip()}")
            seg_count += 1

            if time.time() - last_log_time > 15:
                elapsed = time.time() - t_start
                current_audio_pos = seg.end
                speed = current_audio_pos / max(1.0, elapsed)
                pct = (current_audio_pos / max(1.0, info.duration)) * 100
                log(f"  > Progreso: {format_timestamp(current_audio_pos)} / {format_timestamp(info.duration)} ({pct:.1f}%) | Vel: {speed:.1f}x real-time")
                last_log_time = time.time()

        # Step 3: Save results
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({
                "metadata": rec,
                "duration": info.duration,
                "segments": all_segments
            }, f, ensure_ascii=False, indent=2)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(txt_lines))

        # Cleanup temp audio
        if os.path.exists(wav_path):
            os.remove(wav_path)

        total_elapsed = time.time() - t_start
        overall_speed = info.duration / max(1.0, total_elapsed)
        log(f"Completado {label}: {seg_count} segmentos en {total_elapsed/60:.2f} min ({overall_speed:.1f}x real-time)")
        log(f"Guardado en {txt_path} y {json_path}")

    log("\n=== TODAS LAS TRANSCRIPCIONES FINALIZARON CON ÉXITO ===")

if __name__ == "__main__":
    main()
