# 01 — CRITERIOS, CONVENCIONES Y CONSEJOS DE LA PROFESORA (ING. ANALÍA MARÍN)

> **Propósito de este documento:** Este archivo concentra **las reglas exactas con las que la Prof. Ing. Analía Marín (y el JTP Alejandro) corrigen los parciales y finales**.  
> En Diseño de Sistemas, muchos alumnos desaprueban no por no saber qué es una clase o un patrón, sino por **violar reglas de diseño, trazabilidad o convención** que la profesora repite en clase y deja por escrito en sus guías.  
> **Cada criterio aquí expuesto está respaldado por su cita exacta** al archivo oficial de la cátedra, número de página o minuto de la transcripción de clase.

---

## 1. FILOSOFÍA GENERAL DE CORRECCIÓN: "¿QUÉ BUSCA ANALÍA MARÍN EN EL PARCIAL?"

### 1.1. Nivel de Baja Abstracción: "Estamos en Diseño, NO en Análisis" `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Criterio de la Profesora:** En Análisis de Sistemas alcanzaba con dibujar cajas con sustantivos (Modelo Conceptual del Dominio). En **Diseño de Sistemas**, el modelo debe tener **baja abstracción** y estar **cerca del código fuente**. Esto exige:
  1. Clases del dominio con **atributos concretos** y **métodos de negocio reales**.
  2. **Visibilidad** explícita (`-` privado, `+` público, `#` protegido).
  3. **Clases de Diseño (Fabricación Pura / Soporte):** Controladores (`C_...`), Nóminas/Catálogos/Padrón (si hace falta manejar colecciones globales), Interfaces (`<<interface>>`), Clases Abstractas (`<<abstract>>`), Clases pasarela hacia sistemas externos (ej. `sisExtOS`) y las clases que implementan **Patrones GoF**.
  4. **Parámetros en los métodos clave:** Especialmente en el Diagrama de Secuencia y en los métodos que reciben referencias a objetos o IDs desde la interfaz.
- **Evidencia:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 10 y Pág. 20): *"El diagrama de clases muestra las clases del sistema, sus atributos, métodos y las relaciones entre ellas. Es la base del diseño orientado a objetos y sirve de puente entre los requerimientos y el código"*.
  - `Transcripcion/transcripciones/09_20261015_082342.txt` (`[00:13:02]` y `[01:15:36]`): *"Acá estamos en diseño, nos tenemos que acercar al código... No nos podemos quedar en un modelo conceptual"*.

### 1.2. Prohibición Absoluta de "ABMs / CRUDs Triviales" y Getters/Setters Masivos `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Criterio de la Profesora:** Está terminantemente prohibido llenar las clases de métodos `alta()`, `baja()`, `modificacion()`, `getNombre()`, `setNombre()`, o poner un `Controller` por cada clase para hacer un ABM. **En el parcial se modela el CORE (corazón) del negocio.**
- **Frases textuales de clase y guías:**
  - `Clases/Clases/04/Gym/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx` (Pág. 2): *"Evitar pensar que cada clase tiene un controller para hacer un ABM (alta-baja-modificación). Eso en los parciales NO VA. Siempre vamos al CORE del negocio."*
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 27): *"Si cada clase tiene un controlador para el alta, baja o modificación del objeto, ¿para qué están las relaciones de las clases?... Evitar los get y set, eso ya es por defecto por el paradigma."*
- **Qué hacer en su lugar:** Si la clase necesita inicializarse, usar su constructor (`crear(...)` / `new` / `create()`) y métodos con **nombre de regla de negocio** (ej.: `validarVigencia()`, `registrarVacuna(v)`, `calcularMontoTotal()`, `verificarCupo()`, `confirmarReserva()`). Solo incluir un `get` puntual si en el Diagrama de Secuencia necesitás pedir un dato específico a otro objeto para un cálculo (Experto en Información).

### 1.3. Reglas Formales de Entrega en Hoja (Formato de Examen Presencial) `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Criterio obligatorio en todos los parciales 2026:**
  1. **"ENTREGAR UN DIAGRAMA POR HOJA, ENUMERAR LAS HOJAS A ENTREGAR."** (Aparece en mayúsculas y subrayado al final de `1. [Parcial 1][1C2026][4300][Analia][][].pdf`, `2. -Parcial 1--1C2026--1900--Valeria y Analia-----.pdf` y `3. [Parcial 1][2C2026][1900][][][].pdf`).
  2. **Hoja 1:** Diagrama de Clases completo (con las clases del dominio, los Controllers, la integración del Diagrama de Estados si el examen lo provee y los 2 patrones GoF integrados — marcando claramente qué clases pertenecen a cada patrón GoF) + Justificación de GRASP.
  3. **Hoja 2:** Escenario redactado arriba + Diagrama de Secuencia completo (y en una hoja separada el Diagrama de Componentes modificado/mejorado si el parcial lo solicita, como en los Parciales 2 y 3 de 2026).
  4. **Hoja de Patrones GoF:** Explicación y justificación detallada de los 2 Patrones GoF (Categoría, Nombre, Problema del caso, Por qué es adecuado, Clases reutilizadas y Clases/Interfaces nuevas incorporadas).

