# 04 — METODOLOGÍA DE RESOLUCIÓN DESDE CERO, PARCIALES 2026 RESUELTOS Y BANCO TEÓRICO

> **Propósito de este documento:** Brindarte el **método exacto paso a paso** para enfrentar la hoja en blanco el día del parcial, seguido de la **resolución completa y comentada de los 3 Parciales 2026 de la cátedra** (*Veterinaria PetCare*, *Agencia de Viajes*, *Refugio de Mascotas*), las resoluciones de **Diagramas de Estados de Finales**, y el **compendio de Teoría de Examen** (Calidad, UX, SOA/Microservicios, Testing y STR).

---

## PARTE 1: EL MÉTODO CRONOMETRADO DE 120 MINUTOS PARA RESOLVER EL PARCIAL DESDE CERO

Un error fatal en el parcial de Diseño de Sistemas es dibujar primero todo el Diagrama de Clases en tinta, pasar luego al Diagrama de Secuencia, y descubrir a mitad de la secuencia que te faltan métodos o relaciones en las clases. Para que eso **no te pase**, aplicá este protocolo de 6 pasos:

### Paso 1 (Minutos 0 a 15): Lectura con los 3 Colores y Recorte de Alcance
1. Leé el enunciado completo y mirá la interfaz gráfica y los diagramas base (Componentes y/o Estados) que vienen impresos en la hoja.
2. Marcá según el código de colores de la profesora (`EJEMPLO-Practica-Teoria-version-10.pdf`, Págs. 5–6 y 8):
   - **Sustantivos con identidad propia (Amarillo)** → Clases del Dominio.
   - **Funcionalidad / Comportamiento y verbos (Verde)** → Métodos.
   - **Datos simples o clases secundarias (Celeste)** → Atributos.
3. Identificá los **grandes módulos funcionales** del enunciado (alineados con el Diagrama de Componentes) para definir tus **Controladores (`C_...`)**, respetando estrictamente el tope del examen (**máximo 4 controladores** en los parciales 2026).
4. Leé el punto del **Diagrama de Secuencia** para saber exactamente **qué escenario te piden secuenciar** (ahí es donde vas a poner mayor nivel de detalle en firmas de métodos y parámetros).
5. Leé el punto de **Patrones GoF** y elegí tus **2 patrones GoF de distinta categoría** (recordando la restricción de **no usar Singleton ni Facade**) antes de pasar en limpio el Diagrama de Clases, así ya los dibujás integrados en la Hoja 1.

### Paso 2 (Minutos 15 a 45): Esqueleto del Diagrama de Clases en Hoja 1 (Sin cerrar las cajas por abajo)
1. En la **Hoja 1**, dibujá arriba los **4 `Controllers`** (`C_...`).
2. Debajo, ubicá los contenedores/nóminas (`Nomina...` solo para búsquedas globales con asociación simple `───`, e `HistoriaClinica` para las colecciones propias) y las **Clases del Dominio** con sus atributos privados (`-`) y asociaciones sólidas con **multiplicidad** (`1`, `0..*`, `1..*`), **agregaciones (`◇`)**, **composiciones (`◆`)** y **herencias (`─▷`)**. Si el parcial trae un **Diagrama de Estados impreso**, integrá todos sus eventos como métodos de esa clase y sus estados.
3. **TRUCO DE ORO PARA EL EXAMEN EN PAPEL:** Al dibujar cada clase en la Hoja 1, **dejá abierto el borde inferior del compartimento de métodos** (no cierres la línea horizontal de abajo de la caja todavía). ¿Por qué? Porque cuando hagas el Diagrama de Secuencia en el Paso 3, cada mensaje nuevo que descubras lo vas a ir anotando inmediatamente adentro de la caja de esa clase en la Hoja 1. ¡Al terminar el examen cerrás las cajas y tenés **100% de consistencia garantizada**!

### Paso 3 (Minutos 45 a 75): Escenario y Diagrama de Secuencia en Hoja 2 (En simultáneo con los métodos del DC)
1. En la parte superior de la **Hoja 2**, escribí el **Escenario concreto** con los valores puntuales del enunciado.
2. Trazá las líneas de vida de izquierda a derecha empezando por el **`:C_Controller`** (¡sin Actor!).
3. Por **cada flecha de mensaje `─── metodo(param) ──►`** que dibujes llegando a la línea de vida de un objeto `:ClaseX`:
   - Inmediatamente mirá tu **Hoja 1** y verificá que `+metodo(param)` esté escrito dentro de `ClaseX` y que exista la relación de asociación o dependencia entre el emisor y `ClaseX` (recordando que la visibilidad local no se dibuja en el Diagrama de Clases).
4. Usá `create(...)` para todo objeto nuevo que nazca en ese flujo (`:Consulta`, `:Diagnostico`, `:VacunaAplicada`, `:Receta`, `:Recordatorio`, `:DenunciaExotico`, `:Pago`).

### Paso 4 (Minutos 75 a 95): Inyección de los 2 Patrones GoF en Hoja 1 y Redacción en Hoja Adjunta
1. Dibujá en la **Hoja 1** las interfaces (`<<interface>>`) y clases concretas de los **2 Patrones GoF** conectadas a las clases de tu dominio (podés resaltarlas con un recuadro punteado o color indicando `Patrón 1`, `Patrón 2`).
2. En la hoja correspondiente, redactá los incisos `a)`, `b)`, `c)` y `d)` de cada patrón GoF usando la plantilla de `03_PATRONES_GRASP_Y_GOF_APLICADOS.md` (y si el parcial pide modificar o mejorar el **Diagrama de Componentes**, dibujalo en su propia hoja numerada).

### Paso 5 (Minutos 95 a 110): Redacción de las Justificaciones GRASP
1. Redactá las justificaciones de **Experto en Información**, **Creador**, **Bajo Acoplamiento / Alta Cohesión** (y **Controlador**), citando **nombres exactos de clases y métodos de tu Diagrama de Clases**.

### Paso 6 (Minutos 110 a 120): Auditoría Final con los 12 Mandamientos
- Cerrá la parte inferior de las cajas de clases, verificá que todas las hojas estén numeradas y hacé el chequeo cruzado de métodos entre Secuencia, Estados y Clases.

---

## PARTE 2: RESOLUCIÓN COMPLETA DEL PARCIAL 1C 2026 (COMISIÓN 4300 — ING. ANALÍA MARÍN)
### CASO: RED DE VETERINARIAS "PETCARE" (`Parciales/1. [Parcial 1][1C2026][4300][Analia][][].pdf`)

> **Fuente verificada visualmente:** Escaneo original de 2 páginas de `Parciales/1. [Parcial 1][1C2026][4300][Analia][][].pdf` + corrección en vivo de la Ing. Analía Marín y el JTP Alejandro en la **Clase 09 (`09_20261015_082342.txt`, desde `[01:55:00]` hasta `[03:45:00]`)**.

#### 2.1. Enunciado Original Verificado y Elementos Impresos en la Hoja del Examen
1. **Dominio del Problema (`[EXIGENCIA EXPLÍCITA DEL ENUNCIADO]`):**
   - **"PetCare"** es una **red de veterinarias distribuida en distintas ciudades**.
   - Un **Usuario (dueño)** se registra en el sistema y registra a sus **Mascotas** (cada mascota posee una única **Historia Clínica**).
   - El usuario puede **buscar sucursales de `Veterinaria` por ubicación y horarios**, consultar los **`Profesional`es** que atienden en cada veterinaria (con su especialidad y días/horarios de atención) y **reservar un `Turno`** para una mascota con un profesional en una sucursal.
   - Durante la **Atención Veterinaria**, el profesional accede a la **Historia Clínica** de la mascota y registra la **`Consulta`** del día:
     - Actualiza el **peso** de la mascota.
     - Registra el **`Diagnóstico`** y el **`Tratamiento`** (opcional).
     - Puede emitir una **`Receta`** (medicamento, dosis/indicación), ordenar un **`Estudio`** y/o registrar la aplicación de una **`VacunaAplicada`** (`Vacuna`).
     - Puede programar un **`Recordatorio`** futuro (con fecha y motivo, ej. próxima visita o refuerzo) para que el sistema **notifique al dueño por WhatsApp o Mail**.
   - **Nota manuscrita en el borde superior del examen:** **`max: 4 controladores`**.
2. **Diagramas Base Impresos en la Hoja del Examen (`[EXIGENCIA EXPLÍCITA DEL ENUNCIADO]`):**
   - **Diagrama de Componentes Inicial:** Muestra los bloques `gestion/usuario`, `mascota`, `turno`, `veterinaria/profesional`, `AtencionVeterinario` (conectado a `historialClinico`) y `notificaciones`.
   - **Diagrama de Estados de `Consulta Veterinaria`:**
     ```
     ● ── registrarConsulta() ──► [ Registrada ] ── registrarDiagnostico() ──► [ Diagnosticada ] ── cerrarConsulta() ──► [ Cerrada ] ──► ◉
     ```
   - **Captura de Pantalla y Escenario Exacto del Punto 2 (`"Guardar Consulta"`):**
     - **Fecha:** `06/06/2026`.
     - **Caso:** El veterinario atiende **por primera vez** a **`Homero`**, un **gato siamés de 13 años**, cuyo peso actual es **`5.2 kg`**, y su dueño es **`Juan Pérez`**.
     - **Acciones cargadas en la pantalla antes de presionar el botón `Guardar`:**
       1. Se le da **1 vacuna**: `"Rabia"`.
       2. Se registra su **peso**: `5.2 kg`.
       3. Se le da **1 receta** para tomar pastillas desparasitarias: `"Pastillas desparasitarias"`, `"1 comprimido"`.
       4. Se registra **`Diagnóstico`**: `"SANO"`.
       5. **`Tratamiento`**: vacío (`""`).
       6. Se configura **`Recordatorio`**: `"volver a verlo en 1 año"` (fecha `01/06/2027`).
     - Al hacer clic en el botón **`Guardar`**, llega el mensaje **`"Guardar Consulta"`**, el cual debe crear y asociar los objetos correspondientes (`Consulta`, `Diagnostico`, `Receta`, `VacunaAplicada`, `Recordatorio`, etc.) y agregarlos a la `HistoriaClinica` de la mascota.
3. **Lo que pide la Consigna (`Se Pide`):**
   - **Punto 1:** Construir el **Diagrama de Clases** completo que soporte todos los requerimientos e integre el Diagrama de Estados dado (aplicando **máximo 4 controladores**), e identificar y justificar **al menos 2 patrones GRASP**.
   - **Punto 2:** Construir el **Diagrama de Secuencia** para el escenario dado del gato `Homero` al presionar `"Guardar Consulta"`.
   - **Punto 3:** Aplicar **2 patrones GoF de diferente categoría** sobre el Diagrama de Clases, respondiendo: a) Categoría y nombre, b) Problema que resuelve, c) Justificación, d) Clases reutilizadas y nuevas.

---

### PUNTO 1 (PARCIAL PETCARE): DIAGRAMA DE CLASES DE DISEÑO (MÁXIMO 4 CONTROLLERS) + GRASP

#### 1.A. Diferenciación entre Exigencias Explícitas y Decisiones de Diseño
- **`[EXIGENCIA EXPLÍCITA DEL ENUNCIADO]`:** Clases `Veterinaria`, `Profesional`, `Usuario`, `Mascota`, `Turno`, `HistoriaClinica`, `Consulta` (con los métodos del Diagrama de Estados: `+registrarConsulta()`, `+registrarDiagnostico()`, `+cerrarConsulta()`), `Diagnostico`, `Tratamiento`, `Receta`, `Estudio`, `VacunaAplicada` (`Vacuna`), `Recordatorio` y envío de notificaciones por WhatsApp/Mail. Tope máximo de **4 controladores**.
- **`[DECISIÓN DE DISEÑO / INTERPRETACIÓN VALIDADA EN CLASE 09]`:**
  1. **Los 4 Controladores (`max: 4 controladores`):**
     - `C_UsuarioMascota`: Registro y búsqueda de usuarios (dueños) y sus mascotas.
     - `C_VeterinariaTurno`: Búsqueda de sucursales de `Veterinaria` por ubicación/horario, profesionales y reserva de `Turno`.
     - `C_AtencionVeterinaria`: Recibe el evento `"Guardar Consulta"` (`+guardarConsulta(...)`), coordina la actualización de la mascota, la creación de la `Consulta` en la `HistoriaClinica` y la programación del `Recordatorio`.
     - `C_Notificacion`: Gestiona el disparo de recordatorios y avisos a través de los canales externos (WhatsApp / Mail).
  2. **Uso de `Nomina` vs. Contenedor propio (`Clase 09 [02:38:03]`):** Se incluye `NominaMascotas` (o `NominaUsuarios`) unida con **asociación simple (`───`)** para buscar globalmente a `Homero` por su ID al guardar la consulta, mientras que todas las consultas de `Homero` se guardan dentro de su propia **`HistoriaClinica`** (composición `1` a `1` con `Mascota`), sin inventar una "Nómina de Consultas".
  3. **Los 2 Patrones GoF integrados:**
     - **Patrón GoF 1 (Comportamiento) — `State`:** Aplicado directamente para modelar el **Diagrama de Estados de `Consulta Veterinaria`** que viene impreso en el parcial (`<<interface>> IEstadoConsulta` implementado por `EstadoRegistrada`, `EstadoDiagnosticada`, `EstadoCerrada`). *(Nota: También es 100% válido usar `Observer` para los recordatorios, como discutió la profesora en Clase 09).*
     - **Patrón GoF 2 (Estructural) — `Adapter`:** Aplicado para desacoplar el envío de notificaciones de `Recordatorio` hacia las APIs externas de **WhatsApp** (`AdaptadorWhatsApp` → `API_WhatsAppCloud`) y **Mail** (`AdaptadorEmail` → `ServidorSMTPMail`) detrás de la interfaz `<<interface>> ICanalNotificacion`.

#### 1.B. Diagrama de Clases Completo (`PetCare` — Com. 4300)

