# 02 — GUÍA COMPLETA Y PROGRESIVA DE DIAGRAMAS UML (ORIENTADA AL PARCIAL)

> **Propósito de este documento:** Desarrollar una guía profunda, didáctica y práctica de **todos los diagramas UML** incluidos en el programa de *Diseño de Sistemas*, comenzando con el desarrollo exhaustivo del **Diagrama de Clases de Diseño** y continuando con **Casos de Uso, Actividad, Secuencia, Colaboración/Comunicación, Estados, Componentes y Despliegue**, integrados bajo el **Modelo de 4+1 Vistas de Kruchten**.  
> En cada sección se distingue explícitamente:
> - **[CRITERIO CÁTEDRA / PROF. ANALÍA MARÍN]:** Cómo exige la profesora que lo resuelvas y dibujes en el parcial.
> - **[FUNDAMENTO LARMAN / SOMMERVILLE]:** La base teórica de los libros de cabecera para responder preguntas teóricas.

---

## PARTE 0: EL MARCO INTEGRADOR — LAS 4+1 VISTAS DE KRUCHTEN Y RUP

Antes de dibujar cualquier diagrama, debés comprender dónde se ubica cada uno dentro de la arquitectura del sistema (**Pregunta fija de parcial y final**: `01-Diseño de Sistemas v2.pdf` Págs. 30–46, `Parcial 1C 2024`, `Parcial 2023`, `Final Julio 2026`).

```
         ┌──────────────────────────────────────┐          ┌──────────────────────────────────────┐
         │      1. VISTA LÓGICA / DE DISEÑO     │          │   2. VISTA DE IMPLEMENTACIÓN /       │
         │  (Funcionalidad y estructura OO)     │          │        DESARROLLO (Software)         │
         │  • Diagrama de Clases                │          │  • Diagrama de Componentes           │
         │  • Diagrama de Estados               │          │  • Paquetes y Subsistemas            │
         └──────────────────┬───────────────────┘          └──────────────────┬───────────────────┘
                            │         ┌────────────────────────────┐          │
                            └────────►│   +1. VISTA DE ESCENARIOS  │◄─────────┘
                                      │      (CASOS DE USO)        │
                            ┌────────►│  • Une y valida las 4      │◄─────────┐
                            │         │    vistas entre sí         │          │
         ┌──────────────────┴───────────────────┐          ┌──────────────────┴───────────────────┐
         │         3. VISTA DE PROCESOS         │          │     4. VISTA FÍSICA / DESPLIEGUE     │
         │  (Dinámica, concurrencia, flujo)     │          │  (Topología de Hardware y Red)       │
         │  • Diagrama de Actividad             │          │  • Diagrama de Despliegue (Nodos,    │
         │  • Diag. Secuencia y Colaboración    │          │    Artefactos, Protocolos)           │
         └──────────────────────────────────────┘          └──────────────────────────────────────┘
```

| Vista de Kruchten | ¿A quién le interesa? | ¿Qué muestra? | Diagramas UML Asociados (según Cátedra) | Atributos de Calidad que evalúa |
| :--- | :--- | :--- | :--- | :--- |
| **1. Vista Lógica (o de Diseño)** | Diseñadores, Desarrolladores y Usuarios finales | La descomposición orientada a objetos del sistema: qué abstracciones existen y cómo cumplen los requerimientos funcionales. | **Diagrama de Clases**, **Diagrama de Objetos**, **Diagrama de Estados** *(Nota: en la cátedra a veces agrupan Secuencia/Colaboración entre Vista Lógica y de Procesos)*. | Reusabilidad, Mantenibilidad, Extensibilidad. |
| **2. Vista de Procesos** | Integradores de sistemas, Arquitectos | La dinámica en tiempo de ejecución: hilos de ejecución, concurrencia, sincronización y flujo de mensajes. | **Diagrama de Actividad** (con barras Fork/Join), **Diagramas de Interacción (Secuencia y Colaboración)**. | Performance (Rendimiento), Disponibilidad, Concurrencia, Tolerancia a fallos. |
| **3. Vista de Implementación (o Desarrollo)** | Programadores, Gestores de Configuración | Cómo se organiza el software en módulos, librerías, paquetes y subsistemas dentro del entorno de desarrollo. | **Diagrama de Componentes**, **Diagrama de Paquetes**. | Modularidad, Mantenibilidad, Facilidad de compilación y prueba. |
| **4. Vista Física (o de Despliegue)** | Ingenieros de Sistemas, Redes, DevOps | Cómo se mapean los componentes de software sobre los nodos físicos de hardware y cómo se comunican por red. | **Diagrama de Despliegue** (*Deployment*). | Escalabilidad, Seguridad física/red, Disponibilidad, Rendimiento de red. |
| **+1. Vista de Escenarios (Casos de Uso)** | Todos (Clientes, Analistas, Testers, Arquitectos) | Es el "pegamento" que articula e integra las otras 4 vistas a través de flujos de negocio de punta a punta. | **Diagrama de Casos de Uso** y **Especificación de Casos de Uso**. | Completitud funcional, Usabilidad, Trazabilidad. |

---

## A. DIAGRAMA DE CLASES (EL CORAZÓN DEL PARCIAL)

### A.1. ¿Qué representa y para qué sirve?
- **Definición [Larman Cap. 19 / Sommerville Cap. 5]:** El Diagrama de Clases es un diagrama **estructural y estático** perteneciente a la **Vista Lógica / de Diseño**. Representa los tipos de objetos (clases) que conforman el sistema, su estructura interna (atributos y operaciones/métodos) y las relaciones estáticas permanentes o transitorias que existen entre ellos.
- **Diferencia entre Modelo de Dominio (Análisis) y Diagrama de Clases de Diseño (DCD) [Criterio Cátedra - Clase 03 y 05]:**
  - En **Análisis**, el modelo de dominio es un "diccionario visual" de conceptos del mundo real sin métodos de software ni tipos de visibilidad.
  - En **Diseño de Sistemas (lo que te evalúa Analía Marín)**, construimos el **Diagrama de Clases de Diseño (DCD)**. Sirve como **plano directo previo a la codificación** e incluye:
    1. Clases de negocio con **atributos tipados** y **métodos con firmas reales**.
    2. **Visibilidad** explícita (`-`, `+`, `#`).
    3. **Navegabilidad** y **Multiplicidad** precisa.
    4. **Clases de Fabricación Pura / Diseño:** Controladores (`C_...`), Contenedores/Nóminas (`Padron`, `HistoriaClinica`), Interfaces (`<<interface>>`), Clases Abstractas (`<<abstract>>`) y estructuras de **Patrones GoF**.

---

### A.2. Cómo identificar las clases a partir de un enunciado (Método de los 3 Colores de la Profesora + Pasaje a Diseño)

