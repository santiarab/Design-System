# 03 — GUÍA COMPLETA DE PATRONES GRASP Y GOF (TEORÍA Y APLICACIÓN PRÁCTICA AL PARCIAL)

> **Propósito de este documento:** Dominar al 100% los **9 Patrones GRASP** y los **23 Patrones GoF** tanto para responder cualquier pregunta teórica de parcial/final como para resolver los **Puntos 1 y 3 de los parciales prácticos de la Ing. Analía Marín**.  
> **Fuentes directas:** `Clases/Clases/04-Presencial/UNLaM GRASP-original-marin.pdf`, `Clases/Clases/07/GOF-2Q-2026.pdf`, `Clases/Clases/08/ejerFutbol-2026-10-08.pdf`, `Teoria/Libros/UML y Patrones - Craig Larman.pdf`, y las correcciones de la Clase 09 (`09_20261015_082342.txt`).

---

## PARTE 1: FUNDAMENTOS TEÓRICOS DE PATRONES, COHESIÓN Y ACOPLAMIENTO

### 1.1. ¿Qué es un Patrón de Diseño y cuáles son sus Elementos Esenciales? (Pregunta Clásica de Examen)
- **Origen Histórico (`GOF-2Q-2026.pdf` Págs. 2–7):** Nace en la **Arquitectura civil** en 1977 con **Christopher Alexander** (*"Cada patrón describe un problema que ocurre una y otra vez en nuestro entorno, y describe el núcleo de la solución a ese problema, de tal manera que puedas usar esta solución un millón de veces más sin hacerlo dos veces igual"*). En 1994, la **"Banda de los Cuatro" (GoF — *Gang of Four*: Erich Gamma, Richard Helm, Ralph Johnson y John Vlissides)** publica el libro *Design Patterns*, catalogando los 23 patrones clásicos para diseño orientado a objetos.
- **Los Elementos Esenciales de un Patrón (`GOF-2Q-2026.pdf` Pág. 16 y `Parcial 1C 2024`):**
  1. **Nombre del patrón:** Vocabulario común que permite comunicar la idea de diseño en una palabra.
  2. **Problema / Objetivo (Intención y Motivación):** Describe el problema específico de diseño y el contexto en que se presenta.
  3. **Aplicabilidad (Fuerzas):** En qué situaciones se debe aplicar (y cuándo no).
  4. **Solución (Estructura y Participantes):** Describe los elementos (clases, interfaces, relaciones y responsabilidades) que componen el diseño de forma abstracta, sin atarse a un código puntual.
  5. **Consecuencias (Pros, Contras y Compromisos / *Trade-offs*):** Los resultados, beneficios (ej. mayor extensibilidad, menor acoplamiento) y costos (ej. mayor número de clases) de aplicar el patrón.

### 1.2. Diferencia Fundamental entre Patrones GRASP y Patrones GoF
| Criterio | Patrones GRASP (Craig Larman) | Patrones GoF (Gamma, Helm, Johnson, Vlissides) |
| :--- | :--- | :--- |
| **Naturaleza** | Son **9 principios fundamentales** para **asignar responsabilidades** a clases y objetos mientras diseñamos diagramas de interacción y de clases. | Son **23 soluciones estructurales/conductuales concretas** (plantillas de clases e interfaces) para resolver problemas recurrentes de diseño OO. |
| **¿Cómo se ven en el diagrama?** | Se reflejan en **quién tiene cada método y quién llama a quién** (asignación de métodos y relaciones). | Se reflejan como un **sub-grafo concreto de interfaces y clases** (ej. `Contexto` → `<<interface>> Strategy` ← `ConcreteStrategyA/B`). |

---

### 1.3. Grados de Cohesión y Acoplamiento (Diapositivas de Analía Marín y Pregunta de Final Julio 2026)

En `UNLaM GRASP-original-marin.pdf` (Págs. 39, 46 y 47) y en el **Final de Julio 2026**, se evalúan explícitamente los niveles de **Acoplamiento** y **Cohesión**:

#### A. Los 6 Tipos de Acoplamiento (De PEOR / Más Alto a MEJOR / Más Bajo)
> **Definición:** El acoplamiento mide el **grado de interdependencia o fuerza con que un módulo/clase está conectado a otros**, tiene conocimiento de ellos o depende de ellos. **Buscamos SIEMPRE BAJO ACOPLAMIENTO.**

1. **Acoplamiento de Contenido (El PEOR — Prohibido):** Un módulo `A` accede o modifica directamente los datos privados o el código interno de otro módulo `B` rompiendo su encapsulamiento (`UNLaM GRASP-original-marin.pdf`, Pág. 39).
2. **Acoplamiento Común (o Global — Malo):** Dos o más módulos acceden y modifican una misma estructura de datos global compartida (variables globales). Si cambia la estructura global, se rompen todos los módulos (`Final Julio 2026`).
3. **Acoplamiento Externo:** Dos módulos comparten un formato de datos, protocolo de comunicación o interfaz de dispositivo impuesta externamente.
4. **Acoplamiento de Control (Moderado — Evitar si es posible):** Un módulo `A` le pasa a un módulo `B` un **"flag" o bandera de control** (ej. un booleano o código `tipoOperacion = 2`) que le dicta a `B` qué flujo lógico interno (`if/switch`) debe ejecutar (`Final Julio 2026`).
5. **Acoplamiento de Estampado / Estructura (*Stamp Coupling*):** Dos módulos se pasan como parámetro un objeto o registro complejo entero cuando el módulo receptor solo necesitaba usar uno o dos campos de ese registro.
6. **Acoplamiento de Datos / Normal (El MEJOR y Deseado):** Dos módulos se comunican exclusivamente pasándose por parámetro los datos elementales (o a través de una interfaz limpia) estrictamente necesarios para realizar la tarea (`Final Julio 2026`).