```
========================================================================================================================
                                     CAPA DE CONTROLADORES (MÁXIMO 4 CONTROLLERS)
========================================================================================================================
 ┌────────────────────────────────────┐ ┌────────────────────────────────────┐ ┌────────────────────────────────────────────────────────┐ ┌────────────────────────────────────┐
 │          C_UsuarioMascota          │ │         C_VeterinariaTurno         │ │                 C_AtencionVeterinaria                  │ │           C_Notificacion           │
 ├────────────────────────────────────┤ ├────────────────────────────────────┤ ├────────────────────────────────────────────────────────┤ ├────────────────────────────────────┤
 │ - nominaUsuarios: NominaUsuarios   │ │ - redVeterinarias: NominaVeterinar │ │ - nominaMascotas: NominaMascotas                       │ │ - canales: List<ICanalNotificacion>│
 │ - nominaMascotas: NominaMascotas   │ ├────────────────────────────────────┤ ├────────────────────────────────────────────────────────┤ ├────────────────────────────────────┤
 ├────────────────────────────────────┤ │ + buscarVeterinaria(zona, horario) │ │ + guardarConsulta(idMascota, idProf, fecha, peso,      │ │ + procesarRecordatoriosDelDia(f)   │
 │ + registrarUsuario(datos): Usuario │ │ + reservarTurno(idMasc, idVet,     │ │     textoDiag, textoTrat, medReceta, dosisReceta,      │ │ + enviarAviso(rec: Recordatorio)   │
 │ + registrarMascota(idU, d): Mascota│ │     idProf, fechaHora): Turno      │ │     nombreVacuna, motivoRecordat, fechaRecordat): void │ └─────────────────┬──────────────────┘
 └─────────┬────────────────┬─────────┘ └─────────────────┬──────────────────┘ └────────────────────────────┬───────────────────────────┘                   │
           │                │                             │                                                 │                                               │
           ▼                ▼                             ▼                                                 ▼                                               ▼
========================================================================================================================
                                      NÓMINAS (ASOCIACIÓN SIMPLE) Y RED DE VETERINARIAS
========================================================================================================================
 ┌────────────────────────────────────┐ ┌────────────────────────────────────┐ ┌────────────────────────────────────┐          ┌──────────────────────────────────────────┐
 │           NominaUsuarios           │ │          NominaVeterinarias        │ │           NominaMascotas           │          │               <<interface>>              │
 ├────────────────────────────────────┤ ├────────────────────────────────────┤ ├────────────────────────────────────┤          │            ICanalNotificacion            │
 │ - usuarios: List<Usuario>          │ │ - sucursales: List<Veterinaria>    │ │ - mascotas: List<Mascota>          │          │     [PATRÓN GOF 2: ADAPTER (Estruct.)]   │
 ├────────────────────────────────────┤ ├────────────────────────────────────┤ ├────────────────────────────────────┤          ├──────────────────────────────────────────┤
 │ + buscarUsuario(id): Usuario       │ │ + filtrarPorUbicacionYHorario(     │ │ + buscarMascota(idMasc): Mascota   │          │ + enviarMensaje(dest: String,            │
 │ + agregarUsuario(u: Usuario): void │ │     ubic, hora): List<Veterinaria> │ │ + agregarMascota(m: Mascota): void │          │     asunto: String, cuerpo: String): Bool│
 └─────────────────┬──────────────────┘ └─────────────────┬──────────────────┘ └─────────────────┬──────────────────┘          └─────────────────────△────────────────────┘
                   │ 1                                    │ 1                                    │ 1 (Asociación simple,                             ┆
                   │                                      │                                      │    NO composición)                  ┌─────────────┴──────────────┐
                   │ 0..*                                 │ 1..*                                 │ 0..*                        ┌───────┴──────────────┐    ┌────────┴─────────────┐
                   ▼                                      ▼                                      ▼                             │  AdaptadorWhatsApp   │    │    AdaptadorEmail    │
 ┌────────────────────────────────────┐ ┌────────────────────────────────────┐ ┌────────────────────────────────────┐          ├──────────────────────┤    ├──────────────────────┤
 │              Usuario               │ │            Veterinaria             │ │              Mascota               │          │ - apiWA: APIWhatsApp │    │ - smtp: ServidorSMTP │
 ├────────────────────────────────────┤ ├────────────────────────────────────┤ ├────────────────────────────────────┤          ├──────────────────────┤    ├──────────────────────┤
 │ - idUsuario: int                   │ │ - idVeterinaria: int               │ │ - idMascota: int                   │          │ + enviarMensaje(...) │    │ + enviarMensaje(...) │
 │ - nombreApellido: String           │ │ - nombreSucursal: String           │ │ - nombre: String                   │          └───────────┬──────────┘    └───────────┬──────────┘
 │ - telefonoWhatsApp: String         │ │ - direccion: String                │ │ - especie: String                  │                      ▼                           ▼
 │ - email: String                    │ │ - ciudad: String                   │ │ - raza: String                     │          ┌──────────────────────┐    ┌──────────────────────┐
 ├────────────────────────────────────┤ │ - horarioAtencion: String          │ │ - edad: int                        │          │     APIWhatsApp      │    │     ServidorSMTP     │
 │ + agregarMascota(m: Mascota): void │ ├────────────────────────────────────┤ │ - pesoActual: float                │          ├──────────────────────┤    ├──────────────────────┤
 │ + getTelefonoWhatsApp(): String    │ │ + estaAbiertaEn(hora): Boolean     │ ├────────────────────────────────────┤          │ + sendWAMessageJSON()│    │ + sendMailMIME()     │
 │ + getEmail(): String               │ │ + obtenerProfesionales(): List     │ │ + actualizarPeso(nuevoPeso): void  │          └──────────────────────┘    └──────────────────────┘
 └─────────────────┬──────────────────┘ └─────────┬────────────────┬─────────┘ │ + obtenerHistoriaClinica():        │
                   │ 1                            │ 1              │ 1         │     HistoriaClinica                │
                   │ esDueñoDe                    │ trabajanEn     │ atiende   └─────────┬────────────────┬─────────┘
                   └──────────────────────────────┼────────────────┼───────────► 1..*    │ 1              │ 1
                                                  │ 1..*           │ 0..*                │                ◆ posee (1 a 1 exclusiva)
                                                  ▼                ▼                     │                │ 1
                                        ┌──────────────────┐ ┌──────────────────┐        │                ▼
                                        │   Profesional    │ │      Turno       │        │   ┌────────────────────────────────────────────────────────┐
                                        ├──────────────────┤ ├──────────────────┤ 0..*   │   │                    HistoriaClinica                     │
                                        │ - idProf: int    │ │ - idTurno: int   │◄───────┘   ├────────────────────────────────────────────────────────┤
                                        │ - matricula: Str │ │ - fechaHora: Date│            │ - nroHistoria: int                                     │
                                        │ - nombre: String │ │ - estado: String │            │ - fechaApertura: Date                                  │
                                        │ - especialidad   │ ├──────────────────┤            ├────────────────────────────────────────────────────────┤
                                        │ - diasHorarios   │ │ + confirmar()    │            │ + crearYAgregarConsulta(prof, fecha, peso, textoDiag,  │
                                        ├──────────────────┤ │ + cancelar()     │            │     textoTrat, medRec, dosis, nomVac, motRec, fRec):   │
                                        │ + atiendeEn(f):B │ └────────┬─────────┘            │     Consulta                                           │
                                        └─────────▲────────┘          │ *                    │ + agregarRecordatorio(r: Recordatorio): void           │
                                                  │ 1                 │ asignadoA            └─────────────┬──────────────────────────────┬───────────┘
                                                  └───────────────────┴──────────────────────┐             │ 1                            │ 1
                                                                      │ 1                    │             ◆ contiene                     ◆ agenda
                                                                      │                      │        0..* │                         0..* │
                                                                      │                      ▼             ▼                              ▼
========================================================================================================================   ┌────────────────────────────────────┐
                             CORE CLÍNICO: CONSULTA + INTEGRACIÓN DEL DIAGRAMA DE ESTADOS (GOF STATE)                      │            Recordatorio            │
========================================================================================================================   ├────────────────────────────────────┤
 ┌────────────────────────────────────────────────────────┐         ┌──────────────────────────────────────────────────┐   │ - idRecordatorio: int              │
 │                        Consulta                        │ 1     1 │                   <<interface>>                  │   │ - motivo: String                   │
 │        (Integra el Diagrama de Estados impreso)        ├────────►│                 IEstadoConsulta                  │   │ - fechaProgramada: Date            │
 ├────────────────────────────────────────────────────────┤         │     [PATRÓN GOF 1: STATE (Comportamiento)]       │   │ - enviado: Boolean                 │
 │ - idConsulta: int                                      │         ├──────────────────────────────────────────────────┤   ├────────────────────────────────────┤
 │ - fecha: Date                                          │         │ + registrarConsulta(c: Consulta): void           │   │ + correspondeEnviar(f: Date): Bool │
 │ - pesoRegistrado: float                                │         │ + registrarDiagnostico(c: Consulta, d: String)   │   │ + marcarEnviado(): void            │
 │ - estadoActual: IEstadoConsulta                        │         │ + cerrarConsulta(c: Consulta): void              │   └────────────────────────────────────┘
 ├────────────────────────────────────────────────────────┤         └────────────────────────△─────────────────────────┘
 │ + registrarConsulta(): void                            │                                  ┆
 │ + registrarDiagnostico(textoDiag: String): Diagnostico │            ┌─────────────────────┼─────────────────────┐
 │ + registrarTratamiento(textoTrat: String): Tratamiento │ ┌──────────┴───────────┐ ┌───────┴──────────────┐ ┌────┴─────────────────┐
 │ + emitirReceta(medicamento: String,                    │ │   EstadoRegistrada   │ │ EstadoDiagnosticada  │ │    EstadoCerrada     │
 │     dosis: String): Receta                             │ ├──────────────────────┤ ├──────────────────────┤ ├──────────────────────┤
 │ + aplicarVacuna(nombreVac: String, f: Date):           │ │ + registrarConsulta()│ │ + registrarDiagnos() │ │ + cerrarConsulta()   │
 │     VacunaAplicada                                     │ │ + registrarDiagnos() │ │ + cerrarConsulta()   │ │   (Estado Final)     │
 │ + ordenarEstudio(tipoEstudio: String): Estudio         │ └──────────────────────┘ └──────────────────────┘ └──────────────────────┘
 │ + cerrarConsulta(): void                               │
 │ + cambiarEstado(nuevoEst: IEstadoConsulta): void       │
 └──┬──────────────┬──────────────┬──────────────┬────────┴─────┐
    │ 1            │ 1            │ 1            │ 1            │ 1
    ◆              ◆              ◆              ◆              ◆
    │ 1            │ 0..1         │ 0..1         │ 0..*         │ 0..*
    ▼              ▼              ▼              ▼              ▼
 ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐ ┌──────────────┐
 │ Diagnostico  │ │ Tratamiento  │ │    Receta    │ │  VacunaAplicada  │ │   Estudio    │
 ├──────────────┤ ├──────────────┤ ├──────────────┤ ├──────────────────┤ ├──────────────┤
 │ - descripcion│ │ - indicacion │ │ - medicamento│ │ - nombreVacuna   │ │ - tipoEstudio│
 │ - fecha: Date│ │ - duracion   │ │ - dosis      │ │ - fechaAplicacion│ │ - resultado  │
 └──────────────┘ └──────────────┘ └──────────────┘ └──────────────────┘ └──────────────┘
```

#### 1.C. Justificación de los Patrones GRASP en el Diseño (`PetCare`)
1. **Controlador (*Controller*):** Se aplica en las 4 clases controladoras **`C_UsuarioMascota`**, **`C_VeterinariaTurno`**, **`C_AtencionVeterinaria`** y **`C_Notificacion`** (respetando el máximo de 4 controladores de la consigna). En particular, **`C_AtencionVeterinaria`** recibe el evento externo **`+guardarConsulta(...)`** cuando el veterinario presiona el botón `"Guardar"`, desacoplando la pantalla de las clases de dominio y delegando la actualización de la mascota y el registro clínico.
2. **Experto en Información (*Information Expert*):** Se aplica en **`Mascota`** con los métodos **`+actualizarPeso(nuevoPeso)`** y **`+obtenerHistoriaClinica()`** (porque `Mascota` conoce su propio atributo `-pesoActual` y posee la referencia directa `1 a 1` a su `HistoriaClinica`), y en **`HistoriaClinica`** con el método **`+crearYAgregarConsulta(...)`**, ya que es la clase experta que contiene y administra el historial completo de consultas y recordatorios de esa mascota.
3. **Creador (*Creator*):** Se aplica en **`HistoriaClinica`** al instanciar (`create`) a **`Consulta`** y a **`Recordatorio`** (porque `HistoriaClinica` agrega y contiene por composición todas las consultas y recordatorios de la mascota), y a su vez en **`Consulta`** al instanciar (`create`) a **`Diagnostico`**, **`Receta`** y **`VacunaAplicada`** (mediante `+registrarDiagnostico()`, `+emitirReceta()` y `+aplicarVacuna()`), ya que `Consulta` contiene de manera exclusiva los elementos clínicos generados en ese acto médico y recibe los datos de inicialización.
4. **Bajo Acoplamiento y Alta Cohesión (*Low Coupling & High Cohesion*):** `C_AtencionVeterinaria` no instancia directamente a `Diagnostico`, `Receta` ni `VacunaAplicada`, sino que delega en `HistoriaClinica` y `Consulta`, manteniendo bajo el acoplamiento del controlador y alta la cohesión de `Profesional` (que solo guarda sus datos profesionales sin convertirse en una clase gestora).

---

### PUNTO 2 (PARCIAL PETCARE): ESCENARIO Y DIAGRAMA DE SECUENCIA DE `"Guardar Consulta"`

#### 2.A. Escenario Concreto (Datos Exactos del Enunciado Impreso)
> **Escenario (06/06/2026):** El profesional veterinario (`idProf = 7`) atiende por primera vez a **`Homero`** (`idMascota = 10`, gato siamés de 13 años, dueño **`Juan Pérez`**). Registra su peso actual de **`5.2 kg`**, aplica **1 vacuna** (`"Rabia"`), emite **1 receta** (`"Pastillas desparasitarias"`, `"1 comprimido"`), carga el **Diagnóstico** `"SANO"`, deja el **Tratamiento** vacío (`""`), y programa **1 Recordatorio** `"volver a verlo en 1 año"` para el `"01/06/2027"`. Presiona el botón `"Guardar"` disparando el mensaje **`guardarConsulta(...)`**.

#### 2.B. Diagrama de Secuencia Completo (100% Trazable con el Diagrama de Clases y el Diagrama de Estados)

```
                     :C_AtencionVeterinaria  :NominaMascotas    m:Mascota      hc:HistoriaClinica
                               │                    │               │                   │
 ●──guardarConsulta───────────►┌─┐                  │               │                   │
   (idM=10, idProf=7,          │ ├─buscarMascota───►┌─┐             │                   │
    f="06/06/2026", peso=5.2,  │ │ (10)             │ │             │                   │
    diag="SANO", trat="",      │ │◄─── m (Homero) ──└─┘             │                   │
    med="Pastillas desparasit",│ │                                  │                   │
    dosis="1 comprimido",      │ ├─actualizarPeso(5.2)─────────────►┌─┐                 │
    vac="Rabia",               │ │◄────── ok ───────────────────────└─┘                 │
    motRec="volver a verlo     │ ├─obtenerHistoriaClinica()────────►┌─┐                 │
    en 1 año", fRec="01/06/27")│ │◄────── hc ───────────────────────└─┘                 │
                               │ │                                                      │
                               │ ├─crearYAgregarConsulta(prof, "06/06/2026", 5.2, ...)─►┌─┐
                               │ │                                                      │ ├─create(prof, "06/06/26", 5.2)─►┌──────────┐
                               │ │                                                      │ │                                │c:Consulta│
                               │ │                                                      │ │                                └────┬─────┘
                               │ │                                                      │ ├─registrarConsulta()────────────────►┌─┐ (Estado: Registrada)
                               │ │                                                      │ │◄────── ok ──────────────────────────└─┘
                               │ │                                                      │ │                                     │
                               │ │                                                      │ ├─registrarDiagnostico("SANO")───────►┌─┐
                               │ │                                                      │ │                                     │ ├─create("SANO")─►┌─────────────┐
                               │ │                                                      │ │                                     │ │                 │d:Diagnostico│
                               │ │                                                      │ │                                     │ │                 └─────────────┘
                               │ │                                                      │ │                                     │ ├─cambiarEstado(EstadoDiagnosticada)
                               │ │                                                      │ │◄────── d ───────────────────────────└─┘
                               │ │                                                      │ │                                     │
                               │ │                                                      │ ├─aplicarVacuna("Rabia","06/06/26")──►┌─┐
                               │ │                                                      │ │                                     │ ├─create("Rabia")─►┌─────────────────┐
                               │ │                                                      │ │                                     │ │                  │va:VacunaAplicada│
                               │ │                                                      │ │◄────── va ──────────────────────────└─┘                  └─────────────────┘
                               │ │                                                      │ │                                     │
                               │ │                                                      │ ├─emitirReceta("Pastillas...",        │
                               │ │                                                      │ │              "1 comprimido")───────►┌─┐
                               │ │                                                      │ │                                     │ ├─create(...)─────►┌──────────┐
                               │ │                                                      │ │                                     │ │                  │ r:Receta │
                               │ │                                                      │ │◄────── r ───────────────────────────└─┘                  └──────────┘
                               │ │                                                      │ │                                     │
                               │ │                                                      │ ├─cerrarConsulta()───────────────────►┌─┐ (Estado: Cerrada)
                               │ │                                                      │ │◄────── ok ──────────────────────────└─┘
                               │ │                                                      │ │
                               │ │                                                      │ ├─agregarRecordatorio(...)───────────►┌─┐
                               │ │                                                      │ │ ├─create("volver a verlo en 1 año", │ ├─►┌──────────────┐
                               │ │                                                      │ │ │        "01/06/2027")              │ │  │rec:Recordator│
                               │ │                                                      │ │◄────────── rec ─────────────────────└─┘  └──────────────┘
                               │ │◄────────────────── c:Consulta ───────────────────────└─┘
 ◄── consultaGuardadaOK(c) ────└─┘
```
*(Nota sobre Tratamiento vacío: Como en el escenario del enunciado el campo Tratamiento está vacío `""`, no se ejecuta `registrarTratamiento` en este escenario concreto, o bien puede encerrarse en un fragmento `opt [textoTrat != vacio]`).*

