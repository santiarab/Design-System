# 04 — METODOLOGÍA DE RESOLUCIÓN DESDE CERO, PARCIALES 2026 RESUELTOS Y BANCO TEÓRICO

> **Propósito de este documento:** Brindarte el **método exacto paso a paso** para enfrentar la hoja en blanco el día del parcial, seguido de la **resolución completa y comentada de los 3 Parciales 2026 de la cátedra** (*Veterinaria PetCare*, *Agencia de Viajes*, *Refugio de Mascotas*), las resoluciones de **Diagramas de Estados de Finales**, y el **compendio de Teoría de Examen** (Calidad, UX, SOA/Microservicios, Testing y STR).

---

## PARTE 1: EL MÉTODO CRONOMETRADO DE 120 MINUTOS PARA RESOLVER EL PARCIAL DESDE CERO

Un error fatal en el parcial de Diseño de Sistemas es dibujar primero todo el Diagrama de Clases en tinta, pasar luego al Diagrama de Secuencia, y descubrir a mitad de la secuencia que te faltan métodos o relaciones en las clases. Para que eso **no te pase**, aplicá este protocolo de 6 pasos:

### Paso 1 (Minutos 0 a 15): Lectura con los 3 Colores y Recorte de Alcance
1. Leé el enunciado completo y mirá la interfaz gráfica (si la hay).
2. Marcá:
   - **Sustantivos con identidad propia (Amarillo)** → Clases del Dominio.
   - **Datos simples (Verde)** → Atributos.
   - **Reglas de negocio y verbos (Azul)** → Métodos.
3. Identificá los **3 (o 4) grandes módulos funcionales** del enunciado para definir tus **Controladores (`C_...`)**.
4. Leé el **Punto 2 (Diagrama de Secuencia)** para saber exactamente **qué flujo te van a pedir secuenciar** (ahí es donde vas a poner mayor nivel de detalle en firmas de métodos y parámetros).
5. Leé el **Punto 3 (Patrones GoF)** y elegí tus **2 patrones GoF de distinta categoría** (ej. `Adapter` + `Strategy`, o `Composite`/`Builder` + `State`/`Observer`) antes de pasar en limpio el Diagrama de Clases, así ya los dibujás integrados en la Hoja 1.

### Paso 2 (Minutos 15 a 45): Esqueleto del Diagrama de Clases en Hoja 1 (Sin cerrar las cajas por abajo)
1. En la **Hoja 1**, dibujá arriba los **3 (o 4) `Controllers`** (`C_...`).
2. Debajo, ubicá los contenedores/nóminas (`HistoriaClinica`, `Agenda`, `Catalogo...`) y las **Clases del Dominio** con sus atributos privados (`-`) y asociaciones sólidas con **multiplicidad** (`1`, `0..*`, `1..*`), **agregaciones (`◇`)**, **composiciones (`◆`)** y **herencias (`─▷`)**.
3. **TRUCO DE ORO PARA EL EXAMEN EN PAPEL:** Al dibujar cada clase en la Hoja 1, **dejá abierto el borde inferior del compartimento de métodos** (no cierres la línea horizontal de abajo de la caja todavía). ¿Por qué? Porque cuando hagas el Diagrama de Secuencia en el Paso 3, cada mensaje nuevo que descubras lo vas a ir anotando inmediatamente adentro de la caja de esa clase en la Hoja 1. ¡Al terminar el examen cerrás las cajas y tenés **100% de consistencia garantizada**!

### Paso 3 (Minutos 45 a 75): Escenario y Diagrama de Secuencia en Hoja 2 (En simultáneo con los métodos del DC)
1. En la parte superior de la **Hoja 2**, escribí el **Escenario concreto** con valores puntuales (ej. 1 mascota, 1 vacuna, 1 receta).
2. Trazá las líneas de vida de izquierda a derecha empezando por el **`:C_Controller`** (¡sin Actor!).
3. Por **cada flecha de mensaje `─── metodo(param) ──►`** que dibujes llegando a la línea de vida de un objeto `:ClaseX`:
   - Inmediatamente mirá tu **Hoja 1** y verificá que `+metodo(param)` esté escrito dentro de `ClaseX` y que exista la relación de asociación o dependencia entre el emisor y `ClaseX`.
4. Usá `create(...)` apuntando a la cajita del objeto para todo objeto nuevo que nazca en ese flujo (`:Consulta`, `:VacunaAplicada`, `:Receta`, `:SolicitudViaje`, `:Propuesta`).

### Paso 4 (Minutos 75 a 95): Inyección de los 2 Patrones GoF en Hoja 1 y Redacción en Hoja 3
1. Dibujá en la **Hoja 1** las interfaces (`<<interface>>`) y clases concretas de los **2 Patrones GoF** conectadas a las clases de tu dominio (podés resaltarlas con un recuadro punteado o color indicando `Patrón 1: Adapter`, `Patrón 2: Strategy`).
2. En la **Hoja 3**, redactá los incisos `a)`, `b)`, `c)` y `d)` de cada patrón GoF usando la plantilla de `03_PATRONES_GRASP_Y_GOF_APLICADOS.md`.

### Paso 5 (Minutos 95 a 110): Redacción de las Justificaciones GRASP
1. En la **Hoja 1** (o en la hoja de texto adjunta), redactá las justificaciones de **Experto en Información**, **Creador**, **Bajo Acoplamiento / Alta Cohesión** (y **Controlador** si suma en tu tema), citando **nombres exactos de clases y métodos de tu Diagrama de Clases**.

### Paso 6 (Minutos 110 a 120): Auditoría Final con los 12 Mandamientos
- Cerrá la parte inferior de las cajas de clases, verificá que todas las hojas estén numeradas (`Hoja 1 de 3`, `Hoja 2 de 3`, `Hoja 3 de 3`) y hacé el chequeo cruzado de métodos entre Secuencia y Clases.

---

## PARTE 2: RESOLUCIÓN COMPLETA DEL PARCIAL 1C 2026 (COMISIÓN 4300 — ING. ANALÍA MARÍN)
### CASO: VETERINARIA "PETCARE" (`Parciales/1. [Parcial 1][1C2026][4300][Analia][][].pdf`)

> **Contexto y fuente de validación:** Este examen fue tomado por la Ing. Analía Marín y corregido punto por punto en la **Clase 09 (`09_20261015_082342.txt`, desde `[01:13:07]` hasta `[03:45:00]`)**. La solución que sigue incorpora exactamente todo lo que la profesora validó como un **10 sobresaliente**.

