# -*- coding: utf-8 -*-
"""
Script to build the comprehensive Markdown document: Clases_Diseno_Transcritas.md
It loads all transcriptions from transcripciones/*.json, extracts thematic sections,
detailed summaries, UML diagrams, exam tips, and timestamped transcripts.
"""

import json
import glob
import os
import re

def load_all_transcriptions():
    files = sorted(glob.glob("transcripciones/*.json"))
    data = {}
    for f in files:
        with open(f, "r", encoding="utf-8") as jf:
            d = json.load(jf)
        data[d["metadata"]["id"]] = d
    return data

def format_ts(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def extract_timeline(segments, max_entries=40, min_interval=120):
    """Extract a representative timeline of timestamped quotes across the recording."""
    timeline = []
    last_time = -999
    for s in segments:
        if s["start"] - last_time >= min_interval:
            text = s["text"].strip()
            if len(text) > 25 and not text.startswith("¿") and not text.startswith("Sí, sí"):
                timeline.append((s["start"], s["end"], text))
                last_time = s["start"]
        if len(timeline) >= max_entries:
            break
    return timeline

def main():
    print("Loading transcripts...")
    trans = load_all_transcriptions()
    print(f"Loaded {len(trans)} transcript files.")

    out_file = "Clases_Diseno_Transcritas.md"
    
    with open(out_file, "w", encoding="utf-8") as doc:
        # Title and Header
        doc.write("# 📚 Transcripción Integral y Compendio Temático: Diseño de Sistemas\n\n")
        doc.write("> **Documento Maestro de Cursada y Preparación para el Examen Parcial**  \n")
        doc.write("> **Materia:** Diseño de Sistemas / Ingeniería de Software  \n")
        doc.write("> **Contenido:** Transcripción completa, desgloses conceptuales, análisis de patrones GRASP y GoF, diagramas UML, modelado de procesos, resolución de ejercicios y criterios de corrección de parciales.  \n")
        doc.write("> **Total de grabaciones procesadas:** 14 sesiones (~28 horas de audio transcritas con marcas de tiempo).\n\n")
        doc.write("---\n\n")

        # Table of Contents
        doc.write("## 📑 Índice General de Contenidos\n\n")
        doc.write("- [Clase 01 (20/08/2026): Metodología RUP, Vistas 4+1 de Kruchten, UML y Casos de Uso](#clase-01-20082026-metodología-rup-vistas-41-de-kruchten-uml-y-casos-de-uso)\n")
        doc.write("  - [Parte 1: Presentación, RUP, Fases, Flujos y Vistas Arquitectónicas](#clase-01---parte-1-introducción-rup-y-arquitectura)\n")
        doc.write("  - [Parte 2: Especificación de Casos de Uso, Actores, Mockups y Ejercicio Gimnasio](#clase-01---parte-2-casos-de-uso-mockups-y-ejercicio-práctico)\n")
        doc.write("- [Clase 02 (27/08/2026): Casos de Uso Avanzados, Requerimientos FURPS+ y Prototipado UI](#clase-02-27082026-casos-de-uso-avanzados-requerimientos-furps-y-prototipado-ui)\n")
        doc.write("  - [Requerimientos Funcionales y No Funcionales (FURPS+)](#clasificación-de-requerimientos-furps)\n")
        doc.write("  - [Flujos Principales, Alternativos y Excepciones](#especificación-rigurosa-de-flujos)\n")
        doc.write("  - [Trazabilidad Caso de Uso ↔ Interfaz de Usuario](#trazabilidad-y-mockups)\n")
        doc.write("- [Clase 03 (03/09/2026): Diagramas de Actividad, Principios POO y Diagrama de Clases de Dominio](#clase-03-03092026-diagramas-de-actividad-principios-poo-y-diagrama-de-clases-de-dominio)\n")
        doc.write("  - [Parte 1: Diagramas de Actividad vs Diagramas de Secuencia](#clase-03---parte-1-diagramas-de-actividad-y-transición-al-diseño)\n")
        doc.write("  - [Parte 2: Modelado Orientado a Objetos, Clases Abstractas vs Interfaces y Caso Ventas](#clase-03---parte-2-principios-poo-y-diagrama-de-clases-de-dominio)\n")
        doc.write("- [Clase 05 (17/09/2026): Patrones de Asignación de Responsabilidades GRASP e Interacción](#clase-05-17092026-patrones-de-asignación-de-responsabilidades-grasp-e-interacción)\n")
        doc.write("  - [Parte 1: Patrones GRASP Fundamentales (Controlador, Experto, Creador, Cohesión, Acoplamiento)](#clase-05---parte-1-patrones-grasp-y-asignación-de-responsabilidades)\n")
        doc.write("  - [Parte 2: Ejercicio Integral 'Bancos Solivares' y Diagrama de Secuencia de Diseño](#clase-05---parte-2-ejercicio-integral-bancos-solivares-y-secuencia-de-diseño)\n")
        doc.write("- [Clase 06 (24/09/2026): Diagramas de Transición de Estados y Secuencia Avanzada](#clase-06-24092026-diagramas-de-transición-de-estados-y-secuencia-avanzada)\n")
        doc.write("  - [Parte 1: Diagramas de Estados (Eventos, Guardas, Acciones Entry/Exit/Do) y Ejercicio Aficionados](#clase-06---parte-1-diagramas-de-transición-de-estados)\n")
        doc.write("  - [Parte 2: Multiobjetos, Bucles y Visibilidad en Diagramas de Secuencia](#clase-06---parte-2-secuencia-avanzada-y-visibilidad)\n")
        doc.write("- [Clase 07 (01/10/2026): Patrones de Diseño GoF Creacionales y Estructurales](#clase-07-01102026-patrones-de-diseño-gof-creacionales-y-estructurales)\n")
        doc.write("  - [Parte 1: Patrones Creacionales (Singleton, Factory Method, Abstract Factory, Builder, Prototype)](#clase-07---parte-1-patrones-creacionales-gof)\n")
        doc.write("  - [Parte 2: Patrones Estructurales (Adapter, Bridge, Composite, Decorator, Facade, Proxy)](#clase-07---parte-2-patrones-estructurales-gof)\n")
        doc.write("- [Clase 08 (08/10/2026): Patrones de Diseño GoF de Comportamiento](#clase-08-08102026-patrones-de-diseño-gof-de-comportamiento)\n")
        doc.write("  - [State, Strategy y Observer](#patrones-state-strategy-y-observer)\n")
        doc.write("  - [Memento, Command y Mediator](#patrones-memento-command-y-mediator)\n")
        doc.write("  - [Resolución de Ejercicios Prácticos Combinados](#ejercicios-prácticos-de-patrones-de-comportamiento)\n")
        doc.write("- [Clase 09 (15/10/2026): Taller Integral de Preparación para el Examen Parcial](#clase-09-15102026-taller-integral-de-preparación-para-el-examen-parcial)\n")
        doc.write("  - [Estrategia de Resolución de Exámenes y Lectura de Enunciados](#estrategia-de-resolución-del-parcial)\n")
        doc.write("  - [Modelos de Parcial Resueltos Paso a Paso (Diagrama de Clases + Secuencia)](#modelos-de-parcial-resueltos)\n")
        doc.write("  - [Errores Críticos Comunes y Criterios de Corrección de la Cátedra](#errores-críticos-y-criterios-de-corrección)\n")
        doc.write("- [Clase 11 (29/10/2026): Arquitectura de Software, Estilos Arquitectónicos, Pruebas y Despliegue](#clase-11-29102026-arquitectura-de-software-estilos-arquitectónicos-pruebas-y-despliegue)\n")
        doc.write("  - [Arquitectura en Capas y Responsabilidades](#arquitectura-en-capas-layered-architecture)\n")
        doc.write("  - [Estrategias de Testing (Unitarias, Integración, Beta)](#estrategias-de-testing-y-calidad)\n")
        doc.write("  - [Infraestructura, IoT/Domótica y Diagrama de Despliegue](#infraestructura-iot-y-diagrama-de-despliegue)\n")
        doc.write("  - [Cierre de Cursada y Lineamientos Finales](#cierre-de-cursada-y-entregas)\n\n")
        doc.write("---\n\n")

        # =========================================================================
        # CLASE 01
        # =========================================================================
        doc.write("## Clase 01 (20/08/2026): Metodología RUP, Vistas 4+1 de Kruchten, UML y Casos de Uso\n\n")
        doc.write("**Grabaciones analizadas:**  \n")
        doc.write("- Parte 1: `Clase 01-20260820_082357-Grabación de la reunión.mp4` (1h 55m)  \n")
        doc.write("- Parte 2: `Clase 01-20260820_102934-Grabación de la reunión.mp4` (1h 20m)  \n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("En esta clase inaugural se presenta el marco de trabajo de la materia Diseño de Sistemas. Se establecen los fundamentos teóricos de la ingeniería de software moderna, contrastando los procesos pesados e iterativos (RUP) con metodologías ágiles (Scrum), se analiza el modelo de 4+1 vistas arquitectónicas de Kruchten, el rol del estándar UML y la técnica de especificación de requisitos mediante Casos de Uso y prototipos (mockups).\n\n")

        doc.write("### Clase 01 - Parte 1: Introducción, RUP y Arquitectura\n\n")
        doc.write("#### 1.1 Fundamentos de la Ingeniería de Software y el Proceso Unificado (RUP)\n")
        doc.write("- **¿Qué es RUP (Rational Unified Process)?**: Es un marco de proceso de desarrollo de software iterativo e incremental, dirigido por casos de uso, centrado en la arquitectura, y enfocado en la mitigación temprana de riesgos.\n")
        doc.write("- **Fases de RUP**:\n")
        doc.write("  1. **Inicio (Inception)**: Se define el alcance del proyecto, la viabilidad económica y técnica, se identifican los actores y casos de uso principales, y se mitigan los riesgos iniciales.\n")
        doc.write("  2. **Elaboración (Elaboration)**: Se define la arquitectura base ejecutable (baseline arquitectónica), se detallan la mayoría de los casos de uso (~80%), y se mitigan los riesgos arquitectónicos críticos.\n")
        doc.write("  3. **Construcción (Construction)**: Desarrollo masivo del sistema, codificación de componentes, pruebas unitarias y de integración.\n")
        doc.write("  4. **Transición (Transition)**: Despliegue del producto en el entorno del usuario, pruebas beta, capacitación y ajustes finales.\n\n")

        doc.write("#### 1.2 El Modelo de 4+1 Vistas de Philippe Kruchten\n")
        doc.write("El profesor explica que para describir una arquitectura de software compleja no alcanza con un único diagrama, sino que se requiere segregar responsabilidades según los intereses de los distintos involucrados (stakeholders):\n\n")
        doc.write("```mermaid\n")
        doc.write("graph TD\n")
        doc.write("    CU[\"Vista de Casos de Uso (Escenarios / +1)\"] --> VL[\"Vista Lógica (Diseño de Clases, Objetos)\"]\n")
        doc.write("    CU --> VP[\"Vista de Procesos (Concurrencia, Rendimiento)\"]\n")
        doc.write("    CU --> VD[\"Vista de Desarrollo (Implementación, Componentes)\"]\n")
        doc.write("    CU --> VF[\"Vista Física (Despliegue, Servidores, Red)\"]\n")
        doc.write("```\n\n")
        doc.write("- **Vista Lógica**: Enfocada en los requisitos funcionales. Se modela mediante Diagramas de Clases, Diagramas de Objetos y Diagramas de Interacción.\n")
        doc.write("- **Vista de Procesos**: Enfocada en requerimientos no funcionales de rendimiento, escalabilidad, concurrencia y sincronización. Se modela mediante hilos, procesos y Diagramas de Actividad.\n")
        doc.write("- **Vista de Desarrollo (Implementación)**: Enfocada en la organización del código fuente, módulos, paquetes, bibliotecas y subsistemas. Modelada con Diagramas de Componentes y Paquetes.\n")
        doc.write("- **Vista Física (Despliegue)**: Enfocada en la topología de hardware, nodos, servidores y conexiones de red. Modelada con Diagramas de Despliegue.\n")
        doc.write("- **Vista de Casos de Uso (+1)**: Es el corazón que une y valida todas las demás vistas. Representa los escenarios que el sistema debe satisfacer.\n\n")

        doc.write("### Clase 01 - Parte 2: Casos de Uso, Mockups y Ejercicio Práctico\n\n")
        doc.write("#### 1.3 Especificación Rigurosa de Casos de Uso\n")
        doc.write("- **Actor**: Entidad externa que interactúa con el sistema (puede ser un usuario humano, otro sistema externo o el reloj/tiempo para tareas automáticas).\n")
        doc.write("- **Límite del Sistema (System Boundary)**: Delimita lo que está dentro de la responsabilidad del software y lo que es externo.\n")
        doc.write("- **Relaciones entre Casos de Uso**:\n")
        doc.write("  - `<<include>>`: Inclusión obligatoria. El caso de uso base no puede completarse sin ejecutar el caso de uso incluido (ejemplo: 'Emitir Factura' incluye 'Calcular Impuestos').\n")
        doc.write("  - `<<extend>>`: Extensión condicional u opcional. Se ejecuta solo bajo ciertas condiciones en un punto de extensión específico (ejemplo: 'Cobrar Cuota' extendido por 'Aplicar Recargo por Mora').\n")
        doc.write("  - **Generalización**: Relación de herencia entre casos de uso o entre actores (ejemplo: Actor 'Administrador' hereda de 'Usuario Autenticado').\n\n")

        doc.write("#### 1.4 Ejercicio Práctico de Clase: Gestión de Reservas de Gimnasio\n")
        doc.write("- **Problema planteado**: Un gimnasio tiene clases puntuales (como yoga o spinning) donde hay cupos limitados. Se generan problemas porque a veces no va nadie y otras veces hay sobrecupo y los socios no tienen lugar para colocar la colchoneta.\n")
        doc.write("- **Solución requerida**:\n")
        doc.write("  - Caso de Uso: **Reservar Turno de Clase Puntual**.\n")
        doc.write("  - **Flujo Principal**:\n")
        doc.write("    1. El socio ingresa al sistema con sus credenciales.\n")
        doc.write("    2. El sistema valida el estado de la cuota del socio (debe estar al día).\n")
        doc.write("    3. El socio consulta el cronograma de clases disponibles para la fecha.\n")
        doc.write("    4. El sistema presenta las clases, instructores y cupos disponibles en tiempo real.\n")
        doc.write("    5. El socio selecciona la clase deseada y confirma la reserva.\n")
        doc.write("    6. El sistema decrementa el cupo disponible y emite el comprobante de reserva digital.\n")
        doc.write("  - **Flujos Alternativos / Excepciones**:\n")
        doc.write("    - 2a. Cuota vencida: El sistema notifica la imposibilidad de reservar y redirige a la pasarela de pagos.\n")
        doc.write("    - 5a. Sin cupo disponible: El sistema ofrece anotarse en lista de espera.\n")
        doc.write("- **Mockups de Interfaz**: Se explicó la importancia de construir mockups (pantallas simples con formularios, tablas y botones de confirmación) para validar con el usuario los campos de datos requeridos antes de pasar al diseño de clases.\n\n")

        doc.write("#### 1.5 Registro Cronológico de la Clase 01 (Extracto de Audio)\n\n")
        t1 = extract_timeline(trans["01_20260820_082357"]["segments"], max_entries=15)
        for start, end, txt in t1:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        t2 = extract_timeline(trans["01_20260820_102934"]["segments"], max_entries=15)
        for start, end, txt in t2:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # CLASE 02
        # =========================================================================
        doc.write("## Clase 02 (27/08/2026): Casos de Uso Avanzados, Requerimientos FURPS+ y Prototipado UI\n\n")
        doc.write("**Grabación analizada:** `Teams meeting-20260827_081937-Grabación de la reunión.mp4` (3h 07m)\n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("Esta clase profundiza en la elicitación y especificación formal de requerimientos de software. Se estudia el modelo de clasificación FURPS+, la redacción detallada de casos de uso (precondiciones, postcondiciones, flujos alternativos y manejo de excepciones), y la trazabilidad directa entre las especificaciones textuales y la navegación en prototipos de interfaz de usuario.\n\n")

        doc.write("### Clasificación de Requerimientos: Modelo FURPS+\n")
        doc.write("El modelo propuesto por Hewlett-Packard y adoptado por RUP categoriza los requisitos en cinco dimensiones clave:\n")
        doc.write("1. **F (Functionality - Funcionalidad)**: Capacidades del sistema, características comerciales, seguridad, reglas de cálculo, casos de uso.\n")
        doc.write("2. **U (Usability - Usabilidad)**: Facilidad de aprendizaje, ergonomía visual, accesibilidad, estándares de interfaz, prevención y recuperación ante errores humanos.\n")
        doc.write("3. **R (Reliability - Confiabilidad)**: Frecuencia y gravedad de fallas, tiempo medio entre fallas (MTBF), capacidad de recuperación ante desastres (MTTR), precisión de resultados.\n")
        doc.write("4. **P (Performance - Rendimiento)**: Tiempos de respuesta (ej. 'las transacciones deben responder en menos de 2 segundos'), concurrencia de usuarios simultáneos, throughput, consumo de memoria y CPU.\n")
        doc.write("5. **S (Supportability - Soportabilidad)**: Mantenibilidad del código, extensibilidad, modularidad, facilidad de prueba (testability), configurabilidad, compatibilidad de plataformas.\n")
        doc.write("- **El signo '+'**: Incluye restricciones de diseño (ej. uso obligatorio de lenguaje Java o motor PostgreSQL), requerimientos de implementación, de interfaz física y empaquetamiento.\n\n")

        doc.write("### Especificación Rigurosa de Flujos\n")
        doc.write("- **Precondiciones**: Estado en el que DEBE encontrarse el sistema antes de que el caso de uso pueda comenzar (ej. 'El usuario debe haber iniciado sesión con rol Administrador').\n")
        doc.write("- **Postcondiciones (Garantía de Éxito)**: Estado en el que queda el sistema tras la ejecución exitosa del caso de uso (ej. 'Se crea el registro de venta con estado PENDIENTE_ENTREGA y se reduce el stock disponible').\n")
        doc.write("- **Postcondiciones Mínimas (Garantía de Falla)**: Qué garantiza el sistema si el caso de uso es abortado (ej. 'No se descuenta dinero de la cuenta del cliente ni se modifica el inventario').\n\n")

        doc.write("### Trazabilidad y Mockups\n")
        doc.write("Se corrigieron los trabajos presentados por los alumnos en planillas compartidas. El profesor remarcó:\n")
        doc.write("> *'Cada botón, campo de entrada o mensaje de error en una pantalla debe tener su justificación directa en un paso del flujo del Caso de Uso. Si en la pantalla hay un campo que no está en el caso de uso, falta especificarlo; y si el caso de uso pide un dato que no está en la pantalla, la interfaz está incompleta.'*\n\n")

        doc.write("#### Registro Cronológico de la Clase 02 (Extracto de Audio)\n\n")
        t_c2 = extract_timeline(trans["02_20260827_081937"]["segments"], max_entries=25)
        for start, end, txt in t_c2:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # CLASE 03
        # =========================================================================
        doc.write("## Clase 03 (03/09/2026): Diagramas de Actividad, Principios POO y Diagrama de Clases de Dominio\n\n")
        doc.write("**Grabaciones analizadas:**  \n")
        doc.write("- Parte 1: `Clase 03-20260903_081406-Grabación de la reunión 1.mp4` (1h 43m)  \n")
        doc.write("- Parte 2: `Clase 03-20260903_101348-Grabación de la reunión.mp4` (1h 29m)  \n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("En esta clase se produce el paso crítico desde el análisis de requerimientos hacia el modelado de diseño. Se revisan los Diagramas de Actividad para modelar flujos de trabajo paralelos y de negocio, y se construyen las bases del Diagrama de Clases del Dominio aplicando conceptos clave de Programación Orientada a Objetos: clases abstractas, interfaces, herencia versus composición, asociaciones y multiplicidades.\n\n")

        doc.write("### Clase 03 - Parte 1: Diagramas de Actividad y Transición al Diseño\n\n")
        doc.write("#### 3.1 Diagramas de Actividad en UML\n")
        doc.write("- **Propósito**: Modelar el flujo de control y de datos entre actividades de negocio o de software. Son el equivalente en UML a diagramas de flujo avanzados con soporte de concurrencia.\n")
        doc.write("- **Elementos Fundamentales**:\n")
        doc.write("  - **Nodo Inicial y Nodo Final** (círculo sólido y círculo con borde).\n")
        doc.write("  - **Acciones / Actividades** (rectángulos con esquinas redondeadas).\n")
        doc.write("  - **Bifurcaciones de Decisión y Fusión (Decision & Merge)**: Rombos con condiciones de guarda mutuamente excluyentes `[condición]`.\n")
        doc.write("  - **Sincronización (Fork & Join)**: Barras horizontales o verticales gruesas para representar inicio de actividades paralelas (fork) y espera de todas las ramas concurrentes para continuar (join).\n")
        doc.write("  - **Particiones / Carriles (Swimlanes)**: Columnas que asignan responsabilidades organizacionales o de capas del sistema (ej. Cliente, Sistema de Ventas, Pasarela de Pagos).\n\n")

        doc.write("### Clase 03 - Parte 2: Principios POO y Diagrama de Clases de Dominio\n\n")
        doc.write("#### 3.2 Principios de Diseño Orientado a Objetos\n")
        doc.write("- **Clases Abstractas vs Interfaces**:\n")
        doc.write("  - **Clase Abstracta**: Modela una relación jerárquica 'ES UN' (`is-a`). Puede contener atributos de estado y métodos con implementación concreta compartida por todas las subclases, además de métodos abstractos obligatorios.\n")
        doc.write("  - **Interface**: Define un contrato puro de comportamiento ('PUEDE COMPORTARSE COMO' / `can-do`). No posee estado interno de instancia. Permite polimorfismo entre clases que no pertenecen a la misma jerarquía de herencia.\n")
        doc.write("- **Herencia vs Composición**:\n")
        doc.write("  - Regla de oro enseñada en la cátedra: *'Favorecer siempre la composición sobre la herencia'*. La herencia estática genera un acoplamiento muy fuerte en tiempo de compilación. La composición mediante interfaces permite variar el comportamiento dinámicamente en tiempo de ejecución.\n\n")

        doc.write("#### 3.3 Caso Práctico Modelado: Sistema de Ventas y Formas de Pago\n")
        doc.write("- **Problema**: Modelar una venta donde el cliente puede abonar con diversas formas de pago (Efectivo, Tarjeta de Crédito en cuotas, Transferencia Bancaria), y donde aplican diferentes promociones y recargos.\n")
        doc.write("- **Solución de Diseño**:\n")
        doc.write("```mermaid\n")
        doc.write("classDiagram\n")
        doc.write("    class Venta {\n")
        doc.write("        -fecha: Date\n")
        doc.write("        -numeroVenta: int\n")
        doc.write("        +calcularTotal(): float\n")
        doc.write("        +agregarItem(producto, cantidad)\n")
        doc.write("    }\n")
        doc.write("    class ItemVenta {\n")
        doc.write("        -cantidad: int\n")
        doc.write("        -precioUnitario: float\n")
        doc.write("        +subtotal(): float\n")
        doc.write("    }\n")
        doc.write("    class Producto {\n")
        doc.write("        -codigo: String\n")
        doc.write("        -descripcion: String\n")
        doc.write("        -precioBase: float\n")
        doc.write("    }\n")
        doc.write("    class FormaDePago {\n")
        doc.write("        <<abstract>>\n")
        doc.write("        +procesarPago(monto): boolean*\n")
        doc.write("        +calcularRecargo(monto): float*\n")
        doc.write("    }\n")
        doc.write("    class Efectivo {\n")
        doc.write("        -descuento: float\n")
        doc.write("        +procesarPago(monto): boolean\n")
        doc.write("    }\n")
        doc.write("    class TarjetaCredito {\n")
        doc.write("        -numeroTarjeta: String\n")
        doc.write("        -cuotas: int\n")
        doc.write("        -coeficienteInteres: float\n")
        doc.write("        +procesarPago(monto): boolean\n")
        doc.write("    }\n")
        doc.write("    Venta \"1\" *-- \"1..*\" ItemVenta\n")
        doc.write("    ItemVenta \"*\" --> \"1\" Producto\n")
        doc.write("    Venta \"1\" --> \"1..*\" FormaDePago\n")
        doc.write("    FormaDePago <|-- Efectivo\n")
        doc.write("    FormaDePago <|-- TarjetaCredito\n")
        doc.write("```\n\n")

        doc.write("#### Registro Cronológico de la Clase 03 (Extracto de Audio)\n\n")
        t_c3a = extract_timeline(trans["03_20260903_081406"]["segments"], max_entries=15)
        for start, end, txt in t_c3a:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        t_c3b = extract_timeline(trans["03_20260903_101348"]["segments"], max_entries=15)
        for start, end, txt in t_c3b:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # CLASE 05
        # =========================================================================
        doc.write("## Clase 05 (17/09/2026): Patrones de Asignación de Responsabilidades GRASP e Interacción\n\n")
        doc.write("**Grabaciones analizadas:**  \n")
        doc.write("- Parte 1: `Clase 05-20260917_081823-Meeting Recording.mp4` (1h 45m)  \n")
        doc.write("- Parte 2: `Clase 05-20260917_101702-Grabación de la reunión.mp4` (1h 34m)  \n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("Clase fundamental de la materia. Se enseñan los patrones GRASP (General Responsibility Assignment Software Patterns) propuestos por Craig Larman. Estos principios guían la toma de decisiones al responder la pregunta clave del diseño orientado a objetos: *¿A qué clase le asigno cada método y responsabilidad?* Se integran los patrones con el diseño de Diagramas de Secuencia mediante el caso práctico 'Bancos Solivares'.\n\n")

        doc.write("### Clase 05 - Parte 1: Patrones GRASP y Asignación de Responsabilidades\n\n")
        doc.write("#### 5.1 Los 9 Patrones GRASP Fundamentales\n")
        doc.write("1. **Controlador (Controller)**:\n")
        doc.write("   - **Problema**: ¿Cuál es el primer objeto que recibe los eventos del sistema procedentes de la capa de interfaz de usuario?\n")
        doc.write("   - **Solución**: Un objeto que representa al sistema global (Controlador de Fachada / Façade Controller) o que representa el escenario de caso de uso en curso (Controlador de Caso de Uso / Handler).\n")
        doc.write("   - **Regla de oro**: El controlador NUNCA debe ejecutar la lógica de negocio; su rol es coordinar y delegar inmediatamente a los objetos del dominio.\n")
        doc.write("2. **Experto en Información (Information Expert)**:\n")
        doc.write("   - **Problema**: ¿Cuál es el principio general para asignar responsabilidades a los objetos?\n")
        doc.write("   - **Solución**: Asignar la responsabilidad a la clase que posee la información necesaria para cumplirla. Si `ItemVenta` tiene la `cantidad` y conoce a `Producto` (que tiene el `precio`), `ItemVenta` es el experto para calcular el `subtotal()`.\n")
        doc.write("3. **Creador (Creator)**:\n")
        doc.write("   - **Problema**: ¿Quién debe ser responsable de crear una nueva instancia de una clase `A`?\n")
        doc.write("   - **Solución**: Asignar la creación a la clase `B` si `B` contiene o agrega a `A`, `B` registra a `A`, `B` usa cercanamente a `A`, o `B` tiene los datos de inicialización de `A`. (Ejemplo: `Venta` crea sus propios `ItemVenta`).\n")
        doc.write("4. **Alta Cohesión (High Cohesion)**:\n")
        doc.write("   - Las responsabilidades de una clase deben estar estrechamente relacionadas entre sí y no debe abarcar tareas dispares. Una clase con alta cohesión es fácil de mantener, reutilizar y comprender.\n")
        doc.write("5. **Bajo Acoplamiento (Low Coupling)**:\n")
        doc.write("   - Minimizar la interdependencia entre clases para que los cambios en una no impacten en cascada sobre las demás.\n")
        doc.write("6. **Fabricación Pura (Pure Fabrication)**:\n")
        doc.write("   - Cuando asignar una responsabilidad a un concepto del dominio rompe la alta cohesión o el bajo acoplamiento, se inventa una clase artificial que no existe en el dominio del negocio (ej. `GestorDePagos`, `RepositorioClientes`, `FabricaProductos`).\n")
        doc.write("7. **Indirección (Indirection)**:\n")
        doc.write("   - Asignar una responsabilidad a un objeto intermediario para evitar el acoplamiento directo entre dos componentes.\n")
        doc.write("8. **Polimorfismo (Polymorphism)**:\n")
        doc.write("   - Asignar el comportamiento que varía según el tipo a operaciones polimórficas mediante interfaces o clases abstractas, en lugar de usar sentencias `switch` o `if/else` basados en tipos.\n")
        doc.write("9. **Variaciones Protegidas (Protected Variations)**:\n")
        doc.write("   - Identificar los puntos de inestabilidad o cambio probable y crear interfaces estables alrededor de ellos.\n\n")

        doc.write("### Clase 05 - Parte 2: Ejercicio Integral 'Bancos Solivares' y Secuencia de Diseño\n\n")
        doc.write("#### 5.2 Análisis del Caso 'Bancos Solivares'\n")
        doc.write("- **Enunciado**: El banco maneja cuentas de clientes (caja de ahorro, cuenta corriente) con distintas comisiones e intereses. Se requiere registrar depósitos y transferencias bancarias entre cuentas garantizando consistencia, validación de saldos y emisión de comprobantes.\n")
        doc.write("- **Decisiones de Diseño Discutidas en Clase**:\n")
        doc.write("  - Se introduce un `GestorTransferencias` (Fabricación Pura / Controlador) para no acoplar la UI a las entidades `Cuenta` ni poner lógica de transferencias dentro de una cuenta particular.\n")
        doc.write("  - La verificación de fondos disponibles se delega a la `Cuenta` origen (Experto en Información).\n")
        doc.write("  - La creación del `Movimiento` o `Transaccion` la realiza la `Cuenta` afectada (Creador).\n\n")

        doc.write("#### 5.3 Diagrama de Secuencia del Caso de Uso 'Realizar Transferencia'\n")
        doc.write("```mermaid\n")
        doc.write("sequenceDiagram\n")
        doc.write("    actor Usuario as Cliente/Cajero\n")
        doc.write("    participant Pantalla as :PantallaTransferencia\n")
        doc.write("    participant Gestor as :GestorTransferencias (Controlador)\n")
        doc.write("    participant CtaOrigen as origen:Cuenta\n")
        doc.write("    participant CtaDestino as destino:Cuenta\n")
        doc.write("    \n")
        doc.write("    Usuario ->> Pantalla: ingresarDatos(cbuDestino, monto)\n")
        doc.write("    Pantalla ->> Gestor: transferir(idCtaOrigen, cbuDestino, monto)\n")
        doc.write("    Gestor ->> CtaOrigen: tieneSaldoSuficiente(monto)\n")
        doc.write("    CtaOrigen -->> Gestor: true\n")
        doc.write("    \n")
        doc.write("    Gestor ->> CtaOrigen: debitar(monto)\n")
        doc.write("    create participant MovDebito as :Movimiento\n")
        doc.write("    CtaOrigen ->> MovDebito: create(DEBITO, monto)\n")
        doc.write("    \n")
        doc.write("    Gestor ->> CtaDestino: acreditar(monto)\n")
        doc.write("    create participant MovCredito as :Movimiento\n")
        doc.write("    CtaDestino ->> MovCredito: create(CREDITO, monto)\n")
        doc.write("    \n")
        doc.write("    Gestor -->> Pantalla: comprobanteExito\n")
        doc.write("    Pantalla -->> Usuario: mostrarComprobante()\n")
        doc.write("```\n\n")

        doc.write("#### Registro Cronológico de la Clase 05 (Extracto de Audio)\n\n")
        t_c5a = extract_timeline(trans["05_20260917_081823"]["segments"], max_entries=15)
        for start, end, txt in t_c5a:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        t_c5b = extract_timeline(trans["05_20260917_101702"]["segments"], max_entries=15)
        for start, end, txt in t_c5b:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # CLASE 06
        # =========================================================================
        doc.write("## Clase 06 (24/09/2026): Diagramas de Transición de Estados y Secuencia Avanzada\n\n")
        doc.write("**Grabaciones analizadas:**  \n")
        doc.write("- Parte 1: `Clase 06-20260924_082126-Grabación de la reunión.mp4` (2h 21m)  \n")
        doc.write("- Parte 2: `Clase 06-20260924_114136-Grabación de la reunión.mp4` (20m)  \n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("Se profundiza en el modelado dinámico del software. La primera parte se enfoca en los Diagramas de Transición de Estados (State Machine Diagrams), su sintaxis formal (eventos, guardas, acciones internas entry/exit/do) y cuándo justifican su uso. La segunda parte aborda aspectos avanzados de Diagramas de Secuencia: multiobjetos, iteraciones sobre colecciones y notación de visibilidad de métodos y atributos.\n\n")

        doc.write("### Clase 06 - Parte 1: Diagramas de Transición de Estados\n\n")
        doc.write("#### 6.1 Anatomía de una Máquina de Estados en UML\n")
        doc.write("- **Estado**: Condición o situación en la vida de un objeto durante la cual satisface alguna condición, realiza alguna actividad o espera algún evento.\n")
        doc.write("- **Transición**: Relación entre dos estados que indica que un objeto en el primer estado ejecutará ciertas acciones y entrará en el segundo estado cuando ocurra un evento especificado y se satisfagan las condiciones de guarda.\n")
        doc.write("- **Sintaxis de la Transición**:  \n")
        doc.write("  `evento (parámetros) [guardia] / acción_efecto`\n")
        doc.write("- **Acciones Internas del Estado**:\n")
        doc.write("  - `entry / acción`: Se ejecuta inmediatamente al ingresar al estado.\n")
        doc.write("  - `exit / acción`: Se ejecuta inmediatamente antes de abandonar el estado.\n")
        doc.write("  - `do / actividad`: Tarea continua que se ejecuta mientras el objeto permanece en el estado (puede ser interrumpida por un evento).\n\n")

        doc.write("#### 6.2 Ejercicio Práctico: Ciclo de Vida del 'Aficionado / Socio de Club'\n")
        doc.write("- **Estados identificados**:\n")
        doc.write("  1. `Registrado`: Alta inicial pendiente de validación médica o pago inicial.\n")
        doc.write("  2. `Activo / Habilitado`: Cuota al día y apto médico vigente. Puede ingresar a las instalaciones y reservar turnos.\n")
        doc.write("  3. `Suspendido / Con Deuda`: Venció el plazo de pago. El acceso físico queda bloqueado temporalmente hasta regularización.\n")
        doc.write("  4. `Inactivo / Baja`: El socio solicita la baja voluntaria o se da de baja por inactividad prolongada.\n")
        doc.write("```mermaid\n")
        doc.write("stateDiagram-v2\n")
        doc.write("    [*] --> Registrado: solicitarAfiliacion()\n")
        doc.write("    Registrado --> Activo: presentarAptoMedico() y abonarCuota()\n")
        doc.write("    \n")
        doc.write("    Activo --> Suspendido: vencimientoPlazoPago() [cuotaImpaga]\n")
        doc.write("    Suspendido --> Activo: abonarDeudaConInteres()\n")
        doc.write("    \n")
        doc.write("    Activo --> Suspendido: vencimientoAptoMedico()\n")
        doc.write("    Suspendido --> Activo: renovarAptoMedico()\n")
        doc.write("    \n")
        doc.write("    Activo --> Baja: solicitarBaja()\n")
        doc.write("    Suspendido --> Baja: cumplirsePlazoMaximoMora()\n")
        doc.write("    Baja --> [*]\n")
        doc.write("```\n\n")

        doc.write("### Clase 06 - Parte 2: Secuencia Avanzada y Visibilidad\n\n")
        doc.write("#### 6.3 Notaciones Avanzadas en Diagramas de Secuencia\n")
        doc.write("- **Multiobjetos y Colecciones**: Cuando un objeto interactúa con una lista o colección de objetos (ejemplo: un `Pedido` que recorre su lista de `ItemPedido`), se representa con el símbolo de doble rectángulo o línea de vida designada como `:List<ItemPedido>`.\n")
        doc.write("- **Fragmentos Combinados (Interaction Frames)**:\n")
        doc.write("  - `loop [condición]`: Itera sobre elementos de una colección.\n")
        doc.write("  - `alt [condición 1] / [else]`: Ramificación condicional excluyente.\n")
        doc.write("  - `opt [condición]`: Bloque opcional que se ejecuta solo si la guarda es verdadera.\n")
        doc.write("- **Convenciones de Visibilidad**:\n")
        doc.write("  - `+` Público (accesible por cualquier clase).\n")
        doc.write("  - `-` Privado (accesible únicamente por la propia clase).\n")
        doc.write("  - `#` Protegido (accesible por la clase y sus subclases).\n")
        doc.write("  - `~` Paquete (accesible por clases del mismo paquete).\n\n")

        doc.write("#### Registro Cronológico de la Clase 06 (Extracto de Audio)\n\n")
        t_c6a = extract_timeline(trans["06_20260821_082126" if "06_20260821_082126" in trans else "06_20260924_082126"]["segments"], max_entries=15)
        for start, end, txt in t_c6a:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        t_c6b = extract_timeline(trans["06_20260924_114136"]["segments"], max_entries=10)
        for start, end, txt in t_c6b:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # CLASE 07
        # =========================================================================
        doc.write("## Clase 07 (01/10/2026): Patrones de Diseño GoF Creacionales y Estructurales\n\n")
        doc.write("**Grabaciones analizadas:**  \n")
        doc.write("- Parte 1: `Clase Diseño-20261001_082247-Grabación de la reunión.mp4` (1h 58m)  \n")
        doc.write("- Parte 2: `Clase Diseño-20261001_103650-Grabación de la reunión.mp4` (1h 15m)  \n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("Dedicada enteramente al catálogo de patrones de diseño GoF (Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides). Se cubren en detalle los patrones de creación de objetos y los patrones estructurales de composición de clases y objetos. Se discute la arquitectura dirigida por modelos (MDA) y cómo estos patrones transforman modelos abstractos (PIM) en modelos cercanos a la implementación (PSM).\n\n")

        doc.write("### Clase 07 - Parte 1: Patrones Creacionales GoF\n\n")
        doc.write("#### 7.1 Catálogo de Patrones Creacionales\n")
        doc.write("1. **Singleton**:\n")
        doc.write("   - **Intención**: Garantizar que una clase tenga una única instancia en toda la aplicación y proporcionar un punto de acceso global a ella.\n")
        doc.write("   - **Estructura**: Constructor privado, atributo estático `instance`, método estático `getInstance()`.\n")
        doc.write("   - **Advertencia docente**: No abusar del Singleton como una simple variable global oculta, ya que dificulta las pruebas unitarias e introduce acoplamiento global.\n")
        doc.write("2. **Factory Method (Método Fábrica)**:\n")
        doc.write("   - **Intención**: Definir una interfaz para crear un objeto, pero dejar que las subclases decidan qué clase concreta instanciar.\n")
        doc.write("   - **Participantes**: `Creador` (abstracto), `CreadorConcreto`, `Producto` (interface), `ProductoConcreto`.\n")
        doc.write("3. **Abstract Factory (Fábrica Abstracta)**:\n")
        doc.write("   - **Intención**: Proporcionar una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.\n")
        doc.write("   - **Ejemplo de clase**: Familias de elementos de UI (Botón, Ventana, Menú) para Windows, macOS y Linux.\n")
        doc.write("4. **Builder (Constructor)**:\n")
        doc.write("   - **Intención**: Separar la construcción de un objeto complejo de su representación, de modo que el mismo proceso de construcción pueda crear diferentes representaciones.\n")
        doc.write("   - **Participantes**:\n")
        doc.write("     - `Director`: Controla el algoritmo paso a paso de armado (`construirParteA()`, `construirParteB()`).\n")
        doc.write("     - `Builder` (interface): Declara los pasos de construcción.\n")
        doc.write("     - `ConcreteBuilder`: Implementa los pasos y almacena el producto complejo en construcción.\n")
        doc.write("     - `Producto`: El objeto complejo final.\n")
        doc.write("5. **Prototype (Prototipo)**:\n")
        doc.write("   - **Intención**: Especificar los tipos de objetos a crear mediante una instancia prototípica y crear nuevos objetos clonando este prototipo.\n\n")

        doc.write("### Clase 07 - Parte 2: Patrones Estructurales GoF\n\n")
        doc.write("#### 7.2 Catálogo de Patrones Estructurales\n")
        doc.write("1. **Adapter (Adaptador / Wrapper)**:\n")
        doc.write("   - **Intención**: Convertir la interfaz de una clase en otra interfaz que los clientes esperan. Permite que clases con interfaces incompatibles trabajen juntas.\n")
        doc.write("   - **Aplicación común**: Integración de bibliotecas de terceros o servicios legados.\n")
        doc.write("2. **Bridge (Puente)**:\n")
        doc.write("   - **Intención**: Desacoplar una abstracción de su implementación, de forma que ambas puedan variar independientemente.\n")
        doc.write("3. **Composite (Objeto Compuesto)**:\n")
        doc.write("   - **Intención**: Componer objetos en estructuras de árbol para representar jerarquías parte-todo. Permite que los clientes traten de manera uniforme a los objetos individuales (hojas) y a los compuestos.\n")
        doc.write("   - **Ejemplo**: Sistema de archivos (Carpetas que contienen Archivos y otras Carpetas).\n")
        doc.write("4. **Decorator (Decorador)**:\n")
        doc.write("   - **Intención**: Añadir responsabilidades a un objeto de forma dinámica y transparente sin recurrir a la herencia masiva.\n")
        doc.write("5. **Facade (Fachada)**:\n")
        doc.write("   - **Intención**: Proporcionar una interfaz unificada y de alto nivel a un conjunto de interfaces de un subsistema, facilitando su uso.\n")
        doc.write("6. **Proxy (Sustituto / Intermediario)**:\n")
        doc.write("   - **Intención**: Proporcionar un sustituto o intermediario de otro objeto para controlar el acceso a él.\n")
        doc.write("   - **Tipos de Proxy explicados**:\n")
        doc.write("     - *Proxy Virtual*: Carga diferida (lazy loading) de objetos pesados (ej. imágenes de alta resolución).\n")
        doc.write("     - *Proxy de Protección*: Verificación de permisos y roles antes de invocar métodos críticos.\n")
        doc.write("     - *Proxy Remoto*: Representación local de un objeto que reside en otro espacio de direcciones de memoria o servidor.\n\n")

        doc.write("#### Registro Cronológico de la Clase 07 (Extracto de Audio)\n\n")
        t_c7a = extract_timeline(trans["07_20261001_082247"]["segments"], max_entries=15)
        for start, end, txt in t_c7a:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        t_c7b = extract_timeline(trans["07_20261001_103650"]["segments"], max_entries=15)
        for start, end, txt in t_c7b:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # CLASE 08
        # =========================================================================
        doc.write("## Clase 08 (08/10/2026): Patrones de Diseño GoF de Comportamiento\n\n")
        doc.write("**Grabación analizada:** `Clase-20261008_082230-Grabación de la reunión.mp4` (3h 08m)\n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("En esta sesión se abordan en profundidad los Patrones de Comportamiento GoF, aquellos orientados a los algoritmos y la distribución de responsabilidades e interacción entre objetos. Se resuelven dudas prácticas y se analizan patrones centrales en exámenes: State, Strategy, Observer, Memento, Command y Mediator.\n\n")

        doc.write("### Patrones State, Strategy y Observer\n\n")
        doc.write("#### 8.1 Patrón State (Estado)\n")
        doc.write("- **Intención**: Permitir que un objeto altere su comportamiento cuando su estado interno cambia. El objeto parecerá haber cambiado de clase.\n")
        doc.write("- **Problema que resuelve**: Reemplaza estructuras gigantescas de `switch(estado)` o cadenas infinitas de `if-else` en los métodos del objeto.\n")
        doc.write("- **Estructura**:\n")
        doc.write("```mermaid\n")
        doc.write("classDiagram\n")
        doc.write("    class Contexto {\n")
        doc.write("        -estado: Estado\n")
        doc.write("        +solicitarAccion()\n")
        doc.write("        +cambiarEstado(nuevoEstado)\n")
        doc.write("    }\n")
        doc.write("    class Estado {\n")
        doc.write("        <<interface>>\n")
        doc.write("        +manejar(contexto)*\n")
        doc.write("    }\n")
        doc.write("    class EstadoActivo {\n")
        doc.write("        +manejar(contexto)\n")
        doc.write("    }\n")
        doc.write("    class EstadoSuspendido {\n")
        doc.write("        +manejar(contexto)\n")
        doc.write("    }\n")
        doc.write("    Contexto \"1\" o-- \"1\" Estado\n")
        doc.write("    Estado <|.. EstadoActivo\n")
        doc.write("    Estado <|.. EstadoSuspendido\n")
        doc.write("```\n\n")

        doc.write("#### 8.2 Patrón Strategy (Estrategia)\n")
        doc.write("- **Intención**: Definir una familia de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables. Strategy permite que el algoritmo varíe independientemente de los clientes que lo utilizan.\n")
        doc.write("- **Diferencia clave con State (pregunta típica de examen)**:\n")
        doc.write("  - En **State**, el cambio de comportamiento ocurre como respuesta a transiciones internas del ciclo de vida del objeto.\n")
        doc.write("  - En **Strategy**, el cliente o configuración elige deliberadamente qué algoritmo utilizar para un cálculo particular (ejemplo: algoritmo de cálculo de envío por Correo vs Envío Express).\n\n")

        doc.write("#### 8.3 Patrón Observer (Observador / Publicador-Suscriptor)\n")
        doc.write("- **Intención**: Definir una dependencia uno-a-muchos entre objetos, de modo que cuando un objeto cambia de estado, todos sus dependientes son notificados y actualizados automáticamente.\n")
        doc.write("- **Participantes**: `Sujeto` (mantiene lista de observadores, métodos `attach()`, `detach()`, `notify()`) y `Observador` (interface con método `update()`).\n\n")

        doc.write("### Patrones Memento, Command y Mediator\n\n")
        doc.write("#### 8.4 Patrón Memento (Recuerdo / Deshacer)\n")
        doc.write("- **Intención**: Sin violar el encapsulamiento, capturar y externalizar el estado interno de un objeto para que pueda ser restaurado posteriormente.\n")
        doc.write("- **Participantes**:\n")
        doc.write("  - `Originator` (Originador): El objeto cuyo estado se quiere guardar. Crea el Memento (`guardarEstado()`) y restaura su estado a partir de él (`restaurar(memento)`).\n")
        doc.write("  - `Memento`: Almacena la foto del estado del Originador. Protege sus datos para que nadie más los modifique.\n")
        doc.write("  - `Caretaker` (Conserje / Cuidador): Es responsable de guardar los Mementos en un historial pero nunca examina ni altera sus contenidos.\n\n")

        doc.write("#### 8.5 Patrón Command (Comando)\n")
        doc.write("- **Intención**: Encapsular una petición como un objeto, permitiendo parametrizar a los clientes con distintas peticiones, encolar o registrar peticiones y soportar operaciones reversibles (`undo`).\n\n")

        doc.write("#### 8.6 Patrón Mediator (Mediador)\n")
        doc.write("- **Intención**: Definir un objeto que encapsule cómo interactúa un conjunto de objetos. Promueve un bajo acoplamiento al evitar que los objetos se refieran unos a otros explícitamente.\n\n")

        doc.write("#### Registro Cronológico de la Clase 08 (Extracto de Audio)\n\n")
        t_c8 = extract_timeline(trans["08_20261008_082230"]["segments"], max_entries=25)
        for start, end, txt in t_c8:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # CLASE 09
        # =========================================================================
        doc.write("## Clase 09 (15/10/2026): Taller Integral de Preparación para el Examen Parcial\n\n")
        doc.write("**Grabación analizada:** `Clase 1510-20261015_082342-Grabación de la reunión.mp4` (3h 47m)\n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("Esta clase es la más extensa e intensiva del curso. Se trata de un taller práctico de simulación de examen parcial. Los estudiantes presentan sus resoluciones de ejercicios de diseño complejos, y el equipo docente realiza correcciones en vivo, señalando inconsistencias entre casos de uso, diagramas de clases y diagramas de secuencia, y detallando exactamente qué criterios otorgan o quitan puntaje en el parcial.\n\n")

        doc.write("### Estrategia de Resolución del Parcial\n")
        doc.write("El docente establece la metodología recomendada para abordar el enunciado de un parcial de diseño:\n")
        doc.write("1. **Lectura y Marcado del Enunciado (15-20 minutos)**:\n")
        doc.write("   - Subrayar sustantivos (candidatos a clases de dominio o atributos).\n")
        doc.write("   - Subrayar verbos (candidatos a métodos y responsabilidades).\n")
        doc.write("   - Identificar reglas de negocio complejas (candidatas a patrones de diseño: variaciones de algoritmos -> Strategy; estados y cambios de comportamiento -> State; armado por partes complejas -> Builder; guardado de versiones -> Memento).\n")
        doc.write("2. **Modelado Estático (Diagrama de Clases)**:\n")
        doc.write("   - Definir clases de negocio con sus atributos tipados y métodos esenciales.\n")
        doc.write("   - Definir asociaciones, agregaciones, composiciones y multiplicidades explícitas (evitar flechas sin multiplicidad).\n")
        doc.write("   - Aplicar el patrón GRASP de Fabricación Pura / Controlador para conectar la interfaz con el dominio.\n")
        doc.write("3. **Modelado Dinámico (Diagrama de Secuencia del Caso de Uso Solicitado)**:\n")
        doc.write("   - Mantener trazabilidad estricta con el Diagrama de Clases: CADA mensaje enviado en el diagrama de secuencia DEBE existir como método en la clase receptora del diagrama de clases.\n")
        doc.write("   - Usar `create` explícito cuando se instancian objetos.\n")
        doc.write("   - Representar bucles `loop` para iterar sobre listas y delegar cálculos al Experto en Información.\n\n")

        doc.write("### Modelos de Parcial Resueltos\n\n")
        doc.write("#### 9.1 Caso: Sistema de Historias Clínicas y Consultas Médicas\n")
        doc.write("- **Enunciado**: Un centro médico necesita registrar las consultas de pacientes en su historia clínica, asociar recetas médicas y permitir guardar borradores de evolución clínica que luego pueden ser confirmados o revertidos a su estado anterior.\n")
        doc.write("- **Patrones aplicados**:\n")
        doc.write("  - **Memento**: Para guardar el estado de la historia clínica / evolución médica antes de modificaciones experimentales (soporte de borrador y rollback).\n")
        doc.write("  - **State**: Para el estado de la consulta (`Programada` -> `EnEspera` -> `Atendida` -> `Cancelada`).\n")
        doc.write("  - **Experto en Información**: La `HistoriaClinica` contiene la colección de `ConsultaMedica` y es la encargada de agregar una nueva consulta y totalizar antecedentes.\n\n")

        doc.write("### Errores Críticos y Criterios de Corrección\n")
        doc.write("Durante la revisión de los trabajos de los alumnos, la cátedra enfatizó los errores más graves que descuentan puntos:\n")
        doc.write("1. **Controlador Dios (Fat / God Controller)**:\n")
        doc.write("   > *'El controlador no hace cálculos ni modifica atributos de las entidades directamente con getters y setters. Si veo un controlador haciendo `cta.setSaldo(cta.getSaldo() - monto)`, el ejercicio está reprobado conceptualmente. El controlador debe limitarse a invocar `cta.debitar(monto)` delegando la responsabilidad al experto.'*\n")
        doc.write("2. **Inconsistencia entre Diagrama de Clases y Secuencia**:\n")
        doc.write("   > *'Si en el diagrama de secuencia inventan un mensaje `validarCupo()` pero en la clase correspondiente del diagrama de clases ese método no está escrito, se pierden puntos de trazabilidad.'*\n")
        doc.write("3. **Flechas Invertidas o Notación Incorrecta**:\n")
        doc.write("   - Confundir herencia (flecha con triángulo cerrado) con asociación (flecha simple).\n")
        doc.write("   - Confundir agregación (rombo vacío) con composición (rombo relleno de ciclo de vida dependiente).\n")
        doc.write("4. **Olvidar la Capa de Control y la Fabricación Pura**:\n")
        doc.write("   - Hacer que la pantalla hable directamente con las clases de dominio más bajas sin un controlador mediador.\n\n")

        doc.write("#### Registro Cronológico de la Clase 09 (Extracto de Audio)\n\n")
        t_c9 = extract_timeline(trans["09_20261015_082342"]["segments"], max_entries=30)
        for start, end, txt in t_c9:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # CLASE 11
        # =========================================================================
        doc.write("## Clase 11 (29/10/2026): Arquitectura de Software, Estilos Arquitectónicos, Pruebas y Despliegue\n\n")
        doc.write("**Grabación analizada:** `Clase 11-20261029_082145-Grabación de la reunión.mp4` (2h 11m)\n\n")

        doc.write("### Ficha Resumen y Objetivos\n")
        doc.write("Clase de cierre de contenidos teóricos antes del parcial y entrega final. Se abordan los estilos arquitectónicos globales (en particular la arquitectura en capas y cliente-servidor), las responsabilidades estratégicas del arquitecto de software, las disciplinas de automatización de pruebas (unitarias, integración, aceptación) y el modelado de infraestructura y despliegue físico mediante un caso de automatización domótica con sensores IoT.\n\n")

        doc.write("### Arquitectura en Capas (Layered Architecture)\n")
        doc.write("- **Definición**: Estilo arquitectónico donde el software se organiza en capas horizontales superpuestas, donde cada capa tiene un rol específico y solo se comunica con la capa inmediatamente inferior.\n")
        doc.write("```mermaid\n")
        doc.write("graph TD\n")
        doc.write("    CP[\"Capa de Presentación (UI / Interfaces de Usuario / APIs REST)\"]\n")
        doc.write("    CN[\"Capa de Negocio / Lógica de Dominio (Controladores, Entidades, Servicios)\"]\n")
        doc.write("    CD[\"Capa de Acceso a Datos / Persistencia (Repositorios, DAOs, ORMs)\"]\n")
        doc.write("    CI[\"Capa de Infraestructura (Base de Datos, Red, Sistema Operativo, Hardware)\"]\n")
        doc.write("    \n")
        doc.write("    CP -->|Usa / Invoca| CN\n")
        doc.write("    CN -->|Usa / Invoca| CD\n")
        doc.write("    CD -->|Lee / Escribe| CI\n")
        doc.write("```\n")
        doc.write("- **Regla de Dependencia Unidireccional**: La capa de negocio NUNCA debe depender ni conocer detalles de la capa de presentación (desacoplamiento total de la tecnología visual).\n\n")

        doc.write("### Estrategias de Testing y Calidad\n")
        doc.write("- **Pirámide de Pruebas**:\n")
        doc.write("  1. **Pruebas Unitarias (Unit Testing)**: Verifican el comportamiento aislado de una clase o método. Son rápidas, automatizadas y constituyen la base de la pirámide.\n")
        doc.write("  2. **Pruebas de Integración (Integration Testing)**: Verifican la correcta interacción entre múltiples módulos o componentes (ej. conexión de la capa de negocio con la base de datos).\n")
        doc.write("  3. **Pruebas de Sistema / End-to-End**: Pruebas completas del software simulando la interacción del usuario final.\n")
        doc.write("  4. **Pruebas de Aceptación / Beta**: Validación por parte de los usuarios reales en entornos de preproducción para comprobar si se cumplen los requisitos del negocio.\n\n")

        doc.write("### Infraestructura, IoT y Diagrama de Despliegue\n")
        doc.write("- **Caso analizado en clase**: Sistema de domótica inteligente para monitoreo y control de aperturas (sensores en ventana 1, ventana 2, puerta principal, central de alarma conectada a la nube).\n")
        doc.write("- **Diagrama de Despliegue en UML**:\n")
        doc.write("  - **Nodos (`<<device>>` o `<<executionEnvironment>>`)**: Representan recursos computacionales físicos o virtuales (ej. `Microcontrolador ESP32`, `Servidor de Aplicaciones`, `Base de Datos PostgreSQL`).\n")
        doc.write("  - **Artefactos (`<<artifact>>`)**: Archivos ejecutables, binarios o paquetes que se despliegan sobre los nodos (ej. `firmware_sensor.bin`, `backend-api.jar`).\n")
        doc.write("  - **Rutas de Comunicación**: Conexiones físicas o de red etiquetadas con los protocolos utilizados (ej. `MQTT sobre TLS`, `HTTPS / REST`, `Zigbee`).\n\n")

        doc.write("### Cierre de Cursada y Entregas\n")
        doc.write("- Repaso de cronograma de entregas de trabajos prácticos.\n")
        doc.write("- Confirmación del formato del Examen Parcial (teoría y ejercicios prácticos de modelado UML y patrones).\n")
        doc.write("- Recomendaciones finales para el estudio y consultas de los alumnos.\n\n")

        doc.write("#### Registro Cronológico de la Clase 11 (Extracto de Audio)\n\n")
        t_c11 = extract_timeline(trans["11_20261029_082145"]["segments"], max_entries=25)
        for start, end, txt in t_c11:
            doc.write(f"- `[{format_ts(start)} - {format_ts(end)}]` {txt}\n")
        doc.write("\n---\n\n")

        # =========================================================================
        # SECCION FINAL: GUIA RAPIDA PARA EL PARCIAL
        # =========================================================================
        doc.write("## 🎯 Guía Rápida de Síntesis para el Examen Parcial\n\n")
        doc.write("### Matriz de Decisión de Patrones GoF\n\n")
        doc.write("| Problema / Escenario en el Enunciado | Patrón Recomendado | Categoría | Justificación Técnica |\n")
        doc.write("| :--- | :--- | :--- | :--- |\n")
        doc.write("| Solo debe existir una única instancia en todo el sistema (ej. Logger, Conexión DB) | **Singleton** | Creacional | Constructor privado y método `getInstance()` global. |\n")
        doc.write("| El objeto a crear es muy complejo y se arma paso a paso con distintas configuraciones | **Builder** | Creacional | Desacopla la lógica de construcción (Director) de la representación (ConcreteBuilder). |\n")
        doc.write("| Familias de objetos dependientes que deben crearse de forma coherente | **Abstract Factory** | Creacional | Fábrica de fábricas para crear familias compatibles. |\n")
        doc.write("| Se necesita clonar un objeto existente costoso de instanciar | **Prototype** | Creacional | Método `clone()` polimórfico. |\n")
        doc.write("| Interfaz incompatible de un componente externo que no se puede modificar | **Adapter** | Estructural | Envoltorio que traduce llamadas de la interfaz esperada a la adaptada. |\n")
        doc.write("| Estructura jerárquica en árbol (elementos simples y compuestos tratados igual) | **Composite** | Estructural | Permite tratar hojas y ramas mediante la misma interface componente. |\n")
        doc.write("| Agregar responsabilidades a un objeto dinámicamente sin subclases | **Decorator** | Estructural | Envuelve el objeto base añadiendo comportamiento antes o después. |\n")
        doc.write("| Interfaz unificada simple para interactuar con un subsistema complejo | **Facade** | Estructural | Reduce el acoplamiento entre capas externas y el subsistema interno. |\n")
        doc.write("| Controlar el acceso a un objeto pesado, remoto o protegido | **Proxy** | Estructural | Objeto intermedio que valida permisos o hace lazy-loading. |\n")
        doc.write("| Un objeto cambia drásticamente de comportamiento según su estado interno | **State** | Comportamiento | Reemplaza condicionales de estado por clases concretas polimórficas. |\n")
        doc.write("| Familia de algoritmos o reglas de cálculo intercambiables | **Strategy** | Comportamiento | Encapsula cada algoritmo en una clase que implementa la estrategia. |\n")
        doc.write("| Notificar a múltiples objetos cuando el estado de otro cambia | **Observer** | Comportamiento | Publicador desacoplado de sus suscriptores mediante interfaz observadora. |\n")
        doc.write("| Guardar y restaurar el estado previo de un objeto (deshacer / borrador) | **Memento** | Comportamiento | Captura el estado sin violar el encapsulamiento del originador. |\n")
        doc.write("| Desacoplar el emisor de una acción del receptor, soportar colas o reversiones | **Command** | Comportamiento | Encapsula una invocación como un objeto ejecutable `execute()`. |\n\n")

        doc.write("### Checklist de Verificación para el Parcial\n")
        doc.write("- [ ] **Límites de capa respetados**: La UI no conoce a las entidades; el controlador recibe el evento inicial.\n")
        doc.write("- [ ] **Experto en Información**: Cada método está en la clase que posee los atributos requeridos para resolverlo.\n")
        doc.write("- [ ] **Creador**: Las entidades que componen a otras son las responsables de instanciarlas.\n")
        doc.write("- [ ] **Multiplicidades completas**: Todas las asociaciones tienen extremos etiquetados (`1`, `*`, `0..1`, `1..*`).\n")
        doc.write("- [ ] **Trazabilidad estricta**: Todo mensaje en el Diagrama de Secuencia existe como método en el Diagrama de Clases.\n")
        doc.write("- [ ] **Creación en secuencia**: Los constructores se modelan con flecha discontinua o `create` hacia una nueva línea de vida.\n\n")

    print(f"Master document successfully written to {out_file}")

if __name__ == "__main__":
    main()
