# transacciones.py
# Clases del sistema de gestión de transacciones


class TransaccionBase:
    """Clase base con los datos comunes de una transacción."""

    def __init__(self, cliente_id, monto):
        if not cliente_id.strip():
            raise ValueError("El cliente debe tener un identificador.")

        self._cliente_id = cliente_id.strip()
        self.monto = monto

    @property
    def cliente_id(self):
        return self._cliente_id

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        nuevo_monto = float(nuevo_monto)

        if nuevo_monto < 0:
            raise ValueError("El monto no puede ser negativo.")

        self._monto = nuevo_monto

    @property
    def tipo(self):
        """Cada clase hija debe indicar su tipo."""
        raise NotImplementedError(
            "La clase hija debe definir el tipo de transacción."
        )

    def calcular_impacto(self):
        """Cada clase hija calcula el impacto de forma diferente."""
        raise NotImplementedError(
            "La clase hija debe implementar calcular_impacto()."
        )

    def convertir_diccionario(self):
        """Prepara los datos del objeto para convertirlos a JSON."""
        return {
            "cliente_id": self.cliente_id,
            "tipo": self.tipo,
            "monto": self.monto,
            "impacto": self.calcular_impacto()
        }

    def __str__(self):
        return (
            f"{self.cliente_id} | {self.tipo} | "
            f"${self.monto:,.0f} | "
            f"Impacto: ${self.calcular_impacto():,.0f}"
        )


class TransaccionCredito(TransaccionBase):
    """Transacción de crédito con impacto del 2 %."""

    @property
    def tipo(self):
        return "CREDITO"

    def calcular_impacto(self):
        return self.monto * 0.02


class TransaccionDebito(TransaccionBase):
    """Transacción de débito con costo fijo de $1.500."""

    @property
    def tipo(self):
        return "DEBITO"

    def calcular_impacto(self):
        return 1500


def crear_transaccion(cliente_id, tipo, monto):
    """Crea la clase correspondiente según el tipo recibido."""

    tipo = tipo.strip().upper()

    if tipo == "CREDITO":
        return TransaccionCredito(cliente_id, monto)

    if tipo == "DEBITO":
        return TransaccionDebito(cliente_id, monto)

    raise ValueError(f"Tipo de transacción no válido: {tipo}")