#### Síntesis del Enunciado y de la Pantalla Adjunta ("Gato Homero")
- La clínica veterinaria **PetCare** gestiona la atención médica de mascotas.
- Cuando llega un **Cliente (Dueño)** con su **Mascota**, se verifica si están registrados; si no, se los registra (creando la `Mascota` con su única `HistoriaClinica`).
- La atención puede originarse con un **Turno** previo (o por demanda espontánea).
- En la pantalla de atención médica se observa:
  - Datos de la mascota: *Nombre: Homero, Especie: Gato, Edad: 4 años, Peso: 4.5 kg*.
  - Registro de la **Consulta** médica realizada por un **Veterinario** (fecha, motivo/diagnóstico, observaciones, peso registrado).
  - Aplicación de **una o más Vacunas**: cada vacuna aplicada registra la vacuna del catálogo, lote, fecha de aplicación y **calcula/registra su fecha de vencimiento** para enviar **recordatorios automáticos al dueño** cuando esté por vencer.
  - Emisión opcional de **Receta médica** con medicamentos, dosis, frecuencia y duración del tratamiento.
- Finalizada la atención, se genera la **Factura** por los servicios/prácticas y vacunas aplicadas, se procesa el **Pago** (Efectivo, Tarjeta, Transferencia o Plan de Salud) y se valida electrónicamente con el organismo fiscal externo **ARCA** para obtener el CAE.

---

### PUNTO 1 (PARCIAL PETCARE): DIAGRAMA DE CLASES DE DISEÑO (MÁXIMO 3 CONTROLLERS) + 3 GRASP

#### 1.A. Los 3 Controladores Elegidos (Tope máximo exigido: 3)
1. **`C_Turno`**: Gestiona la reserva, confirmación y cancelación de turnos en la agenda.
2. **`C_AtencionMedica`**: Coordina el flujo core de atención clínica (búsqueda/alta de cliente y mascota, registro de consulta en la historia clínica, aplicación de vacunas y emisión de receta).
3. **`C_Facturacion`**: Coordina la liquidación de los cargos de la consulta, el cobro del pago y la autorización electrónica ante ARCA.

#### 1.B. Diagrama de Clases Completo (Dominio + Controllers + 2 Patrones GoF integrados)