#### B. Los 7 Grados de Cohesión (De PEOR / Más Baja a MEJOR / Más Alta)
> **Definición:** La cohesión mide **cuán enfocadas, relacionadas y afines entre sí están las responsabilidades de una única clase o módulo**. **Buscamos SIEMPRE ALTA COHESIÓN.** (`UNLaM GRASP-original-marin.pdf`, Págs. 46–47).

1. **Cohesión Coincidente (La PEOR):** Una clase agrupa métodos que no tienen absolutamente ninguna relación entre sí (ej. una clase `Utilidades` que calcula impuestos, imprime facturas y valida contraseñas).
2. **Cohesión Lógica:** Un módulo agrupa varias tareas similares en categoría, pero en tiempo de ejecución se elige solo una mediante un `switch/flag` (ej. un método que lee de disco, de red o de teclado según un parámetro).
3. **Cohesión Temporal:** Agrupa tareas que solo tienen en común que se ejecutan en el mismo instante de tiempo (ej. un método `inicializarSistema()` que abre conexión a BD, limpia pantalla, carga logs y saluda al usuario).
4. **Cohesión Procedimental:** Los elementos se agrupan porque siempre se ejecutan siguiendo un orden de secuencia fijo, aunque operen sobre datos distintos.
5. **Cohesión Comunicacional:** Todos los métodos del módulo operan sobre el mismo conjunto de datos de entrada o producen los mismos datos de salida.
6. **Cohesión Secuencial:** La salida de una operación dentro del módulo sirve directamente como entrada para la siguiente operación (como una línea de montaje).
7. **Cohesión Funcional (La MEJOR — Alta Cohesión en OO):** Cada clase o método realiza **una única responsabilidad bien definida** y todos sus elementos contribuyen íntegramente a ese único propósito de negocio.

---

## PARTE 2: LOS 9 PATRONES GRASP Y CÓMO JUSTIFICARLOS EN EL PARCIAL (PUNTO 1)

A continuación se detallan los **9 Patrones GRASP** (`UNLaM GRASP-original-marin.pdf` Págs. 17–77) junto con la **plantilla lista para copiar y adaptar en el Punto 1 del parcial**.

> **ATENCIÓN PARA EL PARCIAL:** En varios temas de 2026 la consigna pide: *"Justificar 2 patrones GRASP aplicados (**sin contar Controller**)"* o *"Justificar 3 patrones GRASP"*. Por eso tenés que saber justificar a la perfección **Experto en Información**, **Creador**, **Alta Cohesión / Bajo Acoplamiento**, **Polimorfismo** y **Fabricación Pura**.