---

### PUNTO 3 (PARCIAL PETCARE): APLICACIÓN Y JUSTIFICACIÓN DE 2 PATRONES GOF DE DIFERENTE CATEGORÍA

#### Patrón GoF N° 1: `State` (Categoría: Comportamiento)
- **a) Categoría y Nombre:** Patrón de **Comportamiento** — **State (Estado)**.
- **b) Problema de diseño que resuelve en el caso:** El enunciado provee el Diagrama de Estados de `Consulta Veterinaria` (`Registrada` → `Diagnosticada` → `Cerrada`). Una consulta solo puede cerrarse si previamente fue diagnosticada, y una vez `Cerrada` no debe permitir modificar el diagnóstico ni agregar nuevas recetas o vacunas. Implementar esto con múltiples condicionales `if/switch` sobre un String dentro de `Consulta` violaría el principio Abierto/Cerrado y la Alta Cohesión.
- **c) Por qué es adecuado:** Encapsula cada estado del diagrama impreso en una clase separada que implementa la interfaz común `<<interface>> IEstadoConsulta`, delegando las transiciones (`+registrarConsulta()`, `+registrarDiagnostico()`, `+cerrarConsulta()`) al objeto de estado actual.
- **d) Clases reutilizadas del Punto 1 y Clases/Interfaces nuevas incorporadas:**
  - *Clase reutilizada (`Context`):* **`Consulta`**, que mantiene el atributo `-estadoActual: IEstadoConsulta` y el método `+cambiarEstado(e)`.
  - *Interfaz nueva incorporada (`State`):* **`<<interface>> IEstadoConsulta`**.
  - *Clases concretas nuevas incorporadas (`ConcreteStates`):* **`EstadoRegistrada`**, **`EstadoDiagnosticada`** y **`EstadoCerrada`**.

#### Patrón GoF N° 2: `Adapter` (Categoría: Estructural)
- **a) Categoría y Nombre:** Patrón **Estructural** — **Adapter (Adaptador)**.
- **b) Problema de diseño que resuelve en el caso:** El sistema PetCare necesita enviar las notificaciones de los `Recordatorio`s (como el recordatorio anual de `Homero`) y avisos de turnos a través de servicios externos de mensajería (**WhatsApp** y **Mail**), los cuales poseen APIs de terceros incompatibles entre sí y ajenas a nuestro modelo de dominio.
- **c) Por qué es adecuado:** Define una interfaz única del dominio (`<<interface>> ICanalNotificacion`) y utiliza clases adaptadoras (`AdaptadorWhatsApp` y `AdaptadorEmail`) que traducen el mensaje `+enviarMensaje(...)` a los métodos nativos de cada proveedor externo (`APIWhatsApp` y `ServidorSMTP`), logrando **Bajo Acoplamiento**, **Indirección** y **Variaciones Protegidas**.
- **d) Clases reutilizadas del Punto 1 y Clases/Interfaces nuevas incorporadas:**
  - *Clases reutilizadas (`Client`):* **`C_Notificacion`** y **`Recordatorio`**.
  - *Interfaz nueva incorporada (`Target`):* **`<<interface>> ICanalNotificacion`**.
  - *Clases nuevas incorporadas (`Adapters` y `Adaptees`):* **`AdaptadorWhatsApp`** (que envuelve a `APIWhatsApp`) y **`AdaptadorEmail`** (que envuelve a `ServidorSMTP`).

---

## PARTE 3: RESOLUCIÓN COMPLETA DEL PARCIAL 1C 2026 (COMISIÓN 1900 — VALERIA Y ANALÍA MARÍN)
### CASO: "SOLUCIÓN DE REENCUENTRO Y ADOPCIÓN DE MASCOTAS" Y ALERTA DE ANIMALES EXÓTICOS (`Parciales/2. -Parcial 1--1C2026--1900--Valeria y Analia-----.pdf`)

> **Fuente verificada visualmente:** Escaneo original de 2 páginas de `Parciales/2. -Parcial 1--1C2026--1900--Valeria y Analia-----.pdf` (y su copia en `Parciales/drive-download-20261111T183304Z-1-001/2. [Parcial 1][1C2026][1900][Valeria y Analia][][].pdf`).

#### 3.1. Enunciado Original Verificado y Elementos Impresos en la Hoja del Examen
1. **Dominio del Problema (`[EXIGENCIA EXPLÍCITA DEL ENUNCIADO]`):**
   - **Ingreso de mascotas encontradas (2 canales):**
     - *Canal Presencial:* Se ingresa al animal físicamente en un **`Refugio`** (validando capacidad/ubicación del refugio).
     - *Canal Autogestionado:* Un ciudadano reporta el hallazgo y aloja temporalmente a la mascota en su domicilio (**`HogarTemporal`**), registrando la **`UbicacionHallazgo`** (calles de referencia, zona, coordenadas GPS), fotos y características físicas.
   - **Módulo de Reclamo ("Soy el dueño"):**
     - Cuando un usuario reclama a una mascota publicada presionando el botón *"Soy el dueño"*, el sistema dispara una **alarma inmediata**, cambia el estado del **`Animal`** de **`"Perdido"`** a **`"En Proceso de Reclamo"`**, registra el **`Reclamo`** (con su evaluación de pruebas de tenencia) y agenda un **`Encuentro`** presencial para la restitución.
   - **Alerta de Reclamos Duplicados (`Conflicto`):**
     - Si un **segundo usuario** reclama la tenencia del mismo animal mientras ya existe un reclamo activo, el sistema genera automáticamente un **`Conflicto`**, **suspende el `Encuentro`** pactado, cambia el estado del **`Animal`** a **`"En Disputa Legal"`** y **bloquea la agenda** para ese animal hasta que la administración resuelva la disputa.
   - **Alerta sobre Encuentro de Animales Exóticos (`AnimalExotico`):**
     - Si un ciudadano avista un animal exótico o peligroso en la vía pública, realiza una **`Denuncia`** de **`AnimalExotico`** indicando descripción, **`UbicacionHallazgo`** y evidencia (fotos/video).
     - El sistema calcula el **nivel de peligrosidad (`ROJO`, `NARANJA`, `AMARILLO`, `VERDE`)** y **notifica automáticamente a dos organismos gubernamentales externos**: la **Dirección de Flora y Fauna** (`organismoFaunaFloraBsAs`) y la **Policía Ecológica**.
   - **Clases esenciales mencionadas explícitamente en la consigna:** `Animal`, `Denuncia`, `Conflicto`, `Encuentro`, `AnimalExotico`, `UbicacionHallazgo`, `OrganismoExternos`, `organismoFaunaFloraBsAs`.
   - **Diagrama de Componentes Base impreso en la hoja:** Muestra 5 bloques (`mascota`, `adminRefugio`, `DenunciaExotico`, `reclamo` [con sub-bloque `evaluacion`], `encuentro`).
2. **Lo que pide la Consigna (`Se Pide`):**
   - **Punto 1:** Construir el **Diagrama de Clases completo** del sistema **usando solo 4 controladores**, justificando los patrones GRASP aplicados.
   - **Punto 2:** **Modificar el Diagrama de Componentes** impreso en la hoja para adecuarlo a la limitación de los **4 controladores**.
   - **Punto 3:** Construir el **Diagrama de Secuencia** para el **Escenario: Denuncia de Animal Exótico** (Un ciudadano ve un **Leopardo** en **Rivadavia, Morón, Bs.As.**), cumpliendo los **7 pasos impresos**:
     1. Recibir la denuncia con los datos y evidencia (foto/video).
     2. Registrar el animal exótico, ubicación, fecha y hora.
     3. Calcular el nivel de peligrosidad (`ROJO / NARANJA / AMARILLO / VERDE`).
     4. Notificar automáticamente a: **Dirección de Flora y Fauna** y **Policía Ecológica** *(nota impresa: `// recomendable usar un Patron GOF`)*.
     5. Marcar la denuncia como `organismoNotificado = SI` (`true`).
     6. Guardar la denuncia.
     7. Informar al ciudadano.
   - **Punto 4:** Aplicar y justificar **2 patrones GoF de diferente categoría** (**prohibido usar Singleton y Facade**).

---

### PUNTO 1 (REENCUENTRO, ADOPCIÓN Y ANIMALES EXÓTICOS): DIAGRAMA DE CLASES (SOLO 4 CONTROLADORES) + GRASP

#### 1.A. Diferenciación entre Exigencias Explícitas y Decisiones de Diseño
- **`[EXIGENCIA EXPLÍCITA DEL ENUNCIADO]`:** Tope estricto de **4 controladores**, clases `Animal`, `Denuncia`, `Conflicto`, `Encuentro`, `AnimalExotico`, `UbicacionHallazgo`, `OrganismoExternos`, `organismoFaunaFloraBsAs`, estados de `Animal` (`Perdido`, `En Proceso de Reclamo`, `En Disputa Legal`), cálculo de peligrosidad (`ROJO/NARANJA/AMARILLO/VERDE`), atributo `organismoNotificado` en `Denuncia`, y prohibición de `Singleton` y `Facade`.
- **`[DECISIÓN DE DISEÑO / INTERPRETACIÓN FUNDAMENTADA]`:**
  1. **Unificación en exactamente 4 Controladores** (que se corresponden 1 a 1 con el Diagrama de Componentes modificado del Punto 2):
     - **`C_Mascota`**: Gestiona el alta y búsqueda de mascotas halladas o en adopción.
     - **`C_AdminRefugio`**: Gestiona la administración de `Refugio`s y `HogarTemporal`es (capacidad, asignación de alojamiento).
     - **`C_ReclamoEncuentro`**: Unifica la recepción de `Reclamo` ("Soy el dueño"), la detección de reclamos duplicados (`Conflicto`), la evaluación y la gestión de la agenda de `Encuentro` (fusionando `reclamo` y `encuentro` del diagrama original de 5 bloques para cumplir los **4 controladores** con Alta Cohesión).
     - **`C_DenunciaExotico`**: Coordina el flujo completo de denuncias de `AnimalExotico`, cálculo de peligrosidad y notificación a organismos externos.
  2. **Los 2 Patrones GoF integrados (sin usar Singleton ni Facade):**
     - **Patrón GoF 1 (Comportamiento) — `Observer`:** Sugerido en el paso 4 del enunciado. `Denuncia` actúa como **Sujeto Observado** que notifica automáticamente a todos los organismos suscritos a través de `<<interface>> IObservadorAlertaExotico`.
     - **Patrón GoF 2 (Estructural) — `Adapter`:** Como la **Dirección de Flora y Fauna** (`organismoFaunaFloraBsAs`) y la **Policía Ecológica** (`SistemaPoliciaEcologica`) son organismos externos con interfaces heterogéneas, se crean `AdaptadorFloraYFauna` y `AdaptadorPoliciaEcologica` que implementan `IObservadorAlertaExotico` (y `OrganismoExternos`) y traducen la alerta al formato nativo de cada entidad gubernamental. *(Además, se modela el patrón `State` sobre `Animal` o `Strategy` para el cálculo de peligrosidad).*

#### 1.B. Diagrama de Clases Completo (`Reencuentro y Animales Exóticos` — Com. 1900)