```
========================================================================================================================
                                     CAPA DE CONTROLADORES (MÁXIMO 3 CONTROLLERS)
========================================================================================================================
   ┌──────────────────────────────────────────┐  ┌──────────────────────────────────────────────────────┐  ┌──────────────────────────────────────────┐
   │                 C_Turno                  │  │                   C_AtencionMedica                   │  │              C_Facturacion               │
   ├──────────────────────────────────────────┤  ├──────────────────────────────────────────────────────┤  ├──────────────────────────────────────────┤
   │ - agenda: AgendaTurnos                   │  │ - nominaClientes: NominaClientes                     │  │ - adaptadorFiscal: IServicioFiscalExt    │
   │                                          │  │ - catalogoVacunas: CatalogoVacunas                   │  ├──────────────────────────────────────────┤
   ├──────────────────────────────────────────┤  ├──────────────────────────────────────────────────────┤  │ + generarFactura(idConsulta, idEstrat):  │
   │ + reservarTurno(dni, idMasc, fecha, idV) │  │ + iniciarAtencion(dni, idMascota): HistoriaClinica   │  │     Factura                              │
   │ + cancelarTurno(idTurno): Boolean        │  │ + registrarAtencion(idMasc, idVet, diag, peso,       │  │ + registrarPago(idFact, medioPago): Pago │
   └────────────────────┬─────────────────────┘  │     codVacuna, lote, indicacionReceta): Consulta     │  └────────────────────┬─────────────────────┘
                        │                        └──────────┬───────────────────────────────┬───────────┘                       │
                        ▼                                   ▼                               ▼                                   ▼
========================================================================================================================
                                    CONTENEDORES / NÓMINAS (FABRICACIÓN PURA) Y DOMINIO
========================================================================================================================
   ┌──────────────────────────────────────────┐  ┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
   │               AgendaTurnos               │  │            NominaClientes            │  │           CatalogoVacunas            │
   ├──────────────────────────────────────────┤  ├──────────────────────────────────────┤  ├──────────────────────────────────────┤
   │ - turnos: List<Turno>                    │  │ - clientes: List<Cliente>            │  │ - vacunas: List<TipoVacuna>          │
   ├──────────────────────────────────────────┤  ├──────────────────────────────────────┤  ├──────────────────────────────────────┤
   │ + verificarDisponibilidad(f, v): Boolean │  │ + buscarCliente(dni): Cliente        │  │ + buscarTipoVacuna(cod): TipoVacuna  │
   │ + crearTurno(m, v, fecha): Turno         │  │ + registrarCliente(datos): Cliente   │  └──────────────────┬───────────────────┘
   └────────────────────┬─────────────────────┘  └──────────────────┬───────────────────┘                     │ 1
                        │ 1                                         │ 1                                       │
                        ◆                                           ◆                                         ◇
                        │ 0..*                                      │ 0..*                                    │ 1..*
                        ▼                                           ▼                                         ▼
   ┌──────────────────────────────────────────┐  ┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
   │                  Turno                   │  │               Cliente                │  │              TipoVacuna              │
   ├──────────────────────────────────────────┤  ├──────────────────────────────────────┤  ├──────────────────────────────────────┤
   │ - idTurno: int                           │  │ - dni: String                        │  │ - codigo: int                        │
   │ - fechaHora: DateTime                    │  │ - nombreApellido: String             │  │ - nombreComercial: String            │
   │ - estado: String                         │  │ - telefono: String                   │  │ - diasVigencia: int                  │
   ├──────────────────────────────────────────┤  │ - email: String                      │  │ - precioLista: float                 │
   │ + confirmar(): void                      │  ├──────────────────────────────────────┤  ├──────────────────────────────────────┤
   │ + cancelar(): void                       │  │ + buscarMascota(idMasc): Mascota     │  │ + getDiasVigencia(): int             │
   │ + marcarAtendido(): void                 │  │ + registrarMascota(datos): Mascota   │  │ + getPrecio(): float                 │
   └─────────┬──────────────────────┬─────────┘  └──────────────────┬───────────────────┘  └──────────────────▲───────────────────┘
             │ *                    │ *                             │ 1                                       │ 1
             │ para                 │ asignadoA                     ◆ posee                                   │ correspondeA
             │                      ▼                               │ 1..*                                    │
             │         ┌──────────────────────┐                     ▼                                         │
             │         │     Veterinario      │  ┌──────────────────────────────────────┐                     │
             │         ├──────────────────────┤  │               Mascota                │                     │
             │         │ - matricula: String  │  ├──────────────────────────────────────┤                     │
             │         │ - nombre: String     │  │ - idMascota: int                     │                     │
             │         │ - especialidad: Str  │  │ - nombre: String                     │                     │
             │         ├──────────────────────┤  │ - especie: String                    │                     │
             │         │ + getMatricula():Str │  │ - fechaNacimiento: Date              │                     │
             │         └────────────▲─────────┘  │ - pesoActual: float                  │                     │
             │ 1                    │ 1          ├──────────────────────────────────────┤                     │
             └──────────────────────┼────────────┤ + actualizarPeso(peso): void         │                     │
                                    │ atendidaPor│ + obtenerHistoriaClinica(): HC       │                     │
                                    │            └──────────────────┬───────────────────┘                     │
                                    │                               │ 1                                       │
                                    │                               ◆ compuestaPor (1 a 1 exclusiva)          │
                                    │                               │ 1                                       │
                                    │                               ▼                                         │
                                    │            ┌──────────────────────────────────────┐                     │
                                    │            │           HistoriaClinica            │                     │
                                    │            ├──────────────────────────────────────┤                     │
                                    │            │ - nroHistoria: int                   │                     │
                                    │            │ - fechaApertura: Date                │                     │
                                    │            ├──────────────────────────────────────┤                     │
                                    │            │ + registrarConsulta(vet, diag, peso, │                     │
                                    │            │     tipoVac, lote, indRec): Consulta │                     │
                                    │            │ + obtenerVacunasPorVencer(f): List   │                     │
                                    │            └──────────────────┬───────────────────┘                     │
                                    │                               │ 1                                       │
                                    │                               ◆ contiene                                │
                                    │                               │ 0..*                                    │
                                    │                               ▼                                         │
                                    │            ┌──────────────────────────────────────┐                     │
                                    └───────────►│               Consulta               │                     │
                                               * ├──────────────────────────────────────┤                     │
                                                 │ - idConsulta: int                    │                     │
                                                 │ - fecha: Date                        │                     │
                                                 │ - diagnostico: String                │                     │
                                                 │ - pesoRegistrado: float              │                     │
                                                 │ - arancelBase: float                 │                     │
                                                 ├──────────────────────────────────────┤                     │
                                                 │ + aplicarVacuna(tv: TipoVacuna,      │                     │
                                                 │     lote: String): VacunaAplicada    │                     │
                                                 │ + emitirReceta(ind: String): Receta  │                     │
                                                 │ + calcularSubtotalConsulta(): float  │                     │
                                                 └───────┬──────────────────────┬───────┘                     │
                                                         │ 1                    │ 1                           │
                                                         ◆                      ◆                             │
                                                    0..* │                 0..1 │                             │
                                                         ▼                      ▼                             │
   ┌──────────────────────────────────────────────────────┐  ┌──────────────────────────────────────┐         │
   │                    VacunaAplicada                    │  │                Receta                │         │
   │              (Sujeto en Patrón Observer)             │  ├──────────────────────────────────────┤         │
   ├──────────────────────────────────────────────────────┤  │ - idReceta: int                      │         │
   │ - fechaAplicacion: Date                              │  │ - fechaEmision: Date                 │         │
   │ - fechaVencimiento: Date                             │  │ - indicacionesGenerales: String      │         │
   │ - lote: String                                       │  ├──────────────────────────────────────┤         │
   │ - observadores: List<IObservadorVencimiento>         │  │ + agregarItem(med, dosis, frec): void│         │
   ├──────────────────────────────────────────────────────┤  └──────────────────┬───────────────────┘         │
   │ + calcularVencimiento(diasVigencia: int): Date       ├─────────────────────┼─────────────────────────────┘
   │ + estaProximaAVencer(fechaActual: Date): Boolean     │                     │ 1
   │ + suscribir(obs: IObservadorVencimiento): void       │                     ◆
   │ + desuscribir(obs: IObservadorVencimiento): void     │                     │ 1..*
   │ + notificarVencimientoProximo(): void                │                     ▼
   └──────────────────────────┬───────────────────────────┘  ┌──────────────────────────────────────┐
                              │ *                            │              ItemReceta              │
                              ▼                              ├──────────────────────────────────────┤
   ┌──────────────────────────────────────────────────────┐  │ - medicamento: String                │
   │                    <<interface>>                     │  │ - dosis: String                      │
   │                IObservadorVencimiento                │  │ - frecuencia: String                 │
   │            [PATRÓN GOF 1: OBSERVER (Comp.)]          │  │ - duracionDias: int                  │
   ├──────────────────────────────────────────────────────┤  └──────────────────────────────────────┘
   │ + actualizarAlertaVencimiento(v: VacunaAplicada):void│
   └──────────────────────────△───────────────────────────┘
                              ┆
               ┌──────────────┴───────────────┐
   ┌───────────┴────────────┐    ┌────────────┴───────────┐
   │   NotificadorEmail     │    │  NotificadorWhatsApp   │
   ├────────────────────────┤    ├────────────────────────┤
   │ - servidorSMTP: String │    │ - apiGateway: String   │
   ├────────────────────────┤    ├────────────────────────┤
   │ + actualizarAlerta...()│    │ + actualizarAlerta...()│
   └────────────────────────┘    └────────────────────────┘

========================================================================================================================
                            SECTOR FACTURACIÓN + PATRÓN GOF 2: ADAPTER (ESTRUCTURAL) + STRATEGY
========================================================================================================================
   ┌──────────────────────────────────────┐         ┌──────────────────────────────────────┐
   │               Factura                │────────►│            <<interface>>             │
   ├──────────────────────────────────────┤         │         IServicioFiscalExt           │
   │ - nroFactura: int                    │         │   [PATRÓN GOF 2: ADAPTER (Estruct.)] │
   │ - fecha: Date                        │         ├──────────────────────────────────────┤
   │ - montoTotal: float                  │         │ + solicitarAutorizacionCAE(f): String│
   │ - cae: String                        │         └──────────────────△───────────────────┘
   │ - consultaAsociada: Consulta         │                            ┆
   │ - estrategiaCobro: IEstrategiaCobro  │         ┌──────────────────┴───────────────────┐
   ├──────────────────────────────────────┤         │            AdaptadorARCA             │
   │ + calcularTotal(): float             │         ├──────────────────────────────────────┤
   │ + autorizarConARCA(srv): void        │         │ - apiExterna: WebServiceARCA_AFIP    │
   └──────────────────┬───────────────────┘         ├──────────────────────────────────────┤
                      │                             │ + solicitarAutorizacionCAE(f): String│
                      ▼                             └──────────────────┬───────────────────┘
   ┌──────────────────────────────────────┐                            ▼
   │            <<interface>>             │         ┌──────────────────────────────────────┐
   │           IEstrategiaCobro           │         │         WebServiceARCA_AFIP          │
   ├──────────────────────────────────────┤         ├──────────────────────────────────────┤
   │ + calcularImporteFinal(base): float  │         │ + enviarXML_FE(cuit, impNeto): XML   │
   └──────────────────△───────────────────┘         └──────────────────────────────────────┘
                      ┆
         ┌────────────┴─────────────┐
   ┌─────┴──────────────┐    ┌──────┴─────────────┐
   │  CobroParticular   │    │  CobroPlanSalud    │
   ├────────────────────┤    ├────────────────────┤
   │ + calcularImporte()│    │ - porcDescuento    │
   └────────────────────┘    ├────────────────────┤
                             │ + calcularImporte()│
                             └────────────────────┘
```