### 1.4. Técnica de Análisis de Enunciado con Código de Colores de la Profesora `[RECOMENDACIÓN PRÁCTICA DE LA PROFESORA]`
- En `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 5–6 y Pág. 8) y en la Clase 03 (`03_20260903_101348.txt`), la profesora enseña a subrayar el texto del enunciado y la especificación de Casos de Uso con **tres colores**:
  - **Amarillo:** Sustantivos principales que representan **Clases candidatas del dominio** (ej.: `Paciente`, `Turno`, `OrdenMedica`, `Estudio`, `Muestra`, `Factura`).
  - **Verde:** Verbos y frases verbales que representan **Funcionalidades / Comportamiento / Métodos** (ej.: `solicitar turno`, `registrar orden`, `validar cobertura`, `calcular importe`).
  - **Celeste (Azul claro):** **Atributos** de las clases o **clases secundarias/de soporte** (ej.: `DNI`, `fecha`, `hora`, `obra social`, `código de barra`).
- Además, en el **Diagrama de Clases** (`EJEMPLO-Practica-Teoria-version-10.pdf`, Pág. 10), la profesora pinta de **color verde** la clase pasarela hacia sistemas externos (`sisExtOS`) para distinguirla visualmente de las clases propias del dominio (amarillas).

---

## 2. EL ERROR ELIMINATORIO N° 1: TRAZABILIDAD E INTEGRACIÓN ENTRE DIAGRAMAS `[REGLA EXPLÍCITA DE CÁTEDRA]`

La profesora repite en **todas** las clases prácticas que los diagramas de UML no son dibujos sueltos, sino **distintas vistas del MISMO sistema** (Modelo 4+1 de Kruchten). Por lo tanto, tienen que ser **100% consistentes entre sí**.

### 2.1. Regla de Oro de Correspondencia de Mensajes y Métodos
> **REGLA ELIMINATORIA:** Si en el **Diagrama de Secuencia** (o de Colaboración) el objeto `A` le envía el mensaje `m()` al objeto `B` (`A ─── m() ──► :B`), entonces:
> 1. **El método `+m()` DEBE estar escrito en el compartimento de métodos de la clase `B` en el Diagrama de Clases.** (¡No en `A`! El método pertenece a la clase que **recibe** el mensaje y ejecuta la acción).
> 2. **La clase `A` DEBE tener visibilidad hacia la clase `B` en el Diagrama de Clases** (una línea de asociación si es visibilidad permanente de atributo, o relación/dependencia si entra por parámetro; ver Regla 3.6 para el caso de la visibilidad local).
> 3. Si el parcial provee o pide un **Diagrama de Estados** para un objeto `B` (como `Consulta Veterinaria` en el Parcial 1C 2026 Com. 4300 o `Reserva` en el Parcial 2C 2026 Com. 1900), **todas las transiciones/eventos de ese Diagrama de Estados (`registrarConsulta()`, `registrarDiagnostico()`, `cerrarConsulta()`, `cancelar()`, etc.) DEBEN figurar como métodos de la clase `B` en el Diagrama de Clases**, y la clase `B` debe tener su atributo `-estado` (o el patrón GoF `State` asociado).

- **Evidencia documental directa:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 16 y Pág. 20): *"NOTA: Todos los mensajes que están presentes en el diagrama de secuencia, colaboración y estado deben estar en el diagrama de clases. Las vistas deben ser consistentes."*
  - `Clases/Clases/04/Gym/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx` (Pág. 3): *"Cada mensaje que llega a un objeto es un método en esa clase. Verificar que en el diag de clases se encuentren esos métodos. Si hay mensajes en el diag. de interacción que no están en el diag de CLASES, el ejercicio está MAL."*
  - `Transcripcion/transcripciones/09_20261015_082342.txt` (`[01:55:12]`): *"Chicos, cuando corregimos ponemos el Diagrama de Secuencia al lado del Diagrama de Clases. Si en secuencia llaman a `validarVacuna()` en `HistoriaClinica`, vamos a buscar `validarVacuna()` en la clase `HistoriaClinica`. Si no está, está mal."*

---

## 3. CRITERIOS ESPECÍFICOS PARA EL DIAGRAMA DE CLASES

### 3.1. Organización Visual del Diagrama de Clases ("Arriba hacia Abajo, Izquierda a Derecha") `[RECOMENDACIÓN PRÁCTICA DE LA PROFESORA]`
La profesora pide que el Diagrama de Clases esté ordenado visualmente por capas para que sea legible al corregir:
1. **Parte Superior (Arriba de todo):** Los **Controladores (`C_...`)**.
2. **Parte Media-Alta (Debajo de los Controllers):** Los **Gestores / Nóminas / Padrón** (únicamente si son necesarios; ver regla 3.3 y 3.5).
3. **Parte Central e Inferior:** Las **Clases del Modelo de Dominio** y las **jerarquías de herencia / patrones GoF**, agrupadas verticalmente en columnas según el módulo o componente al que pertenecen.
4. **¿Qué NO va en el Diagrama de Clases?** No va la capa de Base de Datos (tablas SQL, `DAO`, `Repository` genéricos) ni las pantallas HTML/Vistas, salvo que se aplique un patrón específico que requiera una interfaz de vista.
- **Evidencia:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 10 y Pág. 28): *"Leer el diagrama de arriba hacia abajo, de izquierda a derecha... Arriba van los controladores, debajo las clases del dominio agrupadas por cercanía funcional."*
  - `Clases/Clases/04/Gym/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx` (Pág. 1): *"Organizar visualmente el diagrama: arriba los controllers, luego las clases principales, y hacia abajo las clases de detalle o soporte."*

### 3.2. Cuántos Controladores (`Controller` GRASP) poner y cómo nombrarlos `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Nomenclatura:** La profesora utiliza el prefijo `C_` o `c_` seguido del nombre del módulo/componente o caso de uso agrupado:
  - Ejemplo Laboratorio (`EJEMPLO-Practica-Teoria-version-10.pdf`, Pág. 10): `C_turno`, `C_Recepcion`, `C_Analitica`, `C_Pago`, `C_Validacion`.
  - Ejemplo Banco (`Clases/05/Banco/Banco-diagClase.png`): `C_EvaluacionP`, `C_prestamo`, `C_Cliente`.
  - Ejemplo Estadios (`Clases/06/Estadio/Clase2.png`): `c_empadronar`, `c_ingreso`.
  - Ejemplo Gimnasio (`EJEMPLO-Practica-Teoria-version-10.pdf`, Pág. 28): `C_Inscripcion`.
- **Cantidad exacta en el Parcial:**
  - En la práctica real no se pone 1 Controller para todo el sistema (porque queda **saturado** y viola la Alta Cohesión) ni tampoco 1 Controller por cada Caso de Uso individual si hay 15 casos de uso (por falta de tiempo en el examen).
  - **Criterio de cátedra:** Definir **1 Controller por cada Módulo / Componente funcional principal** del sistema.
  - **Límite explícito en los parciales 2026 (Máximo 4 Controladores):**
    - En `1. [Parcial 1][1C2026][4300][Analia][][].pdf` (Veterinaria PetCare): figura en nota manuscrita superior **`max: 4 controladores`** (y en la discusión oral de Clase 09 `[02:01:15]` se trabajaron 3 o 4 controladores según cómo se agrupen `C_UsuarioMascota`, `C_Turno`, `C_AtencionVeterinaria` / `C_HistoriaClinica`).
    - En `2. -Parcial 1--1C2026--1900--Valeria y Analia-----.pdf` (Reencuentro/Adopción y Animales Exóticos) y `3. [Parcial 1][2C2026][1900][][][].pdf` (Agencia de Viajes): la consigna impresa exige textualmente **"usando solo 4 controladores"**.