```
========================================================================================================================
                                      CAPA DE CONTROLADORES (SOLO 4 CONTROLADORES)
========================================================================================================================
 ┌──────────────────────────────────┐ ┌──────────────────────────────────┐ ┌────────────────────────────────────┐ ┌──────────────────────────────────────────────────┐
 │            C_Mascota             │ │          C_AdminRefugio          │ │         C_ReclamoEncuentro         │ │                C_DenunciaExotico                 │
 ├──────────────────────────────────┤ ├──────────────────────────────────┤ ├────────────────────────────────────┤ ├──────────────────────────────────────────────────┤
 │ - nominaAnimales: NominaAnimales │ │ - refugios: List<Refugio>        │ │ - nominaAnimales: NominaAnimales   │ │ - nominaDenuncias: NominaDenuncias               │
 ├──────────────────────────────────┤ ├──────────────────────────────────┤ │ - agenda: AgendaEncuentros         │ │ - estrategiaPeligro: IEstrategiaPeligrosidad     │
 │ + registrarHallazgo(datosAnimal, │ │ + asignarCupoRefugio(idR, a)     │ ├────────────────────────────────────┤ │ - organismosObs: List<IObservadorAlertaExotico>  │
 │     calle, zona, gps, canal):    │ │ + registrarHogarTemporal(ciu, d) │ │ + reclamarTenencia(idAnimal, idU,  │ ├──────────────────────────────────────────────────┤
 │     Animal                       │ └─────────────────┬────────────────┘ │     pruebas): Reclamo              │ │ + registrarDenunciaExotico(idCiu, especie, desc, │
 └─────────────────┬────────────────┘                   │                  │ + resolverConflicto(idConf): void  │ │     calle, localidad, prov, gps, fecha, hora,    │
                   │                                    │                  └─────────┬────────────────┬─────────┘ │     evidenciaFotoVideo): Denuncia                │
                   ▼                                    ▼                            │                │           └────────────────────────┬─────────────────────────┘
========================================================================================================================                   │
                                    DOMINIO DE REENCUENTRO, REFUGIO, RECLAMOS Y ENCUENTROS                                                 │
========================================================================================================================                   │
 ┌──────────────────────────────────┐ ┌──────────────────────────────────┐ ┌────────────────────────────────────┐                          │
 │          NominaAnimales          │ │       <<abstract>> Alojamiento   │ │          AgendaEncuentros          │                          │
 ├──────────────────────────────────┤ ├──────────────────────────────────┤ ├────────────────────────────────────┤                          │
 │ - animales: List<Animal>         │ │ # direccion: String              │ │ - encuentros: List<Encuentro>      │                          │
 ├──────────────────────────────────┤ │ # capacidadMax: int              │ │ - bloqueada: Boolean               │                          │
 │ + buscarAnimal(id): Animal       │ └─────────────────△────────────────┘ ├────────────────────────────────────┤                          │
 │ + agregarAnimal(a: Animal): void │                   │                  │ + agendarEncuentro(r, f):Encuentro │                          │
 └─────────────────┬────────────────┘         ┌─────────┴─────────┐        │ + suspenderEncuentrosDe(a: Animal) │                          │
                   │ 1              ┌─────────┴────────┐ ┌────────┴──────┐ │ + bloquearAgenda(a: Animal): void  │                          │
                   │ (Asoc. simple) │     Refugio      │ │ HogarTemporal │ └─────────────────┬──────────────────┘                          │
                   │ 0..*           ├──────────────────┤ ├───────────────┤                   │ 1                                           │
                   ▼                │ - nombreRefugio  │ │ - ciudadanoRes│                   │                                             │
 ┌──────────────────────────────────┤ + validarCupo()  │ │ - diasMaximos │                   │ 0..*                                        │
 │              Animal              └──────────────────┘ └───────────────┘                   ▼                                             │
 ├──────────────────────────────────┐                                      ┌────────────────────────────────────┐                          │
 │ - idAnimal: int                  │ 1                               0..* │             Encuentro              │                          │
 │ - especie: String                ├─────────────────────────────────────►├────────────────────────────────────┤                          │
 │ - descripcionFisica: String      │                                      │ - idEncuentro: int                 │                          │
 │ - estado: String                 │ 1                               0..* │ - fechaHora: DateTime              │                          │
 │   ("Perdido" / "En Proceso de    ├───────────────────┐                  │ - estado: String ("Agendado",      │                          │
 │    Reclamo" / "En Disputa Legal")│                   │                  │     "Suspendido", "Realizado")     │                          │
 │ - reclamosActivos: List<Reclamo> │                   ▼                  ├────────────────────────────────────┤                          │
 ├──────────────────────────────────┤ ┌──────────────────────────────────┐ │ + suspender(): void                │                          │
 │ + tieneReclamoActivo(): Boolean  │ │             Reclamo              │ └─────────────────▲──────────────────┘                          │
 │ + iniciarReclamo(u, pr): Reclamo │ ├──────────────────────────────────┤                   │ 0..1                                        │
 │ + pasarADisputaLegal(): Conflicto│ │ - idReclamo: int                 │                   │ genera                                      │
 │ + cambiarEstado(nuevoEst): void  │ │ - fechaReclamo: Date             ├───────────────────┘                                             │
 └─────────────────┬────────────────┘ │ - evidenciaTenencia: String      │                                                                 │
                   │ 1                │ - resultadoEvaluacion: String    │ 2..*                                                            │
                   │ halladoEn        ├──────────────────────────────────┤◄──────────────────┐                                             │
                   │                  │ + evaluarPruebas(): Boolean      │                   │ involucra                                   │
                   │                  └──────────────────────────────────┘ ┌─────────────────┴──────────────────┐                          │
                   │                                                       │             Conflicto              │                          │
                   │                                                       ├────────────────────────────────────┤                          │
                   │                                                       │ - idConflicto: int                 │                          │
                   │                                                       │ - fechaDeteccion: Date             │                          │
                   │                                                       │ - estadoDisputa: String            │                          │
                   │                                                       ├────────────────────────────────────┤                          │
                   │                                                       │ + bloquearProceso(): void          │                          │
                   │                                                       └────────────────────────────────────┘                          │
                   ▼ 1                                                                                                                     ▼
============================================================================================================================================
                MÓDULO DE DENUNCIA DE ANIMALES EXÓTICOS + PATRONES GOF: OBSERVER (COMPORTAMIENTO) + ADAPTER (ESTRUCTURAL)
============================================================================================================================================
 ┌──────────────────────────────────┐         ┌──────────────────────────────────────┐         ┌──────────────────────────────────────────────────┐
 │        UbicacionHallazgo         │         │           NominaDenuncias            │         │                     Denuncia                     │
 ├──────────────────────────────────┤         ├──────────────────────────────────────┤ 1  0..* │            (Sujeto en Patrón Observer)           │
 │ - calleReferencia: String        │◄────────┤ - denuncias: List<Denuncia>          ├────────►├──────────────────────────────────────────────────┤
 │ - localidadZona: String          │  1    1 ├──────────────────────────────────────┤         │ - nroDenuncia: int                               │
 │ - provincia: String              │         │ + guardarDenuncia(d: Denuncia): void │         │ - fecha: Date                                    │
 │ - coordenadasGPS: String         │         └──────────────────────────────────────┘         │ - hora: Time                                     │
 └─────────────────▲────────────────┘                                                          │ - evidenciaMultimedia: String                    │
                   │ 1                                                                         │ - nivelPeligrosidad: String                      │
                   │ localizadoEn                                                              │   ("ROJO","NARANJA","AMARILLO","VERDE")          │
                   │                                                                           │ - organismoNotificado: Boolean                   │
 ┌─────────────────┴────────────────┐                                                          │ - observadores: List<IObservadorAlertaExotico>   │
 │          AnimalExotico           │ 1                                                      1 ├──────────────────────────────────────────────────┤
 ├──────────────────────────────────┤◄─────────────────────────────────────────────────────────┤ + registrarAnimalYHubicacion(esp, desc, calle,   │
 │ - especieExotica: String         │                      involucra (◆)                       │     loc, prov, gps): AnimalExotico               │
 │ - descripcion: String            │                                                          │ + calcularNivelPeligrosidad(                     │
 │ - esDepredador: Boolean          │                                                          │     estrat: IEstrategiaPeligrosidad): String     │
 ├──────────────────────────────────┤                                                          │ + suscribirOrganismo(o: IObservadorAlertaExotico)│
 │ + getEspecie(): String           │                                                          │ + notificarOrganismos(): void                    │
 └──────────────────────────────────┘                                                          │ + marcarOrganismoNotificado(): void              │
                                                                                               └─────────┬──────────────────────────────┬─────────┘
                                                                                                         │                              │ *
                                                                                                         ▼ 1                            ▼
 ┌──────────────────────────────────────────────────┐                         ┌───────────────────────────────────────────────────────────────────┐
 │                   <<interface>>                  │                         │                            <<interface>>                          │
 │             IEstrategiaPeligrosidad              │                         │                      IObservadorAlertaExotico                     │
 ├──────────────────────────────────────────────────┤                         │                        (OrganismoExternos)                        │
 │ + evaluarPeligro(a: AnimalExotico,               │                         │     [PATRÓN GOF 1: OBSERVER (Comp.) + GOF 2: ADAPTER (Estruct.)]  │
 │     u: UbicacionHallazgo): String                │                         ├───────────────────────────────────────────────────────────────────┤
 └────────────────────────△─────────────────────────┘                         │ + actualizarAlertaExotico(d: Denuncia): Boolean                   │
                          ┆                                                   └─────────────────────────────────△─────────────────────────────────┘
                          │                                                                                     ┆
 ┌────────────────────────┴─────────────────────────┐                                        ┌──────────────────┴───────────────────┐
 │         EstrategiaPeligroFaunaSilvestre          │                         ┌──────────────┴───────────────┐       ┌──────────────┴───────────────┐
 ├──────────────────────────────────────────────────┤                         │     AdaptadorFloraYFauna     │       │   AdaptadorPoliciaEcologica  │
 │ + evaluarPeligro(a, u): String                   │                         ├──────────────────────────────┤       ├──────────────────────────────┤
 └──────────────────────────────────────────────────┘                         │ - adaptee:                   │       │ - apiPolicia:                │
                                                                              │   organismoFaunaFloraBsAs    │       │   SistemaPoliciaEcologica    │
                                                                              ├──────────────────────────────┤       ├──────────────────────────────┤
                                                                              │ + actualizarAlertaExotico(d) │       │ + actualizarAlertaExotico(d) │
                                                                              └──────────────┬───────────────┘       └──────────────┬───────────────┘
                                                                                             ▼                                      ▼
                                                                              ┌──────────────────────────────┐       ┌──────────────────────────────┐
                                                                              │   organismoFaunaFloraBsAs    │       │   SistemaPoliciaEcologica    │
                                                                              ├──────────────────────────────┤       ├──────────────────────────────┤
                                                                              │ + recibirReporteFauna(esp,   │       │ + dispararOperativo(gps,     │
                                                                              │     zona, nivel): int        │       │     peligro, foto): Boolean  │
                                                                              └──────────────────────────────┘       └──────────────────────────────┘
```

#### 1.C. Justificación de los Patrones GRASP (`Reencuentro y Animales Exóticos`)
1. **Controlador (*Controller*):** Se aplica en los 4 controladores **`C_Mascota`**, **`C_AdminRefugio`**, **`C_ReclamoEncuentro`** y **`C_DenunciaExotico`**, cumpliendo la restricción de usar solo 4 controladores. Por ejemplo, `C_DenunciaExotico` captura el evento de entrada `+registrarDenunciaExotico(...)` y coordina los 7 pasos del caso de uso sin realizar él mismo la lógica interna del dominio.
2. **Creador (*Creator*):** Se aplica en **`Denuncia`** mediante el método **`+registrarAnimalYHubicacion(...)`**, el cual instancia (`create`) a **`AnimalExotico`** y a **`UbicacionHallazgo`**, ya que la `Denuncia` contiene de manera exclusiva los datos del avistamiento denunciado y recibe todos sus parámetros de inicialización. Asimismo, **`Animal`** crea a **`Conflicto`** en `+pasarADisputaLegal()` cuando detecta que ya poseía un reclamo activo.
3. **Experto en Información (*Information Expert*):** Se aplica en **`Denuncia`** con los métodos **`+calcularNivelPeligrosidad(...)`** y **`+marcarOrganismoNotificado()`**, dado que `Denuncia` conoce al `AnimalExotico`, su `UbicacionHallazgo` y su propio atributo `-organismoNotificado`.

---

### PUNTO 2 (REENCUENTRO Y ANIMALES EXÓTICOS): MODIFICACIÓN DEL DIAGRAMA DE COMPONENTES ACORDE A LOS 4 CONTROLADORES

- **Problema del Diagrama de Componentes Base impreso en el parcial:** El diagrama impreso tenía **5 componentes separados** (`mascota`, `adminRefugio`, `DenunciaExotico`, `reclamo` [con `evaluacion`] y `encuentro`) y además no mostraba explícitamente el componente de integración con los `Organismos Externos`. Si cada componente principal tiene su controlador, 5 componentes implicarían 5 controladores, violando el tope de **4 controladores**.
- **Modificación aplicada (Alineación 1 a 1 con los 4 Controladores + Alta Cohesión):**
  1. Se fusionan **`reclamo` (con `evaluacion`) y `encuentro`** dentro de un único componente cohesivo llamado **`Gestión de Reclamos y Encuentros`** (controlado por `C_ReclamoEncuentro`), ya que el `Encuentro` y el bloqueo por `Conflicto` son consecuencia directa del flujo de un `Reclamo`.
  2. Quedan exactamente **4 Componentes de Dominio** (1 por cada uno de los 4 Controladores) más la interfaz hacia los **Organismos Externos**:

```
 ┌────────────────────────────────────┐         ┌────────────────────────────────────┐
 │ <<component>>                      │         │ <<component>>                      │
 │ 1. Gestión de Mascotas             │◄ - - - -│ 2. Administración de Refugios      │
 │    (Controller: C_Mascota)         │         │    y Hogares Temporales            │
 └─────────────────▲──────────────────┘         │    (Controller: C_AdminRefugio)    │
                   ┆                            └────────────────────────────────────┘
                   ┆ (usa estado de Animal)
 ┌─────────────────┴──────────────────┐         ┌────────────────────────────────────┐
 │ <<component>>                      │         │ <<component>>                      │
 │ 3. Gestión de Reclamos y Encuentros│         │ 4. Denuncia de Animales Exóticos   │
 │    (Controller: C_ReclamoEncuentro)│         │    (Controller: C_DenunciaExotico) │
 │  ┌──────────────┐ ┌──────────────┐ │         └─────────────────┬──────────────────┘
 │  │ Reclamo /    │ │ Agenda de    │ │                           ┆
 │  │ Evaluación / │ │ Encuentros   │ │                           ┆ <<interface>> IObservadorAlertaExotico
 │  │ Conflicto    │ └──────────────┘ │                           ▼
 │  └──────────────┘                  │         ┌────────────────────────────────────┐
 └────────────────────────────────────┘         │ <<component / external>>           │
                                                │ Organismos Externos                │
                                                │ (Flora y Fauna / Policía Ecológica)│
                                                └────────────────────────────────────┘
```

---

### PUNTO 3 (REENCUENTRO Y ANIMALES EXÓTICOS): DIAGRAMA DE SECUENCIA — ESCENARIO DENUNCIA DE ANIMAL EXÓTICO (LEOPARDO EN MORÓN)

#### 3.A. Escenario Concreto (Datos Exactos del Enunciado Impreso)
> **Escenario:** Un ciudadano (`idCiudadano = 42`) avista un **`"Leopardo"`** suelto en la calle **`"Rivadavia"`**, localidad de **`"Morón"`**, provincia de **`"Buenos Aires"`** (`gps = "-34.65, -58.62"`), en la fecha `"15/06/2026"` a las `"14:30"` hs, adjuntando evidencia `"video_leopardo.mp4"`. El sistema registra la denuncia, el animal exótico y su ubicación, calcula el nivel de peligrosidad resultando **`"ROJO"`**, notifica automáticamente a la **Dirección de Flora y Fauna** y a la **Policía Ecológica**, marca `organismoNotificado = true`, guarda la denuncia en la nómina e informa al ciudadano.

#### 3.B. Diagrama de Secuencia Completo (Los 7 Pasos Exactos del Enunciado)