#### 1.C. Justificación de los 3 Patrones GRASP (Punto 1)
1. **Controlador (*Controller*):** Se aplica en las clases **`C_AtencionMedica`**, **`C_Turno`** y **`C_Facturacion`** (respetando el límite máximo de 3 controladores). Por ejemplo, `C_AtencionMedica` recibe el evento externo `+registrarAtencion(...)` desde la interfaz de usuario, desacoplando las pantallas HTML de las clases de negocio y coordinando la búsqueda de la mascota y la delegación del registro clínico.
2. **Experto en Información (*Information Expert*):** Se aplica en la clase **`Consulta`** con el método **`+calcularSubtotalConsulta()`** (que conoce su `arancelBase` y su colección de `VacunaAplicada`, pidiéndole a cada una el precio de su `TipoVacuna`) y en la clase **`VacunaAplicada`** con el método **`+calcularVencimiento(diasVigencia)`**, dado que ella posee el atributo `-fechaAplicacion` y la referencia a `TipoVacuna` (que conoce `-diasVigencia`), siendo la experta para determinar su propia `-fechaVencimiento`.
3. **Creador (*Creator*):** Se aplica en la clase **`HistoriaClinica`** mediante el método **`+registrarConsulta(...)`**, la cual es responsable de instanciar (`create`) el objeto **`Consulta`**, dado que `HistoriaClinica` agrega y contiene de manera exclusiva (relación de composición `1` a `0..*`) todas las consultas históricas de la mascota. Del mismo modo, **`Consulta`** actúa como **Creador** de **`VacunaAplicada`** (en `+aplicarVacuna()`) y de **`Receta`** (en `+emitirReceta()`), porque una consulta médica contiene y registra las vacunas y recetas emitidas durante dicho acto médico.

---

### PUNTO 2 (PARCIAL PETCARE): ESCENARIO Y DIAGRAMA DE SECUENCIA (SIN INCLUIR PAGO)

> **Consigna del Punto 2:** *"Escribir el escenario que se utiliza para el diagrama de secuencia. Construir un diagrama de secuencia que represente el proceso de atención médica de una mascota, desde el registro de la consulta hasta la emisión de la receta y registro de vacunas (No incluir la parte de pago)."*

#### 2.A. Escenario Concreto (Obligatorio escribirlo arriba de la hoja)
> **Escenario:** El cliente ya registrado (DNI `"35111222"`) asiste a la consulta con su mascota registrada `"Homero"` (`idMascota = 10`, Gato, 4 años) atendido por el veterinario `idVet = 3`. Se registra la consulta con diagnóstico `"Control anual sano"` y peso `4.5 kg`, se le aplica **1 vacuna** (`codVacuna = 5`, `"Antirrábica"`, lote `"L-99"`) calculando su fecha de vencimiento, y se emite **1 receta** con la indicación `"Pipeta antipulgas cada 30 días"`.

#### 2.B. Diagrama de Secuencia Completo (100% Trazable con el Diagrama de Clases)

```
                     :C_AtencionMedica   :NominaClientes   cli:Cliente   m:Mascota   :CatalogoVacunas   tv:TipoVacuna   hc:HistoriaClinica
                             │                  │               │            │              │                 │                 │
 ●──registrarAtencion───────►┌─┐                │               │            │              │                 │                 │
   (dni="35111222", idM=10,  │ ├─buscarCliente─►┌─┐             │            │              │                 │                 │
    idVet=3, diag="Control", │ │ ("35111222")   │ │             │            │              │                 │                 │
    peso=4.5, codVac=5,      │ │◄──── cli ──────└─┘             │            │              │                 │                 │
    lote="L-99", ind="Pipeta")│                                 │            │              │                 │                 │
                             │ ├─buscarMascota(10)─────────────►┌─┐          │              │                 │                 │
                             │ │◄────── m ──────────────────────└─┘          │              │                 │                 │
                             │ │                                             │              │                 │                 │
                             │ ├─actualizarPeso(4.5)────────────────────────►┌─┐            │                 │                 │
                             │ │◄────── ok ──────────────────────────────────└─┘            │                 │                 │
                             │ ├─obtenerHistoriaClinica()───────────────────►┌─┐            │                 │                 │
                             │ │◄────── hc ──────────────────────────────────└─┘            │                 │                 │
                             │ │                                                            │                 │                 │
                             │ ├─buscarTipoVacuna(5)───────────────────────────────────────►┌─┐               │                 │
                             │ │◄────── tv ─────────────────────────────────────────────────└─┘               │                 │
                             │ │                                                                              │                 │
                             │ ├─registrarConsulta(vet, "Control", 4.5, tv, "L-99", "Pipeta")─────────────────┼────────────────►┌─┐
                             │ │                                                                              │                 │ ├─create(vet,"Control",4.5)─►┌──────────┐
                             │ │                                                                              │                 │ │                            │c:Consulta│
                             │ │                                                                              │                 │ │                            └────┬─────┘
                             │ │                                                                              │                 │ ├─aplicarVacuna(tv, "L-99")──────►┌─┐
                             │ │                                                                              │                 │ │                                 │ ├─create(tv,"L-99")─►┌──────────────────┐
                             │ │                                                                              │                 │ │                                 │ │                    │va:VacunaAplicada │
                             │ │                                                                              │                 │ │                                 │ │                    └────────┬─────────┘
                             │ │                                                                              │                 │ │                                 │ ├─getDiasVigencia()─►         │
                             │ │                                                                              │                 │ │                                 │ │ (a tv: retorna 365)         │
                             │ │                                                                              │                 │ │                                 │ ├─calcularVencimiento(365)───►┌─┐
                             │ │                                                                              │                 │ │                                 │ │◄──── fechaVenc ─────────────└─┘
                             │ │                                                                              │                 │ │◄────────── va ──────────────────└─┘
                             │ │                                                                              │                 │ │
                             │ │                                                                              │                 │ ├─emitirReceta("Pipeta...")──────►┌─┐
                             │ │                                                                              │                 │ │                                 │ ├─create("Pipeta")──►┌──────────┐
                             │ │                                                                              │                 │ │                                 │ │                    │ r:Receta │
                             │ │                                                                              │                 │ │                                 │ │                    └────┬─────┘
                             │ │                                                                              │                 │ │                                 │ ├─agregarItem(...)───────►┌─┐
                             │ │                                                                              │                 │ │                                 │ │◄───── ok ───────────────└─┘
                             │ │                                                                              │                 │ │◄────────── r ───────────────────└─┘
                             │ │◄────────────────────────── c:Consulta ───────────────────────────────────────┼─────────────────└─┘
 ◄── confirmacionAtencion(c)─└─┘
```
*(Verificación de consistencia: Todos los mensajes `buscarCliente`, `buscarMascota`, `actualizarPeso`, `obtenerHistoriaClinica`, `buscarTipoVacuna`, `registrarConsulta`, `aplicarVacuna`, `getDiasVigencia`, `calcularVencimiento`, `emitirReceta` y `agregarItem` están declarados exactamente como métodos en las clases receptoras del Diagrama de Clases del Punto 1).*

---

### PUNTO 3 (PARCIAL PETCARE): APLICACIÓN Y JUSTIFICACIÓN DE 2 PATRONES GOF DE DIFERENTE CATEGORÍA