- **Qué tiene adentro un Controller (y qué atributos SÍ puede tener):**
  - **NO tiene atributos de datos propios del dominio** (no guarda el `nombreCliente` ni el `saldo`).
  - **SÍ puede tener atributos de referencia de coordinación y estado temporal de sesión o del caso de uso en curso:** Tal como explica explícitamente la profesora en `EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 31), un Controller puede mantener referencias a servicios/nóminas que coordina y referencias al estado temporal de la sesión activa (por ejemplo: `-pacienteActual: Paciente`, `-prestamoActual: Prestamo`, `-estadoValidacion: Boolean`), aunque en los diagramas de clases de pizarrón muchas veces se deje el compartimento de atributos vacío para simplificar.
  - **Sus métodos son los manejadores de los eventos de entrada del sistema** (ej. `+guardarConsulta(...)`, `+registrarDenunciaExotico(...)`, `+realizarPago(...)`).
  - **Su responsabilidad es coordinar ("director de orquesta"):** Recibe datos primitivos/IDs de la UI, busca las referencias a los objetos correspondientes y **delega** el trabajo real a las clases del dominio (Experto).
- **Evidencia:**
  - `Clases/Clases/04-Presencial/UNLaM GRASP-original-marin.pdf` (Pág. 62): *"Aclaración: En el examen, debido a limitaciones de tiempo, no vamos a poder implementar un controlador por cada Caso de Uso (CU). En su lugar, el diseño debe contemplar un controlador por módulo o subsistema."*
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 10, Pág. 28 y Pág. 31): *"El controlador captura el evento y delega a quien corresponda. Tiene lógica mínima... Puede tener referencias a las clases con las que coordina y estado temporal de la sesión."*

### 3.3. Diferencia entre `Controller` y `Gestor` (¡Cuidado con el "Gestor Pasapelotas"!) `[REGLA EXPLÍCITA DE CÁTEDRA]`
En la Clase 07 y en las páginas 29–31 de `EJEMPLO-Practica-Teoria-version-10.pdf`, un alumno preguntó cuándo usar un `Gestor` debajo del `Controller`. La respuesta de la profesora es taxativa:
- **El Error del "Pasapelotas":** Si ponés un `C_Inscripcion` con el método `inscribirSocio()` y abajo ponés un `GestorInscripcion` con el mismo método `inscribirSocio()` que hace exactamente lo mismo, **está MAL** (es redundante y agrega acoplamiento inútil).
- **Cuándo SÍ tiene sentido un Gestor o Nómina/Padrón:**
  1. Cuando el `Controller` se vuelve **saturado** porque además de recibir eventos de UI hay que orquestar reglas de negocio complejas entre múltiples subsistemas.
  2. Cuando necesitás una **clase contenedora de colección global (Fabricación Pura / Multiobjeto)** como `Padron` (en Caso Estadios) o `NominaPacientes` / `NominaMascotas` para buscar objetos en memoria (`buscarAficionado(dni)`, `buscarMascota(id)`) sin ensuciar la clase individual `Aficionado` o `Mascota`.
- **Evidencia:** `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 29–31) y `Transcripcion/transcripciones/07_20261001_082247.txt` (`[00:18:40]`).

### 3.4. Diferencia Estricta entre "Actor del Sistema" y "Clase del Dominio" (El Error del `Recepcionista` / `Veterinario`) `[REGLA EXPLÍCITA DE CÁTEDRA]`
Este es uno de los errores más corregidos en la Clase 09 (`09_20261015_082342.txt`):
- **El Error Frecuente:** El enunciado dice *"El veterinario registra los datos de la mascota, aplica vacunas y emite la receta"* o *"La recepcionista da de alta el turno"*. Muchos alumnos crean la clase `Veterinario` o `Recepcionista` y le ponen los métodos `+registrarMascota()`, `+aplicarVacuna()`, `+emitirReceta()`, o hacen que el `Controller` llame a `veterinario.atender()`.
- **Por qué está MAL según la Profesora:**
  1. La persona humana que tipea en la pantalla es el **Actor** que dispara el evento hacia el `Controller`. **No es un objeto de software ejecutando lógica de negocio.**
  2. Si le ponés todos los métodos del sistema a la clase `Veterinario`, convertís a `Veterinario` en una **clase Dios / Gestor encubierto** (violando **Experto en Información** y **Alta Cohesión**). Quien conoce las consultas y vacunas de una mascota es la `HistoriaClinica` (o `Mascota` / `Consulta`), ¡no el `Veterinario`!
  3. **¿Cuándo SÍ va la clase `Profesional` / `Veterinario` / `Medico` en el Diagrama de Clases?** Únicamente como **entidad de datos del dominio** cuando el negocio requiere guardar **quién** atendió la consulta o turno (ej. en el Parcial 1C 2026 *PetCare*, `Profesional` guarda sus datos y su horario en la `Veterinaria`, y se asocia al `Turno` y a la `Consulta`), o cuando hay que consultar su agenda.
  4. **¿Y si el enunciado habla de permisos de usuarios (Recepcionista, Admin, Bioquímico)?** No se crean subclases de usuario con métodos de negocio, sino el modelo extensible **`Usuario` → `Perfil` (o `Rol`) → `Permiso`** (como muestra la profesora en `EJEMPLO-Practica-Teoria-version-10.pdf`, Pág. 24).
- **Evidencia:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 20 y Pág. 24): *"Recepcionista y Bioquímico son actores, son roles que operan el sistema, NO son clases que lanzan métodos. Si se requiere modelar quién hizo qué o sus permisos, se modela Usuario con Perfil y Permiso para favorecer la Extensibilidad."*
  - `Transcripcion/transcripciones/09_20261015_082342.txt` (`[01:28:15]` y `[01:42:50]`): *"El veterinario es el actor que está sentado frente a la pantalla cargando la consulta del gato Homero. La clase Profesional/Veterinario solo guarda su matrícula y nombre asociada a la Consulta o Receta, ¡el Veterinario no es el que guarda la vacuna en la base ni valida la fecha, eso lo hace Consulta o HistoriaClinica!"*

### 3.5. El Problema de la "Ficha Única" vs. "El Fichero (Colección / Multiobjeto)" y Relación de la `Nomina` `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Criterio de la Profesora:** Una clase como `Socio`, `Aficionado`, `Mascota` o `Consulta` representa **UN único individuo o una única ficha atómica** (una instancia).
  - **Pregunta de control de la profesora:** Si tenés la clase `Consulta` (que representa *una* visita médica del día de hoy), ¿puede esa instancia `Consulta` tener el método `buscarConsultasAnteriores()`? **¡NO! Porque una instancia de `Consulta` solo se conoce a sí misma.**
  - **Distinción clave entre Colección Propia de un Objeto vs. Búsqueda Global (`Nomina` / `Multiobjeto`):**
    1. **Colección propia de una entidad del dominio:** Todas las consultas de una mascota pertenecen a su **`HistoriaClinica`** (1 a 1 con `Mascota`), y todos los ítems de una venta pertenecen a **`Venta`**. Por lo tanto, para agregar o consultar el historial de *esa* mascota **NO hace falta crear una clase `NominaConsultas`**, sino que la propia clase contenedora del dominio (`HistoriaClinica`) maneja su colección `consultas: List<Consulta>` con métodos como `+agregarConsulta(c)` o `+obtenerHistorial()`.
    2. **Búsqueda global entre todas las instancias del sistema (`Nomina` / `Padron` / Multiobjeto):** Cuando el `Controller` recibe un `dni` o `id` desde la interfaz y necesita encontrar a qué objeto `Aficionado`, `Usuario` o `Paciente` corresponde entre todos los registrados en el sistema, una instancia individual no puede buscar a las demás. Allí sí se utiliza una clase contenedora global (**`Padron`**, **`NominaUsuarios`**, **`NominaMascotas`** o un **Multiobjeto** `:Mascota` en Secuencia) con el método `+buscarPorId(id)`.
  - **¿Con qué relación se une la `Nomina` a la clase individual en el Diagrama de Clases? (`[02:38:03]` de Clase 09):**
    - Se une con **Asociación simple (`───`, de `1` a `0..*`)**, **NO con Composición fuerte (`◆`)**, porque la `Nomina` es solo un índice/colección en memoria (Fabricación Pura) y si se destruye el listado o filtro no deben destruirse las entidades del negocio.