```
 :C_DenunciaExotico   d:Denuncia   ae:AnimalExotico   u:UbicacionHallazgo  :EstrategiaPeligro  :AdaptadorFloraFauna  :organismoFaunaFloraBsAs  :AdaptadorPolicia  :SistemaPoliciaEcologica  :NominaDenuncias
         │                 │               │                   │                    │                    │                       │                      │                      │                     │
 ●─1.registrarDenuncia────►│               │                   │                    │                    │                       │                      │                      │                     │
   Exotico(42, "Leopardo", │               │                   │                    │                    │                       │                      │                      │                     │
   "Rivadavia", "Morón",   ├─create(42, "15/06/26", "14:30", "video.mp4")─►┌────────┐                    │                       │                      │                      │                     │
   "Bs.As.", gps, "15/06", │                                               │d:Denun.│                    │                       │                      │                      │                     │
   "14:30", "video.mp4")   │                                               └───┬────┘                    │                       │                      │                      │                     │
         │                 ├─2.registrarAnimalYHubicacion("Leopardo",...)─────►┌─┐                       │                       │                      │                      │                     │
         │                 │                                                   │ ├─create("Rivadavia",   │                       │                      │                      │                     │
         │                 │                                                   │ │  "Morón","BsAs",gps)─►┌───┐                   │                      │                      │                     │
         │                 │                                                   │ │                       │ u │                   │                      │                      │                     │
         │                 │                                                   │ │                       └───┘                   │                      │                      │                     │
         │                 │                                                   │ ├─create("Leopardo",u)─►┌────┐                  │                      │                      │                     │
         │                 │                                                   │ │                       │ ae │                  │                      │                      │                     │
         │                 │◄────────────────── ae ────────────────────────────└─┘                       └────┘                  │                      │                      │                     │
         │                 │                                                   │                         │                       │                      │                      │                     │
         │                 ├─3.calcularNivelPeligrosidad(estrat)──────────────►┌─┐                       │                       │                      │                      │                     │
         │                 │                                                   │ ├─evaluarPeligro(ae,u)─►┌─┐                     │                      │                      │                     │
         │                 │                                                   │ │◄───── "ROJO" ─────────└─┘                     │                      │                      │                     │
         │                 │◄────────────────── "ROJO" ────────────────────────└─┘                                               │                      │                      │                     │
         │                 │                                                   │                                                 │                      │                      │                     │
         │                 ├─suscribirOrganismo(adaptadorFloraFauna)──────────►┌─┐                                               │                      │                      │                     │
         │                 │◄────────────────── ok ────────────────────────────└─┘                                               │                      │                      │                     │
         │                 ├─suscribirOrganismo(adaptadorPolicia)─────────────►┌─┐                                               │                      │                      │                     │
         │                 │◄────────────────── ok ────────────────────────────└─┘                                               │                      │                      │                     │
         │                 │                                                   │                                                 │                      │                      │                     │
         │                 ├─4.notificarOrganismos()──────────────────────────►┌─┐                                               │                      │                      │                     │
         │                 │                                                   │ ├─actualizarAlertaExotico(d)───────────────────►┌─┐                    │                      │                     │
         │                 │                                                   │ │                                               │ ├─recibirReporte────►┌─┐                    │                     │
         │                 │                                                   │ │                                               │ │ ("Leopardo","ROJO")│ │                    │                     │
         │                 │                                                   │ │                                               │ │◄───── idRep ───────└─┘                    │                     │
         │                 │                                                   │ │◄──────────────────── true ────────────────────└─┘                    │                      │                     │
         │                 │                                                   │ ├─actualizarAlertaExotico(d)──────────────────────────────────────────►┌─┐                    │                     │
         │                 │                                                   │ │                                                                      │ ├─dispararOperativo─►┌─┐                   │
         │                 │                                                   │ │                                                                      │ │ (gps,"ROJO",video) │ │                   │
         │                 │                                                   │ │                                                                      │ │◄───── true ────────└─┘                   │
         │                 │                                                   │ │◄─────────────────────────────────── true ────────────────────────────└─┘                                          │
         │                 │◄────────────────── ok ────────────────────────────└─┘                                                                                                                   │
         │                 │                                                   │                                                                                                                     │
         │                 ├─5.marcarOrganismoNotificado()────────────────────►┌─┐ (organismoNotificado = SI / true)                                                                                 │
         │                 │◄────────────────── ok ────────────────────────────└─┘                                                                                                                   │
         │                 │                                                                                                                                                                         │
         ├─6.guardarDenuncia(d)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────►┌─┐
         │◄───────────────────────────────────────────────────────────────────────────────────────── ok ─────────────────────────────────────────────────────────────────────────────────────────────└─┘
 ◄─7.informarCiudadano("Denuncia N° registrada, Peligrosidad ROJO, Flora y Fauna y Policía Ecológica notificadas")
```

---

### PUNTO 4 (REENCUENTRO Y ANIMALES EXÓTICOS): 2 PATRONES GOF DE DIFERENTE CATEGORÍA (SIN SINGLETON NI FACADE)

#### Patrón GoF N° 1: `Observer` (Categoría: Comportamiento)
- **a) Categoría y Nombre:** Patrón de **Comportamiento** — **Observer (Observador)**.
- **b) Problema de diseño que resuelve en el caso:** En el paso 4 de la denuncia de un `AnimalExotico`, el sistema debe disparar notificaciones automáticas simultáneas a múltiples organismos estatales (**Dirección de Flora y Fauna** y **Policía Ecológica**, y potencialmente Defensa Civil o Zoonosis en el futuro) sin acoplar la clase `Denuncia` a una lista fija de organismos concretos.
- **c) Por qué es adecuado:** Define una relación uno-a-muchos entre el Sujeto (`Denuncia`) y la interfaz `<<interface>> IObservadorAlertaExotico`, de modo que cuando se invoca `+notificarOrganismos()`, la denuncia recorre su colección polimórfica de observadores suscritos enviándoles `+actualizarAlertaExotico(this)`.
- **d) Clases reutilizadas y nuevas:**
  - *Clase reutilizada (`Subject`):* **`Denuncia`**, con `-observadores: List<IObservadorAlertaExotico>`, `+suscribirOrganismo(o)` y `+notificarOrganismos()`.
  - *Interfaz nueva (`Observer`):* **`<<interface>> IObservadorAlertaExotico`** (que representa el contrato `OrganismoExternos`).
  - *Observadores concretos:* **`AdaptadorFloraYFauna`** y **`AdaptadorPoliciaEcologica`**.

#### Patrón GoF N° 2: `Adapter` (Categoría: Estructural)
- **a) Categoría y Nombre:** Patrón **Estructural** — **Adapter (Adaptador)**.
- **b) Problema de diseño que resuelve en el caso:** Los sistemas informáticos de la **Dirección de Flora y Fauna de Bs.As.** (`organismoFaunaFloraBsAs`) y de la **Policía Ecológica** (`SistemaPoliciaEcologica`) son sistemas externos gubernamentales preexistentes con firmas de métodos y protocolos distintos e incompatibles con el método uniforme `+actualizarAlertaExotico(d: Denuncia)` que invoca nuestro dominio.
- **c) Por qué es adecuado:** Cada clase adaptadora implementa la interfaz esperada por nuestro dominio (`IObservadorAlertaExotico`) y mantiene una asociación hacia el sistema externo real (`organismoFaunaFloraBsAs` y `SistemaPoliciaEcologica`), traduciendo los datos de la `Denuncia` a los parámetros específicos de cada organismo sin violar la restricción de no usar `Facade`.
- **d) Clases reutilizadas y nuevas:**
  - *Interfaz Objetivo (`Target`):* **`<<interface>> IObservadorAlertaExotico`**.
  - *Clases nuevas (`Adapters`):* **`AdaptadorFloraYFauna`** y **`AdaptadorPoliciaEcologica`**.
  - *Clases adaptadas (`Adaptees`):* **`organismoFaunaFloraBsAs`** (provista en el enunciado) y **`SistemaPoliciaEcologica`**.

---

## PARTE 4: RESOLUCIÓN COMPLETA DEL PARCIAL 2C 2026 (COMISIÓN 1900 — TEMA 1)
### CASO: "AGENCIA DE VIAJES" (`Parciales/drive-download-20261111T183304Z-1-001/3. [Parcial 1][2C2026][1900][][][].pdf`)

> **Fuente verificada visualmente:** Escaneo original de 2 páginas de `Parciales/drive-download-20261111T183304Z-1-001/3. [Parcial 1][2C2026][1900][][][].pdf` (y sus copias en `Parciales/1.jpeg` y `2.jpeg`).

#### 4.1. Enunciado Original Verificado y Elementos Impresos en la Hoja del Examen (`TEMA 1`)
1. **Dominio del Problema (`[EXIGENCIA EXPLÍCITA DEL ENUNCIADO]`):**
   - Una **Agencia de Viajes** ofrece la contratación de **`PaqueteTuristico`s** (ej. Bariloche, Mendoza, Cataratas). Cada paquete tiene un **único destino**, **duración**, **fecha de vigencia** y un **hotel base**, e incluye servicios de:
     - **`Transporte`** (avión, micro, etc.),
     - **`Alojamiento`** (hotel, apart, cabaña),
     - **`Excursion`es**.
   - **Flujo del Caso de Uso impreso en el examen:**
     1. El **`Cliente`** busca paquetes disponibles filtrando por **destino, fechas y cantidad de pasajeros**.
     2. El cliente selecciona un **`PaqueteTuristico`** y opcionalmente puede **cambiar el hotel** y **agregar o quitar excursiones**.
     3. El sistema **verifica la disponibilidad** de los servicios (consultando sistemas externos de aerolínea y hotel) y **calcula el precio total de contratación** (el cual varía según **cantidad de pasajeros, fecha del viaje, servicios incluidos y excursiones extras**).
     4. El cliente selecciona el **medio de pago** (**tarjeta de crédito, tarjeta de débito o transferencia**) y realiza el **`Pago`**.
     5. Si el pago es aprobado por el sistema externo de pago, se genera/confirma la **`Reserva`** y se **envía notificación por mail**.
     6. Una reserva confirmada puede **cancelarse** posteriormente gestionando el **reintegro/reembolso** según corresponda.
2. **Diagramas Impresos en la Hoja del Examen (`[EXIGENCIA EXPLÍCITA DEL ENUNCIADO]`):**
   - **Diagrama de Componentes Defectuoso (para analizar en el Punto 1):** Muestra un gran bloque monolítico llamado **`Solucion`** que encierra acopladamente a `paquete/servicio`, `reserva`, `pago` y `cliente`, mientras afuera aparecen sueltos `notificaciones`, `Sist Ext. Aerolinea`, `Sist Externo Pago` y `Sist Ext. Hotel`.
   - **Diagrama de Estados de `Reserva` (para integrar en el Punto 3):**
     ```
     ● ── creada() ──► [ Pendiente de pago ] ── pagoRealizado() ──► [ Confirmada ] ── CerrarViaje() ──► [ finalizada ] ──► ◉
                                                                          │
                                                                     cancelar()
                                                                          ▼
                                                                   [ cancelada ] ── CerrarReservaCancelada() ──► ◉
     ```
3. **Lo que pide la Consigna (`TEMA 1 - Se Pide`):**
   - **Punto 1:** **Analizar el Diagrama de Componentes** dado y **proponer mejoras** considerando **cohesión, acoplamiento, separación de responsabilidades y mantenibilidad**.
   - **Punto 2:** Realizar el **Diagrama de Secuencia para `"realizar Pago"`** basándose desde el **paso 4 en adelante, MEJORANDO EL ESCENARIO**.
   - **Punto 3:** **Integrar el Diagrama de Estados de `Reserva`** provisto dentro del modelo.
   - **Punto 4:** Construir el **Diagrama de Clases completo usando solo 4 controladores**, aplicando dos patrones GoF:
     - **A-** La complejidad del **cálculo del precio de contratación según diferentes políticas**.
     - **B-** Otro problema de diseño que identifique en el sistema.

---

### PUNTO 1 (AGENCIA DE VIAJES — TEMA 1): ANÁLISIS CRÍTICO Y MEJORA DEL DIAGRAMA DE COMPONENTES

#### 1.A. Problemas Detectados en el Diagrama de Componentes Original Impreso
1. **Baja Cohesión (Bloque Monolítico `"Solucion"`):** El diagrama original mete dentro de un único macro-componente `Solucion` módulos con responsabilidades completamente distintas (`cliente`, `paquete/servicio`, `reserva`, `pago`), violando el principio de **Cohesión Funcional** y los criterios de **Descomponibilidad y Comprensibilidad Modular**.
2. **Alto Acoplamiento e Inconsistencia de Dependencias:** En el dibujo original, `cliente` depende de `pago` y `reserva` de forma cruzada y cíclica, y las conexiones hacia los sistemas externos (`Sist Ext. Aerolinea`, `Sist Ext. Hotel`, `Sist Externo Pago`) y `notificaciones` no están mediadas por interfaces claras ni asignadas al componente responsable.
3. **Falta de Alineación con los 4 Controladores:** Para garantizar la trazabilidad entre la Vista de Implementación (Componentes) y la Vista Lógica (Clases con **4 controladores**), el sistema debe dividirse en **4 componentes internos cohesivos** más los componentes de sistemas externos conectados mediante interfaces provistas/requeridas.

#### 1.B. Diagrama de Componentes Mejorado (4 Componentes Internos Cohesivos + Sistemas Externos Desacoplados)

```
 ┌────────────────────────────────────────────┐         ┌────────────────────────────────────────────┐
 │ <<component>>                              │         │ <<component>>                              │
 │ 1. Gestión de Clientes                     │◄ - - - -│ 2. Catálogo de Paquetes y Servicios        │
 │    (Controller: C_Cliente)                 │         │    (Controller: C_PaqueteServicio)         │
 └─────────────────────▲──────────────────────┘         └──────────┬──────────────────────┬──────────┘
                       ┆                                           ┆                      ┆
                       ┆                                           ▼                      ▼
 ┌─────────────────────┴──────────────────────┐         ┌────────────────────┐ ┌────────────────────┐
 │ <<component>>                              │         │ <<external>>       │ │ <<external>>       │
 │ 3. Gestión de Reservas                     │- - - - ►│ Sist Ext Aerolinea │ │ Sist Ext Hotel     │
 │    (Controller: C_Reserva)                 │         └────────────────────┘ └────────────────────┘
 └──────────┬──────────────────────┬──────────┘
            ┆                      ┆
            ┆ (solicita cobro)     └ - - - - - - - - - - - - - - - ┐
            ▼                                                      ▼
 ┌────────────────────────────────────────────┐         ┌────────────────────────────────────────────┐
 │ <<component>>                              │         │ <<component / external>>                   │
 │ 4. Gestión de Pagos y Reintegros           │         │ Servicio de Notificaciones (Mail)          │
 │    (Controller: C_Pago)                    │         └────────────────────────────────────────────┘
 └─────────────────────┬──────────────────────┘
                       ┆
                       ▼
 ┌────────────────────────────────────────────┐
 │ <<external>>                               │
 │ Sist Externo Pago (Tarjetas/Transferencia) │
 └────────────────────────────────────────────┘
```

---

### PUNTOS 3 Y 4 (AGENCIA DE VIAJES — TEMA 1): INTEGRACIÓN DEL DIAGRAMA DE ESTADOS DE `Reserva` Y DIAGRAMA DE CLASES COMPLETO (SOLO 4 CONTROLADORES + 2 PATRONES GOF `A` Y `B`)

#### 4.A. Resolución de los Patrones GoF Pedidos (`A` y `B`) e Integración del Diagrama de Estados
- **Integración del Diagrama de Estados de `Reserva` (Punto 3):**
  - Se incorporan en la clase **`Reserva`** todos los métodos correspondientes a las transiciones del Diagrama de Estados impreso: constructor `+crearReserva()` (estado inicial `Pendiente de pago`), **`+pagoRealizado()`** (transiciona a `Confirmada`), **`+cancelar()`** (transiciona a `Cancelada` y dispara el cálculo de reembolso), **`+cerrarViaje()`** (transiciona a `Finalizada`) y **`+cerrarReservaCancelada()`**.
  - Además, para modelar el cambio de comportamiento por estado sin condicionales `if/switch`, se aplica el patrón **`State`** (`<<interface>> IEstadoReserva` con las 4 clases de estado: `EstadoPendienteDePago`, `EstadoConfirmada`, `EstadoCancelada`, `EstadoFinalizada`).