#### Patrón GoF N° 1: `Observer` (Categoría: Comportamiento)
- **a) Categoría y Nombre:** Patrón de **Comportamiento** — **Observer (Observador)**.
- **b) Problema de diseño que resuelve en el caso:** El enunciado establece que cada vez que una vacuna aplicada a una mascota está próxima a cumplir su fecha de vencimiento, el sistema debe enviar recordatorios/notificaciones al dueño por distintos medios (Email, WhatsApp, App móvil), sin acoplar la clase clínica `VacunaAplicada` (ni `HistoriaClinica`) a las implementaciones concretas de los canales de mensajería.
- **c) Por qué es adecuado:** Define una dependencia uno-a-muchos entre el sujeto observado (`VacunaAplicada`) y múltiples observadores (`IObservadorVencimiento`), de forma que al detectarse el evento de proximidad de vencimiento (`+notificarVencimientoProximo()`), todos los canales suscritos del cliente son notificados automáticamente sin que `VacunaAplicada` conozca qué canales son ni cómo se envían los mensajes.
- **d) Clases reutilizadas del Punto 1 y Clases/Interfaces nuevas incorporadas:**
  - *Clase reutilizada del Punto 1 (`ConcreteSubject`):* **`VacunaAplicada`**, a la que se le agregan los métodos `+suscribir(o)`, `+desuscribir(o)` y `+notificarVencimientoProximo()`.
  - *Interfaz nueva incorporada (`Observer`):* **`<<interface>> IObservadorVencimiento`** con el método `+actualizarAlertaVencimiento(v: VacunaAplicada)`.
  - *Clases concretas nuevas incorporadas (`ConcreteObservers`):* **`NotificadorEmail`** y **`NotificadorWhatsApp`**, que implementan `IObservadorVencimiento`.

#### Patrón GoF N° 2: `Adapter` (Categoría: Estructural)
- **a) Categoría y Nombre:** Patrón **Estructural** — **Adapter (Adaptador)**.
- **b) Problema de diseño que resuelve en el caso:** Al finalizar la atención y emitir la `Factura`, el sistema PetCare debe validar y autorizar el comprobante electrónicamente ante el sistema externo gubernamental **ARCA (ex AFIP)**, el cual posee una API externa (basada en SOAP/XML) cuya firma y estructura de datos son incompatibles con los objetos de dominio de la veterinaria.
- **c) Por qué es adecuado:** Permite envolver la interfaz incompatible del servicio web externo de ARCA detrás de una interfaz propia del dominio (`<<interface>> IServicioFiscalExt`), traduciendo las llamadas de `Factura` al formato requerido por ARCA. Así se protege al dominio ante cambios futuros en la normativa o API de ARCA (**Bajo Acoplamiento** y **Variaciones Protegidas**).
- **d) Clases reutilizadas del Punto 1 y Clases/Interfaces nuevas incorporadas:**
  - *Clases reutilizadas del Punto 1 (`Client`):* **`C_Facturacion`** y **`Factura`**.
  - *Interfaz nueva incorporada (`Target`):* **`<<interface>> IServicioFiscalExt`** con el método `+solicitarAutorizacionCAE(f: Factura): String`.
  - *Clase concreta nueva incorporada (`Adapter`):* **`AdaptadorARCA`**, que realiza `IServicioFiscalExt` y mantiene una asociación hacia `WebServiceARCA_AFIP`.
  - *Clase externa adaptada (`Adaptee`):* **`WebServiceARCA_AFIP`** con su método nativo `+enviarXML_FE(cuit, impNeto): XML`.

---

## PARTE 3: RESOLUCIÓN COMPLETA DEL PARCIAL 2C 2026 (COMISIÓN 1900)
### CASO: "AGENCIA DE VIAJES" (`Parciales/drive-download-20261111T183304Z-1-001/3. [Parcial 1][2C2026][1900][][][].pdf`)

#### Síntesis del Enunciado y Requisitos Exactos de la Consigna
- Una **Agencia de Viajes** organiza experiencias personalizadas tanto para **grupos familiares/amigos** como para **empresas (corporativos)**.
- Cuando un nuevo **Cliente** se acerca, se lo registra y se crea su **Solicitud de Viaje** (destino, fechas, cantidad de pasajeros, presupuesto estimado, preferencias, tipo de viaje).
- El sistema **asigna automáticamente un Agente de Viajes** adecuado según el destino, tipo de viaje, experiencia y disponibilidad de los agentes.
- El agente (a través del sistema) arma una **Propuesta de Viaje personalizada** combinando **Transporte (Vuelos/Buses)**, **Alojamiento (Hoteles)**, **Excursiones** y **Seguros de Viaje**, consultando disponibilidad y tarifas en tiempo real en **sistemas externos de proveedores**.
- Una vez aceptada la propuesta, pasa a **Reserva** y se gestionan los **Pagos** (con distintas modalidades de financiación/descuento según sea cliente familiar o corporativo).
- **Consigna:**
  1. **Diagrama de Clases** (máximo **4 controllers**) + **2 patrones GRASP justificados (sin contar Controller)**.
  2. **Diagrama de Secuencia** desde que se registra un nuevo cliente, se crea su solicitud de viaje, se le asigna un agente y se arma su propuesta personalizada.
  3. **2 Patrones GoF de diferente categoría** (**prohibido usar Singleton y Facade**).

---

### PUNTO 1 (AGENCIA DE VIAJES): DIAGRAMA DE CLASES (MÁX 4 CONTROLLERS) + 2 GRASP (SIN CONTROLLER)

#### 1.A. Los 4 Controladores Elegidos
1. **`C_SolicitudViaje`**: Registra al cliente, crea la solicitud de viaje y coordina la asignación automática de agente.
2. **`C_Propuesta`**: Coordina la consulta a proveedores externos y el armado de la propuesta personalizada.
3. **`C_Reserva`**: Gestiona la confirmación de la propuesta aceptada y la emisión de vouchers.
4. **`C_Cobranza`**: Gestiona el cobro y plan de financiación de la reserva.

#### 1.B. Diagrama de Clases Integrado (Dominio + 4 Controllers + Patrones GoF `Composite` / `Adapter` + `Strategy`)

