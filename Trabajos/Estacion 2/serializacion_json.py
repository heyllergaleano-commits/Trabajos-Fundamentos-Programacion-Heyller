# serializacion_json.py
# Conversión de objetos Python a JSON y recuperación de objetos

import json

from transacciones import crear_transaccion


def guardar_transacciones_json(transacciones, ruta_archivo):
    """Serializa las transacciones y las guarda en un archivo JSON."""

    datos = []

    for transaccion in transacciones:
        datos.append(transaccion.convertir_diccionario())

    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                ensure_ascii=False,
                indent=4
            )

        print(f"\nArchivo JSON generado: {ruta_archivo}")

    except OSError as error:
        print(f"No fue posible guardar el archivo JSON: {error}")


def cargar_transacciones_json(ruta_archivo):
    """Deserializa el archivo JSON y reconstruye los objetos."""

    transacciones = []

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        for registro in datos:
            transaccion = crear_transaccion(
                registro["cliente_id"],
                registro["tipo"],
                registro["monto"]
            )

            transacciones.append(transaccion)

        print(
            f"Se recuperaron {len(transacciones)} "
            "transacciones desde JSON."
        )

    except FileNotFoundError:
        print(f"No se encontró el archivo JSON: {ruta_archivo}")

    except json.JSONDecodeError as error:
        print(f"El archivo JSON contiene datos incorrectos: {error}")

    except (KeyError, TypeError, ValueError) as error:
        print(f"No fue posible reconstruir una transacción: {error}")

    return transacciones