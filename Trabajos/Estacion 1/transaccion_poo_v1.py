# transaccion_poo_v1.py

class Transaccion:
    """Clase que representa una transacción financiera."""

    def __init__(self, cliente_id, tipo, monto):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = float(monto)

    def obtener_informacion(self):
        return f"{self.cliente_id} | {self.tipo} | ${self.monto}"


class SistemaTransacciones:
    """Clase que gestiona la lectura y análisis de transacciones."""

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.transacciones = []

    def leer_y_almacenar_datos(self):
        with open(self.nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")

                if len(partes) == 3:
                    cliente_id = partes[0]
                    tipo = partes[1]
                    monto = partes[2]

                    transaccion = Transaccion(cliente_id, tipo, monto)
                    self.transacciones.append(transaccion)

    def calcular_monto_total(self):
        total = 0

        for transaccion in self.transacciones:
            total += transaccion.monto

        return total

    def filtrar_por_tipo(self, tipo_filtro):
        lista_filtrada = []

        for transaccion in self.transacciones:
            if transaccion.tipo == tipo_filtro:
                lista_filtrada.append(transaccion)

        return lista_filtrada

    def mostrar_transacciones(self):
        for transaccion in self.transacciones:
            print(transaccion.obtener_informacion())


def ejecutar_sistema():
    sistema = SistemaTransacciones("transacciones.txt")

    sistema.leer_y_almacenar_datos()

    print("--- Transacciones registradas ---")
    sistema.mostrar_transacciones()

    total = sistema.calcular_monto_total()
    print("\nMonto total de todas las transacciones:", total)

    tipo_filtro = "CREDITO"
    print("\n--- Transacciones de tipo", tipo_filtro, "---")

    transacciones_filtradas = sistema.filtrar_por_tipo(tipo_filtro)

    for transaccion in transacciones_filtradas:
        print(transaccion.obtener_informacion())


ejecutar_sistema()