| # | Patrón GRASP | Problema que Resuelve | Solución / Regla de Asignación | Cómo Justificarlo en el Parcial (Plantilla Concreta) |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Experto en Información**<br>(*Information Expert*) | ¿Cuál es el principio general para asignar una responsabilidad (método) a un objeto? | Asignar la responsabilidad a la clase que **posee la información necesaria (atributos o referencias)** para cumplirla (*"Lo hace el que conoce"*). A menudo el cumplimiento se logra colaborando entre varios expertos parciales. | *"Se aplica **Experto en Información** en la clase `[NombreClaseContenedora, ej. HistoriaClinica / Factura / PropuestaViaje]` en el método `+[nombreMetodo, ej. calcularTotal() / verificarVacunasVigentes()]`, ya que es la clase que conoce y posee la colección de `[ObjetosParte, ej. ItemFactura / VacunaAplicada]`, delegando a su vez en cada `[ObjetoParte]` la consulta de su propio atributo privado `-[atributo, ej. subtotal / fechaVencimiento]`."* |
| **2** | **Creador**<br>(*Creator*) | ¿Quién debe ser responsable de crear (`new` / `create`) una nueva instancia de la clase `A`? | Asignar a la clase `B` la responsabilidad de crear instancias de `A` si se cumple que:<br>1) `B` **agrega o contiene** objetos `A` (Composición/Agregación).<br>2) `B` **registra** instancias de `A`.<br>3) `B` utiliza estrechamente objetos `A`.<br>4) `B` **tiene los datos de inicialización** que se pasan al constructor de `A`. | *"Se aplica **Creador** en la clase `[ClaseContenedora, ej. HistoriaClinica / SolicitudViaje / Prestamo]` mediante su método `+[metodoCreador, ej. registrarConsulta() / generarCuotas()]`, el cual instancia (`create`) objetos de la clase `[ClaseCreada, ej. Consulta / Cuota]`. Esto se justifica porque `[ClaseContenedora]` contiene de forma exclusiva (composición) y registra en su colección interna a las instancias de `[ClaseCreada]`."* |
| **3** | **Controlador**<br>(*Controller*) | ¿Qué primer objeto más allá de la capa de Interfaz de Usuario (UI) debe recibir y coordinar un evento de entrada del sistema? | Asignar la responsabilidad a una clase artificial (`C_Modulo`) que represente un subsistema o caso de uso agrupado. El controlador recibe el evento, busca referencias y **delega** el trabajo en el dominio (sin hacer lógica de negocio pesada para no saturarse). | *"Se aplica **Controlador** en las clases `[C_Modulo1, C_Modulo2, C_Modulo3]`, las cuales capturan los eventos provenientes de la interfaz de usuario, desacoplando la capa de presentación (Vista) del modelo de dominio y actuando como coordinadoras que delegan las reglas de negocio en los expertos correspondientes."* |
| **4** | **Bajo Acoplamiento**<br>(*Low Coupling*) | ¿Cómo dar soporte a una baja dependencia entre clases, reducir el impacto de los cambios y aumentar la reutilización? | Asignar responsabilidades de modo que el acoplamiento (cantidad de clases que una clase conoce directamente) se mantenga bajo. Evitar que el `Controller` cree objetos internos que puede crear su propio contenedor (ej. que `Venta` cree a `Pago` en vez de que lo cree `Caja`). | *"Se aplica **Bajo Acoplamiento** al hacer que `[C_Controller]` solo se comunique con `[ClaseRaiz, ej. HistoriaClinica]` y que sea `[HistoriaClinica]` quien cree y gestione internamente a `[Consulta]` y `[VacunaAplicada]`, evitando acoplar al Controlador con todas las clases internas de detalle del dominio."* |
| **5** | **Alta Cohesión**<br>(*High Cohesion*) | ¿Cómo mantener los objetos enfocados, comprensibles, manejables y fáciles de mantener? | Asignar responsabilidades de forma que cada clase tenga un conjunto pequeño de métodos estrechamente relacionados con su abstracción. Si una clase hace demasiadas cosas no afines, dividirla y delegar. | *"Se aplica **Alta Cohesión** al separar las responsabilidades en clases específicas: `[Consulta]` solo gestiona los datos clínicos del acto médico, `[Receta]` gestiona las indicaciones farmacológicas y `[Factura]` gestiona el cálculo y cobro, evitando crear una clase monolítica o sobrecargar a `[Veterinario]` con tareas que no le corresponden."* |
| **6** | **Polimorfismo**<br>(*Polymorphism*) | ¿Cómo manejar alternativas basadas en el tipo de un objeto sin usar condicionales `if / switch` preguntando por el tipo? | Cuando el comportamiento varía según el tipo o subclase, asignar la responsabilidad usando **operaciones polimórficas** (mismo nombre de método en una superclase o interfaz `<<interface>>`, implementado distinto en cada subclase). | *"Se aplica **Polimorfismo** en la jerarquía/interfaz `[Pago / IEstrategiaPrecio / IEstado]`, donde el método `+[procesarPago() / calcularMonto()]` es invocado de forma uniforme sin usar estructuras condicionales (`if/switch`), y cada clase concreta (`[PagoTarjeta, PagoTransferencia]`) ejecuta su propia implementación específica."* |
| **7** | **Fabricación Pura**<br>(*Pure Fabrication*) | ¿A quién asignamos una responsabilidad cuando dársela a una clase del dominio violaría la Alta Cohesión y el Bajo Acoplamiento? | Crear una **clase artificial de diseño** que NO representa un concepto tangible del dominio del problema, diseñada específicamente para agrupar responsabilidades cohesivas (ej. `NominaMascotas`, `Padron`, `AdaptadorARCA`, `Notificador`). | *"Se aplica **Fabricación Pura** al diseñar la clase `[NominaClientes / Padron / AdaptadorARCA]`, la cual no es un objeto físico del dominio del negocio, sino una clase artificial creada para encapsular la responsabilidad de `[búsqueda en la colección / comunicación con el servicio externo]`, preservando la Alta Cohesión de las clases del dominio."* |
| **8** | **Indirección**<br>(*Indirection*) | ¿Cómo evitar el acoplamiento directo entre dos elementos que no deben conocerse directamente? | Asignar la responsabilidad a un **objeto intermediario** para que medie entre los otros dos componentes (base de los patrones *Adapter*, *Facade*, *Mediator*, *Proxy* y *Controller*). | *"Se aplica **Indirección** mediante la clase intermediaria `[AdaptadorARCA / C_Atencion]`, que actúa como puente entre el modelo de dominio interno y el componente externo, impidiendo que las clases de negocio dependan directamente de la API externa."* |
| **9** | **Variaciones Protegidas**<br>(*Protected Variations*) | ¿Cómo diseñar objetos y subsistemas para que la variación o inestabilidad en estos elementos no afecte negativamente a otros? | Identificar los puntos de cambio o inestabilidad previstos (ej. nuevas formas de pago, nuevos proveedores externos, nuevas reglas de cálculo) y **envolverlos detrás de una interfaz estable (`<<interface>>`)**. | *"Se aplica **Variaciones Protegidas** al encapsular el punto de inestabilidad de `[las reglas de cálculo de comisión / los servicios externos de aerolíneas]` detrás de la interfaz `<<interface>> [ICalculadorComision / IServicioReserva]`, de modo que agregar nuevas variantes en el futuro no obligue a modificar el código de las clases clientes."* |

---

## PARTE 3: CATÁLOGO COMPLETO DE LOS 23 PATRONES GOF (CON EJEMPLOS DE CÁTEDRA)

Los 23 patrones GoF se dividen en **3 Categorías** (`GOF-2Q-2026.pdf` Pág. 18):
1. **Patrones Creacionales (5):** Abstraen el proceso de instanciación de objetos, independizando al sistema de cómo se crean, componen y representan sus productos.
2. **Patrones Estructurales (7):** Tratan sobre cómo se combinan y componen clases y objetos para formar estructuras más grandes y flexibles.
3. **Patrones de Comportamiento (11):** Tratan sobre algoritmos y la asignación de responsabilidades e interacción entre objetos en tiempo de ejecución.

---

### 3.1. LOS 5 PATRONES CREACIONALES (`GOF-2Q-2026.pdf` Págs. 19–29)

