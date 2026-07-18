# diseno_pilares_poo.py
# Semana 3 - Encapsulamiento, Herencia y Polimorfismo

class TransaccionBase:
    """Clase base que contiene los datos comunes de una transacción."""

    def __init__(self, cliente_id, tipo, monto):
        self._cliente_id = cliente_id
        self._tipo = tipo
        self.monto = monto

    @property
    def cliente_id(self):
        return self._cliente_id

    @property
    def tipo(self):
        return self._tipo

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        nuevo_monto = float(nuevo_monto)

        if nuevo_monto < 0:
            raise ValueError("El monto no puede ser negativo.")

        self._monto = nuevo_monto

    def calcular_impacto(self):
        """Método que será sobrescrito por las clases hijas."""
        raise NotImplementedError("Este método debe ser implementado por la clase hija.")

    def obtener_informacion(self):
        return f"{self.cliente_id} | {self.tipo} | ${self.monto}"


class TransaccionCredito(TransaccionBase):
    """Clase hija para transacciones de tipo crédito."""

    def __init__(self, cliente_id, monto):
        super().__init__(cliente_id, "CREDITO", monto)

    def calcular_impacto(self):
        return self.monto * 0.02


class TransaccionDebito(TransaccionBase):
    """Clase hija para transacciones de tipo débito."""

    def __init__(self, cliente_id, monto):
        super().__init__(cliente_id, "DEBITO", monto)

    def calcular_impacto(self):
        return 1500


def crear_transaccion(cliente_id, tipo, monto):
    tipo = tipo.strip().upper()

    if tipo == "CREDITO":
        return TransaccionCredito(cliente_id, monto)
    elif tipo == "DEBITO":
        return TransaccionDebito(cliente_id, monto)
    else:
        raise ValueError("Tipo de transacción no válido.")


def leer_transacciones(nombre_archivo):
    transacciones = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")

            if len(partes) == 3:
                cliente_id = partes[0]
                tipo = partes[1]
                monto = partes[2]

                try:
                    transaccion = crear_transaccion(cliente_id, tipo, monto)
                    transacciones.append(transaccion)
                except ValueError as error:
                    print(f"Registro ignorado: {cliente_id} - {error}")

    return transacciones


def ejecutar_sistema():
    transacciones = leer_transacciones("transacciones.txt")

    print("--- Transacciones cargadas Semana 3 ---")

    for transaccion in transacciones:
        print(
            transaccion.obtener_informacion(),
            "| Impacto:",
            transaccion.calcular_impacto()
        )


ejecutar_sistema()