En `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 5–6 y Pág. 8), en `Clases/Clases/03/03-CU-GYM-2026-09-03.docx` y en la **Clase 03 Parte 2 (`03_20260903_101348.txt`, `[00:52:00]`)**, la profesora enseña el **Método de Análisis del Texto con Código de Colores** y luego cómo transformarlo al Diseño:

#### Paso 1: Subrayado del Enunciado y de los Casos de Uso con 3 Colores (`EJEMPLO-Practica-Teoria-version-10.pdf` Págs. 5–6 y 8)
Al leer el texto del caso (y mirar la captura de pantalla o los diagramas base si el parcial los incluye):
1. **Color AMARILLO (Sustantivos con entidad propia) → Clases Candidatas Principales del Dominio:**
   - Buscá sustantivos que tengan **múltiples datos propios**, **ciclo de vida** o **reglas de negocio asociadas**.
   - *Ejemplo en Laboratorio (`EJEMPLO-Practica...` Pág. 8):* `Paciente`, `Turno`, `Orden`, `Estudio`, `Muestra`, `Resultado`, `Factura`, `ObraSocial`.
   - *Ejemplo en Veterinaria PetCare:* `Veterinaria`, `Usuario`, `Mascota`, `HistoriaClinica`, `Consulta`, `Diagnostico`, `Tratamiento`, `VacunaAplicada`, `Receta`, `Estudio`, `Recordatorio`, `Turno`, `Profesional`.
2. **Color VERDE (Verbos y frases verbales de negocio) → Funcionalidad / Comportamiento (Métodos):**
   - En la guía oficial de la profesora (`EJEMPLO-Practica-Teoria-version-10.pdf`, Págs. 5–6 y 8), el color **verde** resalta la **funcionalidad/comportamiento** (los verbos de negocio): *"solicitar turno"*, *"registrar orden"*, *"validar cobertura"*, *"guardar consulta"*, *"calcular peligrosidad"*, *"notificar organismo"*.
   - **Nota sobre el color verde en el Diagrama de Clases (`EJEMPLO-Practica...` Pág. 10):** Además, cuando dibuja el Diagrama de Clases del Laboratorio, la profesora pinta de **color verde la caja de la clase pasarela hacia el sistema externo (`sisExtOS`)** para distinguir visualmente la frontera de integración externa respecto de las clases propias del dominio (amarillas).
3. **Color CELESTE / AZUL CLARO (Sustantivos simples o soporte) → Atributos o Clases Secundarias:**
   - Si un sustantivo es un simple dato primitivo (texto, número, fecha, booleano) que describe a una clase amarilla y no tiene comportamiento propio, **NO es una clase, es un atributo** (`-nombre: String`, `-peso: float`, `-fechaVencimiento: Date`).
   - **¿Cuándo una característica pasa de ser Atributo (Celeste) a ser Clase (Amarillo)? [Pregunta de Clase 05 y 09]:**
     - Si "Especie" o "Categoría" es solo un texto informativo sin reglas propias, puede ser un atributo.
     - Pero si de la `Categoria`, `Plan`, `Especialidad` o `EspecificacionEstudio` dependen **precios, descuentos, valores de referencia, tiempos de ayuno o reglas de validación**, entonces **DEBE ser una Clase** asociada (para no hardcodear valores y permitir **Extensibilidad**).

#### Paso 2: Filtrado de "Falsas Clases" [Criterio Analía Marín]
Una vez que tenés tus sustantivos candidatos, **eliminá o transformá** estos 4 errores clásicos:
1. **El Sistema mismo:** Si el enunciado dice *"El sistema registra..."*, **NO crees una clase `Sistema`** (Atención: en el Parcial 1C 2026 *PetCare*, como es una **Red de Veterinarias** donde el usuario busca sucursales por ubicación y horarios y cada sucursal tiene sus profesionales, la clase `Veterinaria` **SÍ es una clase del dominio** que representa cada sucursal física de la red).
2. **Los Actores Operadores:** Si el texto dice *"La recepcionista carga el turno"* o *"El administrativo imprime..."*, `Recepcionista` es el **Actor** que usa la pantalla, **NO es una clase gestora**. Solo modelá una persona como clase del dominio si el negocio guarda datos sobre ella (ej. `Usuario`, `Profesional` que atiende el `Turno` o `Consulta` con su matrícula y horarios).
3. **Pantallas, Formularios y Reportes:** *"Pantalla de Atención"*, *"Formulario HTML"*, *"Listado por pantalla"* pertenecen a la Vista (UI), **NO van como clases del modelo de dominio**.
4. **Sustantivos sinónimos:** Si en un párrafo dice *"Dueño"* y en otro dice *"Usuario/Cliente"*, unificalos en una sola clase.

#### Paso 3: Incorporación de las Clases de Diseño (Fabricación Pura)
Al modelo de clases de dominio filtrado, agregale las clases propias de **Diseño**:
1. **Los Controladores (`C_...`):** Respetando el tope del parcial (**máximo 4 Controladores** en los parciales 2026) en la parte superior del diagrama (1 por cada gran componente funcional del sistema).
2. **Los Contenedores / Nóminas (solo cuando se requiere búsqueda global):** Clases que contienen colecciones globales de fichas individuales (`Padron` para `Aficionado`s, `Nomina` para buscar por ID), mientras que las colecciones propias de un objeto las administra su propio contenedor de dominio (`HistoriaClinica` para las `Consulta`s de una `Mascota`).
3. **Las Interfaces y Clases de los 2 Patrones GoF.**

---

### A.3. Cómo identificar Atributos y Métodos (y dónde ubicarlos)

Estructura visual de una clase en UML:
```
┌──────────────────────────────────────────────┐
│               <<estereotipo>>                │  <-- Opcional: <<abstract>>, <<interface>>, <<controller>>
│                 NombreClase                  │  <-- Sustantivo en Singular, PascalCase
├──────────────────────────────────────────────┤
│ - atributoPrivado: TipoDato                  │  <-- Compartimento de ATRIBUTOS (Estado)
│ - otroAtributo: TipoDato                     │      (NO poner acá como texto los objetos que ya
├──────────────────────────────────────────────┤       están unidos con línea de asociación, o si los
│ + metodoPublico(param: Tipo): TipoRetorno    │       ponés, que coincidan 100% con el rol de la línea)
│ - metodoAuxiliarPrivado(): Boolean           │  <-- Compartimento de MÉTODOS (Comportamiento)
└──────────────────────────────────────────────┘
```

- **Reglas para Atributos [Criterio Cátedra]:**
  - Van siempre con visibilidad **privada (`-`)** (o protegida `#` si es una superclase de una jerarquía de herencia) para respetar el **Encapsulamiento y Ocultamiento de la Información**.
  - **No poner Claves Foráneas de Base de Datos (`idCliente_FK`, `idFactura_FK`):** ¡Estamos en Orientación a Objetos, no en un DER de Base de Datos! En objetos, `Mascota` no tiene `-idDueno: int`, sino que hay una **línea de asociación** entre `Cliente` y `Mascota` (que en código equivale al atributo de referencia `-mascota: List<Mascota>` o `-dueno: Cliente`).