- **Evidencia:**
  - `Transcripcion/transcripciones/06_20260924_114136.txt` (`[00:05:10]` a `[00:16:30]`).
  - `Transcripcion/transcripciones/09_20261015_082342.txt` (`[00:35:20]`, `[01:36:40]` y `[02:38:03]`): *"Una clase representa una ficha. Para buscar en el fichero necesitás a quien contiene la colección: la Historia Clínica para las consultas de esa mascota, o el Padrón/Nómina para buscar en general... Y entre Nómina y la clase va asociación normal, no composición."*

### 3.6. Visibilidad (Larman Cap. 18) y la Tabla Oficial de la Profesora sobre qué se dibuja en el Diagrama de Clases `[REGLA EXPLÍCITA DE CÁTEDRA]`
En la Clase 07 (`07_20261001_082247.txt`) y en las páginas 19, 32 y 33 de `EJEMPLO-Practica-Teoria-version-10.pdf`, la profesora incluye un cuadro comparativo explícito de los **4 tipos de visibilidad de Craig Larman** y define cuáles se grafican en el Diagrama de Clases:

| Tipo de Visibilidad (Larman) | ¿Cómo se logra en código? | ¿Duración de la relación? | ¿Aparece graficada en el Diagrama de Clases según Analía Marín (`EJEMPLO-Practica...` Pág. 19)? |
| :--- | :--- | :--- | :--- |
| **1. Visibilidad de Atributo** | `B` es un atributo declarado dentro de la clase `A` (`private B miB;`). | **Permanente** (perdura mientras exista `A`). | **SÍ, SIEMPRE.** Se dibuja como una **línea sólida de Asociación** (o Agregación/Composición) entre `A` y `B` con su multiplicidad. |
| **2. Visibilidad de Parámetro** | `B` se pasa como parámetro en un método de `A` (`metodo(B unB)`). | **Temporal** (dura lo que dura la ejecución del método). | **SÍ (si se detallan firmas o dependencias).** Se ve en la firma del método `+metodo(b: B)` y puede representarse con una **flecha punteada de Dependencia (`- - - >`)**. Se transforma en Visibilidad de Atributo si `A` guarda ese parámetro en un atributo propio (`this.b = unB`). |
| **3. Visibilidad Local** | `A` declara una variable local de tipo `B` adentro de un método (`B temp = ...`). | **Temporal** (muere al terminar el método). | **NO APARECE en el Diagrama de Clases** (*Cuadro oficial Pág. 19: "¿Aparece en el Diagrama de Clases?: No"*). Solo se observa dinámicamente en el **Diagrama de Secuencia** cuando el método crea o pide localmente esa instancia. |
| **4. Visibilidad Global** | `B` es accesible globalmente por cualquier objeto (ej. variable global o `Singleton.getInstance()`). | Permanente/Global. | Solo si se modela el patrón `Singleton` (que además suele estar restringido en los parciales 2026). |

- **Advertencia clave de la Profesora sobre las líneas del `Controller` (`EJEMPLO-Practica...` Págs. 32–33):** *"En el diagrama de clases se grafican las relaciones permanentes (visibilidad de atributo) y las más significativas. NO tiren líneas de asociación sólidas desde el Controller hacia las 20 clases del diagrama porque queda una telaraña ilegible y conceptualmente incorrecta (el Controller no es dueño permanente de todo el dominio)"*. El Controller solo se relaciona con las 2 o 3 clases raíz/nóminas a las que delega la coordinación.
- **Evidencia:** `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 19 y Págs. 32–33).

### 3.7. Pasaje de Parámetros desde la UI: "IDs Primitivos afuera, Referencias a Objetos adentro" `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Criterio de la Profesora:** Cuando el evento entra desde la pantalla HTML al `Controller`, la pantalla envía **datos primitivos o IDs** (ej.: `idMascota`, `dniCliente`, `codigoVacuna`, `peso`, `observaciones`).
  1. El **`Controller`** recibe esos datos primitivos: `+guardarConsulta(idMascota, peso, diag, receta, vacuna, recordatorio)`.
  2. El primer paso dentro del sistema es **obtener la referencia al objeto** buscando por ese ID (ej.: pidiéndole a la nómina/contenedor `mascota = buscarMascota(idMascota)`).
  3. Una vez obtenida la referencia `mascota`, entre los objetos del dominio se pasan **referencias a objetos** (ej.: `historiaClinica.agregarConsulta(nuevaConsulta)` pasa el objeto `nuevaConsulta`, no un `idConsulta`).
- **Evidencia:** `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 28): *"De la interfaz vienen los IDs; el controlador busca el objeto para obtener su referencia y a partir de ahí trabaja con referencias a objetos."*

### 3.8. Uso Correcto de Agregación (Rombo Blanco) vs. Composición (Rombo Negro) vs. Asociación Simple `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Asociación simple (`───`):** Relación estructural normal entre dos clases independientes (ej. `Consulta` con `Profesional`, `Turno` con `Mascota`, `Nomina` con `Mascota`). **Ante la duda, usar asociación simple con multiplicidad correcta.**
- **Agregación (`◇───` rombo blanco del lado del Todo):** Relación "Todo-Parte" débil donde las partes pueden existir independientemente del Todo y compartirse (ej.: `Equipo` y `Jugador`, `PaqueteTuristico` y `Excursion`).
- **Composición (`◆───` rombo negro relleno del lado del Todo):** Relación "Todo-Parte" **fuerte y de pertenencia exclusiva**. Si se destruye el Todo, carece de sentido o se destruyen sus Partes, y una instancia de la Parte pertenece a un único Todo (ej.: `Factura` ◆── `ItemFactura`, `Prestamo` ◆── `Cuota`, `Mascota` ◆── `HistoriaClinica`, `Aficionado` ◆── `Huella`).
- **Evidencia:** `Transcripcion/transcripciones/03_20260903_101348.txt` (`[00:41:15]`) y `Clases/Clases/05/Banco/Banco-diagClase.png`.

