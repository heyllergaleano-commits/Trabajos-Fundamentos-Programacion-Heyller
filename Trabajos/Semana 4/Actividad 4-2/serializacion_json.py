import json


class Transaccion:

    def __init__(self, cliente_id: str, tipo: str, monto: float):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        return (
            f"Transacción [{self.tipo}] - "
            f"ID: {self.cliente_id}, Monto: {self.monto}"
        )


# Creación del objeto
transaccion = Transaccion(
    cliente_id="C001",
    tipo="CREDITO",
    monto=500000
)

# Objeto a diccionario
datos_transaccion = {
    "cliente_id": transaccion.cliente_id,
    "tipo": transaccion.tipo,
    "monto": transaccion.monto
}

# Diccionario a cadena JSON
cadena_json = json.dumps(
    datos_transaccion,
    ensure_ascii=False,
    indent=4
)

print("JSON generado:")
print(cadena_json)

# Cadena JSON a diccionario
datos_recibidos = json.loads(cadena_json)

# Diccionario a nuevo objeto
nueva_transaccion = Transaccion(
    cliente_id=datos_recibidos["cliente_id"],
    tipo=datos_recibidos["tipo"],
    monto=datos_recibidos["monto"]
)

print("\nObjeto recuperado:")
print(nueva_transaccion)