- **Reglas para Métodos [Criterio Cátedra]:**
  - Sus nombres siempre comienzan con un **verbo en infinitivo en `camelCase`**: `+calcularSubtotal()`, `+validarVigencia()`, `+agregarVacuna(v: VacunaAplicada)`.
  - Van con visibilidad **pública (`+`)** si son invocados por otros objetos en el Diagrama de Secuencia, o **privada (`-`)** si es un sub-cálculo interno (mensaje recursivo `self` que no debe ser llamado desde afuera).

---

### A.4. Cómo determinar Responsabilidades (Conocer vs. Hacer — Larman Cap. 16 y Clase 04)

En el PDF de la profesora (`Clases/Clases/04-Presencial/UNLaM GRASP-original-marin.pdf`, Págs. 20–23) y en Larman, una **Responsabilidad** es un **contrato u obligación de un clasificador (clase)** y se divide en dos tipos:

1. **Responsabilidades de CONOCER (Estado / Atributos y Asociaciones):**
   - Conocer sus propios datos privados encapsulados (atributos).
   - Conocer los objetos relacionados con los que está conectado (asociaciones).
   - Conocer las cosas que puede derivar o calcular a partir de lo que posee.
2. **Responsabilidades de HACER (Comportamiento / Métodos):**
   - Hacer algo él mismo (ej. crear un objeto o realizar un cálculo con sus propios datos → **Experto**).
   - Iniciar una acción en otros objetos (enviarles mensajes).
   - Controlar y coordinar actividades en otros objetos (rol del **Controlador**).

> **Traducción práctica para el parcial:**  
> *"Una responsabilidad NO es un método, sino que las responsabilidades se implementan mediante uno o más métodos que colaboran entre sí"* (`UNLaM GRASP-original-marin.pdf`, Pág. 20).  
> Para saber **en qué clase poner un método**, hacete siempre la pregunta del **Experto en Información (GRASP)**: *¿Qué clase tiene los atributos o las referencias necesarias para responder esto?* Esa clase debe tener el método.

---

### A.5. Visibilidad: de Atributos/Métodos y entre Objetos (Larman Cap. 18 y Clase 07)

Hay **dos conceptos de visibilidad** que debés dominar tanto para la práctica como para las preguntas teóricas:

#### 1. Visibilidad de Miembros dentro de la Clase (Modificadores de Acceso UML)
| Símbolo | Nombre | Significado en POO y Cuándo Usarlo en el Parcial |
| :-: | :--- | :--- |
| **`-`** | **Privado (`private`)** | Solo visible dentro de la misma clase. **Usalo en TODOS los atributos de las clases concretas** y en métodos internos auxiliares (mensajes `self`). |
| **`+`** | **Público (`public`)** | Visible por cualquier otra clase que tenga referencia a esta. **Usalo en los métodos que reciben mensajes desde otras clases en el Diagrama de Secuencia.** |
| **`#`** | **Protegido (`protected`)** | Visible por la propia clase y por sus **subclases (hijas)**. **Usalo en los atributos de las Clases Abstractas / Superclases** (ej. en `Pago`, `Producto`, `Bien`) para que sus hijas accedan a ellos directamente. |
| **`~`** | **Paquete (`package`)** | Visible solo por clases del mismo paquete/componente. (Rara vez se usa en el parcial escrito). |

#### 2. Visibilidad entre Objetos (¿Cómo puede el objeto `A` enviarle un mensaje al objeto `B`?)
Explicado por Analía Marín en **Clase 07 (`07_20261001_082247.txt`)** y en **`EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 19 y Págs. 32–33)**, basado en **Craig Larman (Cap. 18)**:

Para que un objeto emisor `A` pueda enviar un mensaje a un objeto receptor `B` en el Diagrama de Secuencia, `A` tiene que "ver" (tener una referencia a) `B` de alguna de estas **4 maneras**:

| Tipo de Visibilidad (Larman) | ¿Cómo se logra en código? | ¿Cuándo ocurre en el Parcial? | ¿Aparece en el Diagrama de Clases según Analía Marín (`EJEMPLO-Practica...` Pág. 19)? |
| :--- | :--- | :--- | :--- |
| **1. Visibilidad de Atributo (Permanente)** | `B` está declarado como un atributo de instancia dentro de la clase `A` (`private B miB;`). Persiste mientras `A` y `B` existan. | `Mascota` tiene su `HistoriaClinica`; `Consulta` tiene su `Diagnostico`, `Receta` y `VacunaAplicada`; `Factura` tiene sus `ItemFactura`. | **SÍ, SIEMPRE.** Se dibuja como **Línea continua (sólida) de Asociación / Agregación / Composición** entre `A` y `B`. |
| **2. Visibilidad de Parámetro (Transitoria)** | `B` se pasa como argumento de un método de `A`: `A.calcular(B unObjetoB)`. Dura solo mientras se ejecuta ese método. | El `Controller` busca la `Vacuna` y se la pasa por parámetro a `consulta.aplicarVacuna(v)` (o si `Consulta` guarda `v` en un atributo propio, se convierte en Visibilidad de Atributo). | **SÍ (si se detallan firmas o dependencias).** Se ve en la firma `+metodo(b: B)` o con **flecha punteada de Dependencia (`A - - - > B`)**. |
| **3. Visibilidad Local (Transitoria)** | Dentro de un método de `A`, se declara una variable local a la que se le asigna un objeto `B` (`B b = new B()` o `B b = otroObjeto.getB()`). | El `C_Atencion` llama a `hc = mascota.obtenerHistoriaClinica()` y usa `hc` localmente dentro de ese método. | **NO APARECE en el Diagrama de Clases** (*Cuadro oficial Pág. 19: "¿Aparece en el Diagrama de Clases?: No"*). Solo se observa en el **Diagrama de Secuencia**. |
| **4. Visibilidad Global** | `B` es accesible globalmente desde cualquier punto (ej. a través de un método estático `Singleton.getInstance()`). | Cuando una clase accede a una configuración global o servicio único. | Solo si se modela el patrón `Singleton`. |

---

### A.6. Asociaciones, Multiplicidad (Cardinalidad) y Navegabilidad

#### 1. Asociación (`──────`)
Representa una conexión estructural permanente (**visibilidad de atributo**) entre instancias de dos o más clases.
```
┌──────────────┐ 1          tiene          1..* ┌──────────────┐
│   Cliente    ├───────────────────────────────►│   Mascota    │
└──────────────┘                       -mascotas└──────────────┘
```
- **Nombre de la asociación:** Verbo opcional en el medio de la línea (`tiene`, `solicita`, `emite`).
- **Nombre de rol (`-mascotas`):** Indica cómo llama la clase origen al atributo que referencia a la clase destino.

#### 2. Multiplicidad y Cardinalidad
Indica **cuántas instancias** de la clase de ese extremo pueden vincularse con **una única instancia** de la clase del otro extremo:
- **`1`** (o `1..1`): Exactamente uno (obligatorio y único). Ej.: Una `HistoriaClinica` pertenece a `1` `Mascota`.
- **`0..1`**: Cero o uno (opcional). Ej.: Una `Consulta` puede generar `0..1` `Receta` (si en algunas consultas no se receta nada).
- **`0..*`** (o simplemente **`*`**): Cero o muchos. Ej.: Un `Cliente` puede haber realizado `0..*` `SolicitudViaje`.
- **`1..*`**: Uno o muchos (al menos uno obligatorio). Ej.: Una `Factura` debe tener `1..*` `DetalleFactura` (no existe una factura con 0 renglones).

#### 3. Navegabilidad (`──────►`)
- Define la dirección en la que se puede recorrer la asociación en tiempo de ejecución (quién tiene el atributo que apunta a quién):
  - **Unidireccional (`A ──────► B`):** `A` conoce a `B` (`A` tiene un atributo de tipo `B`), pero `B` **no** conoce a `A`. **En Diseño se prefiere la navegabilidad unidireccional siempre que alcance**, porque reduce el acoplamiento (si `B` no necesita enviarle mensajes a `A`, no debe conocer a `A`).
  - **Bidireccional (`A ────── B` sin flechas en los extremos):** `A` conoce a `B` y `B` conoce a `A`. Solo usala si en el negocio se navega en ambos sentidos.

---

### A.7. Agregación (`◇──`) vs. Composición (`◆──`)

Ambas son casos particulares de Asociación que modelan relaciones **"Todo / Parte"** (*Whole-Part*). **¡REGLA CRUCIAL DE DIBUJO: El rombo SIEMPRE se dibuja pegado a la clase "TODO" (la contenedora), NUNCA pegado a la parte!**

```
AGREGACIÓN (Débil / Compartida):
┌──────────────────┐          1..* ┌──────────────────┐
│ CatalogoServicios│◇─────────────►│     Servicio     │
└──────────────────┘               └──────────────────┘
 (El Todo: Catálogo)                (La Parte: puede existir sin el catálogo)