#### 1. `Builder` (Constructor Paso a Paso) — ★ *ALTAMENTE RECOMENDADO PARA EL PARCIAL*
- **Problema / Intención:** Separar la construcción de un **objeto complejo** de su representación, de modo que el mismo proceso de construcción paso a paso pueda crear diferentes representaciones (o configuraciones con partes opcionales).
- **Cuándo usarlo en el Parcial:**
  - **Parcial Agencia de Viajes (2C 2026):** Armar una `PropuestaViaje` (o `PaqueteTuristico`) compleja paso a paso: `+construirVuelo()`, `+construirAlojamiento()`, `+construirExcursiones()`, `+construirSeguro()`. Un viaje corporativo y un viaje familiar usan los mismos pasos pero arman configuraciones distintas sin tener un constructor monstruoso de 15 parámetros.
  - **Parcial Veterinaria / Laboratorio / Refugio:** Construir un `InformeMedicoCompleto` o un `ContratoAdopcion` con cláusulas paso a paso.
- **Estructura UML a dibujar en tu Diagrama de Clases:**
```
┌──────────────────┐        ┌──────────────────────────────────┐
│     Director     │───────►│           <<interface>>          │
│ (ej. C_Propuesta)│        │         IPropuestaBuilder        │
├──────────────────┤        ├──────────────────────────────────┤
│ + armarViaje()   │        │ + reset(): void                  │
└──────────────────┘        │ + agregarTransporte(v): void     │
                            │ + agregarAlojamiento(h): void    │
                            │ + agregarExcursiones(l): void    │
                            │ + agregarSeguro(s): void         │
                            │ + obtenerPropuesta(): Propuesta  │
                            └─────────────────△────────────────┘
                                              ┆
                        ┌─────────────────────┴─────────────────────┐
           ┌────────────┴─────────────┐               ┌─────────────┴────────────┐
           │ PropuestaFamiliarBuilder │               │PropuestaCorporativaBuilder│
           ├──────────────────────────┤               ├──────────────────────────┤
           │ - resultado: Propuesta   │               │ - resultado: Propuesta   │
           ├──────────────────────────┤               ├──────────────────────────┤
           │ + agregarTransporte(v)   │               │ + agregarTransporte(v)   │
           │ + agregarAlojamiento(h)  │               │ + agregarAlojamiento(h)  │
           │ + obtenerPropuesta()     ├────── - - - -►│     PropuestaViaje       │ (Producto complejo)
           └──────────────────────────┘               └──────────────────────────┘
```

#### 2. `Factory Method` (Método de Fábrica / Constructor Virtual) — ★ *ALTAMENTE RECOMENDADO PARA EL PARCIAL*
- **Problema / Intención:** Definir una interfaz o clase abstracta para crear un objeto, pero **dejar que sean las subclases quienes decidan qué clase concreta instanciar**.
- **Cuándo usarlo en el Parcial:**
  - Cuando el sistema debe crear distintos tipos de objetos de una jerarquía (ej.: en **Reclamos Municipales — Final Julio 2026**: `CreadorReclamo` con subfábricas para `ReclamoLuminaria`, `ReclamoBacheo`, `ReclamoResiduos`; en **Seguridad Ciudadana — Clase 09**: crear distintos tipos de `Alerta` o `Denuncia`; en **Refugio 1C 2026**: crear distintos tipos de `Donacion` —monetaria, insumo médico, alimento— o distintos tipos de `FichaAnimal`).
- **Estructura UML:**
  - `<<abstract>> Creador` (con el método `+ <<abstract>> crearProducto(): IProducto`) ← heredan `CreadorConcretoA` y `CreadorConcretoB`.
  - `<<interface>> IProducto` (o `<<abstract>> Producto`) ← implementan `ProductoConcretoA` y `ProductoConcretoB`.

#### 3. `Abstract Factory` (Fábrica Abstracta de Familias)
- **Problema / Intención:** Proporcionar una interfaz para crear **familias de objetos relacionados o dependientes entre sí** sin especificar sus clases concretas, garantizando que los productos de una familia no se mezclen con los de otra (`Final Dic 2025` y `Final Julio 2026`).
- **Diferencia clave con Factory Method:** *Factory Method* crea **UN** tipo de producto mediante herencia del método creador; *Abstract Factory* tiene **múltiples métodos de creación** en la misma fábrica (`+crearVuelo()`, `+crearHotel()`, `+crearSeguro()`) para producir una **familia entera coherente** (ej. `FabricaViajeLowCost` vs `FabricaViajePremium`, o `FabricaDocumentacionArgentina` vs `FabricaDocumentacionExterior`).

#### 4. `Prototype` (Prototipo / Clonación)
- **Problema / Intención:** Especificar los tipos de objetos a crear por medio de una **instancia prototípica ya existente**, y crear nuevos objetos **copiando/clonando (`+clonar(): Prototipo`)** ese prototipo.
- **Cuándo usarlo en el Parcial:** Cuando un cliente o veterinario quiere **repetir una receta médica mensual idéntica**, o en la **Agencia de Viajes** cuando se toma una `PropuestaViaje` plantilla de un viaje anterior y se la **clona (`+clonar()`)** para ajustarle solo las fechas para un nuevo cliente sin volver a armarla desde cero.

#### 5. `Singleton` (Instancia Única) — *(¡OJO: No usar en Parciales 2026 donde está prohibido!)*
- **Problema / Intención:** Garantizar que una clase tenga **una única instancia** en todo el sistema y proporcionar un punto de acceso global a ella (`- instancia: Singleton` estática, constructor privado `- Singleton()` y método estático `+ getInstance(): Singleton`).
- **Por qué saberlo:** Lo preguntan en teoría/finales, pero **en la práctica de los parciales 2026 la consigna prohíbe explícitamente usarlo como uno de los 2 patrones GoF**.