### 3.9. Clases Abstractas (`<<abstract>>`) vs. Interfaces (`<<interface>>`) `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Clase Abstracta (`<<abstract>>` o nombre en cursiva):**
  - Se usa cuando existe una **relación de identidad "ES UN" (herencia)** entre las subclases y **comparten atributos comunes** y/o **métodos ya implementados**, además de declarar métodos abstractos que cada hija sobrescribe (polimorfismo).
  - *Ejemplo de la Profesora (`Banco/Banco-diagClase.png` y `EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 23):* La clase `Producto` (`<<abstract>>`) tiene `nroProducto`, `fechaAlta` y es padre de `Prestamo` y `Cuenta`. La clase `Pago` (`<<abstract>>`) tiene `monto`, `fecha` y el método polimórfico `+procesarPago()`, siendo padre de `Efectivo`, `Tarjeta` y `Transferencia`.
- **Interfaz (`<<interface>>`):**
  - Es un **contrato puro de comportamiento**: **NO tiene atributos de estado** ni código implementado (en el modelo clásico OO que evalúa la cátedra), solo firmas de métodos públicos abstractos (`+calcular()`, `+notificar()`, `+conectar()`).
  - La relación desde la clase que la implementa hacia la interfaz es de **Realización** (flecha triangular cerrada con **línea punteada** `- - -▷`).
  - Es fundamental en los **Patrones GoF** (`Strategy`, `Observer`, `State`, `Adapter`, `Command`, `Decorator`, `Factory Method`).
- **Regla de notación de la profesora en hoja (`[RECOMENDACIÓN PRÁCTICA DE LA PROFESORA]`):** Como escribiendo a mano no se nota la letra *cursiva*, **escribir SIEMPRE el estereotipo `<<abstract>>` o `<<interface>>` arriba del nombre de la clase** y también al lado de los métodos abstractos si querés máxima claridad.
- **Evidencia:** `Transcripcion/transcripciones/03_20260903_101348.txt` (`[00:25:10]` a `[00:39:00]`) y `Clases/Clases/04/Gym/GUIA-EjercicioGYM-Estudiantes-2026- V01.docx`.

---

## 4. CRITERIOS ESPECÍFICOS PARA EL DIAGRAMA DE SECUENCIA (PUNTO 2 DEL PARCIAL)

El Punto 2 de los parciales de Analía Marín pide construir un **Diagrama de Secuencia** para un flujo específico del enunciado. Sus reglas son súper precisas:

### 4.1. Regla N° 1: Escribir Arriba el "Escenario Concreto" con Datos Puntuales `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Por qué lo exige la profesora:** Si intentás dibujar en un solo Diagrama de Secuencia todos los `if/else` posibles del sistema (qué pasa si el cliente existe, si no existe, si paga con efectivo, con tarjeta, con transferencia, si lleva 1 o N vacunas...), el diagrama se vuelve un monstruo inmanejable y no te alcanzan las 2 horas del parcial.
- **Qué tenés que hacer (Obligatorio):** Antes de trazar la primera línea de vida, **escribí un párrafo de 2 o 4 renglones arriba de la hoja definiendo el ESCENARIO CONCRETO** que vas a modelar, usando los datos del enunciado o de la pantalla adjunta al parcial:
  - *En Parcial 1C 2026 Com. 4300 (PetCare):* El enunciado ya fija el escenario exacto del **06/06/2026**: primera atención de **`Homero`** (gato siamés, 13 años, `5.2 kg`, dueño **`Juan Pérez`**), se aplica 1 vacuna (`Rabia`), se emite 1 receta (`Pastillas desparasitarias`, `1 comprimido`), diagnóstico `SANO`, tratamiento vacío y recordatorio `"volver a verlo en 1 año"` (`01/06/2027`) al presionar `"Guardar Consulta"`.
  - *En Parcial 1C 2026 Com. 1900 (Reencuentro/Adopción y Animales Exóticos):* El enunciado fija el escenario de **Denuncia de Animal Exótico**: un ciudadano avista un **Leopardo** en Rivadavia, Morón, Bs.As., envía foto/video, se calcula peligrosidad `ROJO` y se notifica a **Dirección de Flora y Fauna** y **Policía Ecológica**.
  - *En Parcial 2C 2026 Com. 1900 (Agencia de Viajes):* El Punto 2 pide redactar un escenario concreto que **mejore** el caso de uso a partir del paso 4 para **`"realizar Pago"`** (por ejemplo: el cliente selecciona un paquete a Bariloche para 2 pasajeros, agrega 1 excursión extra, paga con tarjeta de crédito aprobada, se confirma la `Reserva` y se envía notificación por email).
- **Evidencia:**
  - `Parciales/1. [Parcial 1][1C2026][4300][Analia][][].pdf`, `2. -Parcial 1--1C2026--1900--Valeria y Analia-----.pdf` y `3. [Parcial 1][2C2026][1900][][][].pdf`.
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 11): Muestra el recuadro con el escenario concreto antes del Diagrama de Secuencia (*"Un paciente solicita un turno para Hemograma y Hepatograma, para el día 15/05/2025 a las 8hs"*).

### 4.2. Regla N° 2: ¡NO Dibujar al Actor Humano en el Diagrama de Secuencia de Diseño! `[REGLA EXPLÍCITA DE CÁTEDRA]`
- **Criterio estricto de la Profesora:** En el Diagrama de Secuencia de Diseño **NO se dibuja el muñequito (stickman) del Actor** (`:Veterinario`, `:Recepcionista`, `:Cliente`) ni tampoco la pantalla (`:UI`).
- **¿Cómo empieza el Diagrama de Secuencia?** Empieza en el extremo superior izquierdo con un **mensaje entrante** (`───────► :C_Modulo`) que llega directamente a la línea de vida del **Controlador (`:C_...`)**.
- **Justificación teórica de la Profesora (pregunta de examen):** Porque gracias al patrón GRASP **Controlador** y a la separación de capas (MVC), al modelo de diseño del backend **no le importa quién disparó el evento** (pudo haber sido una secretaria haciendo clic en una web, un cliente desde una app móvil, un tótem autoservicio o un proceso batch por API). El sistema es agnóstico de la interfaz.
- **Evidencia:**
  - `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Pág. 11 y Pág. 28): *"En el diagrama de secuencia NO ponemos al actor. Empezamos directamente desde el evento que llega al controlador, porque no importa si lo dispara una persona desde una pantalla o un servicio."*
  - `Transcripcion/transcripciones/05_20260917_101702.txt` (`[00:45:10]`) y `09_20261015_082342.txt` (`[01:50:00]`).

### 4.3. Regla N° 3: Creación de Objetos en Tiempo de Ejecución (`create()`) `[CONVENCIÓN PARTICULAR DE CÁTEDRA vs. ESTÁNDAR UML]`
- **Estándar UML 2.x (Larman):** En UML estándar, la flecha del mensaje `create(...)` apunta directamente a la cajita `:NombreClase` ubicada a la altura vertical del instante en que nace el objeto.
- **Convención de la Prof. Analía Marín en clase y guías (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 11 y `Banco-diagSecuencia.png`):**
  - La profesora acepta tanto que la cajita del objeto esté alineada arriba con las demás como a la altura del `create()`, pero **exige como regla obligatoria** que la activación de creación lleve explícitamente el mensaje **`create(...)`** (y/o el retorno de la instancia creada) y que **quien envíe el `create()` sea el objeto Creador (GRASP)** (por ejemplo, `:Orden` creando `:itemOrden`, o `:HistoriaClinica` / `:Consulta` creando sus partes).
  - Además, en el Caso Laboratorio (`EJEMPLO-Practica-Teoria-version-10.pdf`, Págs. 11–12), muestra también la creación mediante el patrón GoF **Prototype** enviando `clone()` a `:especificacionEstudio` para obtener una nueva instancia `:estudio`.
- **Evidencia:** `Clases/Clases/05/EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 11–12) y `Transcripcion/transcripciones/07_20261001_082247.txt` (`[00:12:15]`).

