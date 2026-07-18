# robustez_try_except.py

class Transaccion:

    def __init__(self, cliente_id, tipo, monto):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, valor):
        if int(valor) < 0:
            raise ValueError("el monto no puede ser negativo")

        self._monto = int(valor)

    def __str__(self):
        return f"{self.cliente_id} | {self.tipo} | ${self.monto}"


def cargar_transacciones(nombre_archivo):

    transacciones = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:

        for numero, linea in enumerate(archivo, start=1):

            linea = linea.strip()

            if not linea:
                continue

            try:
                partes = linea.split(",")

                transaccion = Transaccion(*partes)

                transacciones.append(transaccion)

            except ValueError as error:
                print(
                    f"[Línea {numero}] ValueError: {error} "
                    f"-> Se ignora: {linea}"
                )

            except TypeError:
                print(
                    f"[Línea {numero}] TypeError: datos insuficientes "
                    f"-> Se ignora: {linea}"
                )

    return transacciones


def ejecutar_sistema():

    transacciones = cargar_transacciones(
        "transacciones_corruptas.txt"
    )

    print()
    print(
        f"Se procesaron {len(transacciones)} "
        "transacciones válidas:"
    )

    for transaccion in transacciones:
        print(transaccion)


if __name__ == "__main__":
    ejecutar_sistema()