- **Patrón GoF `A` (Complejidad del cálculo del precio de contratación según diferentes políticas):**
  - **Categoría y Nombre:** Patrón de **Comportamiento — `Strategy` (Estrategia)**.
  - **Problema que resuelve:** El precio total de contratación varía según múltiples políticas (temporada/fecha del viaje, cantidad de pasajeros/grupo familiar, paquete con excursiones extras).
  - **Diseño:** La clase `Reserva` (o `ConfiguracionPaquete`) se asocia a la interfaz **`<<interface>> IPoliticaPrecio`** (`+calcularPrecioTotal(paqBase, cantPasajeros, fechaViaje, hotelElegido, excursionesExtras): float`), implementada por **`PoliticaPrecioTemporadaAlta`**, **`PoliticaPrecioGrupoFamiliar`** y **`PoliticaPrecioPromocional`**.
- **Patrón GoF `B` (Segundo problema de diseño en el sistema — De diferente categoría: Estructural):**
  - **Categoría y Nombre:** Patrón **Estructural — `Adapter` (Adaptador)** *(Nota: También puede combinarse con `Decorator` o `Composite` para los servicios del paquete)*.
  - **Problema que resuelve:** El sistema necesita comunicarse con **`Sist Externo Pago`**, **`Sist Ext. Aerolinea`** y **`Sist Ext. Hotel`**, cuyas APIs externas son incompatibles con el modelo de dominio.
  - **Diseño:** Para el proceso de pago y reintegro se define la interfaz **`<<interface>> IPasarelaPagoExt`** (`+procesarCobro(medio, monto, datos): Boolean`, `+ejecutarReintegro(idTransaccion, monto): Boolean`), implementada por **`AdaptadorSistemaPagoExt`** que envuelve y adapta a la clase externa **`SistExternoPago`** (y análogamente `IServicioProveedorExt` con `AdaptadorAerolineaExt` y `AdaptadorHotelExt`).

#### 4.B. Diagrama de Clases Completo (`Agencia de Viajes` — 4 Controladores + Estados de `Reserva` + GoF `A` Strategy + GoF `B` Adapter)

```
========================================================================================================================
                                      CAPA DE CONTROLADORES (SOLO 4 CONTROLADORES)
========================================================================================================================
 ┌──────────────────────────────────┐ ┌────────────────────────────────────┐ ┌────────────────────────────────────┐ ┌────────────────────────────────────────────────┐
 │            C_Cliente             │ │         C_PaqueteServicio          │ │             C_Reserva              │ │                     C_Pago                     │
 ├──────────────────────────────────┤ ├────────────────────────────────────┤ ├────────────────────────────────────┤ ├────────────────────────────────────────────────┤
 │ - nominaClientes: NominaClientes │ │ - catalogo: CatalogoPaquetes       │ │ - nominaReservas: NominaReservas   │ │ - nominaReservas: NominaReservas               │
 ├──────────────────────────────────┤ ├────────────────────────────────────┤ ├────────────────────────────────────┤ │ - pasarelaPago: IPasarelaPagoExt               │
 │ + registrarCliente(datos):Cliente│ │ + buscarPaquetes(dest, f, cantP)   │ │ + crearReservaPersonalizada(idCli, │ │ - servicioMail: IServicioNotificacion          │
 │ + buscarCliente(idCli): Cliente  │ │ + personalizarYCotizar(idPaq,      │ │     idPaq, idHotel, listExc, cantP,│ ├────────────────────────────────────────────────┤
 └─────────────────┬────────────────┘ │     idHotelNuevo, listExcursiones, │ │     fViaje, politica): Reserva     │ │ + realizarPago(idReserva, tipoMedioPago,       │
                   │                  │     cantPasaj, fViaje): float      │ │ + cancelarReserva(idRes): Reembolso│ │     datosMedio): Pago                          │
                   ▼                  └─────────────────┬──────────────────┘ └─────────────────┬──────────────────┘ └───────────────────────┬────────────────────────┘
 ┌──────────────────────────────────┐                   │                                      │                                            │
 │          NominaClientes          │                   ▼                                      ▼                                            │
 ├──────────────────────────────────┤ ┌────────────────────────────────────┐ ┌────────────────────────────────────┐                         │
 │ - clientes: List<Cliente>        │ │          CatalogoPaquetes          │ │           NominaReservas           │                         │
 ├──────────────────────────────────┤ ├────────────────────────────────────┤ ├────────────────────────────────────┤                         │
 │ + buscarCliente(id): Cliente     │ │ - paquetes: List<PaqueteTuristico> │ │ - reservas: List<Reserva>          │                         │
 └─────────────────┬────────────────┘ ├────────────────────────────────────┤ ├────────────────────────────────────┤                         │
                   │ 1                │ + buscarPorDestinoYFecha(d, f)     │ │ + buscarReserva(idRes): Reserva    │                         │
                   │                  │ + obtenerPaquete(idPaq): Paquete   │ │ + agregarReserva(r: Reserva): void │                         │
                   │ 0..*             └─────────────────┬──────────────────┘ └─────────────────┬──────────────────┘                         │
                   ▼                                    │ 1                                    │ 1                                          │
 ┌──────────────────────────────────┐                   │                                      │ 0..*                                       │
 │             Cliente              │                   │ 1..*                                 ▼                                            │
 ├──────────────────────────────────┤                   ▼                    ┌────────────────────────────────────────────────────────┐     │
 │ - idCliente: int                 │ ┌────────────────────────────────────┐ │                        Reserva                         │◄────┘
 │ - nombreApellido: String         │ │          PaqueteTuristico          │ │     (Integra el Diagrama de Estados del Punto 3)       │
 │ - dni: String                    │ ├────────────────────────────────────┤ ├────────────────────────────────────────────────────────┤
 │ - email: String                  │ │ - idPaquete: int                   │ │ - idReserva: int                                       │
 ├──────────────────────────────────┤ │ - destinoUnico: String             │ │ - fechaCreacion: Date                                  │
 │ + getEmail(): String             │ │ - duracionDias: int                │ │ - fechaViaje: Date                                     │
 └─────────────────┬────────────────┘ │ - fechaVigencia: Date              │ │ - cantPasajeros: int                                   │
                   │ 1                │ - precioBase: float                │ │ - montoTotalCalculado: float                           │
                   │ titularDe        ├────────────────────────────────────┤ │ - paqueteBase: PaqueteTuristico                        │
                   └─────────────────►│ + verificarDisponibilidad(f, cantP)│ │ - alojamientoElegido: Alojamiento                      │
                                 0..* │ + calcularCostoServiciosBase():flt │ │ - excursionesElegidas: List<Excursion>                 │
                                      └─────────┬────────────────┬─────────┘ │ - estadoActual: IEstadoReserva                         │
                                                │ 1              │ 1         │ - politicaPrecio: IPoliticaPrecio                      │
                                                │ incluye        │ hotelBase ├────────────────────────────────────────────────────────┤
                                                │ 1..*           │ 1         │ + calcularPrecioContratacion(): float                  │
                                                ▼                ▼           │ + registrarPagoAprobado(p: Pago): void                 │
                                      ┌────────────────────────────────────┐ │ + pagoRealizado(): void                                │
                                      │      <<abstract>> Servicio         │ │ + cancelar(): Reembolso                                │
                                      ├────────────────────────────────────┤ │ + cerrarViaje(): void                                  │
                                      │ # idServicio: int                  │ │ + cerrarReservaCancelada(): void                       │
                                      │ # descripcion: String              │ │ + cambiarEstado(nuevoEstado: IEstadoReserva): void     │
                                      │ # costoUnitario: float             │ └──┬──────────────────────────┬────────────────────────┬─┘
                                      ├────────────────────────────────────┤    │ 1                        │ 1                      │ 1
                                      │ + <<abstract>> hayCupo(f, c): Bool │    │                          │                        │
                                      │ + getCosto(): float                │    │                          │                        │ 0..1
                                      └─────────────────△──────────────────┘    │                          │                        ▼
                                                        │                       │                          │         ┌──────────────────────────────────┐
                         ┌──────────────────────────────┼───────────────────────┐                          │         │               Pago               │
            ┌────────────┴───────────┐     ┌────────────┴───────────┐     ┌─────┴──────────────────┐       │         ├──────────────────────────────────┤
            │       Transporte       │     │      Alojamiento       │     │       Excursion        │       │         │ - idPago: int                    │
            ├────────────────────────┤     ├────────────────────────┤     ├────────────────────────┤       │         │ - fechaHora: DateTime            │
            │ - tipo: String         │     │ - categoria: String    │     │ - nombreExcursion: Str │       │         │ - monto: float                   │
            │   (Avion / Micro)      │     │   (Hotel/Apart/Cabaña) │     │ - esOpcional: Boolean  │       │         │ - tipoMedioPago: String          │
            │ - compania: String     │     │ - nombreHotel: String  │     ├────────────────────────┤       │         │   (Credito/Debito/Transferencia) │
            ├────────────────────────┤     ├────────────────────────┤     │ + hayCupo(f, c): Bool  │       │         │ - estadoPago: String             │
            │ + hayCupo(f, c): Bool  │     │ + hayCupo(f, c): Bool  │     └────────────────────────┘       │         │ - nroTransaccionExt: String      │
            └────────────────────────┘     └────────────────────────┘                                      │         ├──────────────────────────────────┤
                                                                                                           │         │ + esAprobado(): Boolean          │
===========================================================================================================┼=========└──────────────────────────────────┘
        INTEGRACIÓN DEL DIAGRAMA DE ESTADOS (PUNTO 3) + PATRÓN GOF A (STRATEGY) + PATRÓN GOF B (ADAPTER)   │
===========================================================================================================▼=============================================
 ┌────────────────────────────────────────────────────┐         ┌────────────────────────────────────────────────────────┐
 │                    <<interface>>                   │         │                      <<interface>>                     │
 │                   IEstadoReserva                   │         │                    IPoliticaPrecio                     │
 │       [INTEGRACIÓN DIAGRAMA ESTADOS PUNTO 3]       │         │        [PATRÓN GOF A: STRATEGY (Comportamiento)]       │
 ├────────────────────────────────────────────────────┤         ├────────────────────────────────────────────────────────┤
 │ + pagoRealizado(r: Reserva): void                  │         │ + calcularPrecioTotal(r: Reserva): float               │
 │ + cancelar(r: Reserva): Reembolso                  │         └───────────────────────────△────────────────────────────┘
 │ + cerrarViaje(r: Reserva): void                    │                                     ┆
 │ + cerrarReservaCancelada(r: Reserva): void         │               ┌─────────────────────┼─────────────────────┐
 └─────────────────────────△──────────────────────────┘ ┌─────────────┴─────────────┐ ┌─────┴───────────────────┐ │
                           ┆                            │PoliticaPrecioTemporadaAlta│ │PoliticaGrupoPasajeros   │ │
      ┌────────────────────┼───────────────┬────────────┐├──────────────────────────┤ ├─────────────────────────┤ │
 ┌────┴────────────────┐ ┌─┴────────────┐ ┌┴──────────┐ ││ + calcularPrecioTotal(r) │ │ + calcularPrecioTotal(r)│ │
 │EstadoPendienteDePago│ │EstadoConfirma│ │EstadoCance│ │└──────────────────────────┘ └─────────────────────────┘ │
 ├─────────────────────┤ ├──────────────┤ ├───────────┤ │                                                         │
 │ + pagoRealizado(r)  │ │ + cancelar(r)│ │ + cerrar  │ │       ┌─────────────────────────────────────────────────┘
 │ + cancelar(r)       │ │ + cerrarViaje│ │   Reserva │ │       │ ┌───────────────────────────┐
 └─────────────────────┘ └──────────────┘ │   Cancel()│ │       └►│PoliticaConExcursionesExtra│
                                          └───────────┘ │         ├───────────────────────────┤
                                                 ┌──────┴────────┐│ + calcularPrecioTotal(r)  │
                                                 │EstadoFinalizad│└───────────────────────────┘
                                                 └───────────────┘
 ┌────────────────────────────────────────────────────┐         ┌────────────────────────────────────────────────────────┐
 │                    <<interface>>                   │         │                 AdaptadorSistemaPagoExt                │
 │                  IPasarelaPagoExt                  │         ├────────────────────────────────────────────────────────┤
 │        [PATRÓN GOF B: ADAPTER (Estructural)]       │◄ - - - -│ - sistExtPago: SistExternoPago                         │
 ├────────────────────────────────────────────────────┤         ├────────────────────────────────────────────────────────┤
 │ + autorizarPago(medio, monto, datos): String       │         │ + autorizarPago(medio, monto, datos): String           │
 │ + procesarReembolso(nroTrans, monto): Boolean      │         │ + procesarReembolso(nroTrans, monto): Boolean          │
 └────────────────────────────────────────────────────┘         └───────────────────────────┬────────────────────────────┘
                                                                                            ▼
                                                                ┌────────────────────────────────────────────────────────┐
                                                                │                    SistExternoPago                     │
                                                                ├────────────────────────────────────────────────────────┤
                                                                │ + executePaymentTransaction(cardData, amount): int     │
                                                                │ + refundTransaction(txId): int                         │
                                                                └────────────────────────────────────────────────────────┘
```

---

### PUNTO 2 (AGENCIA DE VIAJES — TEMA 1): ESCENARIO MEJORADO Y DIAGRAMA DE SECUENCIA PARA `"realizar Pago"` (PASO 4 EN ADELANTE)

#### 2.A. Escenario Mejorado (A partir del Paso 4 del Enunciado)
> **Escenario Mejorado:** El cliente `"Martín Gómez"` (`email = "martin@mail.com"`) ya seleccionó y personalizó el paquete a `"Bariloche"` para `2` pasajeros con `1` excursión extra, habiéndose creado la `Reserva` (`idReserva = 500`) en estado **`"Pendiente de pago"`**. En el **Paso 4**, el cliente selecciona como medio de pago **`"Tarjeta de Crédito"`** e ingresa los datos de su tarjeta. El controlador **`C_Pago`** recibe el mensaje **`realizarPago(500, "TarjetaCredito", datosTarjeta)`**, le pide a la **`Reserva`** su precio final calculado mediante su **`IPoliticaPrecio`**, solicita la autorización del cobro a través de **`AdaptadorSistemaPagoExt`** hacia **`SistExternoPago`**, y al recibir la aprobación (`txId = "TX-998"`):
> 1. Instancia el objeto **`Pago`** aprobado y lo asocia a la **`Reserva`**.
> 2. Dispara la transición **`pagoRealizado()`** en **`Reserva`**, pasando su estado de **`EstadoPendienteDePago`** a **`EstadoConfirmada`**.
> 3. Obtiene el email del **`Cliente`** titular y envía la notificación de confirmación por mail a través de **`IServicioNotificacion`**.

#### 2.B. Diagrama de Secuencia Completo de `"realizar Pago"`