COMPOSICIÓN (Fuerte / Exclusiva / Ciclo de vida atado):
┌──────────────────┐ 1        1..* ┌──────────────────┐
│     Factura      │◆─────────────►│   ItemFactura    │
└──────────────────┘               └──────────────────┘
 (El Todo exclusivo)                (La Parte: no existe fuera de esta Factura)
```

| Característica | Agregación (Rombo Blanco `◇───`) | Composición (Rombo Negro Relleno `◆───`) |
| :--- | :--- | :--- |
| **Fuerza del vínculo** | **Débil ("tiene un").** | **Fuerte / Exclusiva ("está compuesto por").** |
| **Ciclo de vida (Destrucción)** | **Independiente:** Si se elimina el Todo (`Equipo`), las Partes (`Jugador`) **siguen existiendo** en el sistema. | **Dependiente:** Si se destruye el Todo (`Factura`, `Prestamo`, `HistoriaClinica`), sus Partes (`ItemFactura`, `Cuota`, `Consulta`) pierden sentido o se eliminan con él. |
| **Exclusividad de la Parte** | Una misma instancia de la Parte puede ser compartida por varios Todos (multiplicidad del lado del rombo puede ser `*`). | Una instancia de la Parte pertenece a **UN SOLO Todo a la vez** (la multiplicidad del lado del rombo negro es siempre **`1`**). |
| **Ejemplos de las Clases de Analía Marín** | - `Club` ◇── `Socio`<br>- `Combo` ◇── `Producto`<br>- `Equipo` ◇── `Jugador` | - `Prestamo` ◆── `Cuota` (`Banco/Banco-diagClase.png`)<br>- `Aficionado` ◆── `Huella` y `Iris` (`Estadio/Clase2.png`)<br>- `Mascota` ◆── `HistoriaClinica` ◆── `Consulta` (Clase 09)<br>- `Orden` ◆── `itemOrden` (`EJEMPLO-Practica...` Pág. 10) |

---

### A.8. Generalización / Herencia (`───▷`), Clases Abstractas (`<<abstract>>`) e Interfaces (`<<interface>>`)

#### 1. Generalización / Herencia (`Subclase ───▷ Superclase` — línea continua con triángulo blanco cerrado apuntando al Padre)
- Representa una relación taxonómica **"ES UN" (*is-a*)**, nunca un "tiene un".
- La subclase **hereda todos los atributos y métodos** de la superclase, y puede **agregar** atributos/métodos propios o **sobrescribir (redefinir)** métodos del padre (**Polimorfismo**).
- **Prueba de validación en el parcial:** Preguntate siempre: *"¿Un `PrestamoHipotecario` ES UN `Prestamo`?"* (Sí → Herencia). *"¿Un `Cliente` cambia de tipo durante su vida?"* Si un objeto necesita cambiar de clase en tiempo de ejecución o combinar varios tipos a la vez, **NO uses herencia estática** en la clase principal; usá **Composición / Patrón Strategy / State / Decorator** (Principio GoF: *"Favorecer la composición de objetos sobre la herencia de clases"*).

#### 2. Clase Abstracta vs. Interfaz (Cuadro Comparativo para Práctica y Teoría — Clase 03 Parte 2)

```
       HERENCIA DE CLASE ABSTRACTA                         REALIZACIÓN DE INTERFAZ
      ┌───────────────────────────┐                     ┌───────────────────────────┐
      │       <<abstract>>        │                     │       <<interface>>       │
      │           Pago            │                     │     IEstrategiaPrecio     │
      ├───────────────────────────┤                     ├───────────────────────────┤
      │ # monto: float            │                     │  (Sin atributos de estado)│
      │ # fecha: Date             │                     ├───────────────────────────┤
      ├───────────────────────────┤                     │ + calcularPrecio(m): float│
      │ + registrarFecha(): void  │                     └─────────────△─────────────┘
      │ + <<abstract>> procesar() │                                   ┆ (Línea punteada)
      └─────────────△─────────────┘                                   ┆
                    │ (Línea sólida)                       ┌──────────┴────────────┐
         ┌──────────┴──────────┐                           │                       │
