# 01 — CRITERIOS, CONVENCIONES Y CONSEJOS DE LA PROFESORA (ING. ANALÍA MARÍN)

> **Propósito de este documento:** Este archivo concentra **las reglas exactas con las que la Prof. Ing. Analía Marín (y el JTP Alejandro) corrigen los parciales y finales**.  
> En Diseño de Sistemas, muchos alumnos desaprueban no por no saber qué es una clase o un patrón, sino por **violar reglas de diseño, trazabilidad o convención** que la profesora repite en clase y deja por escrito en sus guías.  
> **Cada criterio aquí expuesto está respaldado por su cita exacta** al archivo oficial de la cátedra, número de página o minuto de la transcripción de clase.

---

## 1. FILOSOFÍA GENERAL DE CORRECCIÓN: "¿QUÉ BUSCA ANALÍA MARÍN EN EL PARCIAL?"

### 1.1. Nivel de Baja Abstracción: "Estamos en Diseño, NO en Análisis"
- **Criterio de la Profesora:** En Análisis de Sistemas alcanzaba con dibujar cajas con sustantivos (Modelo Conceptual del Dominio). En **Diseño de Sistemas**, el modelo debe tener **baja abstracción** y estar **cerca del código fuente**. Esto exige:
  1. Clases del dominio con **atributos tipados/concretos** y **métodos de negocio reales**.
  2. **Visibilidad** explícita (`-` privado, `+` público, `#` protegido).
  3. **Clases de Diseño (Fabricación Pura / Soporte):** Controladores (`C_...`), Nóminas/Catálogos/Padrón (si hace falta manejar colecciones), Interfaces (`<<interface>>`), Clases Abstractas (`<<abstract>>`) y las clases que implementan **Patrones GoF**.
  4. **Parámetros en los métodos clave:** Especialmente en el Diagrama de Secuencia y en los métodos que reciben referencias a objetos o IDs desde la interfaz.
- **Evidencia:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 16): *"El diagrama de clases muestra las clases del sistema, sus atributos, métodos y las relaciones entre ellas. Es la base del diseño orientado a objetos y sirve de puente entre los requerimientos y el código"*.
  - `Transcripcion/transcripciones/09_20261015_082342.txt` (`[00:13:02]` y `[01:15:36]`): *"Acá estamos en diseño, nos tenemos que acercar al código... No nos podemos quedar en un modelo conceptual"*.

### 1.2. Prohibición Absoluta de "ABMs / CRUDs Triviales" y Getters/Setters Masivos
- **Criterio de la Profesora:** Está terminantemente prohibido llenar las clases de métodos `alta()`, `baja()`, `modificacion()`, `getNombre()`, `setNombre()`, o poner un `Controller` por cada clase para hacer un ABM. **En el parcial se modela el CORE (corazón) del negocio.**
- **Frases textuales de clase y guías:**
  - `Clases/Clases/03/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx` (Sección Clases): *"Evitar pensar que cada clase tiene un controller para hacer un ABM (alta-baja-modificación). Eso en los parciales NO VA. Siempre vamos al CORE del negocio."*
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 30): *"Si cada clase tiene un controlador para el alta, baja o modificación del objeto, ¿para qué están las relaciones de las clases?... Evitar los get y set, eso ya es por defecto por el paradigma."*
  - `Parciales/1. [Parcial 1][1C2026][4300][Analia][][].pdf` (Nota al pie): *"NO realizar operaciones CRUD triviales (alta/baja/modificación sin reglas de negocio) ni getters y setters."*
- **Qué hacer en su lugar:** Si la clase necesita inicializarse, usar su constructor (`crear(...)` / `new`) y métodos con **nombre de regla de negocio** (ej.: `validarVigencia()`, `registrarVacuna(v)`, `calcularMontoTotal()`, `verificarCupo()`, `confirmarReserva()`). Solo incluir un `get` puntual si en el Diagrama de Secuencia necesitás pedir un dato específico a otro objeto para un cálculo (Experto en Información).

### 1.3. Reglas Formales de Entrega en Hoja (Formato de Examen Presencial)
- **Criterio obligatorio en todos los parciales 2026:**
  1. **"ENTREGAR UN DIAGRAMA POR HOJA, ENUMERAR LAS HOJAS A ENTREGAR."** (Aparece en mayúsculas y subrayado al final de `1. [Parcial 1][1C2026][4300][Analia][][].pdf`, `2. [Parcial 1][1C2026][1900]...` y `3. [Parcial 1][2C2026][1900]...`).
  2. **Hoja 1:** Diagrama de Clases completo (con las clases del dominio, los Controllers y los 2 patrones GoF integrados — o marcando claramente con color/estereotipo qué clases pertenecen a cada patrón GoF) + Tabla/Justificación de GRASP.
  3. **Hoja 2:** Escenario redactado arriba + Diagrama de Secuencia completo.
  4. **Hoja 3:** Explicación y justificación detallada de los 2 Patrones GoF (Categoría, Nombre, Problema del caso, Por qué es adecuado, Clases reutilizadas del Punto 1 y Clases/Interfaces nuevas incorporadas).

---

## 2. EL ERROR ELIMINATORIO N° 1: TRAZABILIDAD E INTEGRACIÓN ENTRE DIAGRAMAS

La profesora repite en **todas** las clases prácticas que los diagramas de UML no son dibujos sueltos, sino **distintas vistas del MISMO sistema** (Modelo 4+1 de Kruchten). Por lo tanto, tienen que ser **100% consistentes entre sí**.

### 2.1. Regla de Oro de Correspondencia de Mensajes y Métodos
> **REGLA ELIMINATORIA:** Si en el **Diagrama de Secuencia** (o de Colaboración) el objeto `A` le envía el mensaje `m()` al objeto `B` (`A ─── m() ──► :B`), entonces:
> 1. **El método `+m()` DEBE estar escrito en el compartimento de métodos de la clase `B` en el Diagrama de Clases.** (¡No en `A`! El método pertenece a la clase que **recibe** el mensaje y ejecuta la acción).
> 2. **La clase `A` DEBE tener visibilidad hacia la clase `B` en el Diagrama de Clases** (ya sea una línea de asociación si es visibilidad permanente de atributo, o una flecha punteada de dependencia `..>` si `B` entra como parámetro o variable local).
> 3. Si además se pide un **Diagrama de Estados** para el objeto `B`, todas las transiciones/eventos de ese Diagrama de Estados **DEBEN coincidir con los métodos de la clase `B` en el Diagrama de Clases**.

