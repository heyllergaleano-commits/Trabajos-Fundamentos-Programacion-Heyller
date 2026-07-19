# main.py
# Punto de entrada del sistema Quantum Core

from pathlib import Path

from gestor_transacciones import (
    cargar_transacciones,
    mostrar_transacciones
)
from serializacion_json import (
    guardar_transacciones_json,
    cargar_transacciones_json
)


# Permite encontrar la carpeta datos sin importar
# desde qué ubicación se ejecute el programa.
CARPETA_PROYECTO = Path(__file__).resolve().parent

ARCHIVO_TXT = (
    CARPETA_PROYECTO
    / "datos"
    / "transacciones_prueba.txt"
)

ARCHIVO_JSON = (
    CARPETA_PROYECTO
    / "datos"
    / "transacciones.json"
)


def ejecutar_sistema():
    """Integra POO, excepciones y serialización JSON."""

    print("=" * 55)
    print("       QUANTUM CORE - GESTIÓN DE TRANSACCIONES")
    print("=" * 55)

    # 1. Leer el archivo TXT controlando los errores
    transacciones = cargar_transacciones(ARCHIVO_TXT)

    # 2. Mostrar únicamente las transacciones válidas
    mostrar_transacciones(transacciones)

    if not transacciones:
        print("\nEl sistema finalizó sin datos para serializar.")
        return

    # 3. Serializar los objetos válidos
    guardar_transacciones_json(
        transacciones,
        ARCHIVO_JSON
    )

    # 4. Deserializar y reconstruir los objetos
    transacciones_recuperadas = cargar_transacciones_json(
        ARCHIVO_JSON
    )

    print("\n--- OBJETOS RECUPERADOS DESDE JSON ---")

    for transaccion in transacciones_recuperadas:
        print(transaccion)

    print("\nEl sistema finalizó correctamente.")


if __name__ == "__main__":
    ejecutar_sistema()