```
========================================================================================================================
                                     CAPA DE CONTROLADORES (MÁXIMO 4 CONTROLLERS)
========================================================================================================================
 ┌──────────────────────────────────────────┐ ┌──────────────────────────────────────────┐ ┌────────────────────┐ ┌────────────────────┐
 │             C_SolicitudViaje             │ │               C_Propuesta                │ │     C_Reserva      │ │     C_Cobranza     │
 ├──────────────────────────────────────────┤ ├──────────────────────────────────────────┤ ├────────────────────┤ ├────────────────────┤
 │ - nominaClientes: NominaClientes         │ │ - catalogoProveedores: CatalogoProveedor │ │ + confirmarReserva │ │ + procesarPago     │
 │ - nominaAgentes: NominaAgentes           │ ├──────────────────────────────────────────┤ │   (idProp):Reserva │ │   (idRes, medio)   │
 ├──────────────────────────────────────────┤ │ + armarPropuesta(idSol, datosServ):      │ └─────────┬──────────┘ └─────────┬──────────┘
 │ + procesarNuevaSolicitud(datosCli,       │ │     PropuestaViaje                       │           │                      │
 │     destino, fechas, cantPasaj, tipo):   │ └────────────────────┬─────────────────────┘           │                      │
 │     SolicitudViaje                       │                      │                                 │                      │
 └────────┬────────────────────────┬────────┘                      │                                 │                      │
          ▼                        ▼                               ▼                                 ▼                      ▼
 ┌────────────────────────┐ ┌────────────────────────┐ ┌──────────────────────────────────────────┐ ┌──────────────────────────────────┐
 │     NominaClientes     │ │     NominaAgentes      │ │            CatalogoProveedores           │ │             Reserva              │
 ├────────────────────────┤ ├────────────────────────┤ ├──────────────────────────────────────────┤ ├──────────────────────────────────┤
 │ - clientes:List<Cli>   │ │ - agentes:List<Agente> │ │ - proveedores: List<IProveedorTuristico> │ │ - codigoReserva: String          │
 ├────────────────────────┤ ├────────────────────────┤ ├──────────────────────────────────────────┤ │ - fechaConfirmacion: Date        │
 │ + registrarCliente(d): │ │ + buscarAgenteApto(    │ │ + cotizarServicio(tipo, dest, fecha):    │ │ - estado: String                 │
 │     Cliente            │ │   dest, tipo, estrat): │ │     IServicioTuristico                   │ │ - propuestaAceptada: Propuesta   │
 │ + buscarCliente(id)    │ │     Agente             │ └────────────────────┬─────────────────────┘ ├──────────────────────────────────┤
 └───────────┬────────────┘ └───────────┬────────────┘                      │ 1..*                  │ + calcularSaldoPendiente():float │
             │ 1                        │ 1                                 ▼                       │ + registrarPago(m): Pago         │
             ◆                          ◆              ┌──────────────────────────────────────────┐ └──────────────────────────────────┘
             │ 0..*                     │ 1..*         │              <<interface>>               │
             ▼                          ▼              │           IProveedorTuristico            │
 ┌────────────────────────┐ ┌────────────────────────┐ │     [PATRÓN GOF 1: ADAPTER (Estruct.)]   │
 │        Cliente         │ │         Agente         │ ├──────────────────────────────────────────┤
 ├────────────────────────┤ ├────────────────────────┤ │ + consultarDisponibilidad(d, f): Boolean │
 │ - idCliente: int       │ │ - legajo: int          │ │ + obtenerServicioCotizado(d, f):         │
 │ - nombreRazonSoc: Str  │ │ - nombre: String       │ │     IServicioTuristico                   │
 │ - tipoCliente: String  │ │ - destinosEsp: List    │ └────────────────────△─────────────────────┘
 │ - email: String        │ │ - disponible: Boolean  │                      ┆
 ├────────────────────────┤ ├────────────────────────┤        ┌─────────────┴──────────────┐
 │ + crearSolicitud(dest, │ │ + esAptoPara(dest):Bool│ ┌──────┴────────────────┐  ┌────────┴───────────────┐
 │   fechas, pasaj, tipo):│ │ + asignarSolicitud():  │ │AdaptadorGDS_Aerolinea │  │ AdaptadorBookingHotel  │
 │   SolicitudViaje       │ │     void               │ ├───────────────────────┤  ├────────────────────────┤
 └───────────┬────────────┘ └───────────▲────────────┘ │ - apiGDS: API_Amadeus │  │ - apiHotel: API_HotelWS│
             │ 1                        │ 1            ├───────────────────────┤  ├────────────────────────┤
             ◆ realiza                  │ asignadoA    │ + consultarDisponib() │  │ + consultarDisponib()  │
             │ 0..*                     │              │ + obtenerServicio...()│  │ + obtenerServicio...() │
             ▼                          │              └───────────┬───────────┘  └────────────┬───────────┘
 ┌──────────────────────────────────────┴────────────┐             ▼                           ▼
 │                  SolicitudViaje                   │ ┌───────────────────────┐  ┌────────────────────────┐
 │         (Contexto en Patrón GoF Strategy)         │ │      API_Amadeus      │  │      API_HotelWS       │
 ├───────────────────────────────────────────────────┤ ├───────────────────────┤  ├────────────────────────┤
 │ - nroSolicitud: int                               │ │ + searchFlightsXML()  │  │ + getRoomsJSON()       │
 │ - destino: String                                 │ └───────────────────────┘  └────────────────────────┘
 │ - fechaSalida: Date                               │
 │ - fechaRegreso: Date                              │ =================================================================================
 │ - cantPasajeros: int                              │                   ESTRUCTURA DE PROPUESTA Y SERVICIOS
 │ - tipoViaje: String                               │ =================================================================================
 ├───────────────────────────────────────────────────┤              ┌──────────────────────────────────────────────┐
 │ + asignarAgente(a: Agente): void                  │              │                PropuestaViaje                │
 │ + crearPropuesta(): PropuestaViaje                ├─────────────►├──────────────────────────────────────────────┤
 └─────────────────────────┬─────────────────────────┘ 1        0..*│ - nroPropuesta: int                          │
                           │                                        │ - fechaArmado: Date                          │
                           ▼ 1                                      │ - estado: String                             │
 ┌───────────────────────────────────────────────────┐              ├──────────────────────────────────────────────┤
 │                   <<interface>>                   │              │ + agregarServicio(s: IServicioTuristico):void│
 │            IEstrategiaAsignacionAgente            │              │ + calcularTotalPropuesta(): float            │
 │       [PATRÓN GOF 2: STRATEGY (Comportamiento)]   │              └──────────────────────┬───────────────────────┘
 ├───────────────────────────────────────────────────┤                                     │ 1
 │ + seleccionarAgente(agentes: List<Agente>,        │                                     ◆ incluye (1..* servicios)
 │     sol: SolicitudViaje): Agente                  │                                     ▼
 └─────────────────────────△─────────────────────────┘              ┌──────────────────────────────────────────────┐
                           ┆                                        │                 <<interface>>                │
             ┌─────────────┴─────────────┐                          │              IServicioTuristico              │
 ┌───────────┴───────────┐   ┌───────────┴───────────┐              ├──────────────────────────────────────────────┤
 │AsignacionViajeFamiliar│   │AsignacionCorporativa  │              │ + obtenerCosto(): float                      │
 ├───────────────────────┤   ├───────────────────────┤              │ + obtenerDescripcion(): String               │
 │ + seleccionarAgente() │   │ + seleccionarAgente() │              └──────────────────────△───────────────────────┘
 └───────────────────────┘   └───────────────────────┘                                     ┆
                                                                   ┌───────────────┬───────┴────────┬──────────────┐
                                                             ┌─────┴─────┐   ┌─────┴─────┐    ┌─────┴─────┐  ┌─────┴─────┐
                                                             │   Vuelo   │   │Alojamiento│    │ Excursion │  │  Seguro   │
                                                             ├───────────┤   ├───────────┤    ├───────────┤  ├───────────┤
                                                             │ - aerolin │   │ - hotel   │    │ - guia    │  │ - cobert  │
                                                             │ - costo   │   │ - noches  │    │ - costo   │  │ - costo   │
                                                             ├───────────┤   ├───────────┤    ├───────────┤  ├───────────┤
                                                             │ +obtener..│   │ +obtener..│    │ +obtener..│  │ +obtener..│
                                                             └───────────┘   └───────────┘    └───────────┘  └───────────┘
```