---

### 3.2. LOS 7 PATRONES ESTRUCTURALES (`GOF-2Q-2026.pdf` Págs. 30–44)

#### 1. `Adapter` (Adaptador / Wrapper) — ★ *COMODÍN N° 1 PARA EL PARCIAL*
- **Problema / Intención:** Convertir la interfaz de una clase existente (generalmente un **sistema externo, API de terceros o librería legacy**) en otra interfaz que el cliente de nuestro dominio espera. Permite que clases con interfaces incompatibles trabajen juntas sin modificar su código interno.
- **Cuándo usarlo en el Parcial (¡Aparece en casi TODOS los parciales!):**
  - **Parcial Veterinaria PetCare (1C 2026):** El sistema debe comunicarse con el sistema externo **ARCA (ex AFIP)** para autorizar la factura electrónica.
  - **Parcial Agencia de Viajes (2C 2026):** El sistema debe consultar disponibilidad y tarifas en tiempo real en **sistemas externos de Aerolíneas, Cadenas de Hoteles y Aseguradoras** (que tienen formatos XML/JSON propietarios distintos).
  - **Caso Banco Solivares (Clase 05 y Clase 08 `ejerFutbol-2026-10-08.pdf` Pág. 32):** Conectarse con **VISA** y **Veraz**.
  - **Caso Estadios (Clase 06):** Conectarse con **Renaper** y **Policía**.
- **Estructura UML a dibujar en tu Diagrama de Clases:**
```
┌──────────────────┐         ┌──────────────────────────────────┐
│     Factura      │────────►│           <<interface>>          │
│  (o C_Factura)   │         │     IServicioFacturacionExt      │  <-- Target (Interfaz de nuestro dominio)
└──────────────────┘         ├──────────────────────────────────┤
                             │ + autorizarComprobante(f): String│
                             └─────────────────△────────────────┘
                                               ┆ (Realización)
                             ┌─────────────────┴────────────────┐
                             │          AdaptadorARCA           │  <-- Adapter (Traductor)
                             ├──────────────────────────────────┤
                             │ - apiArca: WebServiceARCA        │──────┐ (Asociación al Adaptee)
                             ├──────────────────────────────────┤      │
                             │ + autorizarComprobante(f): String│      ▼
                             └──────────────────────────────────┘  ┌──────────────────────────────────┐
                                                                   │          WebServiceARCA          │ <-- Adaptee (API externa incompatible)
                                                                   ├──────────────────────────────────┤
                                                                   │ + requestCAE_XML(cuit, imp): XML │
                                                                   └──────────────────────────────────┘
```

#### 2. `Composite` (Compuesto / Árbol Todo-Parte) — ★ *MUY RECOMENDADO PARA EL PARCIAL*
- **Problema / Intención:** Componer objetos en **estructuras de árbol** para representar jerarquías "Todo-Parte", permitiendo que los clientes **traten de manera uniforme a los objetos individuales (Hojas / *Leaf*) y a las composiciones de objetos (Compuestos / *Composite*)**.
- **Cuándo usarlo en el Parcial:**
  - **Parcial Agencia de Viajes (2C 2026):** Un `ComponenteServicioTuristico` (`<<interface>>` o `<<abstract>>` con `+obtenerPrecio(): float` y `+verificarDisponibilidad(): bool`) que puede ser tanto un servicio individual (**Hoja**: `Vuelo`, `EstadiaHotel`, `Excursion`, `Seguro`) como un **`PaqueteCompuesto` (Composite)** que agrupa varios servicios y otros sub-paquetes, calculando su precio como la suma (o suma con descuento) de sus hijos.
  - **Caso Laboratorio (Modelo de Parcial):** Una `PracticaMedica` que puede ser un estudio individual (**Hoja**: `Glucemia`) o un `PerfilCompuesto` (**Composite**: `Hemograma Completo` o `Hepatograma` compuesto por múltiples determinaciones hijas).
  - **Parcial Veterinaria PetCare:** Un `ServicioVeterinario` que puede ser una práctica individual (`ConsultaGeneral`, `AplicacionVacuna`) o un `PackSanitarioAnual` (Composite) que agrupa varias prácticas.

#### 3. `Decorator` (Decorador / Envoltorio Dinámico) — ★ *MUY RECOMENDADO PARA EL PARCIAL*
- **Problema / Intención:** Adjuntar **responsabilidades o funcionalidades adicionales a un objeto dinámicamente** en tiempo de ejecución, proporcionando una alternativa flexible a la herencia para extender la funcionalidad (`ejerFutbol-2026-10-08.pdf` Págs. 24–25: jugador con habilidades especiales, lesionado, cansado).
- **Cuándo usarlo en el Parcial:**
  - Cuando tenés un objeto base (ej. `ReservaViaje` o `ConsultaVeterinaria` o `Seguro`) al que se le pueden **apilar adicionales opcionales combinables** en tiempo de ejecución (ej. decorar una `PropuestaBase` con `DecoradorAsistenciaAlViajero`, `DecoradorTrasladoVIP`, `DecoradorEquipajeExtra`, donde cada decorador envuelve al componente y le suma su costo al método `+calcularCosto()`).

