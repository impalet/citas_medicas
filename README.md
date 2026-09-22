# 🏥 Sistema de Gestión de Citas Médicas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![POO](https://img.shields.io/badge/Programación-POO-orange)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow)

## 📌 Descripción

Este proyecto consiste en el desarrollo de un **sistema básico de gestión de citas médicas utilizando Python y Programación Orientada a Objetos (POO)**.

El sistema permite representar las principales entidades involucradas en una atención médica, como pacientes, médicos, citas y atenciones.

El proyecto fue desarrollado con fines académicos para reforzar conceptos fundamentales de Python, especialmente:

* Clases y objetos
* Atributos
* Métodos
* Constructores `__init__`
* Encapsulamiento
* Propiedades
* Relaciones entre objetos
* Listas y colecciones
* Validación de datos
* Organización del código

---

## 🎯 Objetivo del proyecto

Desarrollar una aplicación en Python que permita modelar el proceso básico de atención médica mediante diferentes clases relacionadas entre sí.

El objetivo principal es aplicar los conocimientos de **Programación Orientada a Objetos** en un problema práctico y cercano a un sistema real.

---

## 🧩 Estructura del proyecto

```text
📁 Sistema-Citas-Medicas
│
├── 📄 Paciente.py
├── 📄 Medico.py
├── 📄 Cita.py
├── 📄 Atencion.py
├── 📄 main.py
│
└── 📄 README.md
```

### 👤 `Paciente.py`

Representa al paciente que utiliza el sistema.

Contiene información relacionada con el paciente y permite trabajar con sus datos mediante atributos y métodos.

---

### 👨‍⚕️ `Medico.py`

Representa al médico encargado de atender las citas.

Permite almacenar y gestionar información correspondiente al profesional médico.

---

### 📅 `Cita.py`

Representa una cita médica entre un paciente y un médico.

Esta clase permite relacionar las entidades principales del sistema y representar una cita programada.

---

### 🩺 `Atencion.py`

Representa la atención médica realizada durante una cita.

Contiene información relacionada con la atención, como:

* Código de atención
* Cita asociada
* Diagnóstico

La clase recibe estos datos mediante su constructor.

---

### ▶️ `main.py`

Es el archivo principal del programa.

Aquí se crean los objetos de las diferentes clases y se realizan las operaciones necesarias para probar el funcionamiento del sistema.

---

## 🔗 Relación entre las clases

La estructura básica del sistema puede representarse de la siguiente manera:

```text
             👤 PACIENTE
                  │
                  │
                  ▼
              📅 CITA
                  ▲
                  │
                  │
             👨‍⚕️ MÉDICO
                  │
                  │
                  ▼
             🩺 ATENCIÓN
```

Una **cita** relaciona a un paciente con un médico.

Después, una **atención** puede asociarse a una cita y almacenar información como el diagnóstico.

---

## 💻 Tecnologías utilizadas

### Python 🐍

El proyecto está desarrollado utilizando **Python 3**.

### Programación Orientada a Objetos

Se utilizan los principales conceptos de POO para organizar el sistema mediante clases y objetos.

---

## 🧠 Conceptos de Python aplicados

Durante el desarrollo se aplican conceptos como:

### Clases

Las clases permiten representar entidades del sistema.

```python
class Paciente:
    ...
```

### Objetos

Los objetos representan instancias concretas de cada clase.

```python
paciente = Paciente(...)
```

### Constructor

El método `__init__()` permite inicializar los atributos de un objeto.

```python
def __init__(self, codigo, nombre):
    self.codigo = codigo
    self.nombre = nombre
```

### Métodos

Permiten definir acciones que puede realizar un objeto.

```python
def mostrar_datos(self):
    ...
```

### Encapsulamiento

Se utiliza para controlar el acceso a los atributos y organizar mejor la información de cada objeto.

### Listas

Las listas permiten almacenar múltiples objetos y trabajar con colecciones de datos.

```python
pacientes = []
medicos = []
citas = []
atenciones = []
```

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar a la carpeta

```bash
cd Sistema-Citas-Medicas
```

### 3. Ejecutar el programa

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

---

## 📋 Funcionamiento general

El funcionamiento básico del sistema sigue una secuencia similar a:

```text
Inicio
  │
  ▼
Crear paciente
  │
  ▼
Crear médico
  │
  ▼
Registrar cita
  │
  ▼
Realizar atención
  │
  ▼
Registrar diagnóstico
  │
  ▼
Mostrar información
  │
  ▼
Fin
```

---

## 🚧 Estado del proyecto

🟡 **En desarrollo**

Actualmente el proyecto se encuentra en una etapa académica de desarrollo y se irá ampliando progresivamente para incorporar nuevas funcionalidades.

### Funcionalidades actuales

* [x] Creación de clases
* [x] Creación de objetos
* [x] Uso de constructores
* [x] Uso de atributos y métodos
* [x] Relación entre objetos
* [x] Manejo de citas
* [x] Registro de atenciones
* [ ] Interfaz gráfica
* [ ] Persistencia en base de datos
* [ ] Sistema de usuarios
* [ ] API
* [ ] Aplicación web

---

## 📚 Propósito académico

Este proyecto forma parte del proceso de aprendizaje de **Python y Programación Orientada a Objetos**.

El desarrollo busca pasar progresivamente desde ejercicios básicos de Python hacia la construcción de aplicaciones más completas, aplicando conceptos de programación en un escenario práctico.

---

## 👨‍💻 Autor

**Proyecto académico — Ingeniería de Software**

Desarrollado utilizando:

🐍 Python
🧱 Programación Orientada a Objetos
💻 Visual Studio Code

---

## ⭐ Próximas mejoras

Como parte de la evolución del proyecto, se plantea incorporar:

* Validaciones más completas.
* Menús interactivos.
* Búsqueda de pacientes y médicos.
* Gestión de citas.
* Listado de registros.
* Interfaz gráfica.
* Almacenamiento de información.
* Base de datos.
* Comunicación mediante sockets.
* Posible implementación de una API.

---

## 📄 Licencia

Este proyecto ha sido desarrollado con fines **educativos y académicos**.
