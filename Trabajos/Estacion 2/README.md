# Quantum Core - Sistema de Gestión de Transacciones

## Autor

**Heyller De Jesús Galeano Guarín**  
Programa de Ingeniería de Sistemas  
CEIPA Business School

## Descripción

Quantum Core es un sistema desarrollado en Python para gestionar transacciones financieras desde un archivo de datos de prueba.

El proyecto integra los conocimientos desarrollados durante las semanas 3, 4 y 5 del curso:

- Programación Orientada a Objetos.
- Encapsulamiento, herencia y polimorfismo.
- Principios SOLID.
- Manejo de excepciones con `try-except`.
- Serialización y deserialización JSON.
- Control de versiones con Git y GitHub.

## Funcionalidades

- Lectura de transacciones desde un archivo TXT.
- Creación de transacciones de crédito y débito.
- Validación de identificadores, tipos y montos.
- Recuperación ante registros incorrectos.
- Cálculo polimórfico del impacto de cada transacción.
- Almacenamiento de transacciones válidas en JSON.
- Reconstrucción de objetos desde el archivo JSON.

## Estructura del proyecto

```text
Estacion 2/
├── datos/
│   ├── transacciones_prueba.txt
│   └── transacciones.json
├── transacciones.py
├── gestor_transacciones.py
├── serializacion_json.py
├── main.py
└── README.md