#### 4. `Proxy` (Apoderado / Subrogado de Control de Acceso)
- **Problema / Intención:** Proporcionar un **sustituto o intermediario** de otro objeto para **controlar el acceso a él** (`Final Dic 2025`).
- **Tipos de Proxy vistos en clase (`GOF-2Q-2Q-2026.pdf` Págs. 43–44):**
  - **Proxy de Protección:** Verifica permisos/roles antes de delegar la llamada al objeto real (ej. validar si el usuario tiene permiso para ver o modificar la `HistoriaClinica` o aprobar una `Adopcion`).
  - **Proxy Virtual (Carga diferida / *Lazy Loading*):** Retrasa la carga en memoria de objetos muy pesados (ej. imágenes de radiografías de alta resolución en `Veterinaria` o videos de visitas en `Refugio de Mascotas`) hasta que realmente se solicitan.
  - **Proxy Remoto / Caché:** Representa localmente a un objeto que está en otro espacio de direcciones o guarda en caché respuestas de servicios externos costosos.

#### 5. `Bridge` (Puente)
- **Problema / Intención:** **Desacoplar una abstracción de su implementación**, de manera que ambas puedan variar y extenderse independientemente mediante dos jerarquías separadas unidas por una asociación/agregación (`Final Dic 2025` y `Final Julio 2026`).

#### 6. `Flyweight` (Peso Mosca)
- **Problema / Intención:** Usar el uso compartido para soportar eficientemente **grandes cantidades de objetos de grano fino** que comparten datos idénticos, separando el **estado intrínseco** (compartido e inmutable, ej. datos de la especie/raza o datos de camiseta/club en los miles de hinchas del estadio en `ejerFutbol-2026-10-08.pdf` Págs. 26–28) del **estado extrínseco** (particular de cada instancia).

#### 7. `Facade` (Fachada) — *(¡OJO: Prohibido en Parciales 2026 junto con Singleton!)*
- **Problema / Intención:** Proporcionar una **interfaz unificada y simplificada** para un conjunto de interfaces de un subsistema complejo. (Saberlo para la teoría, pero **NO elegirlo en el Punto 3 del parcial**).

---

### 3.3. LOS 11 PATRONES DE COMPORTAMIENTO (`GOF-2Q-2026.pdf` Págs. 45–66)

#### 1. `Strategy` (Estrategia) — ★ *COMODÍN N° 1 DE COMPORTAMIENTO PARA EL PARCIAL*
- **Problema / Intención:** Definir una **familia de algoritmos**, encapsular cada uno de ellos en una clase separada y hacerlos **intercambiables** en tiempo de ejecución a través de una interfaz común (`Final Dic 2025` y `ejerFutbol-2026-10-08.pdf` Pág. 14).
- **Cuándo usarlo en el Parcial (¡Encaja en TODOS los parciales!):**
  - **Cálculo de Precios / Descuentos / Financiación / Comisiones:**
    - En **Veterinaria PetCare**: Estrategia de cálculo de facturación/descuento según plan de mascota, medio de pago o cliente frecuente (`IEstrategiaFacturacion` ← `FacturacionParticular`, `FacturacionPlanSalud`, `FacturacionCampañaVacunacion`).
    - En **Agencia de Viajes (2C 2026)**: Estrategia de **asignación automática de Agente** (`IEstrategiaAsignacionAgente` ← `AsignacionPorDestino`, `AsignacionPorTipoViajeCorporativo`, `AsignacionPorCargaDeTrabajo`) o estrategia de **cálculo de tarifa/financiación** (viaje familiar vs. corporativo).
    - En **Refugio de Mascotas (1C 2026)**: Estrategia de **evaluación de aptitud de postulantes a adopción** (`IEstrategiaEvaluacionAdoptante` ← `EvaluacionAnimalEspecial`, `EvaluacionCachorro`, `EvaluacionEstandar`).
    - En **Préstamos Bancarios (2C 2025)**: Cálculo de cuotas por `SistemaFrances` vs `SistemaAleman`.
- **Estructura UML a dibujar en tu Diagrama de Clases:**
```
┌──────────────────────────┐         ┌──────────────────────────────────────┐
│    Contexto              │────────►│             <<interface>>            │
│ (ej. Solicitud / Factura)│         │          IEstrategiaCalculo          │
├──────────────────────────┤         ├──────────────────────────────────────┤
│ - estrategia: IEstrategia│         │ + calcular(datos): float             │
├──────────────────────────┤         └───────────────────△──────────────────┘
│ + cambiarEstrategia(e)   │                             ┆
│ + ejecutarCalculo()      │            ┌────────────────┴────────────────┐
└──────────────────────────┘            │                                 │
                         ┌──────────────┴──────────────┐   ┌──────────────┴──────────────┐
                         │  EstrategiaViajeCorporativo │   │   EstrategiaViajeFamiliar   │
                         ├─────────────────────────────┤   ├─────────────────────────────┤
                         │ + calcular(datos): float    │   │ + calcular(datos): float    │
                         └─────────────────────────────┘   └─────────────────────────────┘
```

#### 2. `State` (Estado) — ★ *COMODÍN N° 2 DE COMPORTAMIENTO PARA EL PARCIAL*
- **Problema / Intención:** Permitir que un objeto **altere su comportamiento cuando su estado interno cambia**; el objeto parecerá cambiar de clase. Reemplaza condicionales gigantes (`if (estado == PENDIENTE) ... else if (estado == CONFIRMADO)`) delegando el comportamiento en un objeto Estado polimórfico (`Final Julio 2026` y Clase 08/09).
- **Cuándo usarlo en el Parcial:**
  - En **cualquier caso donde la entidad central pase por un ciclo de vida con reglas por estado**:
    - **Turno / Consulta (`PetCare` / `Consultorios`):** `EstadoTurno` (`Pendiente`, `Confirmado`, `Atendido`, `Cancelado`).
    - **Solicitud de Viaje / Propuesta (`Agencia de Viajes`):** `EstadoSolicitud` (`Iniciada`, `ConAgenteAsignado`, `ConPropuestaEnviada`, `Confirmada`, `Cancelada`).
    - **Proceso de Adopción o Animal (`Refugio de Mascotas`):** `EstadoAnimal` (`EnRecuperacion`, `DisponibleParaAdopcion`, `EnProcesoAdopcion`, `Adoptado`).