- **Evidencia documental directa:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 16): *"NOTA: Todos los mensajes que están presentes en el diagrama de secuencia, colaboración y estado deben estar en el diagrama de clases. Las vistas deben ser consistentes."*
  - `Clases/Clases/03/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx` (Sección Secuencia): *"Cada mensaje que llega a un objeto es un método en esa clase. Verificar que en el diag de clases se encuentren esos métodos. Si hay mensajes en el diag. de interacción que no están en el diag de CLASES, el ejercicio está MAL."*
  - `Transcripcion/transcripciones/09_20261015_082342.txt` (`[01:55:12]`): *"Chicos, cuando corregimos ponemos el Diagrama de Secuencia al lado del Diagrama de Clases. Si en secuencia llaman a `validarVacuna()` en `HistoriaClinica`, vamos a buscar `validarVacuna()` en la clase `HistoriaClinica`. Si no está, está mal."*

---

## 3. CRITERIOS ESPECÍFICOS PARA EL DIAGRAMA DE CLASES

### 3.1. Organización Visual del Diagrama de Clases ("Arriba hacia Abajo, Izquierda a Derecha")
La profesora exige que el Diagrama de Clases esté ordenado visualmente por capas para que sea legible al corregir:
1. **Parte Superior (Arriba de todo):** Los **Controladores (`C_...`)**.
2. **Parte Media-Alta (Debajo de los Controllers):** Los **Gestores / Nóminas / Padrón** (únicamente si son necesarios; ver regla 3.3).
3. **Parte Central e Inferior:** Las **Clases del Modelo de Dominio** y las **jerarquías de herencia / patrones GoF**, agrupadas verticalmente en columnas según el módulo o componente al que pertenecen.
4. **¿Qué NO va en el Diagrama de Clases?** No va la capa de Base de Datos (tablas SQL, `DAO`, `Repository` genéricos) ni las pantallas HTML/Vistas, salvo que se aplique un patrón específico que requiera una interfaz de vista.
- **Evidencia:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 28): *"Leer el diagrama de arriba hacia abajo, de izquierda a derecha... Arriba van los controladores, debajo las clases del dominio agrupadas por cercanía funcional."*
  - `Clases/Clases/03/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx`: *"Organizar visualmente el diagrama: arriba los controllers, luego las clases principales, y hacia abajo las clases de detalle o soporte."*

### 3.2. Cuántos Controladores (`Controller` GRASP) poner y cómo nombrarlos
- **Nomenclatura:** La profesora utiliza el prefijo `C_` o `c_` seguido del nombre del módulo/componente o caso de uso agrupado:
  - Ejemplo Laboratorio (`EJEMPLO-Practica-Teoria-version-10.pdf`, Pág. 16): `C_turno`, `C_Recepcion`, `C_Analitica`, `C_Pago`, `C_Validacion`.
  - Ejemplo Banco (`Clases/05/Banco/diagramaClases.png`): `C_EvaluacionP`, `C_prestamo`, `C_Cliente`.
  - Ejemplo Estadios (`Clases/06/Estadio/Clases.jpg`): `c_empadronar`, `c_ingreso`.
  - Ejemplo Gimnasio (`EJEMPLO-Practica-Teoria-version-10.pdf`, Pág. 28): `C_Inscripcion`.
- **Cantidad exacta en el Parcial:**
  - En la práctica real no se pone 1 Controller para todo el sistema (porque queda **saturado** y viola la Alta Cohesión) ni tampoco 1 Controller por cada Caso de Uso individual si hay 15 casos de uso (por falta de tiempo en el examen).
  - **Criterio de cátedra:** Definir **1 Controller por cada Módulo / Componente funcional principal** del sistema.
  - **Límite explícito en los parciales 2026:**
    - En `1. [Parcial 1][1C2026][4300][Analia][][].pdf` (Veterinaria PetCare): **"incluir máximo 3 controllers"**. (Por ejemplo: `C_AtencionMedica` / `C_Consulta`, `C_Turno`, `C_Facturacion` / `C_Pago`).
    - En `2. [Parcial 1][1C2026][1900]...` (Refugio) y `3. [Parcial 1][2C2026][1900]...` (Agencia de Viajes): **"incluir máximo 4 controllers"**.
- **Qué tiene adentro un Controller:**
  - **NO tiene atributos de negocio propios** (no guarda el `nombreCliente` ni el `saldo`). A lo sumo guarda referencias temporales a los objetos con los que coordina la sesión.
  - **Sus métodos son los manejadores de los eventos de entrada del sistema** (ej. `iniciarAtencion(...)`, `registrarVacuna(...)`, `emitirReceta(...)`, `finalizarConsulta(...)`).
  - **Su responsabilidad es coordinar ("director de orquesta"):** Recibe datos primitivos/IDs de la UI, busca las referencias a los objetos correspondientes y **delega** el trabajo real a las clases del dominio (Experto).
- **Evidencia:**
  - `Clases/Clases/04-Presencial/UNLaM GRASP-original-marin.pdf` (Pág. 62): *"Aclaración: En el examen, debido a limitaciones de tiempo, no vamos a poder implementar un controlador por cada Caso de Uso (CU). En su lugar, el diseño debe contemplar un controlador por módulo o subsistema."*
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 16 y Pág. 28): *"El controlador captura el evento y delega a quien corresponda. Tiene lógica mínima."*