┌────────┴────────┐   ┌────────┴────────┐         ┌────────┴────────┐     ┌────────┴────────┐
│   PagoTarjeta   │   │  PagoEfectivo   │         │ PrecioObraSocial│     │PrecioParticular │
├─────────────────┤   ├─────────────────┤         ├─────────────────┤     ├─────────────────┤
│ - nroTarjeta    │   │ - descuentoEf   │         │ - porcentajeCob │     │ - recargo       │
├─────────────────┤   ├─────────────────┤         ├─────────────────┤     ├─────────────────┤
│ + procesar()    │   │ + procesar()    │         │ + calcularPrecio│     │ + calcularPrecio│
└─────────────────┘   └─────────────────┘         └─────────────────┘     └─────────────────┘
```

| Criterio | Clase Abstracta (`<<abstract>>`) | Interfaz (`<<interface>>`) |
| :--- | :--- | :--- |
| **¿Se puede instanciar (`new`)?** | **No.** Solo se instancian sus subclases concretas. | **No.** Solo se instancian las clases concretas que la implementan. |
| **¿Tiene atributos de estado?** | **Sí** (generalmente protegidos `#` para factorizar datos comunes a todas las subclases). | **No** tiene atributos de estado (solo constantes estáticas si hiciera falta). |
| **¿Tiene métodos implementados?** | **Sí**, puede combinar métodos concretos (con código heredado) y métodos abstractos (`<<abstract>>`). | **No** (en el modelo OO puro de cátedra): solo declara **firmas de métodos públicos abstractos** (el "QUÉ" hacer, sin el "CÓMO"). |
| **Herencia múltiple** | Una clase solo puede heredar (`───▷`) de **1 sola** superclase (en Java/C#). | Una clase puede implementar (`- - -▷`) **múltiples** interfaces a la vez. |
| **Flecha UML** | **Generalización:** Línea **continua** con punta triangular vacía (`───▷`) apuntando a la clase abstracta. | **Realización:** Línea **punteada** con punta triangular vacía (`- - -▷`) apuntando a la interfaz. |

---

### A.9. Dependencias (`- - - >`)
- **Notación:** Línea **punteada** con punta de flecha abierta (`A - - - > B`).
- **Qué significa:** Es la relación más débil entre clases ("**USA UN**" temporalmente). Indica que un cambio en la especificación de `B` puede afectar a `A`, pero `A` **no** guarda una referencia permanente a `B` como atributo.
- **Cuándo aparece:**
  1. `A` recibe un objeto de tipo `B` como **parámetro** en uno de sus métodos (**Visibilidad de Parámetro**).
  2. El creador en un patrón **Factory Method** (`Creator - - - > ConcreteProduct`) que instancia y devuelve el producto sin quedárselo como atributo.
  *(Recordar que la **Visibilidad Local** no se dibuja en el Diagrama de Clases según el cuadro de la Prof. Analía Marín en `EJEMPLO-Practica-Teoria-version-10.pdf`, Pág. 19).*

---

### A.10. Clases Asociativas / Intermedias (Cuándo romper un Muchos-a-Muchos `* ── *`) y Solucionario del Caso Gimnasio (`GUIA-EjercicioGYM-Estudiantes-2026- V01.docx`)

En `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 28) y en `Clases/Clases/04/Gym/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx`, la profesora explica las **3 Reglas de Craig Larman** para saber cuándo una relación entre dos clases (`Socio` y `Clase` de gimnasio, o `Usuario` y `Veterinaria` a través de `Turno`) **requiere una clase intermedia/asociativa** (`Inscripcion` o `Turno`):

1. **Regla 1:** Cuando existe un atributo que pertenece al vínculo mismo y no a ninguna de las dos clases por separado (por ejemplo: `fechaInscripcion`, `estadoInscripcion`, `calificacion` pertenecen a `Inscripcion`, no al `Socio` ni a la `Clase`).
2. **Regla 2:** Cuando las instancias de la clase asociativa tienen un **ciclo de vida independiente** o histórico (un mismo `Socio` puede inscribirse en varias fechas o darse de baja y volver a inscribirse, quedando el historial de `Inscripcion`es).
3. **Regla 3:** Cuando la relación original es **Muchos a Muchos (`* ──── *`)** (`Un Socio se inscribe a muchas Clases, y una Clase tiene muchos Socios`) y necesitamos gestionar el cupo, la asistencia o el estado de cada vínculo individual:
   ```
   ┌──────────────┐ 1          0..* ┌──────────────┐ 0..*         1 ┌──────────────┐
   │    Socio     ├────────────────►│ Inscripcion  │◄───────────────┤    Clase     │
   └──────────────┘                 ├──────────────┤                └──────────────┘
                                    │ - fecha: Date│
                                    │ - estado     │
                                    └──────────────┘
   ```

#### Solucionario Oficial de los 10 Espacios en Blanco de `Clases/Clases/04/Gym/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx`
En la guía de autoevaluación del Caso Gimnasio, la profesora dejó 10 oraciones con espacios en blanco (`......`) sobre lectura del Diagrama de Clases y Secuencia. Aquí están las respuestas exactas verificadas con `EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 27–33):

1. *"En la parte superior del diagrama de clases se ubican los **`Controladores (Controllers)`**."*
2. *"Evitar pensar que cada clase tiene un controller para hacer un **`ABM (Alta, Baja y Modificación)`**. Eso en los parciales NO VA. Siempre vamos al **`CORE (corazón)`** del negocio."*
3. *"Para que un socio pueda inscribirse a una clase del gimnasio, debemos verificar que posea **`apto médico vigente`**, que tenga la **`cuota al día`** y que la clase tenga **`cupo disponible`**."*
4. *"Entre `Socio` y `Clase` existe una relación muchos a muchos, por lo que aparece la clase intermedia **`Inscripcion`** que registra la fecha y el estado."*
5. *"Cada mensaje que llega a un objeto en el diagrama de secuencia es un **`método`** en la clase de ese objeto."*
6. *"Si hay mensajes en el diagrama de interacción (secuencia o colaboración) que no están en el diagrama de **`Clases`**, el ejercicio está **`MAL`**."*
7. *"En el diagrama de secuencia de diseño NO se dibuja al **`Actor`**, sino que comienza directamente con el evento que llega al **`Controlador`**."*
8. *"Desde la interfaz de usuario llegan datos primitivos o **`IDs`**, con los cuales el controlador busca al objeto para obtener su **`referencia`**."*
9. *"La visibilidad de **`Atributo`** es permanente y se representa con una línea de **`Asociación`** en el diagrama de clases."*
10. *"El patrón GRASP **`Experto (en Información)`** asigna la responsabilidad a la clase que tiene la información necesaria para cumplirla."*

---

## B. DIAGRAMA DE CASOS DE USO Y ESPECIFICACIÓN (CLASE 03 Y MODELO LABORATORIO)

### B.1. Elementos del Diagrama de Casos de Uso
1. **Límite del Sistema (Rectángulo contenedor):** Encierra todos los óvalos (Casos de Uso) que pertenecen al software a construir. Los actores quedan **afuera** del rectángulo.
2. **Actores (`Stickman`):** Rol externo que interactúa con el sistema:
   - **Actor Primario (a la izquierda):** Quien inicia el Caso de Uso para alcanzar un objetivo (ej. `Socio`, `Paciente`, `Recepcionista`).
   - **Actor Secundario / Sistema Externo (a la derecha):** Quien es consultado o notificado durante la ejecución del CU para que éste pueda completarse (ej. `Sistema ARCA/AFIP`, `Sistema Veraz`, `Pasarela de Pago VISA`, `Renaper`).
3. **Relaciones entre Casos de Uso:**
   - **Inclusión (`CU Base - - - <<include>> - - > CU Incluido`):** Comportamiento **obligatorio** que siempre se ejecuta o que se factoriza porque es común a varios casos de uso.
   - **Extensión (`CU Extensor - - - <<extend>> - - > CU Base`):** Comportamiento **opcional / condicional** que se dispara solo si se cumple una condición en un punto de extensión. **¡Recordá siempre que la flecha de `<<extend>>` apunta hacia el Caso de Uso Base!**