### 4.4. Regla N° 4: Respetar el Alcance Exacto Pedido en el Punto de Secuencia `[REGLA EXPLÍCITA DE CÁTEDRA]`
- Leé con lupa qué parte del enunciado te pide secuenciar el examen:
  - En **Parcial PetCare 1C 2026 (Com. 4300)**, el Punto 2 pide secuenciar el evento **`"Guardar Consulta"`** para los datos cargados del gato `Homero` (creación y asociación de `Consulta`, `Diagnostico`, `Receta`, `VacunaAplicada`, `Recordatorio` y agregado a `HistoriaClinica`).
  - En **Parcial Reencuentro/Adopción 1C 2026 (Com. 1900)**, el Punto 3 pide secuenciar los **7 pasos de la Denuncia de Animal Exótico** (avistamiento del Leopardo en Morón, registro de `AnimalExotico` y `UbicacionHallazgo`, cálculo de peligrosidad, notificación a Flora y Fauna y Policía Ecológica, marcado de `organismoNotificado = SI` y guardado de `Denuncia`).
  - En **Parcial Agencia de Viajes 2C 2026 (Com. 1900)**, el Punto 2 pide secuenciar **`"realizar Pago"`** mejorando el escenario a partir del paso 4.
- **Moraleja:** En el **Diagrama de Clases** modelás **TODO** el sistema del enunciado, pero en el **Diagrama de Secuencia** solo secuenciás el escenario exacto que pide la consigna.

---

## 5. CRITERIOS PARA LOS DEMÁS DIAGRAMAS UML (CU, ACTIVIDAD, COLABORACIÓN, ESTADO, COMPONENTES, DESPLIEGUE)

En los parciales 2026, además de Clases y Secuencia, **los tres exámenes incluyen Diagrama de Componentes y/o Diagrama de Estados** (ya sea para integrarlos al Diagrama de Clases o para criticarlos y rediseñarlos), y en finales se evalúa también **Despliegue**, **Colaboración**, **Actividad** y **Casos de Uso**. Aquí están las reglas exactas de la profesora para cada uno:

### 5.1. Casos de Uso y su Especificación (`EJEMPLO-Practica-Teoria-version-10.pdf` Págs. 4–7 y Clase 03)
- **Nombres de Casos de Uso:** Siempre **Verbo en infinitivo + Objeto** (ej. `Solicitar Turno`, `Registrar Atención`, `Pagar Cuota`).
- **`<<include>>` vs `<<extend>>`:**
  - `CU_Base - - - <<include>> - - > CU_Incluido`: El paso incluido es **obligatorio** y siempre se ejecuta como parte del flujo normal (o sirve para reutilizar un subflujo común a varios CU, ej. `Validar Identidad`). La flecha apunta hacia el caso incluido.
  - `CU_Extensor - - - <<extend>> - - > CU_Base`: El comportamiento extensor es **opcional/condicional** (solo ocurre bajo cierta condición o punto de extensión, ej. `Registrar Paciente` cuando el paciente no existe). **¡OJO con el sentido de la flecha!** En `<<extend>>`, la flecha punteada **apunta hacia el Caso de Uso Base**.
- **Formato de Especificación preferido por la Profesora (Forma 2 — Tabla de 2 Columnas, Págs. 5–6):**
  - Encabezado con: *Nombre del CU, Actores, Propósito, Precondiciones, Postcondiciones*.
  - **Curso Normal (Camino Feliz):** Tabla dividida en dos columnas: **Acción del Actor** (izquierda) y **Respuesta del Sistema** (derecha), numerando los pasos correlativamente.
  - **Cursos Alternativos:** Al pie de la tabla, referenciando el número exacto del paso donde se bifurca.

### 5.2. Diagrama de Actividad (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 7 y Clase 03/06)
- Representa el flujo de trabajo (workflow) paso a paso, permitiendo mostrar **decisiones** (rombos con condiciones `[si]` / `[no]` mutuamente excluyentes) y **actividades paralelas/concurrentes** mediante **Barras de Sincronización**:
  - **Fork (Bifurcación):** Entra 1 flecha a la barra negra gruesa y salen 2 o más flechas que se ejecutan en paralelo.
  - **Join (Unión):** Entran las N ramas paralelas a la barra negra gruesa y sale 1 sola flecha recién cuando **todas** las ramas paralelas terminaron.
- Se divide en **Carriles (Swimlanes)** verticales u horizontales por área o responsable.

### 5.3. Diagrama de Colaboración / Comunicación (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 12 y Clase 04)
- **Criterio de la Profesora:** Es **semánticamente isomorfo (equivalente)** al Diagrama de Secuencia (ambos son Diagramas de Interacción).
- **Diferencia clave que siempre pregunta en Teoría:**
  - El **Diagrama de Secuencia** enfatiza el **orden temporal** de los mensajes (de arriba hacia abajo a lo largo de las líneas de vida).
  - El **Diagrama de Colaboración (Comunicación)** enfatiza la **estructura estática de enlaces (links)** entre los objetos que colaboran, indicando el orden temporal mediante **numeración correlativa o jerárquica** en las etiquetas de los mensajes (`1: msg1()`, `2: subMsg()`, `3: otroMsg()`).

### 5.4. Diagrama de Estados (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 13, Parciales 1 y 3 de 2026, Finales Dic 2025 y Jul 2026)
- **Regla N° 1 (¡El error más grave!):** El Diagrama de Estados **SIEMPRE modela el ciclo de vida de UN ÚNICO OBJETO de una clase específica del dominio** (ej. un objeto `Consulta`, un objeto `Reserva`, un objeto `Orden`, un objeto `Articulo`, un objeto `Aficionado`). **¡NUNCA es un diagrama de flujo del sistema entero!** (Si mezclás estados del `Cliente`, del `Pago` y del `Envío` en el mismo diagrama, está **MAL**).
- **Regla N° 2 (Nombres de Estados vs. Nombres de Transiciones):**
  - **Dentro de las cajas redondeadas (Estados):** Van **adjetivos o participios** que describen la situación en la que se encuentra el objeto: `Registrada`, `Diagnosticada`, `Cerrada` (en *PetCare*); `Pendiente de pago`, `Confirmada`, `Cancelada`, `Finalizada` (en *Agencia de Viajes*); `Ingresada`, `Validada`, `En Proceso`, `Cerrada` (en *Laboratorio*). (**PROHIBIDO** poner verbos de acción como *"Pagar"* o *"Validar tarjeta"* adentro de una caja de estado).
  - **Sobre las flechas (Transiciones):** Va la sintaxis oficial `evento [condición de guarda] / acción` (donde `evento` es el **método** que recibe el objeto, `[guarda]` es la condición booleana entre corchetes, y `/ acción` es la respuesta inmediata).