#### 1.C. Justificación de los 2 Patrones GRASP (Sin contar Controller, tal como exige la consigna)
1. **Creador (*Creator*):** Se aplica en la clase **`Cliente`** con el método **`+crearSolicitud(destino, fechas, pasaj, tipo)`** que instancia a **`SolicitudViaje`**, y a su vez en **`SolicitudViaje`** con el método **`+crearPropuesta()`** que instancia a **`PropuestaViaje`**. Esto se justifica porque `Cliente` agrega y registra sus solicitudes de viaje, y `SolicitudViaje` contiene los datos de inicialización y registra las propuestas confeccionadas para dicha solicitud.
2. **Experto en Información (*Information Expert*):** Se aplica en la clase **`PropuestaViaje`** en el método **`+calcularTotalPropuesta()`**, dado que `PropuestaViaje` es la clase que conoce y contiene la colección de objetos `IServicioTuristico` (`Vuelo`, `Alojamiento`, `Excursion`, `Seguro`), por lo que itera sobre ellos pidiéndole a cada servicio experto su propio costo mediante `+obtenerCosto()`.

---

### PUNTO 2 (AGENCIA DE VIAJES): ESCENARIO Y DIAGRAMA DE SECUENCIA

#### 2.A. Escenario Concreto
> **Escenario:** Se registra un nuevo cliente corporativo (`"TechCorp SA"`, email `"viajes@techcorp.com"`), se crea su solicitud de viaje a `"Madrid"` para `4` pasajeros en modalidad `"Corporativo"`, el sistema le asigna automáticamente un agente disponible especializado en viajes corporativos a Europa, y se arma su propuesta personalizada cotizando e incluyendo `1 Vuelo` y `1 Alojamiento` a través de los proveedores externos.

#### 2.B. Diagrama de Secuencia Completo

```
  :C_SolicitudViaje  :NominaClientes     cli:Cliente       sol:SolicitudViaje  :NominaAgentes  :AsignacionCorp  ag:Agente    :C_Propuesta   :CatalogoProv     p:PropuestaViaje
          │                 │                 │                    │                 │                │            │              │               │                  │
 ●─procesarNuevaSolicitud──►│                 │                    │                 │                │            │              │               │                  │
   (datosCli, "Madrid",     ├─registrarCli()─►┌─┐                  │                 │                │            │              │               │                  │
    fechas, 4, "Corp")      │                 │ ├─create(datosCli)►┌─┐               │                │            │              │               │                  │
          │                 │◄───── cli ──────└─┘                  └┬┘               │                │            │              │               │                  │
          │                 │                                       │                │                │            │              │               │                  │
          ├─crearSolicitud("Madrid", fechas, 4, "Corp")────────────►┌─┐              │                │            │              │               │                  │
          │                 │                                       │ ├─create(...)─►┌─┐              │            │              │               │                  │
          │◄─────────────────────────── sol ────────────────────────└─┘              └┬┘              │            │              │               │                  │
          │                                                                           │               │            │              │               │                  │
          ├─buscarAgenteApto("Madrid", "Corp", estratCorp)───────────────────────────►┌─┐             │            │              │               │                  │
          │                                                                           │ ├─seleccionar►┌─┐          │              │               │                  │
          │                                                                           │ │  Agente(..) │ ├─esApto()►┌─┐            │               │                  │
          │                                                                           │ │             │ │◄─ true ──└─┘            │               │                  │
          │                                                                           │ │◄─── ag ─────└─┘          │              │               │                  │
          │◄─────────────────────────── ag ───────────────────────────────────────────└─┘                          │              │               │                  │
          │                                                                                                        │              │               │                  │
          ├─asignarAgente(ag)────────────────────────────────────────────────────────►┌─┐                          │              │               │                  │
          │                                                                           │ ├─asignarSolicitud()──────►┌─┐            │               │                  │
          │                                                                           │ │◄────── ok ───────────────└─┘            │               │                  │
          │◄─────────────────────────── ok ───────────────────────────────────────────└─┘                                         │               │                  │
 ◄──sol───┘                                                                           │                                           │               │                  │
                                                                                      │                                           │               │                  │
 ●─armarPropuesta(idSol, datosServicios)──────────────────────────────────────────────┼──────────────────────────────────────────►┌─┐             │                  │
                                                                                      │◄─────────crearPropuesta()─────────────────┤ │             │                  │
                                                                                      ├─create()──────────────────────────────────┼─┼─────────────┼─────────────────►┌─┐
                                                                                      │                                           │ ├──cotizarServicio("Vuelo",...)─►┌─┐│
                                                                                      │                                           │ │◄──── s1:Vuelo ─────────────────└─┘│
                                                                                      │                                           │ ├──agregarServicio(s1)──────────►┌─┐
                                                                                      │                                           │ │◄──── ok ───────────────────────└─┘
                                                                                      │                                           │ ├──cotizarServicio("Hotel",...)─►┌─┐│
                                                                                      │                                           │ │◄──── s2:Alojamiento ───────────└─┘│
                                                                                      │                                           │ ├──agregarServicio(s2)──────────►┌─┐
                                                                                      │                                           │ │◄──── ok ───────────────────────└─┘
                                                                                      │                                           │ ├──calcularTotalPropuesta()─────►┌─┐
                                                                                      │                                           │ │◄──── montoTotal ───────────────└─┘
 ◄── propuestaArmada(p) ──────────────────────────────────────────────────────────────┴───────────────────────────────────────────└─┘
```

---

### PUNTO 3 (AGENCIA DE VIAJES): 2 PATRONES GOF DE DIFERENTE CATEGORÍA (SIN SINGLETON NI FACADE)

1. **Patrón 1 — `Adapter` (Categoría: Estructural):**
   - **Problema que resuelve:** La agencia necesita consultar disponibilidad y tarifas en tiempo real en múltiples sistemas externos de aerolíneas (`API_Amadeus`) y hoteles (`API_HotelWS`), los cuales tienen interfaces incompatibles entre sí y ajenas a nuestro dominio.
   - **Justificación:** Mediante la interfaz `<<interface>> IProveedorTuristico` y las clases adaptadoras `AdaptadorGDS_Aerolinea` y `AdaptadorBookingHotel`, el `CatalogoProveedores` consulta a cualquier proveedor externo con un único método uniforme (`+obtenerServicioCotizado()`), desacoplando por completo al dominio de las APIs externas.