#### 3. `Observer` (Observador / Publicador-Suscriptor) — ★ *COMODÍN N° 3 DE COMPORTAMIENTO PARA EL PARCIAL*
- **Problema / Intención:** Definir una **dependencia de uno a muchos** entre objetos, de forma que cuando un objeto (**Sujeto / Observado**) cambia su estado, **todos sus dependientes (Observadores) sean notificados y actualizados automáticamente** (`ejerFutbol-2026-10-08.pdf` Págs. 5–12: la `Pelota` es el Sujeto observado y los `Jugador`es son los Observadores).
- **Cuándo usarlo en el Parcial:**
  - **Veterinaria PetCare (1C 2026):** Notificar automáticamente al `Cliente` (por Email, SMS, WhatsApp) cuando una `VacunaAplicada` está próxima a vencer o cuando se confirma/cancela un `Turno` (analizado en Clase 09, `[02:25:00]` y en `Parcial 1C 2024`).
  - **Refugio de Mascotas (1C 2026):** Notificar alertas cuando el stock de un `Insumo` baja del mínimo o cuando vence una fecha de control post-adopción.
  - **Agencia de Viajes (2C 2026):** Notificar al `Cliente` y al `Agente` cuando cambia el estado de la `PropuestaViaje` o de un vuelo.

#### 4. `Template Method` (Método Plantilla)
- **Problema / Intención:** Definir el **esqueleto de un algoritmo** en una operación de una superclase abstracta, delegando a las subclases la redefinición de ciertos pasos específicos del algoritmo sin cambiar su estructura general.
- **Ejemplo:** Proceso de `EvaluacionCrediticia` o `EvaluacionAdopcion` que siempre ejecuta `1. validarIdentidad()`, `2. verificarAntecedentes()`, `3. calcularPuntajeEspecifico()` (abstracto), `4. emitirDictamen()`.

#### 5. `Chain of Responsibility` (Cadena de Responsabilidad)
- **Problema / Intención:** Evitar acoplar el emisor de una petición a su receptor dando a **más de un objeto la posibilidad de responder a la petición**, encadenando los objetos receptores y pasando la petición a través de la cadena (`siguienteHandler`) hasta que uno la procese o valide.
- **Ejemplo:** Cadena de validaciones de un préstamo o de una adopción (1° Validador de DNI → 2° Validador de Ingresos/Vivienda → 3° Validador de Antecedentes), o escalamiento de atención de un reclamo (Nivel 1 Bot → Nivel 2 Operador → Nivel 3 Supervisor).

#### 6. `Command` (Comando / Orden)
- **Problema / Intención:** Encapsular una **petición o acción como un objeto**, permitiendo parametrizar clientes con distintas peticiones, encolar tareas, registrar bitácoras (logs) y soportar operaciones de **deshacer (`undo`)**. (`ejerFutbol-2026-10-08.pdf` Págs. 19–21: acciones patear, saltar, pasar).

#### 7. `Memento` (Recuerdo / Instantánea de Estado)
- **Problema / Intención:** Capturar y externalizar el **estado interno de un objeto (`Originator`)** dentro de un objeto `Memento` (custodiado por un `Caretaker`) sin violar el encapsulamiento, para poder **restaurar el objeto a ese estado más adelante** (ej. historial de versiones de una `PropuestaViaje` o estado del partido en `ejerFutbol-2026-10-08.pdf` Págs. 22–23).

#### 8. `Mediator` (Mediador)
- **Problema / Intención:** Definir un objeto que **encapsula cómo interactúa un conjunto de objetos (`Colleagues`)**, evitando que se referencien explícitamente todos contra todos (convierte una red "muchos a muchos" en una estrella centralizada; `ejerFutbol-2026-10-08.pdf` Págs. 17–18).

#### 9. `Iterator` (Iterador)
- **Problema / Intención:** Proporcionar un modo de **acceder secuencialmente a los elementos de una colección agregada** (`hasNext()`, `next()`) sin exponer su representación interna (lista, árbol, grafo).

#### 10. `Visitor` (Visitante)
- **Problema / Intención:** Representar una **operación que se realiza sobre los elementos de una estructura de objetos**, permitiendo definir una nueva operación (ej. exportar a PDF, calcular impuestos, auditar) sin cambiar las clases de los elementos sobre los que opera.

#### 11. `Interpreter` (Intérprete)
- **Problema / Intención:** Dada una lengua o gramática simple (ej. expresiones regulares, fórmulas de reglas), definir una representación de su gramática y un intérprete que la evalúe.

---

## PARTE 4: MANUAL TÁCTICO PARA RESOLVER EL PUNTO 3 DEL PARCIAL (ELECCIÓN DE 2 PATRONES GOF)

En el Punto 3 del parcial te piden elegir **2 patrones GoF de DIFERENTE CATEGORÍA** (sin usar `Singleton` ni `Facade`). Para no dudar ni un segundo en el examen, usá esta **Matriz de Combinaciones Ganadoras**:

| Si el Enunciado tiene... | Patrón 1 Recomendado | Categoría 1 | Patrón 2 Recomendado | Categoría 2 |
| :--- | :--- | :--- | :--- | :--- |
| **Conexión con sistema externo** (ARCA/AFIP, Veraz, VISA, Renaper, Aerolíneas/Hoteles) **+** **Distintas formas de calcular precios/asignar/evaluar** | **`Adapter`**<br>(Desacopla y adapta la interfaz del sistema externo a una interfaz propia del dominio) | **Estructural** | **`Strategy`**<br>(Intercambia dinámicamente el algoritmo de cálculo, descuento, evaluación o asignación) | **Comportamiento** |
| **Armado de un paquete/combo o servicios anidables** (Paquete turístico con vuelos+hotel+excursiones, o Estudios médicos simples y compuestos) **+** **Ciclo de vida con estados cambiantes** (Reserva, Turno, Solicitud, Adopción) | **`Composite`** *(o **`Decorator`**)*<br>(Trata igual a un servicio simple que a un paquete compuesto, o agrega adicionales dinámicos) | **Estructural** | **`State`**<br>(Encapsula las reglas y transiciones de cada estado del objeto en clases polimórficas) | **Comportamiento** |
| **Construcción paso a paso de un objeto complejo con partes opcionales** (Propuesta de viaje, Contrato de adopción, Informe clínico) **+** **Envío de alertas/notificaciones ante eventos o vencimientos** (Vencimiento de vacunas, falta de stock, cambio de estado) | **`Builder`** *(o **`Factory Method`**)*<br>(Construye paso a paso distintas variantes del objeto complejo) | **Creacional** | **`Observer`**<br>(Notifica automáticamente a múltiples canales/interesados cuando ocurre el evento en el Sujeto) | **Comportamiento** |

### Plantilla Exacta para Redactar el Punto 3 en la Hoja del Parcial (Incisos `a`, `b`, `c`, `d`)

Copiá esta estructura exacta para cada uno de tus 2 patrones GoF elegidos:

> #### **PATRÓN GOF N° 1**
> - **a) Categoría y Nombre del Patrón:** Patrón **Estructural** — **Adapter (Adaptador)**.
> - **b) Problema de diseño que resuelve dentro del caso:** El sistema debe comunicarse con un servicio externo (`[ej. ARCA / Sistemas de Aerolíneas y Hoteles]`) cuya API e interfaz de datos son propietarias, externas e incompatibles con el modelo de dominio de nuestra aplicación, además de estar sujetas a cambios externos que no controlamos.
> - **c) Justificación de por qué es adecuado:** Es adecuado porque permite convertir la interfaz incompatible de la clase externa en una interfaz propia esperada por nuestro dominio (`<<interface>> [IServicioExterno]`). De este modo se logra **Bajo Acoplamiento**, **Indirección** y **Variaciones Protegidas**: si el proveedor externo cambia su API o si mañana se agregan nuevos proveedores externos, solo se modifica o agrega un nuevo `AdaptadorConcreto` sin tocar una sola línea de código de nuestras clases de negocio.
> - **d) Clases reutilizadas del Punto 1 y Clases/Interfaces nuevas incorporadas:**
>   - *Clase del Punto 1 que actúa como Cliente (`Client`):* `[ej. Factura / C_PropuestaViaje]`.
>   - *Interfaz nueva incorporada (`Target`):* `<<interface>> [IAutorizadorFacturacion / IProveedorTransporte]` con el método `+[autorizarFactura(f) / consultarDisponibilidad(fecha, destino)]`.
>   - *Clase nueva incorporada (`Adapter`):* `[AdaptadorARCA / AdaptadorAerolineaExt]` que implementa la interfaz `Target` y mantiene una referencia por asociación hacia el `Adaptee`.
>   - *Clase externa adaptada (`Adaptee`):* `[API_ARCA_SOAP / SistemaExternoAerolinea]` con su método nativo incompatible.
>
> ---
> #### **PATRÓN GOF N° 2**
> - **a) Categoría y Nombre del Patrón:** Patrón de **Comportamiento** — **Strategy (Estrategia)** *(o **State** / **Observer**)*.
> - **b) Problema de diseño que resuelve dentro del caso:** El sistema necesita `[ej. calcular el costo final de la atención / asignar automáticamente un agente de viajes / evaluar la solicitud]` utilizando distintos algoritmos o reglas de negocio según `[el tipo de cobertura / el tipo de cliente familiar o corporativo]`, evitando llenar la clase principal de condicionales `if / switch` rígidos.
> - **c) Justificación de por qué es adecuado:** Es adecuado porque encapsula cada algoritmo o regla de negocio en una clase separada que implementa una interfaz común (`<<interface>> [IEstrategia...]`), permitiendo intercambiar el algoritmo dinámicamente en tiempo de ejecución y facilitando agregar nuevas reglas en el futuro cumpliendo el Principio Abierto/Cerrado (OCP), **Polimorfismo** y **Alta Cohesión**.
> - **d) Clases reutilizadas del Punto 1 y Clases/Interfaces nuevas incorporadas:**
>   - *Clase del Punto 1 que actúa como Contexto (`Context`):* `[ej. Factura / SolicitudViaje]`, a la cual se le agrega la asociación `-estrategia: IEstrategia...`.
>   - *Interfaz nueva incorporada (`Strategy`):* `<<interface>> [IEstrategiaCalculo / IEstrategiaAsignacion]` con el método abstracto `+[calcularMonto(...) / seleccionarAgente(...)]`.
>   - *Clases nuevas incorporadas (`ConcreteStrategies`):* `[EstrategiaParticular]`, `[EstrategiaObraSocial]` y `[EstrategiaPlanVeterinario]`, que implementan dicha interfaz.