### B.2. Plantilla Oficial de Especificación de Caso de Uso (Forma 2 — Dos Columnas de Analía Marín)
Tomada de `Clases/Clases/03/03-FORMATO-VACIO-2026-2c.docx` y `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 3–7):

| Campo | Contenido Requerido |
| :--- | :--- |
| **Nombre del Caso de Uso** | Verbo en infinitivo + Sustantivo (ej.: *Solicitar Turno de Laboratorio*) |
| **Actor Primario** | *Paciente* / *Recepcionista* |
| **Actores Secundarios** | *Servicio de Validación de Obra Social* |
| **Precondiciones** | Lo que **debe ser verdadero en el sistema ANTES** de que empiece el CU (ej.: *El usuario debe haber iniciado sesión; las especialidades deben estar cargadas*). |
| **Postcondiciones** | Cómo queda el estado del sistema **DESPUÉS** de terminar el CU:<br>- **De éxito:** *El turno queda registrado en estado Confirmado y se descuenta el cupo de la agenda.*<br>- **De fallo / alternativa:** *No se registra el turno y la agenda permanece sin cambios.* |

**Curso Normal (Camino Feliz):**

| Acción del Actor | Respuesta del Sistema |
| :--- | :--- |
| **1.** El Actor solicita iniciar el registro de un nuevo turno e ingresa el DNI del paciente. | **2.** El Sistema busca al paciente en la nómina, valida que exista y muestra sus datos personales y obra social asociada. |
| **3.** El Actor carga las prácticas médicas indicadas en la orden y selecciona la fecha y hora deseada. | **4.** El Sistema verifica los requisitos de ayuno de cada práctica, comprueba la disponibilidad en la agenda y valida la cobertura con la Obra Social. |
| **5.** El Actor confirma la reserva del turno. | **6.** El Sistema registra el turno, actualiza la disponibilidad de la agenda y emite el comprobante con las indicaciones de preparación. Fin del CU. |

**Cursos Alternativos / Excepciones:**
- **2a. El paciente no se encuentra registrado en el sistema:**
  - `2a.1` El Sistema informa que el DNI no existe y habilita la carga de datos de nuevo paciente.
  - `2a.2` El Actor ingresa nombre, apellido, fecha de nacimiento, contacto y obra social.
  - `2a.3` El Sistema registra al paciente y continúa en el paso **3**.
- **4a. La Obra Social rechaza la cobertura del estudio:**
  - `4a.1` El Sistema informa el rechazo de cobertura y ofrece cotizar el estudio en modalidad Particular.

---

## C. DIAGRAMA DE ACTIVIDAD (CLASE 03 Y CLASE 06)

- **Qué representa:** Modela el flujo de trabajo (*workflow*) procedimental paso a paso de un proceso de negocio o de un Caso de Uso, incluyendo sus bifurcaciones condicionales y **operaciones concurrentes (en paralelo)**.
- **Notación exigida por la Profesora (`EJEMPLO-Practica-Teoria-version-10.pdf` Págs. 9–10 y `Estadio/Actividades.jpg`):**
  1. **Carriles (*Swimlanes*):** Columnas verticales que dividen quién ejecuta cada actividad (ej. `Cliente` | `Sistema Web` | `Servicio Externo`).
  2. **Nodo Inicial (`●`)** y **Nodo Final de Actividad (`◉`)**.
  3. **Acciones (Rectángulos con bordes redondeados):** Siempre nombradas con **Verbo + Objeto** (`Validar Huella`, `Calcular Monto`).
  4. **Nodo de Decisión (`◇` Rombo):** Entra 1 flecha y salen 2 o más flechas con **condiciones de guarda mutuamente excluyentes entre corchetes** (`[Huella Válida]`, `[Huella Inválida]`).
  5. **Barras de Sincronización (Concurrencia):**
     - **Barra Fork (División en paralelo):** Entra 1 flecha y salen 2 o más flechas que se ejecutan al mismo tiempo (ej. en Caso Estadios: validar en paralelo con Renaper y con Policía).
     - **Barra Join (Sincronización / Unión):** Entran las ramas paralelas y sale 1 sola flecha cuando todas finalizaron.

---

## D. DIAGRAMA DE SECUENCIA DE DISEÑO (CLASE 04, 05, 06, 07 Y 09)

Es el **Punto 2 obligatorio de todos los parciales**. Muestra la interacción dinámica entre instancias (objetos) ordenada cronológicamente de arriba hacia abajo.

### D.1. Elementos y Convenciones de la Cátedra

```
Escenario: Se registra la atención médica del gato "Homero" (idMascota=10), aplicando 1 vacuna ("Antirrábica", cod=5) y 1 receta ("Pipeta").

                 :C_Atencion      :NominaMascotas     m:Mascota     hc:HistoriaClinica              :CatalogoVacunas
                      │                  │                │                 │                               │
 ●──registrarAtencion─►┌─┐               │                │                 │                               │
    (10, datos, 5...)  │ ├──buscar(10)──►┌─┐              │                 │                               │
                       │ │◄──── m ───────└─┘              │                 │                               │
                       │ │                                │                 │                               │
                       │ ├───────obtenerHC()─────────────►┌─┐               │                               │
                       │ │◄────────── hc ─────────────────└─┘               │                               │
                       │ │                                                  │                               │
                       │ ├──────────buscarVacuna(5)─────────────────────────┼──────────────────────────────►┌─┐
                       │ │◄───────────── v:Vacuna ──────────────────────────┼───────────────────────────────└─┘
                       │ │                                                  │                               │
                       │ ├──────────registrarConsulta(datos, v, ...)───────►┌─┐                             │
                       │ │                                                  │ ├──create(datos)─►┌──────────┐│
                       │ │                                                  │ │                 │c:Consulta││
                       │ │                                                  │ │                 └────┬─────┘│
                       │ │                                                  │ ├──aplicarVacuna(v)───►┌─┐    │
                       │ │                                                  │ │                      │ ├─create(v)─►┌────────────────┐
                       │ │                                                  │ │                      │ │            │va:VacunaAplicada│
                       │ │                                                  │ │                      │ │            └───────┬────────┘
                       │ │                                                  │ │                      │ ├─calcularVenc()────►┌─┐
                       │ │                                                  │ │                      │ │◄── fechaVenc ──────└─┘
                       │ │                                                  │ │◄────── ok ───────────└─┘            │
                       │ │◄───────────── consultaRegistrada ────────────────└─┘                      │              │
 ◄─── confirmacion ────└─┘
