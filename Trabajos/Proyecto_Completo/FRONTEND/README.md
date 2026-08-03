# 💳 Quantum Core Finance

## Sistema de Gestión Financiera Full Stack

Quantum Core Finance es una aplicación Full Stack desarrollada como proyecto final de la asignatura **Fundamentos de Programación**. El sistema permite administrar transacciones financieras mediante operaciones **CRUD (Crear, Leer, Actualizar y Eliminar)** utilizando una arquitectura moderna basada en React, Flask, Prisma, MySQL y Docker.

---

# 📌 Objetivo del proyecto

Desarrollar un sistema de gestión financiera que integre un frontend, un backend y una base de datos, aplicando los conceptos aprendidos durante el curso:

- Programación Orientada a Objetos (POO)
- Arquitectura por capas
- Bases de datos relacionales
- API REST
- Persistencia de datos
- Docker
- Git y GitHub

---

# 🛠 Tecnologías utilizadas

## Frontend

- React
- Vite
- Tailwind CSS
- JavaScript

## Backend

- Python
- Flask
- Prisma ORM

## Base de datos

- MySQL 8
- Docker Desktop

## Control de versiones

- Git
- GitHub

---

# 🏗 Arquitectura del sistema

```
             React + Vite
                   │
             HTTP / JSON
                   │
              Flask API
                   │
             Prisma ORM
                   │
           MySQL (Docker)
```

El sistema está dividido en tres componentes independientes:

- **Frontend:** interfaz desarrollada con React.
- **Backend:** API REST construida con Flask.
- **Base de datos:** MySQL ejecutándose dentro de un contenedor Docker.

Esta arquitectura facilita el mantenimiento, la escalabilidad y la separación de responsabilidades.

---

# ⚙ Funcionalidades

El sistema permite:

- ✅ Crear transacciones
- ✅ Consultar transacciones
- ✅ Editar transacciones
- ✅ Eliminar transacciones
- ✅ Validación de datos
- ✅ Persistencia de información en MySQL
- ✅ Comunicación mediante API REST

---

# 📂 Estructura del proyecto

```
Proyecto_Completo
│
├── BACKEND
│   ├── app.py
│   ├── controllers
│   ├── models
│   ├── routes
│   └── schema.prisma
│
├── FRONTEND
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# ▶ Cómo ejecutar el proyecto

## 1. Iniciar MySQL en Docker

```bash
docker start empresa
```

---

## 2. Ejecutar el Backend

```bash
cd Proyecto_Completo/BACKEND

pip install -r requirements.txt

prisma db push

python app.py
```

El servidor quedará disponible en:

```
http://localhost:5000
```

---

## 3. Ejecutar el Frontend

```bash
cd Proyecto_Completo/FRONTEND

npm install

npm run dev
```

La aplicación quedará disponible en:

```
http://localhost:5173
```

---

# 📸 Evidencias

Durante la ejecución del proyecto se verificó:

- Contenedor Docker funcionando.
- Base de datos MySQL activa.
- API REST operativa.
- Frontend React funcionando.
- Operaciones CRUD completadas correctamente.
- Persistencia de datos en MySQL.

---

# 🎓 Autor

**Heyller Galeano**

Estudiante de Ingeniería de Sistemas

CEIPA Business School

Asignatura: Fundamentos de Programación

---

# 👨‍🏫 Profesor

Simón

---

# 📅 Año

2026

---

# 📄 Licencia

Proyecto desarrollado con fines académicos para la asignatura **Fundamentos de Programación**.