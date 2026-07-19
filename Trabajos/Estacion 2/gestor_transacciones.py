# gestor_transacciones.py
# Lectura de archivos y recuperación mediante try-except

from transacciones import crear_transaccion


def cargar_transacciones(ruta_archivo):
    """
    Lee las transacciones del archivo TXT.
    Los registros incorrectos se informan y se ignoran,
    permitiendo que el sistema continúe.
    """

    transacciones = []

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:

            for numero_linea, linea in enumerate(archivo, start=1):

                linea = linea.strip()

                if not linea:
                    continue

                try:
                    partes = linea.split(",")

                    transaccion = crear_transaccion(*partes)

                    transacciones.append(transaccion)

                except ValueError as error:
                    print(
                        f"[Línea {numero_linea}] "
                        f"Error de valor: {error} "
                        f"-> Se ignora: {linea}"
                    )

                except TypeError:
                    print(
                        f"[Línea {numero_linea}] "
                        "Datos incompletos o adicionales "
                        f"-> Se ignora: {linea}"
                    )

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_archivo}")

    except OSError as error:
        print(f"No fue posible leer el archivo: {error}")

    return transacciones


def mostrar_transacciones(transacciones):
    """Muestra las transacciones válidas procesadas."""

    print("\n--- TRANSACCIONES VÁLIDAS ---")

    if not transacciones:
        print("No se encontraron transacciones válidas.")
        return

    for transaccion in transacciones:
        print(transaccion)

    print(
        f"\nTotal de transacciones válidas: "
        f"{len(transacciones)}"
    )