```
 :C_Pago     :NominaReservas     r:Reserva     :PoliticaPrecio   :AdaptadorSistemaPagoExt   :SistExternoPago     p:Pago     :EstadoPendienteDePago   cli:Cliente   :IServicioNotificacion
    │               │                │                │                      │                      │               │                  │                  │                   │
 ●──realizarPago───►│                │                │                      │                      │               │                  │                  │                   │
   (500,"Credito",  ├─buscarReserva─►┌─┐              │                      │                      │               │                  │                  │                   │
    datosTarjeta)   │ (500)          │ │              │                      │                      │               │                  │                  │                   │
    │               │◄───── r ───────└─┘              │                      │                      │               │                  │                  │                   │
    │               │                │                │                      │                      │               │                  │                  │                   │
    ├─calcularPrecioContratacion()──►┌─┐              │                      │                      │               │                  │                  │                   │
    │                                │ ├─calcular────►┌─┐                    │                      │               │                  │                  │                   │
    │                                │ │ PrecioTotal  │ │                    │                      │               │                  │                  │                   │
    │                                │ │◄── $850.000 ─└─┘                    │                      │               │                  │                  │                   │
    │◄────────── $850.000 ───────────└─┘                                     │                      │               │                  │                  │                   │
    │                                │                                       │                      │               │                  │                  │                   │
    ├─autorizarPago("Credito", $850.000, datosTarjeta)──────────────────────►┌─┐                    │               │                  │                  │                   │
    │                                │                                       │ ├─executePayment────►┌─┐             │                  │                  │                   │
    │                                │                                       │ │ Transaction(...)   │ │             │                  │                  │                   │
    │                                │                                       │ │◄──── "TX-998" ─────└─┘             │                  │                  │                   │
    │◄─────────────────────────── "TX-998" (Aprobado) ───────────────────────└─┘                                    │                  │                  │                   │
    │                                │                                                                              │                  │                  │                   │
    ├─create($850.000, "Credito", "Aprobado", "TX-998")────────────────────────────────────────────────────────────►┌─┐                │                  │                   │
    │◄──────────────────────────────────────────────────── p:Pago ──────────────────────────────────────────────────└─┘                │                  │                   │
    │                                │                                                                                                 │                  │                   │
    ├─registrarPagoAprobado(p)──────►┌─┐                                                                                               │                  │                   │
    │                                │ ├─pagoRealizado()──────────────────────────────────────────────────────────────────────────────►┌─┐                │                   │
    │                                │ │                                                                                               │ ├─cambiarEstado(EstadoConfirmada)    │
    │                                │ │◄──────────────────────────────────────────── ok ──────────────────────────────────────────────└─┘                │                   │
    │◄────────── ok (Confirmada) ────└─┘                                                                                                                  │                   │
    │                                │                                                                                                                    │                   │
    ├─getEmailCliente()─────────────►┌─┐                                                                                                                  │                   │
    │                                │ ├─getEmail()──────────────────────────────────────────────────────────────────────────────────────────────────────►┌─┐                 │
    │                                │ │◄── "martin@mail.com" ────────────────────────────────────────────────────────────────────────────────────────────└─┘                 │
    │◄────── "martin@mail.com" ──────└─┘                                                                                                                                      │
    │                                                                                                                                                                         │
    ├─enviarMailConfirmacion("martin@mail.com", "Reserva #500 Confirmada", detalleVoucher)───────────────────────────────────────────────────────────────────────────────────►┌─┐
    │◄───────────────────────────────────────────────────────────────────────────────────────── ok ───────────────────────────────────────────────────────────────────────────└─┘
 ◄── pagoYReservaConfirmados(p, r)
```

---

## PARTE 4-BIS: CASO PRÁCTICO DE TALLER PRE-PARCIAL (CLASE 09 — PRIMERA MITAD `[00:00:00 a 01:55:00]`)
### CASO: "SISTEMA DE SEGURIDAD CIUDADANA — ALERTAS Y DENUNCIAS" (`Transcripcion/transcripciones/09_20261015_082342.txt`)

> **Por qué estudiar este caso:** Durante la primera hora y cincuenta minutos de la Clase 09, la Ing. Analía Marín y Alejandro corrigieron en vivo este modelo de parcial con los grupos. De aquí salieron varias de las advertencias clave para el examen.

#### 4-Bis.1. Requisitos del Caso Discutidos en Clase 09
1. Los **Ciudadanos (Vecinos)** registrados pueden emitir **Alertas rápidas (Botón Antipánico)** o cargar **Denuncias** detalladas (con fotos, audio/video, geolocalización y tipo de incidente: robo, incendio, violencia, accidente).
2. El sistema **evalúa la veracidad / riesgo de la denuncia** para detectar **falsas denuncias**: si un ciudadano acumula múltiples falsas denuncias, se lo **penaliza / bloquea**.
3. Si la alerta o denuncia es válida, se genera un **Incidente**, se calcula su **prioridad/gravedad**, se despacha el recurso correspondiente (**Patrulla Policial, Bomberos, Ambulancia**) según cercanía y disponibilidad, y se actualiza el **Mapa de Calor (*Heat Map*)** delictivo por zona.

#### 4-Bis.2. Lecciones de Corrección de la Profesora sobre este Caso (`09_20261015_082342.txt`)
1. **Diferencia entre `Alerta` y `Denuncia`:** Pueden modelarse con una superclase abstracta ` <<abstract>> ReporteCiudadano` (con `fechaHora`, `ubicacionGPS`, `estado`) de la cual heredan `AlertaAntipanico` (inmediata, prioridad crítica) y `Denuncia` (con `evidenciaMultimedia`, `descripcion`, `evaluacionVeracidad`).
2. **Evaluación de Falsas Denuncias y Penalización del Ciudadano:**
   - La clase `Ciudadano` conoce su atributo `-cantidadFalsasDenuncias: int` y su `-estadoCuenta`.
   - Cuando un operador o validador marca una denuncia como falsa (`denuncia.marcarComoFalsa()`), la denuncia le avisa al `Ciudadano` (`ciudadano.registrarFalsaDenuncia()`), y es el propio `Ciudadano` (**Experto**) quien incrementa su contador y evalúa si supera el umbral para bloquearse.
3. **Patrones GoF Ideales validados por la Profesora en este Caso:**
   - **`Observer` (Comportamiento):** Cuando se confirma un `Incidente`, notifica automáticamente a las centrales externas (`CentralPolicia`, `CuartelBomberos`, `SAME_Emergencias`) y actualiza el `MapaDeCalor`.
   - **`Strategy` (Comportamiento):** Para el algoritmo de **cálculo de nivel de prioridad/criticidad del incidente** o para la **estrategia de asignación de patrulla más cercana**.
   - **`State` (Comportamiento):** Ciclo de vida de la `Denuncia` / `Incidente` (`Reportada` → `EnVerificacion` → `ConfirmadaEnAtencion` / `DesestimadaPorFalsa` → `Resuelta`).
   - **`Adapter` (Estructural):** Para conectarse con los sistemas externos del **911 / Cámaras Municipales / Bomberos**.

---

## PARTE 5: RESOLUCIÓN DE DIAGRAMAS DE ESTADOS DE FINALES RECIENTES (DIC 2025 Y JULIO 2026)

### 5.1. Final Diciembre 2025 (`Parciales/Final_-_2C2025.jpg`): Diagrama de Estados de una `Reserva` de Paquete Turístico
- **Reglas del enunciado:**
  1. La reserva se crea en estado **Pendiente de Pago** y mantiene el bloqueo de cupos durante **15 minutos**.
  2. Si pasan los 15 minutos sin recibir pago, pasa a **Expirada / Vencida** (estado final) liberando el cupo.
  3. Si el pago es rechazado, puede reintentar mientras no hayan pasado los 15 minutos.
  4. Si el pago es aprobado dentro de los 15 minutos, pasa a **Confirmada**.
  5. Desde **Confirmada**, el cliente puede cancelar: si cancela con más de 48 hs de anticipación pasa a **Cancelada sin Penalidad (Reembolso Total)**; si cancela con menos de 48 hs pasa a **Cancelada con Penalidad**.
  6. Llegada la fecha del viaje, el pasajero realiza el check-in pasando a **En Curso (Check-in Realizado)**, y al concluir el viaje pasa a **Finalizada**.

```
                                              reintentarPago() [pagoRechazado AND t <= 15m] / notificarError()
                                                             ┌───────────────────────┐
                                                             │                       ▼
             crearReserva() / bloquearCupo()         ┌───────┴───────────────────────────┐
      ● ────────────────────────────────────────────►│         Pendiente de Pago         │
                                                     ├───────────────────────────────────┤
                                                     │ entry / iniciarTimer(15 min)      │
                                                     │ do / esperarConfirmacionPago()    │
                                                     └───────┬───────────────────┬───────┘
                                                             │                   │
                 expirarTiempo() [t > 15m] / liberarCupo()   │                   │ registrarPago() [pagoAprobado AND t <= 15m]
                                     ┌───────────────────────┘                   │   / emitirVoucher()
                                     ▼                                           ▼
                             ┌───────────────┐                        ┌──────────────────────┐
                             │    Vencida    ├──► ◉                   │      Confirmada      │
                             └───────────────┘                        ├──────────────────────┤
                                                                      │ entry / fijarCupo()  │
                                                                      └──┬────────┬────────┬─┘
                      ┌──────────────────────────────────────────────────┘        │        └────────────────────────────┐
                      │ cancelar() [antiguedad >= 48hs]                           │ realizarCheckIn() [fecha == hoy]    │ cancelar() [antiguedad < 48hs]
                      │   / reembolsar100()                                       │   / habilitarServicios()            │   / aplicarRetencionPenalidad()
                      ▼                                                           ▼                                     ▼
        ┌───────────────────────────┐                               ┌───────────────────────────┐         ┌───────────────────────────┐
        │  Cancelada Sin Penalidad  ├──► ◉                          │         En Curso          │         │  Cancelada Con Penalidad  ├──► ◉
        └───────────────────────────┘                               └─────────────┬─────────────┘         └───────────────────────────┘
                                                                                  │ concluirViaje() / enviarEncuesta()
                                                                                  ▼
                                                                    ┌───────────────────────────┐
                                                                    │        Finalizada         ├──► ◉
                                                                    └───────────────────────────┘
```

### 5.2. Final Julio 2026 Mesa B (`Parciales/Final_Diseno_Julio_2026.pdf`): Diagrama de Estados de un `Articulo` de Supermercado
- **Ciclo de vida del objeto `Articulo`:**
  - `●` ── `solicitarAProveedor()` ──► **`Pedido a Proveedor`**
  - **`Pedido a Proveedor`** ── `recibirMercaderia() [controlCalidadOK] / incrementarStock()` ──► **`Disponible en Stock`**
  - **`Disponible en Stock`** ── `vender() [stockActual > stockMinimo] / descontarStock()` ──► **`Disponible en Stock`** *(auto-transición)*
  - **`Disponible en Stock`** ── `vender() [stockActual <= stockMinimo AND stockActual > 0] / generarAlertaReposicion()` ──► **`En Punto de Pedido (Stock Crítico)`**
  - **`En Punto de Pedido`** ── `vender() [stockActual == 0]` ──► **`Agotado (Sin Stock)`**
  - **`En Punto de Pedido`** o **`Agotado`** ── `recibirReposicion() / actualizarStock()` ──► **`Disponible en Stock`**
  - **`Disponible en Stock`** ── `detectarVencimientoORotura() / retirarDeGondola()` ──► **`Dado de Baja / Devolución a Proveedor`** ──► `◉`.

---

## PARTE 6: SÍNTESIS DE LAS UNIDADES TEÓRICAS FINALES Y BANCO DE PREGUNTAS DE EXAMEN

Para asegurar el 100% de los puntos en las preguntas teóricas del Parcial y del Final, aquí tenés el desarrollo exacto según las diapositivas de la Prof. Analía Marín:

### 6.1. Calidad de Software y Atributos de Calidad (`02-Diseño Calidad- UNLaM-2026Agosto.pdf`)
1. **David Garvin (Dimensiones de la Calidad, Pág. 7):** Desempeño, Características, Confiabilidad, Conformidad, Durabilidad, Servicio, Estética y Percepción.
2. **Robert Glass (Calidad del Diseño, Pág. 8):** Es el grado en que el diseño cumple las funciones y características especificadas en el modelo de requerimientos.
3. **Factores de Calidad de McCall (Págs. 9–10 — Pregunta del Final Julio 2026 Mesa B):** Se agrupan en **3 ejes**:
   - **Operación del Producto:** *Corrección* (cumple especificaciones), *Confiabilidad* (precisión sin fallas), *Eficiencia* (uso de recursos), *Integridad/Seguridad* (control de acceso), *Usabilidad* (facilidad de uso).
   - **Revisión del Producto:** *Facilidad de Mantenimiento* (localizar y arreglar errores), *Flexibilidad* (modificar el sistema operativo), *Facilidad de Prueba* (validar el software).
   - **Transición del Producto:** *Portabilidad* (llevar a otro hardware/SO), *Reusabilidad* (reusar partes en otros sistemas), *Interoperabilidad* (conectarse con otros sistemas).
4. **Atributos de Calidad Clave para Evaluar Arquitecturas (Págs. 11 y 16 — Pregunta de Parcial 2023, Final Dic 2025 y Final Jul 2026):**
   - **Performance (Rendimiento):** Tiempo de respuesta y capacidad de procesamiento (*throughput*) bajo una carga determinada.
   - **Escalabilidad:** Capacidad de crecer para manejar un incremento brusco de usuarios o transacciones (ej. e-commerce en CyberMonday) agregando recursos (escalado horizontal o vertical) sin degradar el rendimiento.
   - **Disponibilidad (*Availability*):** Proporción de tiempo en que el sistema está operativo y accesible cuando se lo requiere ($99.9\%$), estrechamente ligada a la **Tolerancia a Fallos** y **Confiabilidad**.
   - **Seguridad:** Capacidad de resistir accesos no autorizados garantizando Confidencialidad, Integridad y Autenticación.
   - **Mantenibilidad y Extensibilidad:** Facilidad para corregir defectos o agregar nueva funcionalidad con mínimo impacto (lograda con **Alta Cohesión, Bajo Acoplamiento y Patrones GoF**).

### 6.2. Diseño de Interfaz de Usuario y UX (`02-DiseñoUX-Alumno-2Q-2026-JUEVES.pdf`)
1. **Las 3 Reglas Doradas de Theo Mandel (Pág. 4 — Pregunta de Parcial 2C 2025):**
   - **Regla 1: Dejar el control al usuario:** No obligar al usuario a realizar acciones innecesarias, permitir que la interacción sea interrumpible y **reversible (Deshacer/Undo)**, y ocultar los detalles técnicos internos.
   - **Regla 2: Reducir la carga de memoria del usuario:** No obligar al usuario a recordar datos de una pantalla a otra; ofrecer valores por defecto coherentes, atajos intuitivos y metáforas del mundo real.
   - **Regla 3: Hacer que la interfaz sea consistente:** Mantener coherencia visual, de colores, tipografía, ubicación de botones y comportamiento en todas las pantallas para que la experiencia sea predecible.
2. **Herramientas de Investigación UX vistas en Clase 02 (Págs. 12–18):**
   - **User Personas:** Arquetipos o personajes ficticios basados en datos reales de usuarios para comprender sus objetivos, frustraciones, contexto y expectativas.
   - **Pruebas de Usabilidad (7 pasos):** Observar a usuarios reales ejecutando un guion de tareas sobre el prototipo sin ayudarlos, midiendo dónde dudan o fallan.
   - **Heat Maps (Mapas de Calor):** Representación visual de dónde hacen clic o fijan la vista los usuarios (zonas rojas = calientes/más vistas; zonas azules = frías/ignoradas).