- **Regla N° 3 (Integración con el Diagrama de Clases y Patrón GoF State):**
  - En los Parciales 1 y 3 de 2026, la hoja del examen **te da dibujado el Diagrama de Estados** (`Consulta Veterinaria` o `Reserva`) y te pide **integrarlo en el Diagrama de Clases**.
  - Eso significa: (1) asegurarte de que todos los eventos de las flechas (`registrarConsulta()`, `registrarDiagnostico()`, `cerrarConsulta()`, `pagoRealizado()`, `cancelar()`, `cerrarViaje()`) estén como métodos en la clase `Consulta` o `Reserva`; y (2) si aplicás el patrón GoF **State**, crear la interfaz `<<interface>> IEstadoConsulta` / `IEstadoReserva` y una subclase concreta por cada cajita de estado del diagrama impreso.

### 5.5. Diagrama de Componentes (`EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 14, `Banco-diagComponente.png`, `ComponenteVersion2.png` y Parciales 1, 2 y 3 de 2026) `[CONVENCIÓN PARTICULAR DE CÁTEDRA vs. ESTÁNDAR UML]`
- Muestra la arquitectura modular de alto nivel del software (subsistemas/módulos).
- **Las DOS notaciones que utiliza la cátedra:**
  1. **Notación Estándar UML 2.x (enseñada en `UNLaM GRASP-original-marin.pdf` Págs. 12–15 y `Banco-diagComponente.png`):** Componentes con el ícono `<<component>>` unidos mediante **Interfaz Provista (chupetín / círculo completo `──○`)** e **Interfaz Requerida (media luna / enchufe `──(`)** ensamblados (`──○)──`), y conectores de delegación desde los puertos.
  2. **Notación Simplificada de Cajas Anidadas y Dependencias (usada en `EJEMPLO-Practica-Teoria-version-10.pdf` Pág. 14 y en las hojas impresas de los 3 Parciales 2026):** Módulos representados como contenedores con sub-módulos internos (ej. `gestion/usuario`, `mascota`, `turno`, `AtencionVeterinario` con `historiaClinica`) conectados mediante **flechas punteadas de dependencia (`- - - >`)** hacia los componentes de los cuales dependen (incluyendo sistemas externos como `Sist Externo Pago`, `Sist Ext. Aerolinea`, `Organismos Externos`).
- **Regla de Oro de Trazabilidad entre Componentes y Controladores (evaluada en Parcial 2 y Parcial 3 de 2026):**
  - **Cada Componente funcional principal del sistema se corresponde con 1 `Controller` (`C_...`) en el Diagrama de Clases.**
  - Por eso, cuando el Parcial 2 (*Reencuentro/Adopción*) y el Parcial 3 (*Agencia de Viajes*) imponen **"usar solo 4 controladores"**, te piden **modificar o mejorar el Diagrama de Componentes** para que los componentes queden agrupados exactamente en **4 componentes cohesivos de negocio** (más las interfaces hacia sistemas externos), evitando tanto el "monolito acoplado" como tener 8 componentes sueltos sin controlador.

### 5.6. Diagrama de Despliegue (`EJEMPLO-Practica-Teoria-version-10.pdf` Págs. 15–16, `Banco-diagDesplieguev2.png` y `Despliegue2.png`) `[CONVENCIÓN PARTICULAR DE CÁTEDRA vs. ESTÁNDAR UML]`
- Modela la **topología física de hardware**, los entornos de ejecución, los artefactos desplegados y los **protocolos de comunicación** en los enlaces.
- **Los DOS estilos que presenta la profesora en `EJEMPLO-Practica-Teoria-version-10.pdf` (Págs. 15 y 16):**
  1. **Diagrama de Despliegue UML 2.0 Estándar (Pág. 15 y `Banco-diagDesplieguev2.png`):** Nodos representados como **cubos 3D** (`<<device>> Servidor Web`, `<<device>> Servidor Aplicacion`, `<<device>> Servidor BD`, `<<device>> PC Cliente`) que contienen artefactos (`.war`, `.jar`, `.dll`) y se conectan indicando el protocolo (`HTTPS`, `TCP/IP`, `JDBC`, `REST/JSON`, `SOAP/XML`).
  2. **Diagrama de Despliegue por Dominios / Zonas de Red (Pág. 16 y `Despliegue2.png`):** Diagrama arquitectónico dividido mediante líneas punteadas en **Dominios o Ambientes físicos separados** (ej.: `Dominio Laboratorio` con Red Local LAN vs. `Dominio Obra Social` externo vs. `Dominio Paciente` a través de Internet/Firewall, o en Estadios: `Tótem Local` vs. `Servidor Estadio` vs. `Servidor Central AFA` vs. `Renaper`).
- **En el examen:** Podés utilizar los cubos 3D estándar de UML 2.0 agrupándolos dentro de recuadros punteados que marquen las **Zonas/Ambientes** y escribiendo siempre los **protocolos** (`HTTPS`, `REST/JSON`, `TCP/IP`, `MQTT`, `USB`) sobre las líneas de comunicación.

---

## 6. CÓMO RESPONDER LAS JUSTIFICACIONES DE PATRONES EN EL PARCIAL

### 6.1. Cómo Justificar los Patrones GRASP (Punto 1 del Parcial) `[REGLA EXPLÍCITA DE CÁTEDRA]`
En los parciales 2026 (`1. [Parcial 1]...`, `2. -Parcial 1...`, `3. [Parcial 1]...`), se pide aplicar y justificar los patrones GRASP en el diseño.
- **Regla de Oro de la Profesora:** **¡NUNCA des una definición teórica genérica de libro!** Si escribís *"Apliqué Experto porque asigna la responsabilidad a la clase que tiene la información"*, te pone **0 puntos o Incompleto**.
- **Fórmula obligatoria para justificar cada GRASP en el examen:**
  > **[Nombre del Patrón GRASP]** → **¿En qué clase concreta de TU diagrama lo aplicaste?** + **¿En qué método concreto?** + **¿Por qué esa clase (y no otra) tiene los atributos/referencias o el rol para hacerlo?**
  - *Ejemplo 10 puntos (Experto en Información):* *"Se aplica **Experto en Información** en la clase `HistoriaClinica` con el método `+registrarConsulta(c)`, y en la clase `PaqueteTuristico` con el método `+calcularPrecioBase()`, ya que son las clases que poseen los atributos y las colecciones de objetos propios necesarios para cumplir esa responsabilidad."*
  - *Ejemplo 10 puntos (Creador):* *"Se aplica **Creador** en la clase `Consulta` (o `HistoriaClinica`) al instanciar `Diagnostico`, `Receta` y `VacunaAplicada`, ya que `Consulta` agrega y contiene de forma exclusiva a dichos objetos registrándolos como parte de la atención médica."*
  - *Ejemplo 10 puntos (Bajo Acoplamiento y Alta Cohesión / Polimorfismo / Fabricación Pura / Indirección):* *"Se aplica **Alta Cohesión y Bajo Acoplamiento** al delegar la responsabilidad del registro clínico en `HistoriaClinica` y `Consulta` en lugar de sobrecargar al controlador `C_AtencionVeterinaria` o a la clase `Profesional`, manteniendo cada clase enfocada únicamente en las responsabilidades propias de su abstracción."*