### 3.3. Diferencia entre `Controller` y `Gestor` (¡Cuidado con el "Gestor Pasapelotas"!)
En la Clase 07 y en las páginas 29–31 de `EJEMPLO-Practica-Teoria-version-10.pdf`, un alumno preguntó cuándo usar un `Gestor` debajo del `Controller`. La respuesta de la profesora es taxativa:
- **El Error del "Pasapelotas":** Si ponés un `C_Inscripcion` con el método `inscribirSocio()` y abajo ponés un `GestorInscripcion` con el mismo método `inscribirSocio()` que hace exactamente lo mismo, **está MAL** (es redundante y agrega acoplamiento inútil).
- **Cuándo SÍ tiene sentido un Gestor o Nómina/Padrón:**
  1. Cuando el `Controller` se vuelve **saturado** porque además de recibir eventos de UI hay que orquestar reglas de negocio complejas entre múltiples subsistemas.
  2. Cuando necesitás una **clase contenedora de colección (Fabricación Pura / Multiobjeto)** como `Padron` (en Caso Estadios) o `NominaPacientes` / `CatalogoEstudios` para buscar objetos en memoria (`buscarAficionado(dni)`, `existeSocio(id)`) sin ensuciar la clase individual `Aficionado` o `Socio`.
- **Evidencia:** `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 29–31) y `Transcripcion/transcripciones/07_20261001_082247.txt` (`[00:18:40]`).

### 3.4. Diferencia Estricta entre "Actor del Sistema" y "Clase del Dominio" (El Error del `Recepcionista` / `Veterinario`)
Este es uno de los errores más corregidos en la Clase 09 (`09_20261015_082342.txt`):
- **El Error Frecuente:** El enunciado dice *"El veterinario registra los datos de la mascota, aplica vacunas y emite la receta"* o *"La recepcionista da de alta el turno"*. Muchos alumnos crean la clase `Veterinario` o `Recepcionista` y le ponen los métodos `+registrarMascota()`, `+aplicarVacuna()`, `+emitirReceta()`, o hacen que el `Controller` llame a `veterinario.atender()`.
- **Por qué está MAL según la Profesora:**
  1. La persona humana que tipea en la pantalla es el **Actor** que dispara el evento hacia el `Controller`. **No es un objeto de software ejecutando lógica de negocio.**
  2. Si le ponés todos los métodos del sistema a la clase `Veterinario`, convertís a `Veterinario` en una **clase Dios / Gestor encubierto** (violando **Experto en Información** y **Alta Cohesión**). Quien conoce las consultas y vacunas de una mascota es la `HistoriaClinica` (o `Mascota` / `Consulta`), ¡no el `Veterinario`!
  3. **¿Cuándo SÍ va la clase `Veterinario`, `Medico` o `AgenteDeViajes` en el Diagrama de Clases?** Únicamente como **entidad de datos del dominio** cuando el negocio requiere guardar **quién** atendió la consulta (ej. `Consulta` tiene una asociación con `Veterinario` que guarda `matricula`, `nombre`, `especialidad`), o cuando el sistema debe **asignar automáticamente un Agente/Profesional según su disponibilidad o especialidad** (como en el Parcial de *Agencia de Viajes* donde se busca un `Agente` por destino/experiencia, o en *Turnos* donde se consulta la `Agenda` del `Profesional`).
  4. **¿Y si el enunciado habla de permisos de usuarios (Recepcionista, Admin, Bioquímico)?** No se crean subclases de usuario con métodos de negocio, sino el modelo extensible **`Usuario` → `Perfil` (o `Rol`) → `Permiso`** (como muestra la profesora en `EJEMPLO-Practica-Teoria-version-10.pdf`, Pág. 24).
- **Evidencia:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 20 y Pág. 24): *"Recepcionista y Bioquímico son actores, son roles que operan el sistema, NO son clases que lanzan métodos. Si se requiere modelar quién hizo qué o sus permisos, se modela Usuario con Perfil y Permiso para favorecer la Extensibilidad."*
  - `Transcripcion/transcripciones/09_20261015_082342.txt` (`[01:28:15]` y `[01:42:50]`): *"El veterinario es el actor que está sentado frente a la pantalla cargando la consulta del gato Homero. La clase Veterinario solo guarda su matrícula y nombre asociada a la Consulta o Receta, ¡el Veterinario no es el que guarda la vacuna en la base ni valida la fecha, eso lo hace Consulta o HistoriaClinica!"*

### 3.5. El Problema de la "Ficha Única" vs. "El Fichero (Colección / Multiobjeto)"
- **Criterio de la Profesora:** Una clase como `Socio`, `Aficionado`, `Mascota` o `Consulta` representa **UN único individuo o una única ficha atómica** (una instancia).
  - **Pregunta de control de la profesora:** Si tenés la clase `Consulta` (que representa *una* visita médica del día de hoy), ¿puede esa instancia `Consulta` tener el método `buscarConsultasAnteriores()`? **¡NO! Porque una instancia de `Consulta` solo se conoce a sí misma.**
  - **Solución correcta en Diseño:** Quien tiene la colección de todas las consultas de una mascota (` List<Consulta>`) es su **`HistoriaClinica`** (o `Mascota`). Por lo tanto, el método `agregarConsulta(c)` o `obtenerHistorial()` o `verificarVacunasVigentes()` pertenece a **`HistoriaClinica`**, la cual itera sobre su colección de objetos `Consulta` / `VacunaAplicada`.
  - Del mismo modo, si necesitás buscar un `Aficionado` por DNI entre todos los hinchas del país (Caso Estadios, Clase 06), una instancia de `Aficionado` no puede buscar a todos los demás aficionados; para eso existe la clase contenedora **`Padron`** (o un multiobjeto `:Aficionado` / `NominaAficionados` en el DC) que contiene `aficionados: List<Aficionado>` y tiene el método `+buscarAficionado(dni): Aficionado`.
- **Evidencia:**
  - `Transcripcion/transcripciones/06_20260924_114136.txt` (`[00:05:10]` a `[00:16:30]`).
  - `Transcripcion/transcripciones/09_20261015_082342.txt` (`[00:35:20]` y `[01:36:40]`): *"Una clase representa una ficha. Para buscar en el fichero necesitás a quien contiene la colección: la Historia Clínica, el Padrón o la Nómina."*

### 3.6. Visibilidad (Larman Cap. 18) y Cuándo Dibujar Asociación vs. Dependencia en el Diagrama de Clases
En la Clase 07 (`07_20261001_082247.txt`) y en las páginas 32–33 de `EJEMPLO-Practica-Teoria-version-10.pdf`, la profesora explica cómo aplicar los 4 tipos de visibilidad de Craig Larman:
1. **Visibilidad de Atributo (Permanente):** `A` tiene un atributo que apunta a `B` (la relación perdura más allá de la ejecución de un método; ej.: `Mascota` conoce a su `HistoriaClinica`, `Consulta` conoce a sus `Vacuna`s).
   - **¿Cómo se dibuja en el Diagrama de Clases?** Como una **línea sólida de Asociación** (o Agregación/Composición) entre `A` y `B`, con su **multiplicidad** (`1`, `0..*`, `1..*`) y navegabilidad si corresponde.
2. **Visibilidad de Parámetro o Local (Transitoria/Temporal):** `A` no guarda a `B` como atributo permanente, sino que recibe a `B` como parámetro en un método (`metodo(b: B)`) o lo instancia/busca localmente dentro de un método para llamarle una operación y luego lo descarta (muy común en los `Controllers`).
   - **¿Cómo se dibuja en el Diagrama de Clases?** Con una **línea punteada con flecha abierta de Dependencia (`- - - >`)**, o bien como relación del `Controller` hacia las clases principales con las que inicia el flujo.
   - **Advertencia de la Profesora:** *"En el diagrama de clases se grafican las relaciones permanentes (visibilidad de atributo) y las más significativas. NO tiren líneas de asociación sólidas desde el Controller hacia las 20 clases del diagrama porque queda una telaraña ilegible y conceptualmente incorrecta (el Controller no es dueño permanente de todo el dominio)"*. El Controller solo se relaciona con las 2 o 3 clases raíz a las que delega la coordinación.
- **Evidencia:** `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 32–33).