2. **Patrón 2 — `Strategy` (Categoría: Comportamiento):** *(Nota: También podrías elegir `Builder` como Creacional para el armado paso a paso de la `PropuestaViaje`, o `State` para los estados de la `SolicitudViaje`).*
   - **Problema que resuelve:** El criterio para asignar automáticamente al `Agente` varía según si la solicitud es para un viaje familiar/amigos (prioriza experiencia en el destino turístico y recreación) o un viaje corporativo (prioriza ejecutivos de cuentas corporativas, gestión de salas de convenciones y facturación empresarial).
   - **Justificación:** La interfaz `<<interface>> IEstrategiaAsignacionAgente` implementada por `AsignacionViajeFamiliar` y `AsignacionCorporativa` permite intercambiar dinámicamente el algoritmo de selección de agente sin usar condicionales rígidos en `NominaAgentes` ni en `SolicitudViaje`.

---

## PARTE 4: RESOLUCIÓN COMPLETA DEL PARCIAL 1C 2026 (COMISIÓN 1900 — VALERIA Y ANALÍA MARÍN)
### CASO: "REFUGIO DE MASCOTAS" (`Parciales/2. -Parcial 1--1C2026--1900--Valeria y Analia-----.pdf`)

#### Síntesis del Enunciado y Requisitos Exactos
- Un **Refugio de Mascotas** rescata animales, les crea una **Ficha Animal** (con su **Historial Médico** y **Evaluación Conductual**), gestiona **Postulantes a Adopción** (quienes pasan por una **Entrevista/Evaluación**), formaliza la adopción mediante un **Contrato de Adopción**, realiza un **Seguimiento Post-Adopción** periódico (visitas, fotos, estado de adaptación) y además administra **Donaciones** recibidas y el **Inventario de Insumos** (alimentos, medicamentos).
- **Consigna:**
  1. **Diagrama de Clases** (máximo **4 controllers**) + **2 patrones GRASP (sin contar Controller)**.
  2. **Diagrama de Secuencia** desde que se registra un postulante, se evalúa y aprueba su solicitud de adopción y se genera el contrato de adopción.
  3. **2 Patrones GoF de diferente categoría** (**sin usar Singleton ni Facade**).

#### Resumen Estructural de la Solución 10 Puntos (Refugio de Mascotas)
- **Los 4 Controladores:**
  1. `C_RescateSanidad` (Ingreso de animales rescatados, ficha médica y conductual).
  2. `C_Adopcion` (Registro de postulante, evaluación de entrevista, aprobación y firma de contrato).
  3. `C_Seguimiento` (Visitas y controles post-adopción).
  4. `C_DonacionInventario` (Registro de donaciones y control de stock de insumos).
- **Clases Principales del Dominio y sus Relaciones:**
  - `NominaAnimales` ◆── `AnimalRescatado` (`1` ◆── `1` `FichaMedica` y `1` ◆── `1` `FichaConductual`).
  - `NominaPostulantes` ◆── `Postulante` (`+registrarPostulante()`, `+evaluarAptitud()`).
  - `SolicitudAdopcion` (conoce a `1` `Postulante`, `1` `AnimalRescatado`, `1..*` `Entrevista`, y al aprobarse genera `0..1` `ContratoAdopcion`).
  - `ContratoAdopcion` (`+generarClausulas()`, `+registrarFirma()`) ◆── `1..*` `ControlSeguimiento` (fecha, informeVisita, fotos).
  - `Inventario` ◆── `Insumo` (`stockActual`, `stockMinimo`) y `Donacion` (`DonacionMonetaria`, `DonacionEspecie`).
- **2 Patrones GRASP Justificados (sin contar Controller):**
  1. **Creador (*Creator*):** `SolicitudAdopcion` crea (`create`) a `ContratoAdopcion` mediante `+aprobarYGenerarContrato()`, ya que posee todos los datos de inicialización (`Postulante` aprobado, `AnimalRescatado` asignado, fecha y condiciones) y registra el contrato resultante.
  2. **Experto en Información (*Information Expert*):** `AnimalRescatado` junto con su `FichaConductual` y `FichaMedica` son los expertos para responder `+esCompatibleCon(postulante: Postulante): Boolean`, comparando los requerimientos del animal (ej. necesita patio cerrado, tratamiento crónico) con las características de vivienda y disponibilidad declaradas por el `Postulante`.
- **Secuencia (Punto 2 — Registro de postulante, aprobación y generación de contrato):**
  - **Escenario:** Se registra al postulante `"Juan Pérez"` (DNI `"38999888"`, casa con patio cerrado), quien solicita adoptar al perro rescatado `"Toby"` (`idAnimal = 12`). Se registra su entrevista con resultado `"Apto"`, se aprueba la solicitud de adopción cambiando el estado de `"Toby"` a `"Adoptado"` y se genera el `ContratoAdopcion`.
  - **Flujo de mensajes:** `● ──► :C_Adopcion.procesarAdopcion(datosPostulante, idAnimal=12, datosEntrevista)` → `:NominaPostulantes.registrarPostulante(datos)` → `create() ► p:Postulante` → `:NominaAnimales.buscarAnimal(12)` → retorna `a:AnimalRescatado` → `:C_Adopcion` crea `sol:SolicitudAdopcion(p, a)` → `sol.registrarEntrevista(datosEntrevista)` → `sol.evaluarCompatibilidad()` (que consulta a `a.esCompatibleCon(p)`) → `sol.aprobarAdopcion()` → `a.cambiarEstado(EstadoAdoptado)` → `sol.generarContrato()` → `create() ► c:ContratoAdopcion(p, a, fecha)`.
- **2 Patrones GoF de Diferente Categoría (Punto 3 — Sin Singleton ni Facade):**
  1. **Categoría Comportamiento — Patrón `State`:** Aplicado sobre `AnimalRescatado` (o sobre `SolicitudAdopcion`). El animal atraviesa los estados `EstadoEnRecuperacion`, `EstadoDisponibleAdopcion`, `EstadoReservadoEnEvaluacion` y `EstadoAdoptado`, implementando la interfaz `<<interface>> IEstadoAnimal` (`+postularAdopcion()`, `+aprobarAdopcion()`, `+registrarControlMed()`). Así, un animal en estado `EnRecuperacion` rechaza automáticamente cualquier intento de adopción sin usar condicionales `if`.
  2. **Categoría Creacional — Patrón `Builder`** *(o **Categoría Estructural — Patrón `Decorator` / `Adapter`**)*:
     - Con **`Builder` (Creacional):** `IContratoAdopcionBuilder` implementado por `ContratoAnimalEstandarBuilder` y `ContratoCuidadosEspecialesBuilder` para construir paso a paso el `ContratoAdopcion` (`+construirEncabezadoLegal()`, `+agregarCompromisoCastracion()`, `+agregarCalendarioVacunacion()`, `+agregarCronogramaSeguimiento()`).

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