```

1. **Cajas de Objetos (Cabeceras de Líneas de Vida):**
   - Sintaxis: `nombreInstancia : NombreClase` (ej. `m : Mascota` o simplemente `:Mascota` o `:C_Atencion`), subrayado según el estándar UML porque representa una **instancia**, no la clase estática.
   - Si es una colección o contenedor de objetos del mismo tipo (multiobjeto), en StarUML o en papel se puede representar como la clase contenedora (`:Padron`, `:HistoriaClinica`, `:NominaMascotas`) o como doble cajita superpuesta `:Mascota` *(recordando siempre la regla de Analía Marín: si usás una nómina o contenedor en Secuencia, ¡debe existir en el Diagrama de Clases!)*.
2. **Mensaje Entrante del Sistema (`●───────► :C_Controller`):**
   - **SIN Actor humano.** Parte de un punto negro (o desde el borde izquierdo) hacia la barra de activación del Controlador.
3. **Tipos de Flechas de Mensajes:**
   - **Mensaje Sincrónico (`──────►` línea sólida con punta rellena):** El objeto emisor espera a que el receptor termine su foco de control (barra vertical de activación) para continuar.
   - **Mensaje de Retorno (`◄- - - -` línea punteada con flecha abierta):** Devuelve el resultado o la referencia al objeto buscado (`m`, `hc`, `true`, `montoTotal`).
   - **Mensaje de Creación (`──────►` con etiqueta `create(...)` apuntando directo a la caja `:ObjetoNuevo`):**La caja del objeto recién instanciado se dibuja más abajo en el eje vertical (en el instante exacto en que nace), no arriba de todo junto con los objetos preexistentes.
   - **Auto-mensaje / Mensaje Recursivo (`self`):** Flecha que sale de la barra de activación de un objeto y vuelve a entrar a la misma barra (un rectángulo superpuesto sobre la activación) cuando el objeto llama a un método privado propio (ej. `calcularVencimiento()`).
4. **Fragmentos Combinados (Marcos de control UML 2):**
   - **`alt [condición 1] ... [else]`**: Equivalente a un `if / else` (camino mutuamente excluyente).
   - **`opt [condición]`**: Equivalente a un `if` sin `else` (paso opcional).
   - **`loop [1..N / para cada ítem]`**: Equivalente a un `for / foreach / while` (iteración sobre una colección).

---

## E. DIAGRAMA DE COMUNICACIÓN / COLABORACIÓN (CLASE 04 Y MODELO LABORATORIO PÁG. 18)

- **Qué representa:** Es el segundo tipo de **Diagrama de Interacción** de UML. Muestra exactamente la **misma información** que el Diagrama de Secuencia, pero en lugar de usar un eje de tiempo vertical, dispone a los objetos como un **grafo de nodos conectados por enlaces (*links*)** y expresa el orden temporal mediante **números con punto decimal (numeración jerárquica de Dewey)**.
- **Cómo se numera (Anidamiento de mensajes):**
  - El mensaje inicial que entra al controlador es `1: registrarAtencion(...)`.
  - Todos los mensajes que el controlador dispara dentro de la ejecución del mensaje `1` se numeran `1.1: buscarMascota(id)`, `1.2: obtenerHC()`, `1.3: registrarConsulta(...)`.
  - A su vez, los mensajes que `:HistoriaClinica` dispara dentro de `1.3` se numeran `1.3.1: create()`, `1.3.2: aplicarVacuna(v)`, y así sucesivamente.

---

## F. DIAGRAMA DE ESTADOS (CLASE 03, 04, 06 Y FINALES DIC 2025 / JUL 2026)

### F.1. ¿Qué representa y cuándo se usa?
- Modela el **ciclo de vida completo de UNA instancia de una clase específica** (reactiva a eventos), mostrando todos los **estados** posibles por los que atraviesa desde que se crea hasta que se destruye o archiva, y qué **eventos (métodos)** provocan las **transiciones** de un estado a otro.

### F.2. Sintaxis Completa de un Estado y de una Transición (`UNLaM GRASP-original-marin.pdf` Págs. 2–5)

```
                                eventoDisparador() [condiciónGuarda] / acciónAsociada()
   ┌───────────────────────────┐                                                       ┌───────────────────────────┐
●─►│         Pendiente         ├──────────────────────────────────────────────────────►│        Confirmada         │
   ├───────────────────────────┤                                                       ├───────────────────────────┤
   │ entry / iniciarTimer15m() │                                                       │ entry / descontarCupo()   │
   │ do / esperarPago()        │                                                       │ exit / registrarCambio()  │
   │ exit / detenerTimer()     │                                                       └─────────────┬─────────────┘
   └─────────────┬─────────────┘                                                                     │
                 │ expirarTiempo() [t > 15 min] / liberarCupo()                                      │ finalizarViaje()
                 ▼                                                                                   ▼
   ┌───────────────────────────┐                                                       ┌───────────────────────────┐
   │          Vencida          ├───► ◉                                                 │        Finalizada         ├───► ◉
   └───────────────────────────┘                                                       └───────────────────────────┘
```

1. **Estado Inicial (Pseudonodo inicial `●`):** Círculo negro relleno. Todo diagrama de estados tiene **exactamente un** punto de inicio. La flecha que sale de `●` al primer estado suele llevar el evento constructor (`crear()`).
2. **Estado Simple o Compuesto (Rectángulo de bordes redondeados):**
   - **Nombre del Estado:** Siempre en **Adjetivo / Participio** (`Solicitado`, `Pendiente de Pago`, `Confirmado`, `En Preparación`, `Entregado`, `Cancelado`).
   - **Actividades internas opcionales del estado:**
     - `entry / acción`: Se ejecuta instantáneamente al **entrar** al estado.
     - `do / actividad`: Actividad continua que se ejecuta **mientras** permanece en ese estado.
     - `exit / acción`: Se ejecuta instantáneamente justo antes de **salir** del estado.
3. **Transición (Flecha dirigida de un Estado Origen a un Estado Destino):**
   - Etiqueta formal: **`evento(parámetros) [condición de guarda] / acción`**
   - **`evento`**: Es el **nombre del método** que recibe el objeto (y que debe figurar en el Diagrama de Clases) o un evento temporal (`after(15 min)`).
   - **`[condición de guarda]`**: Expresión booleana entre corchetes. La transición solo se dispara si ocurre el evento **Y** la guarda da `true` (ej. `[stock >= cantidadPedida]`).
   - **`/ acción`**: Proceso atómico e ininterrumpible que se ejecuta durante el disparo de la transición (ej. `/ emitirNotificacion()`).
4. **Estado Final (`◉` Círculo negro rodeado por un anillo):** Indica que el objeto terminó su ciclo de vida (no admite más transiciones).

---

## G. DIAGRAMA DE COMPONENTES (CLASE 04, 05, 06 Y PARCIALES 2026)

- **Ubicación:** **Vista de Implementación / Desarrollo** de Kruchten.
- **Qué representa:** Muestra cómo se divide el sistema de software en **piezas modulares, reemplazables y reutilizables (Componentes / Subsistemas)** y cómo dependen unas de otras.

### G.1. Las DOS Notaciones que utiliza la Cátedra (Conocer ambas para el Parcial)

#### 1. Notación Estándar UML 2.x (Con Interfaces Lollipop/Socket y Puertos — `UNLaM GRASP-original-marin.pdf` Págs. 12–15 y `Banco-diagComponente.png`)
1. **Componente (`<<component>>` o ícono de bloque con dos pestañitas):** Agrupa un conjunto cohesivo de clases (ej. `Gestión de Turnos`, `Atención Clínica`, `Facturación`, `Integración Externa`).
2. **Interfaz Provista (Notación "Lollipop" / Chupetín `───○`):** Servicios u operaciones que el componente **expone y ofrece** al resto del sistema.
3. **Interfaz Requerida (Notación "Socket" / Enchufe `───(`):** Servicios que el componente **necesita consumir** de otro componente para poder funcionar.
4. **Conector de Ensamblaje (*Assembly Connector* `───○)───`):** Une la interfaz requerida de un componente con la interfaz provista de otro.
5. **Puertos (Cuadraditos sobre el borde del componente):** Puntos de interacción explícitos con el entorno (usados para conectores de delegación hacia subcomponentes internos).

#### 2. Notación Simplificada de Cajas Anidadas y Dependencias (Usada en `EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 14 y en los 3 Parciales 2026) `[CONVENCIÓN PARTICULAR DE CÁTEDRA]`
En los enunciados impresos de los Parciales 1, 2 y 3 de 2026 y en la página 14 de `EJEMPLO-Practica-Teoria-version-10.pdf`, la profesora dibuja los componentes como **cajas contenedoras de módulos (con sub-cajas internas)** unidas por **flechas punteadas de dependencia (`- - - >`)**:
```
┌─────────────────────────┐       ┌─────────────────────────┐       ┌─────────────────────────┐
│ <<component>>           │       │ <<component>>           │       │ <<component>>           │
│ Atención Veterinaria    │- - - >│ Gestión Mascota / Turno │- - - >│ Gestión Usuario         │
│ ┌─────────────────────┐ │       └─────────────────────────┘       └─────────────────────────┘
│ │ Historia Clínica    │ │
│ └─────────────────────┘ │- - - >┌─────────────────────────┐
└─────────────────────────┘       │ <<component>>           │
                                  │ Notificaciones (Ext)    │
                                  └─────────────────────────┘
```
- **Regla de Oro de Trazabilidad Componente ↔ Controlador (Evaluada en Parcial 2 y Parcial 3 de 2026):**
  - En el criterio de la cátedra, **cada Componente funcional principal del sistema se traduce en 1 `Controller` (`C_...`) en el Diagrama de Clases**.
  - Si el parcial pide **"usar solo 4 controladores"** y **"modificar/mejorar el Diagrama de Componentes"**, debés agrupar los módulos de negocio con **Alta Cohesión y Bajo Acoplamiento** en **4 componentes principales** (uno por cada uno de tus 4 controladores), dejando fuera del monolito a los **Sistemas Externos** conectados mediante interfaces/dependencias bien definidas.