### 3.7. Pasaje de Parámetros desde la UI: "IDs Primitivos afuera, Referencias a Objetos adentro"
- **Criterio de la Profesora:** Cuando el evento entra desde la pantalla HTML al `Controller`, la pantalla no tiene "el objeto `Socio` en memoria de backend"; la pantalla envía **datos primitivos o IDs** (ej.: `idMascota`, `dniCliente`, `codigoVacuna`, `observaciones`).
  1. El **`Controller`** recibe esos datos primitivos: `+registrarAtencion(idMascota, datosConsulta, listaCodigosVacunas)`.
  2. El primer paso dentro del sistema es **obtener la referencia al objeto** buscando por ese ID (ej.: pidiéndole a la nómina/contenedor `mascota = buscarMascota(idMascota)`).
  3. Una vez obtenida la referencia `mascota`, entre los objetos del dominio se pasan **referencias a objetos** (ej.: `historiaClinica.agregarConsulta(nuevaConsulta)` pasa el objeto `nuevaConsulta`, no un `idConsulta`).
- **Evidencia:** `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 28): *"De la interfaz vienen los IDs; el controlador busca el objeto para obtener su referencia y a partir de ahí trabaja con referencias a objetos."*

### 3.8. Uso Correcto de Agregación (Rombo Blanco) vs. Composición (Rombo Negro) vs. Asociación Simple
- **Asociación simple (`───`):** Relación estructural normal entre dos clases independientes (ej. `Consulta` con `Veterinario`, `Turno` con `Paciente`). **Ante la duda, usar asociación simple con multiplicidad correcta.**
- **Agregación (`◇───` rombo blanco del lado del Todo):** Relación "Todo-Parte" débil donde las partes pueden existir independientemente del Todo y compartirse (ej.: `Equipo` y `Jugador`, `Catalogo` y `Producto`).
- **Composición (`◆───` rombo negro relleno del lado del Todo):** Relación "Todo-Parte" **fuerte y de pertenencia exclusiva**. Si se destruye el Todo, carece de sentido o se destruyen sus Partes, y una instancia de la Parte pertenece a un único Todo (ej.: `Factura` ◆── `ItemFactura`, `Prestamo` ◆── `Cuota`, `Mascota` ◆── `HistoriaClinica`, `Aficionado` ◆── `Huella`).
- **Evidencia:** `Transcripcion/transcripciones/03_20260903_101348.txt` (`[00:41:15]`) y `Clases/Clases/05/Banco/diagramaClases.png`.

### 3.9. Clases Abstractas (`<<abstract>>`) vs. Interfaces (`<<interface>>`)
- **Clase Abstracta (`<<abstract>>` o nombre en cursiva):**
  - Se usa cuando existe una **relación de identidad "ES UN" (herencia)** entre las subclases y **comparten atributos comunes** y/o **métodos ya implementados**, además de declarar métodos abstractos que cada hija sobrescribe (polimorfismo).
  - *Ejemplo de la Profesora (`Banco/diagramaClases.png` y `EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 23):* La clase `Producto` (`<<abstract>>`) tiene `nroProducto`, `fechaAlta` y es padre de `Prestamo` y `Cuenta`. La clase `Pago` (`<<abstract>>`) tiene `monto`, `fecha` y el método polimórfico `+procesarPago()`, siendo padre de `Efectivo`, `Tarjeta` y `Transferencia`.
- **Interfaz (`<<interface>>`):**
  - Es un **contrato puro de comportamiento**: **NO tiene atributos de estado** ni código implementado (en el modelo clásico OO que evalúa la cátedra), solo firmas de métodos públicos abstractos (`+calcular()`, `+notificar()`, `+conectar()`).
  - La relación desde la clase que la implementa hacia la interfaz es de **Realización** (flecha triangular cerrada con **línea punteada** `- - -▷`).
  - Es fundamental en los **Patrones GoF** (`Strategy`, `Observer`, `State`, `Adapter`, `Command`, `Decorator`, `Factory Method`).
- **Regla de notación de la profesora en hoja:** Como escribiendo a mano no se nota la letra *cursiva*, **escribir SIEMPRE el estereotipo `<<abstract>>` o `<<interface>>` arriba del nombre de la clase** y también al lado de los métodos abstractos si querés máxima claridad.
- **Evidencia:** `Transcripcion/transcripciones/03_20260903_101348.txt` (`[00:25:10]` a `[00:39:00]`) y `Clases/Clases/03/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx`.