### 6.3. Arquitectura Orientada a Servicios (SOA), Microservicios y APIs (`11/soa 2026-v10.pdf` — Clase 11)
1. **¿Qué es SOA? (Págs. 1–8):** Es un estilo arquitectónico que estructura los sistemas como un conjunto de **servicios de negocio débilmente acoplados, reutilizables e interoperables** que se comunican mediante protocolos estándar (históricamente SOAP/XML).
   - **ESB (*Enterprise Service Bus*, Págs. 4–5):** Middleware o bus de interconexión que implementa la **lógica de integración, enrutamiento, transformación de mensajes y orquestación** entre servicios. **Regla de Oro de la Profesora (Pág. 5):** *"El ESB implementa la lógica de integración de los servicios, NUNCA la lógica de negocios (la cual reside en los componentes)"*.
   - **BPM (*Business Process Management*) y BAM (*Business Activity Monitoring*, Pág. 6):** BPM modela y orquesta los procesos de negocio de punta a punta; BAM monitorea en tiempo real los indicadores (KPIs) y alertas de esos procesos.
2. **SOA vs. Microservicios (Pág. 10):**
   - **Microservicios:** Evolución moderna donde la aplicación se divide en servicios **pequeños, autónomos y especializados**, cada uno con **su propia base de datos independiente** y desplegable por separado en contenedores, comunicándose mediante APIs ligeras (REST/JSON o colas de eventos) sin un ESB pesado centralizado.
3. **API y Swagger / OpenAPI (Págs. 11–12):**
   - **API (*Application Programming Interface*):** Contrato o puerta de entrada que permite que otros programas se conecten e intercambien datos (mediante verbos HTTP: `GET`, `POST`, `PUT`, `DELETE`).
   - **Swagger / OpenAPI:** Herramienta y especificación estándar que genera una página web interactiva documentando todos los endpoints de una API REST, sus parámetros de entrada, códigos de respuesta y botones para probar cada endpoint en vivo.

### 6.4. Pruebas de Software / Testing (`11/Testing UNLaM.ppt` — Clase 11 y Parcial 2023)
1. **Objetivo del Testing (Glenford Myers):** El testing es el proceso de ejecutar un programa con la intención de **encontrar errores**. Una buena prueba es aquella que tiene alta probabilidad de descubrir un error aún no descubierto (el testing demuestra la presencia de defectos, nunca su ausencia total).
2. **Verificación vs. Validación (Boehm):**
   - **Verificación:** *"¿Estamos construyendo el producto correctamente?"* (Compara contra la especificación técnica de diseño).
   - **Validación:** *"¿Estamos construyendo el producto correcto?"* (Compara contra las necesidades y expectativas reales del usuario/cliente).
3. **Estrategias y Niveles de Prueba (De menor a mayor alcance — Pregunta de Parcial 2023 y Recuperatorio 2023):**
   - **Pruebas Unitarias (*Unit Testing*):** Prueban el componente más pequeño del diseño (una clase o método individual) de forma aislada, generalmente aplicando **Caja Blanca** (conociendo la estructura interna del código, caminos lógicos, bucles y condiciones).
   - **Pruebas de Integración:** Prueban la interacción e interfaces entre módulos o componentes combinados (enfoque *Top-Down* usando *Stubs*, *Bottom-Up* usando *Drivers*, o *Regression Testing* / Prueba de Regresión para asegurar que un cambio nuevo no rompió lo que ya funcionaba, y *Smoke Testing* / Prueba de Humo).
   - **Pruebas de Validación / Aceptación:** Verifican los requerimientos funcionales del usuario mediante **Caja Negra** (evaluando entradas y salidas sobre la interfaz sin mirar el código interno; incluye pruebas **Alfa** en el entorno del desarrollador y pruebas **Beta** en el entorno real del cliente).
   - **Pruebas del Sistema:** Prueban el sistema completo integrado con el hardware y otros elementos (incluye **Pruebas de Recuperación** ante fallos, **Pruebas de Seguridad**, **Pruebas de Estrés / Esfuerzo** llevando el sistema al límite de carga, y **Pruebas de Rendimiento**).

### 6.5. Sistemas de Tiempo Real (STR) (`11/str-alumno.pdf` — Clase 11)
1. **¿Qué es un STR? (Págs. 2–3):** Es un sistema informático que interactúa fuertemente con un **ambiente físico real (la Planta)** donde la **validez del resultado depende NO SOLO de que la respuesta sea lógicamente correcta, sino también del INSTANTE DE TIEMPO en que se produce**.
2. **Características de un STR (Pág. 3):** Interacción con un proceso real irreversible ("el sistema no vuelve atrás"), cumplimiento de **restricciones temporales (*deadlines*)**, alta confiabilidad, concurrencia y manejo de estímulos periódicos y aperiódicos (asincrónicos).
3. **Clasificación de STR (Pág. 4):**
   - **Tiempo Real Estricto (*Hard Real Time*):** Es absolutamente crítico que la respuesta ocurra dentro del límite de tiempo; incumplir el *deadline* provoca una **catástrofe** con riesgo de vidas humanas o destrucción física (ej. control de vuelo de un avión, frenos ABS, airbag, reactor nuclear, marcapasos).
   - **Tiempo Real Blando / Flexible (*Soft Real Time*):** Se requiere respuesta rápida, pero superar ocasionalmente el límite de tiempo solo **degrada la calidad del servicio** sin causar una catástrofe (ej. streaming de video/audio, reservas online, domótica hogareña).
4. **Arquitectura de un STR: Sensores, Controlador y Actuadores (Págs. 5–12):**
   ```
   [PLANTA / MUNDO FÍSICO] ──(Magnitud Física)──► [SENSOR] ──(Señal Eléctrica/Digital)──► [SISTEMA DE CONTROL]
              ▲                                                                                    │
              └────────────────(Acción Física)─── [ACTUADOR] ◄────(Señal de Mando/Control)─────────┘
   ```
   - **Sensores (Págs. 5–8):** Dispositivos de entrada que detectan una magnitud física del mundo real (temperatura, presión, luz, movimiento, huella) y la convierten en una señal eléctrica/digital para el controlador. Según su salida se clasifican en:
     1. **Analógicos:** Entregan una señal continua variable en un rango (ej. termistor que varía voltaje de $0\text{ V}$ a $5\text{ V}$).
     2. **Digitales:** Entregan un valor numérico codificado en bits discretos.
     3. **Lógicos (Todo o Nada / Binarios):** Solo tienen **dos estados posibles** (`1` o `0`, encendido/apagado, abierto/cerrado; ej. sensor magnético de puerta o detector de presencia simple).
   - **Actuadores (Pág. 10):** Dispositivos de salida que reciben la orden del sistema de control y **modifican físicamente el mundo real (la planta)** (ej. motor eléctrico, electroválvula, relé, sirena, destrabe de molinete).

---

### 6.6. Solucionario Oficial Completo de `Clases/Clases/11/preguntasGuiaAutoEstudio-2.docx` (Arquitectura Web, HTTP, Servidores, HTML y APIs)

En la carpeta `Clases/Clases/11/preguntasGuiaAutoEstudio-2.docx` (vinculada también al TP inicial `Clases/Clases/01/TP_HTML_JavaScript_Formularios_v2.docx`), la cátedra lista el temario integral (RUP, Metodologías Ágiles, Scrum, Kanban, Historias de Usuario, UX, UML, GoF, GRASP, Arquitectura, API/Endpoint, Testing, SOA, Calidad, STR) y formula **18 preguntas específicas de Arquitectura Web, Backend y Frontend**. Aquí están todas respondidas de forma precisa y directa para el examen:

1. **¿Qué responsabilidades tiene un navegador web (*Web Browser*)?**
   - Es el cliente HTTP encargado de: (1) enviar peticiones HTTP/HTTPS al servidor a partir de una URL o acción del usuario; (2) recibir la respuesta del servidor (HTML, CSS, JavaScript, JSON, imágenes); (3) **interpretar y renderizar** el código HTML/CSS construyendo el árbol DOM para mostrar la interfaz visual al usuario; y (4) ejecutar el código JavaScript del lado del cliente y validar formularios en el frontend.
2. **¿Qué es una URL y qué partes tiene?**
   - **URL (*Uniform Resource Locator*):** Es el identificador o dirección única que permite localizar un recurso en Internet.
   - **Partes de una URL** (ej. `https://turnos.petcare.com.ar:443/api/mascotas?id=10#historial`):
     - **Protocolo o Esquema:** `https://` (o `http://`).
     - **Subdominio:** `turnos.`
     - **Dominio (y TLD):** `petcare.com.ar`
     - **Puerto *(opcional)*:** `:443` (por defecto `80` en HTTP y `443` en HTTPS).
     - **Ruta (*Path*):** `/api/mascotas` (ubicación lógica del recurso o endpoint en el servidor).
     - **Parámetros de consulta (*Query String*):** `?id=10` (pares `clave=valor` separados por `&`).
     - **Fragmento o Ancla (*Anchor*):** `#historial`.
3. **¿Qué es una petición HTTP (*HTTP Request*)?**
   - Es un mensaje estructurado de texto enviado por el cliente (navegador o aplicación) hacia un servidor siguiendo el protocolo **HTTP (*HyperText Transfer Protocol*)** para solicitar una acción sobre un recurso. Consta de: (1) **Línea de petición** (Método HTTP + URI + versión), (2) **Cabeceras (*Headers*)** con metadatos (`Content-Type`, `Authorization`, `Accept`), y (3) **Cuerpo (*Body* opcional)** con los datos enviados (ej. un JSON en un `POST`).
4. **¿Cuáles son los métodos (verbos) HTTP más comunes?**
   - **`GET`**: Solicita recuperar/consultar la representación de un recurso (no modifica datos en el servidor; es idempotente).
   - **`POST`**: Envía datos en el cuerpo de la petición para **crear** un nuevo recurso o disparar un procesamiento en el servidor.
   - **`PUT`**: Actualiza o reemplaza **íntegramente** un recurso existente.
   - **`PATCH`**: Actualiza **parcialmente** algunos campos de un recurso existente.
   - **`DELETE`**: Elimina un recurso específico en el servidor.
5. **¿Qué es un recurso en la Web?**
   - Es cualquier entidad de información o servicio identificable mediante una URI/URL a la que se puede acceder o manipular a través de la web (una página HTML, una imagen, un documento PDF o una entidad de negocio expuesta por una API REST como `/mascotas/10`).
6. **¿Qué es un dominio y qué es un subdominio?**
   - **Dominio:** Es el nombre único y legible por humanos (ej. `unlam.edu.ar` o `petcare.com`) que traduce una dirección IP numérica de un servidor a través del sistema **DNS (*Domain Name System*)**.
   - **Subdominio:** Es una subdivisión o prefijo jerárquico antepuesto al dominio principal para organizar distintas secciones o servicios independientes del sitio (ej. `miel.unlam.edu.ar`, `api.petcare.com`, `turnos.petcare.com`).
7. **¿Qué función cumple un Servidor HTTP (*Web Server*)?**
   - Escucha permanentemente peticiones entrantes en los puertos HTTP/HTTPS (`80`/`443`), procesa la solicitud y devuelve como respuesta los recursos estáticos solicitados (archivos HTML, CSS, JS, imágenes) o actúa como proxy inverso redirigiendo las peticiones dinámicas al Servidor de Aplicaciones, junto con el **código de estado HTTP** (`200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `500 Internal Server Error`).
8. **¿Qué es el *Hosting* (Alojamiento Web)?**
   - Es el servicio de infraestructura (física o en la nube) que provee servidores conectados a Internet las 24 horas para almacenar los archivos, bases de datos y artefactos de una aplicación web para que sean accesibles públicamente.
9. **¿Qué es un *Application Server* (Servidor de Aplicaciones), dónde se aloja, para qué sirve y qué softwares son los más comunes?**
   - Es el entorno de ejecución de software (*nodo de ejecución en el Diagrama de Despliegue*) alojado en el backend/datacenter que se encarga de **ejecutar la lógica de negocio (nuestros Controladores y Clases del Dominio)**, gestionar transacciones, seguridad, pools de conexiones a la Base de Datos y exponer APIs dinámicas.
   - **Softwares más comunes:** Apache Tomcat, WildFly / JBoss, GlassFish (en Java EE / Spring), IIS / Kestrel (.NET), Node.js / Express, Gunicorn / Uvicorn (Python).
10. **¿En qué se diferencia un *Web Server* de un *Application Server*?**
    - El **Web Server (Servidor Web, ej. Apache HTTP Server, Nginx)** está optimizado para servir **contenido estático** (HTML, CSS, imágenes) por protocolo HTTP y balancear carga; mientras que el **Application Server (Servidor de Aplicaciones)** ejecuta **código de negocio dinámico** en el backend, procesa reglas transaccionales y se comunica con la base de datos y sistemas externos.
11. **¿Qué es HTML y qué son las etiquetas (*Tags*)?**
    - **HTML (*HyperText Markup Language*):** Es el lenguaje de marcado estándar utilizado para definir la **estructura semántica y el contenido** de una página web (no es un lenguaje de programación).
    - **Etiquetas (*Tags*):** Son los delimitadores entre corchetes angulares (`<etiqueta>...</etiqueta>`) que le indican al navegador qué representa cada bloque de contenido (`<h1>`, `<p>`, `<table>`, `<form>`, `<input>`, `<button>`).
12. **¿Qué significa que una web sea *Responsive* (Diseño Web Adaptable)?**
    - Significa que el diseño y la disposición visual de las páginas se **adaptan automáticamente al tamaño y resolución de cualquier pantalla o dispositivo** (computadora de escritorio, notebook, tablet, teléfono móvil) mediante grillas flexibles y *Media Queries* de CSS, garantizando una buena **Usabilidad (UX)** sin necesidad de hacer zoom horizontal.
13. **¿Para qué sirve la etiqueta `<form>` en HTML?**
    - Define un **formulario interactivo** que agrupa controles de entrada de datos para que el usuario ingrese información y la envíe hacia un endpoint del servidor (definido en el atributo `action` mediante el método HTTP indicado en `method="POST"` o `"GET"`), disparando el evento que recibe nuestro **`Controller` (`C_...`)**.
14. **¿Para qué sirve la etiqueta `<input>` y cuáles son sus tipos más comunes?**
    - Es el elemento de formulario que permite capturar un dato puntual ingresado por el usuario.
    - **Tipos de `<input>` más comunes (`type="..."`):** `text` (texto simple), `password` (contraseña oculta), `number` (numérico), `email` (valida formato de correo), `date` (selector de fecha), `checkbox` (casillas de selección múltiple), `radio` (opción excluyente), `file` (adjuntar archivo/foto), `submit` (botón de envío del formulario).
15. **¿Qué significa *Renderizar* páginas web?**
    - Es el proceso mediante el cual el motor del navegador transforma el código fuente (HTML, CSS y JS) en la **representación gráfica e interactiva en píxeles** que el usuario ve en su pantalla.
16. **¿Qué es una API y para qué sirve en una aplicación web (Respuestas, Datos y Formatos)?**
    - Una **API (*Application Programming Interface*)** es un contrato de comunicación que expone un conjunto de **endpoints (URLs)** para que el Frontend (o un sistema externo) pueda solicitar servicios o intercambiar datos con el Backend sin conocer su implementación interna.
    - **Respuestas, Datos y Formatos:** Cuando el cliente invoca un endpoint de la API (por ejemplo en arquitectura **REST**), la API devuelve un **código de estado HTTP** y los **datos estructurados** serializados en formatos livianos e independientes del lenguaje, principalmente **JSON (*JavaScript Object Notation*)** o **XML** (como vimos en las integraciones con VISA, Veraz, ARCA y sistemas externos en el Diagrama de Despliegue y en el patrón GoF **Adapter**).