---

## H. DIAGRAMA DE DESPLIEGUE (CLASE 04, 05, 06 Y 11)

- **Ubicación:** **Vista Física / de Despliegue** de Kruchten.
- **Qué representa:** La arquitectura física de **Hardware (Nodos)** en tiempo de ejecución, qué **artefactos/componentes de software** corren dentro de cada nodo y mediante qué **protocolos de comunicación/red** se conectan los nodos entre sí.

### H.1. Los DOS Estilos de Diagrama de Despliegue de la Profesora (`EJEMPLO-Practica-Teoria-version-10.pdf` Págs. 15 y 16, `Banco-diagDesplieguev2.png` y `Despliegue2.png`)

1. **Estilo 1 — UML 2.0 Clásico de Nodos 3D y Artefactos (Pág. 15 y `Banco-diagDesplieguev2.png`):**
   - Muestra los **Nodos 3D (`<<device>>`)**, los entornos de ejecución (`<<executionEnvironment>>`), los **Artefactos (`<<artifact>>`)** desplegados adentro y los protocolos en cada línea.
2. **Estilo 2 — Arquitectura Física Separada por Dominios / Zonas de Red (Pág. 16 y `Despliegue2.png`) `[CONVENCIÓN PARTICULAR DE CÁTEDRA]`:**
   - Divide el plano con líneas punteadas en **Dominios o Ambientes de Red** claramente diferenciados (ej. en Laboratorio Pág. 16: `Dominio Paciente` | `Dominio Laboratorio (Red Local LAN: Servidor Web, Servidor App, Servidor BD, Impresora Código de Barras)` | `Dominio Obra Social`; en Bancos: `Cliente` | `Sucursal` | `Sede Central` | `Servicios Externos VISA/Veraz`; en Estadios: `Tótem Local` | `Servidor Estadio` | `Servidor Central AFA` | `Renaper/Policía`).

```
   [DOMINIO CLIENTE / SUCURSAL]                 [DOMINIO SERVIDOR CENTRAL]                [DOMINIO SERVICIOS EXTERNOS]
┌───────────────────────────────┐             ┌───────────────────────────────┐          ┌─────────────────────────┐
│ <<device>>                    │             │ <<device>>                    │          │ <<device>>              │
│ Terminal PC / Tótem           │   HTTPS /   │ Servidor de Aplicaciones      │  HTTPS   │ Servidor Externo        │
│ ┌───────────────────────────┐ │   REST JSON │ ┌───────────────────────────┐ │ SOAP/XML │ ┌─────────────────────┐ │
│ │ <<executionEnvironment>>  │ ├────────────►│ │ <<artifact>>              │ ├─────────►│ │ API / Web Service   │ │
│ │ Navegador Web / App       │ │             │ │ Backend_Sistema.jar       │ │  o JSON  │ └─────────────────────┘ │
│ └───────────────────────────┘ │             │ └───────────────────────────┘ │          └─────────────────────────┘
└───────────────┬───────────────┘             └───────────────┬───────────────┘
                │ USB / Bluetooth                             │ TCP/IP (JDBC)
                ▼                                             ▼
┌───────────────────────────────┐             ┌───────────────────────────────┐
│ <<device>>                    │             │ <<device>>                    │
│ Lector Código Barras / Huella │             │ Servidor de Base de Datos     │
└───────────────────────────────┘             │ ┌───────────────────────────┐ │
                                              │ │ Motor RDBMS (PostgreSQL)  │ │
                                              │ └───────────────────────────┘ │
                                              └───────────────────────────────┘
```

1. **Nodos (Cubos 3D):** Representan recursos computacionales físicos (`<<device>>`: Servidor, PC, Smartphone, Tótem, Microcontrolador PLC/Arduino en STR, Sensor, Actuador) o entornos de ejecución de software (`<<executionEnvironment>>`: Navegador Web, JVM, Contenedor Docker, Motor de BD).
2. **Artefactos (`<<artifact>>`):** Archivos físicos ejecutables desplegados dentro de los nodos (`.jar`, `.war`, `.dll`, `.exe`, scripts, esquemas de base de datos).
3. **Asociaciones de Comunicación (Líneas sólidas entre Nodos):** **SIEMPRE deben tener escrito el protocolo de red o bus físico** (`HTTPS`, `REST / JSON`, `SOAP / XML`, `TCP/IP`, `JDBC`, `MQTT`, `USB`, `Bluetooth`).
4. **Agrupación por Dominios / Ambientes:** Encerrar o rotular claramente cada zona de red (`Dominio Cliente`, `Dominio Sucursal/Local`, `Dominio Sede Central`, `Dominio Servicios Externos`).