---

## 4. CRITERIOS ESPECÍFICOS PARA EL DIAGRAMA DE SECUENCIA (PUNTO 2 DEL PARCIAL)

El Punto 2 de todos los parciales de Analía Marín pide construir un **Diagrama de Secuencia** para un flujo específico del enunciado. Sus reglas son súper precisas:

### 4.1. Regla N° 1: Escribir Arriba el "Escenario Concreto" con Datos Puntuales
- **Por qué lo exige la profesora:** Si intentás dibujar en un solo Diagrama de Secuencia todos los `if/else` posibles del sistema (qué pasa si el cliente existe, si no existe, si paga con efectivo, con tarjeta, con transferencia, si lleva 1 o N vacunas, si falla AFIP...), el diagrama se vuelve un monstruo inmanejable y no te alcanzan las 2 horas del parcial.
- **Qué tenés que hacer (Obligatorio):** Antes de trazar la primera línea de vida, **escribí un párrafo de 2 o 3 renglones arriba de la hoja definiendo el ESCENARIO CONCRETO** que vas a modelar, usando los datos del ejemplo o de la pantalla adjunta al parcial.
  - *Ejemplo en Parcial Veterinaria PetCare (explicado por la profesora en Clase 09, `[01:18:20]`):* Como el parcial trae la captura de pantalla del **"Gato Homero"**, tu escenario dice: *"Escenario: Se registra la atención médica de la mascota registrada 'Homero' (Gato, 4 años), con una consulta clínica por control anual, aplicándole 1 vacuna ('Antirrábica') y emitiendo 1 receta por 'Pipeta antipulgas' cada 30 días."*
  - **Ventaja estratégica aprobada por la profesora:** Al fijar en tu escenario que en esta corrida se aplica **1 vacuna y 1 receta** (o que el cliente ya está registrado, según permita la consigna), ¡te ahorrás anidar múltiples fragmentos `loop` o `alt` innecesarios y el diagrama queda limpio, directo y 100% correcto! (Si la consigna dice explícitamente *"aplicar una o más vacunas"*, podés poner un recuadro `loop [para cada vacuna]` alrededor de la creación/agregado de la vacuna, o aclarar en el escenario cuántas se cargan).
- **Evidencia:**
  - `Parciales/1. [Parcial 1][1C2026][4300][Analia][][].pdf`: *"Escribir el escenario que se utiliza para el diagrama de secuencia."*
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 17): Muestra el recuadro amarillo con el escenario exacto antes del Diagrama de Secuencia (*"Un paciente solicita un turno para Hemograma y Hepatograma, para el día 15/05/2025 a las 8hs"*).

### 4.2. Regla N° 2: ¡NO Dibujar al Actor Humano en el Diagrama de Secuencia de Diseño!
- **Criterio estricto de la Profesora:** En el Diagrama de Secuencia de Diseño **NO se dibuja el muñequito (stickman) del Actor** (`:Veterinario`, `:Recepcionista`, `:Cliente`) ni tampoco la pantalla (`:UI`).
- **¿Cómo empieza el Diagrama de Secuencia?** Empieza en el extremo superior izquierdo con un **mensaje entrante anónimo / mensaje encontrado** (`●───────► :C_Modulo`) que llega directamente a la línea de vida del **Controlador (`:C_...`)**.
- **Justificación teórica de la Profesora (pregunta de examen):** Porque gracias al patrón GRASP **Controlador** y a la separación de capas (MVC), al modelo de diseño del backend **no le importa quién disparó el evento** (pudo haber sido una secretaria haciendo clic en una web, un cliente desde una app móvil, un tótem autoservicio o un proceso batch por API). El sistema es agnóstico de la interfaz.
- **Evidencia:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 17 y Pág. 28): *"En el diagrama de secuencia NO ponemos al actor. Empezamos directamente desde el evento que llega al controlador, porque no importa si lo dispara una persona desde una pantalla o un servicio."*
  - `Transcripcion/transcripciones/05_20260917_101702.txt` (`[00:45:10]`) y `09_20261015_082342.txt` (`[01:50:00]`).

### 4.3. Regla N° 3: Creación de Objetos en Tiempo de Ejecución (`create()`)
- Cuando durante la secuencia se instancia un objeto nuevo (por ejemplo, `nuevaConsulta`, `nuevaVacuna`, `nuevaReceta`, `nuevaReserva` — aplicando el patrón GRASP **Creador**), la flecha del mensaje **`create(...)`** (o `<<create>>`) **no va a la línea punteada**, sino que **apunta directamente a la cajita `:NombreClase`** ubicada a la altura vertical del instante en que nace ese objeto. Recién debajo de esa cajita comienza su línea de vida punteada.
- Si además ese objeto recién creado debe guardarse en una colección (por ejemplo, dentro de `:HistoriaClinica` o `:Consulta`), recordá que:
  - O bien lo crea directamente el contenedor (`:HistoriaClinica ── create() ──► :Consulta`) y al crearlo ya lo agrega a su lista interna (`this.consultas.add(c)`).
  - O bien, si lo creó otra clase, debe haber un mensaje posterior `agregarConsulta(c)` para vincularlo. (En GRASP **Creador**, lo ideal es que **el contenedor cree al contenido** para cumplir Creador + Bajo Acoplamiento + Alta Cohesión, tal como enseña el ejemplo de `Venta` creando `LineaDeVenta` en `UNLaM GRASP-original-marin.pdf`, Págs. 30–32).