### 6.2. Cómo Elegir, Dibujar y Justificar los 2 Patrones GoF `[REGLA EXPLÍCITA DE CÁTEDRA]`
En los parciales 2026, el punto de Patrones GoF vale una parte decisiva de la nota y pide:
> *"Aplicar dos patrones GOF (de diferente categoría) al problema planteado sobre el diagrama de clases:*
> *a) Indicar categoría y nombre del patrón.*
> *b) Explicar qué problema de diseño resuelve dentro del caso.*
> *c) Justificar por qué ese patrón es adecuado.*
> *d) Indicar qué clases del modelo se reutilizan y qué clases/interfaces nuevas se incorporan al diagrama."*
> *(Nota explícita en Parcial 2 de 2026: **"no usar singleton, ni facade"**).*

- **Criterios de corrección de la Profesora (Clase 08 y Clase 09 `[02:15:00]` a `[03:30:00]`):**
  1. **Tienen que ser de DISTINTA CATEGORÍA:** Es decir, elegís 1 **Comportamiento** + 1 **Estructural**, o 1 **Comportamiento** + 1 **Creacional**, o 1 **Estructural** + 1 **Creacional**.
  2. **Evitar `Singleton` y `Facade` en los parciales:** Incluso si en tu tema no dice explícitamente "no usar singleton ni facade", en la Clase 09 la profesora aclaró que muchos alumnos metían un Singleton en el Controller sin justificación real de negocio, por lo que empezaron a prohibirlos en las consignas.
  3. **El patrón GoF DEBE verse dibujado en el Diagrama de Clases con toda su estructura UML completa:**
     - Si aplicás **Strategy** (Comportamiento): Tiene que verse la clase Contexto (ej. `Reserva` / `CalculadoraPrecio` en *Agencia de Viajes*), la interfaz `<<interface>> IPoliticaPrecio` con el método abstracto (`+calcularPrecio(...)`), y al menos **2 o 3 clases concretas** (`PoliticaTemporadaAlta`, `PoliticaGrupoFamiliar`, `PoliticaAnticipada`) que realizan (`- - -▷`) la interfaz.
     - Si aplicás **State** (Comportamiento): Tiene que verse el Contexto (ej. `Consulta` en *PetCare*, `Animal` en *Reencuentro/Adopción*, o `Reserva` en *Agencia de Viajes*) con el atributo `-estadoActual: IEstado...`, la interfaz `<<interface>> IEstado...` con los métodos de transición y las **clases concretas de estado** que coinciden 1 a 1 con el Diagrama de Estados del enunciado.
     - Si aplicás **Observer** (Comportamiento): Ideal en el **Parcial 2 (*Denuncia de Animal Exótico*)** para notificar automáticamente a **Dirección de Flora y Fauna** y **Policía Ecológica**, o en **PetCare** para los recordatorios por WhatsApp/Mail. Tiene que verse el Sujeto observado con su lista `-observadores: List<IObservador>` y métodos `+suscribir(o)`, `+desuscribir(o)`, `+notificar()`, la interfaz `<<interface>> IObservador` y los observadores concretos.
     - Si aplicás **Adapter** (Estructural): Ideal siempre que el enunciado mencione **conectarse a un organismo o sistema externo con interfaz incompatible** (`OrganismoFaunaFloraBsAs`, `PoliciaEcologica`, `SistExtAerolinea`, `SistExtHotel`, `SistExternoPago`, `VISA`, `Veraz`). Tiene que verse la interfaz esperada por tu dominio (`<<interface>> IOrganismoExterno` o `IPasarelaPago`), la clase `Adaptador...` que implementa esa interfaz y envuelve (asociación) a la clase externa traduciendo el llamado.
     - Si aplicás **Decorator** o **Composite** (Estructural): Ideal para paquetes de viaje con excursiones/servicios adicionales o tratamientos compuestos.
     - Si aplicás **Factory Method**, **Builder** o **Prototype** (Creacional): `Prototype` es usado por la propia profesora en el Caso Laboratorio (`especificacionEstudio.clone()`); `Builder` es ideal para armar un `PaqueteTuristico` personalizado; `Factory Method` para crear distintos tipos de denuncias o estudios.

---

## 7. CHECKLIST RÁPIDO DE CONTROL ANTES DE ENTREGAR EL PARCIAL (LOS 12 MANDAMIENTOS DE ANALÍA)

Antes de entregar las hojas en el examen, verificá estos 12 puntos uno por uno:

- [ ] **1. ¿Entregué un diagrama por hoja y numeré todas las hojas?**
- [ ] **2. ¿Respeté el límite máximo de `Controllers` (`max: 4 controladores`) en la parte superior del Diagrama de Clases y están alineados con los componentes principales del Diagrama de Componentes?**
- [ ] **3. ¿Me aseguré de que ningún Actor humano (`Recepcionista`, `Veterinario`, `Ciudadano`) esté actuando como un Gestor lleno de métodos del sistema?**
- [ ] **4. ¿Eliminé todos los métodos `get/set` triviales y los `alta/baja/modificación` genéricos, dejando métodos con nombres de reglas de negocio?**
- [ ] **5. ¿Separé correctamente la "Ficha individual" (`Consulta`, `Mascota`, `Aficionado`) de la clase que maneja "la Colección" (`HistoriaClinica` para las consultas de esa mascota, o `Nomina`/`Padron` con asociación simple para búsquedas globales)?**
- [ ] **6. ¿Puse visibilidades (`-` en atributos, `+` en métodos) y multiplicidades (`1`, `0..*`, `1..*`) en todas las asociaciones sólidas del Diagrama de Clases (recordando que la visibilidad local no se dibuja en el DC)?**
- [ ] **7. ¿Escribí el estereotipo `<<interface>>` o `<<abstract>>` arriba del nombre de todas las interfaces y clases abstractas?**
- [ ] **8. ¿Integré todos los eventos y estados del Diagrama de Estados impreso en la hoja dentro de la clase correspondiente del Diagrama de Clases?**
- [ ] **9. ¿Escribí arriba del Diagrama de Secuencia el ESCENARIO CONCRETO con los datos puntuales del caso e inicié la secuencia SIN Actor humano, entrando directo al `:C_Controller`?**
- [ ] **10. ¿Verifiqué uno por uno que TODOS los mensajes que llegan a un objeto `:X` en el Diagrama de Secuencia están escritos como métodos `+metodo()` dentro de la clase `X` en el Diagrama de Clases?**
- [ ] **11. ¿Justifiqué los patrones GRASP nombrando las clases y métodos exactos de MI diagrama en lugar de recitar teoría genérica?**
- [ ] **12. ¿Elegí 2 patrones GoF de DISTINTA categoría (sin usar Singleton ni Facade), los dibujé completos en el Diagrama de Clases y respondí los 4 incisos (`a`, `b`, `c`, `d`)?**