- **Evidencia:** `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 17) y `Transcripcion/transcripciones/07_20261001_082247.txt` (`[00:12:15]`).

### 4.4. Regla N° 4: Respetar el Alcance Exacto Pedido en el Punto 2
- Leé con lupa qué parte del enunciado te pide secuenciar el Punto 2:
  - En **Parcial PetCare 1C 2026**, el enunciado general habla de Turnos, Atención Médica y Facturación ARCA, pero el Punto 2 dice explícitamente: *"Construir un diagrama de secuencia que represente el proceso de atención médica de una mascota, desde el registro de la consulta hasta la emisión de la receta y registro de vacunas (**No incluir la parte de pago**)"*.
  - En **Parcial Agencia de Viajes 2C 2026**, el Punto 2 dice: *"desde que se registra un nuevo cliente, se crea su solicitud de viaje, se le asigna un agente y se arma su propuesta personalizada"* (no pide secuenciar el cobro ni la post-venta).
- **Moraleja:** En el **Diagrama de Clases (Punto 1)** modelás **TODO** el sistema del enunciado (incluyendo Pagos/Facturación/Seguimiento), pero en el **Diagrama de Secuencia (Punto 2)** solo secuenciás el tramo exacto que pide la consigna.

---

## 5. CRITERIOS PARA LOS DEMÁS DIAGRAMAS UML (CU, ACTIVIDAD, COLABORACIÓN, ESTADO, COMPONENTES, DESPLIEGUE)

Aunque en el Primer Parcial de 2026 el núcleo práctico es **Diagrama de Clases + GRASP + Diagrama de Secuencia + GoF**, en las preguntas teóricas, en los recuperatorios y en los finales aparecen **Diagrama de Estados**, **Componentes**, **Despliegue**, **Colaboración**, **Actividad** y **Casos de Uso**. Aquí están las reglas exactas de la profesora para cada uno:

### 5.1. Casos de Uso y su Especificación (Clase 03 y `EJEMPLO-Practica-Teoria-version-10.pdf` Págs. 2–8)
- **Nombres de Casos de Uso:** Siempre **Verbo en infinitivo + Objeto** (ej. `Solicitar Turno`, `Registrar Atención`, `Pagar Cuota`).
- **`<<include>>` vs `<<extend>>`:**
  - `CU_Base - - - <<include>> - - > CU_Incluido`: El paso incluido es **obligatorio** y siempre se ejecuta como parte del flujo normal (o sirve para reutilizar un subflujo común a varios CU, ej. `Validar Identidad`). La flecha apunta hacia el caso incluido.
  - `CU_Extensor - - - <<extend>> - - > CU_Base`: El comportamiento extensor es **opcional/condicional** (solo ocurre bajo cierta condición o punto de extensión, ej. `Emitir Receta` o `Aplicar Descuento por Obra Social` extiende a `Facturar`). **¡OJO con el sentido de la flecha!** En `<<extend>>`, la flecha punteada **apunta hacia el Caso de Uso Base**.
- **Formato de Especificación preferido por la Profesora (Forma 2 — Tabla de 2 Columnas):**
  - Encabezado con: *Nombre del CU, Actor Primario, Actores Secundarios, Precondiciones, Postcondiciones (de éxito y de fallo)*.
  - **Curso Normal (Camino Feliz):** Tabla dividida en dos columnas: **Acción del Actor** (izquierda) y **Respuesta del Sistema** (derecha), numerando los pasos correlativamente (`1`, `2`, `3`, `4`...).
  - **Cursos Alternativos / Excepciones:** Al pie de la tabla, referenciando el número exacto del paso donde se bifurca (ej. *"3a. El socio no posee apto médico vigente: 3a.1 El sistema informa el rechazo y cancela la inscripción"*).

### 5.2. Diagrama de Actividad (`EJEMPLO-Practica-Teoria-version-10.pdf` Págs. 9–10 y Clase 03/06)
- Representa el flujo de trabajo (workflow) paso a paso, permitiendo mostrar **decisiones** (rombos con condiciones `[si]` / `[no]` mutuamente excluyentes) y **actividades paralelas/concurrentes** mediante **Barras de Sincronización**:
  - **Fork (Bifurcación):** Entra 1 flecha a la barra negra gruesa y salen 2 o más flechas que se ejecutan en paralelo (ej. en Caso Estadios: validar huella y validar iris simultáneamente; en Laboratorio: procesar sangre y procesar orina).
  - **Join (Unión):** Entran las N ramas paralelas a la barra negra gruesa y sale 1 sola flecha recién cuando **todas** las ramas paralelas terminaron.
- Se divide en **Carriles (Swimlanes)** verticales u horizontales por área o responsable.

### 5.3. Diagrama de Colaboración / Comunicación (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 18 y Clase 04)
- **Criterio de la Profesora:** Es **semánticamente isomorfo (equivalente)** al Diagrama de Secuencia (ambos son Diagramas de Interacción de la Vista de Diseño/Procesos).
- **Diferencia clave que siempre pregunta en Teoría:**
  - El **Diagrama de Secuencia** enfatiza el **orden temporal** de los mensajes (de arriba hacia abajo a lo largo de las líneas de vida).
  - El **Diagrama de Colaboración (Comunicación)** enfatiza la **estructura estática de enlaces (links)** entre los objetos que colaboran, indicando el orden temporal mediante **numeración jerárquica anidada** en las etiquetas de los mensajes (`1: msg1()`, `1.1: subMsg()`, `1.2: otroMsg()`, `2: msg2()`).

### 5.4. Diagrama de Estados (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 19, Finales Dic 2025 y Jul 2026)
- **Regla N° 1 (¡El error más grave!):** El Diagrama de Estados **SIEMPRE modela el ciclo de vida de UN ÚNICO OBJETO de una clase específica del dominio** (ej. un objeto `Turno`, un objeto `AnalisisClinico`, un objeto `Reserva`, un objeto `Articulo`, un objeto `Aficionado`). **¡NUNCA es un diagrama de flujo del sistema entero!** (Si mezclás estados del `Cliente`, del `Pago` y del `Envío` en el mismo diagrama, está **MAL**).
- **Regla N° 2 (Nombres de Estados vs. Nombres de Transiciones):**
  - **Dentro de las cajas redondeadas (Estados):** Van **adjetivos o participios** que describen la situación en la que se encuentra el objeto durante un lapso de tiempo: `Pendiente`, `Confirmado`, `En Curso`, `En Espera de Stock`, `Pagado`, `Cancelado`, `Finalizado`. (**PROHIBIDO** poner verbos de acción como *"Pagar"* o *"Validar tarjeta"* adentro de una caja de estado).
  - **Sobre las flechas (Transiciones):** Va la sintaxis oficial `evento [condición de guarda] / acción` (donde `evento` es el **método** que recibe el objeto, `[guarda]` es la condición booleana entre corchetes, y `/ acción` es la respuesta inmediata). Ejemplo: `confirmarPago() [monto == total] / emitirComprobante()`.
- **Regla N° 3 (Relación con el Patrón GoF State):** En Clase 08 y Clase 09 la profesora explica que si en tu sistema un objeto (como `Turno`, `SolicitudViaje`, `Adopcion` o `Reclamo`) tiene múltiples estados y **su comportamiento/validaciones cambian drásticamente según el estado en el que está**, ese Diagrama de Estados es el candidato perfecto para aplicar el patrón GoF **State** en el Diagrama de Clases (creando la interfaz `EstadoTurno` y una clase hija por cada estado del diagrama).

### 5.5. Diagrama de Componentes (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 11–13 y Clase 05/06)
- Muestra la arquitectura modular de alto nivel del software (subsistemas/módulos).
- **Guía de la profesora:** Pensar en 3 grandes bloques funcionales:
  1. **Componentes de Entrada / Captación** (ej. `Gestión de Turnos`, `Empadronamiento`).
  2. **Componentes Core / Procesamiento** (ej. `Atención Clínica`, `Evaluación Crediticia`, `Control de Acceso`).
  3. **Componentes de Salida / Soporte / Integración Externa** (ej. `Facturación / Pagos`, `Notificaciones`, `Integración ARCA/Veraz/Renaper`).
- **Notación:** Usar conectores de **Interfaz Provista (chupetín / círculo completo `──○`)** e **Interfaz Requerida (media luna / enchufe `──(`)** unidos en un conector de ensamblaje (*assembly connector* `──○)──`).
- **Trazabilidad:** Normalmente, **cada Componente principal del Diagrama de Componentes se traduce en 1 `Controller` (`C_...`) en el Diagrama de Clases**.

### 5.6. Diagrama de Despliegue (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 14–15 y Clase 05/06/11)
- Modela la **topología física de hardware (Nodos 3D)**, los entornos de ejecución, los artefactos desplegados adentro y los **protocolos de comunicación reales** en las líneas que unen los nodos.
- **Regla de la Profesora (Clase 05 Bancos y Clase 06 Estadios):**
  1. **Separar claramente los Ambientes/Zonas:** (ej. Ambiente Público/Cliente, Ambiente Sucursal/Estadio Local, Ambiente Sede Central/DataCenter, Ambiente Servicios Externos como VISA/Veraz/ARCA/Renaper).
  2. **Poner siempre los protocolos en los enlaces entre nodos:** `HTTPS`, `TCP/IP`, `REST / JSON`, `SOAP / XML`, `JDBC / ODBC`, `MQTT` (en IoT/STR), `Bluetooth / USB` (para sensores/lectores biométricos).
  3. **En casos con dispositivos físicos / Tiempo Real (Estadios o Domótica):** Incluir los periféricos/sensores/actuadores conectados al nodo controlador o tótem (ej. `Lector de Huella`, `Cámara de Iris`, `Molinete`, `Sensor de Temperatura`).

---

## 6. CÓMO RESPONDER LAS JUSTIFICACIONES DE PATRONES EN EL PARCIAL

### 6.1. Cómo Justificar los Patrones GRASP (Punto 1 del Parcial)
En los parciales 2026 (`1. [Parcial 1]...`, `2. [Parcial 1]...`, `3. [Parcial 1]...`), el Punto 1 pide:
- *"Identificar y justificar al menos 3 patrones GRASP aplicados en el diseño"* (o *"2 patrones GRASP sin contar Controller"* en las comisiones donde Controller ya viene dado en la consigna).
- **Regla de Oro de la Profesora:** **¡NUNCA des una definición teórica genérica de libro!** Si escribís *"Apliqué Experto porque asigna la responsabilidad a la clase que tiene la información"*, te pone **0 puntos o Incompleto**.
- **Fórmula obligatoria para justificar cada GRASP en el examen:**
  > **[Nombre del Patrón GRASP]** → **¿En qué clase concreta de TU diagrama lo aplicaste?** + **¿En qué método concreto?** + **¿Por qué esa clase (y no otra) tiene los atributos/referencias o el rol para hacerlo?**
  - *Ejemplo 10 puntos (Experto en Información):* *"Se aplica **Experto en Información** en la clase `HistoriaClinica` con el método `+verificarVacunasVigentes()`, ya que `HistoriaClinica` es la clase que posee la colección de objetos `VacunaAplicada` de la `Mascota`, por lo cual delega en cada `VacunaAplicada` el mensaje `+estaVencida(fechaActual)` que conoce su propio atributo `fechaVencimiento`."*
  - *Ejemplo 10 puntos (Creador):* *"Se aplica **Creador** en la clase `HistoriaClinica` (o `Consulta`) mediante el método `+registrarConsulta(...)` (o `+agregarVacuna(...)`), ya que `HistoriaClinica` contiene y agrega de forma exclusiva (composición) a las instancias de `Consulta`, registrándolas en su colección interna."*
  - *Ejemplo 10 puntos (Bajo Acoplamiento y Alta Cohesión / Polimorfismo / Fabricación Pura):* *"Se aplica **Alta Cohesión y Bajo Acoplamiento** al delegar la responsabilidad del cálculo y registro clínico en `HistoriaClinica` y `Consulta` en lugar de sobrecargar al controlador `C_AtencionMedica` o a la clase `Veterinario`, manteniendo cada clase enfocada únicamente en las responsabilidades propias de su abstracción."*

### 6.2. Cómo Elegir, Dibujar y Justificar los 2 Patrones GoF (Punto 3 del Parcial)
En los parciales 2026, el Punto 3 vale una parte decisiva de la nota y pide:
> *"Aplicar dos patrones GOF (de diferente categoría) al problema planteado sobre el diagrama de clases del punto 1:*
> *a) Indicar categoría y nombre del patrón.*
> *b) Explicar qué problema de diseño resuelve dentro del caso.*
> *c) Justificar por qué ese patrón es adecuado.*
> *d) Indicar qué clases del modelo del punto 1 se reutilizan y qué clases/interfaces nuevas se incorporan al diagrama."*
> *(Nota en Parciales 2 y 3 de 2026: **"no usar singleton, ni facade"**).*

- **Criterios de corrección de la Profesora (Clase 08 y Clase 09 `[02:15:00]` a `[03:30:00]`):**
  1. **Tienen que ser de DISTINTA CATEGORÍA:** Es decir, elegís 1 **Comportamiento** + 1 **Estructural**, o 1 **Comportamiento** + 1 **Creacional**, o 1 **Estructural** + 1 **Creacional**.
  2. **No uses `Singleton` ni `Facade`:** Incluso si en tu tema no dice explícitamente "no usar singleton ni facade", en la Clase 09 la profesora aclaró que muchos alumnos metían un Singleton en el Controller sin justificación real de negocio, por lo que empezaron a prohibirlos en las consignas.
  3. **El patrón GoF DEBE verse dibujado en el Diagrama de Clases con toda su estructura UML completa:**
     - Si aplicás **Strategy** (Comportamiento): Tiene que verse la clase Contexto (ej. `Factura`, `Prestamo`, `PropuestaViaje`), la interfaz `<<interface>> IEstrategia...` con el método abstracto (ej. `+calcularPrecio()`), y al menos **2 o 3 clases concretas** (`EstrategiaEfectivo`, `EstrategiaObraSocial`, `EstrategiaParticular`) que realizan (`- - -▷`) la interfaz.
     - Si aplicás **State** (Comportamiento): Tiene que verse el Contexto (ej. `SolicitudViaje`, `Adopcion`, `Turno`) con el atributo `-estadoActual: IEstado...`, la interfaz `<<interface>> IEstado...` con los métodos de transición (`+confirmar()`, `+cancelar()`, etc.) y las **clases concretas de estado** (`EstadoPendiente`, `EstadoAprobado`, `EstadoRechazado`).
     - Si aplicás **Observer** (Comportamiento): Tiene que verse el Sujeto observado (ej. `HistoriaClinica` / `Vacuna` / `Turno` / `Alerta`) con su lista `-observadores: List<IObservador>` y métodos `+suscribir(o)`, `+desuscribir(o)`, `+notificar()`, la interfaz `<<interface>> IObservador` con `+actualizar(...)`, y los observadores concretos (`NotificadorEmail`, `NotificadorWhatsApp`, `NotificadorApp`).
     - Si aplicás **Adapter** (Estructural): Ideal siempre que el enunciado mencione **conectarse a un sistema externo** (`ARCA / AFIP`, `Veraz`, `VISA`, `Renaper`, `Aerolíneas / Hoteles externos`). Tiene que verse la interfaz esperada por tu dominio (`<<interface>> IServicioFacturacion` o `IProveedorVuelo`), la clase `AdaptadorARCA` que implementa esa interfaz y envuelve (asociación) a la clase externa `ServicioWebARCA_API` traduciendo el llamado.
     - Si aplicás **Decorator** (Estructural) o **Composite** (Estructural): Ideal para paquetes de viaje con excursiones/seguros opcionales o combos de servicios veterinarios/estudios clínicos.
     - Si aplicás **Builder** o **Factory Method** (Creacional): `Builder` es perfecto para construir paso a paso un objeto complejo con partes opcionales (`PropuestaViaje` con vuelos + hotel + excursiones + seguro, o `ContratoAdopcion`); `Factory Method` es perfecto para instanciar distintos tipos de documentos, contratos, alertas o estudios según el tipo.

---

## 7. CHECKLIST RÁPIDO DE CONTROL ANTES DE ENTREGAR EL PARCIAL (LOS 12 MANDAMIENTOS DE ANALÍA)

Antes de entregar las hojas en el examen, verificá estos 12 puntos uno por uno:

- [ ] **1. ¿Entregué un diagrama por hoja y numeré todas las hojas?**
- [ ] **2. ¿Puse como máximo 3 (o 4) `Controllers` (`C_...`) en la parte superior del Diagrama de Clases?**
- [ ] **3. ¿Me aseguré de que ningún Actor humano (`Recepcionista`, `Veterinario`, `Secretaria`) esté actuando como un Gestor lleno de métodos del sistema?**
- [ ] **4. ¿Eliminé todos los métodos `get/set` triviales y los `alta/baja/modificación` genéricos, dejando métodos con nombres de reglas de negocio?**
- [ ] **5. ¿Separé correctamente la "Ficha individual" (`Consulta`, `Mascota`, `Aficionado`) de la clase que maneja "la Colección / Fichero" (`HistoriaClinica`, `Padron`, `Agenda`)?**
- [ ] **6. ¿Puse visibilidades (`-` en atributos, `+` en métodos) y multiplicidades (`1`, `0..*`, `1..*`) en todas las asociaciones sólidas del Diagrama de Clases?**
- [ ] **7. ¿Escribí el estereotipo `<<interface>>` o `<<abstract>>` arriba del nombre de todas las interfaces y clases abstractas?**
- [ ] **8. ¿Escribí arriba del Diagrama de Secuencia el ESCENARIO CONCRETO con datos puntuales del caso?**
- [ ] **9. ¿Inicié el Diagrama de Secuencia SIN Actor humano, con un mensaje entrante directamente hacia el `:C_Controller`?**
- [ ] **10. ¿Verifiqué uno por uno que TODOS los mensajes que llegan a un objeto `:X` en el Diagrama de Secuencia están escritos como métodos `+metodo()` dentro de la clase `X` en el Diagrama de Clases?**
- [ ] **11. ¿Justifiqué los patrones GRASP nombrando las clases y métodos exactos de MI diagrama en lugar de recitar teoría genérica?**
- [ ] **12. ¿Elegí 2 patrones GoF de DISTINTA categoría (sin usar Singleton ni Facade), los dibujé completos en el Diagrama de Clases y respondí los 4 incisos (`a`, `b`, `c`, `d`)?**
