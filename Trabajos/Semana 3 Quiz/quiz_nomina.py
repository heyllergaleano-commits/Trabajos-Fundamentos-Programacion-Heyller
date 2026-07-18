# quiz_nomina.py
# Quiz Semana 3 - Fundamentos de Programación
# Tema: Pilares de POO aplicados a una nómina empresarial

import pandas as pd


# 1. CLASE BASE
class EmpleadoBase:
    """Representa la información común de todos los empleados."""

    def __init__(self, nombre, salario_base, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.salario_base = salario_base

    # Getter
    @property
    def salario_base(self):
        """Devuelve el salario base del empleado."""
        return self._salario_base

    # Setter
    @salario_base.setter
    def salario_base(self, nuevo_salario):
        """Valida que el salario no sea negativo antes de guardarlo."""
        nuevo_salario = int(nuevo_salario)

        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo.")

        self._salario_base = nuevo_salario

    def calcular_pago(self):
        """Método que debe ser implementado por las clases hijas."""
        raise NotImplementedError(
            "Cada tipo de empleado debe calcular su propio pago."
        )

    def obtener_informacion(self):
        """Devuelve la información principal del empleado."""
        return (
            f"{self.nombre} | "
            f"{type(self).__name__} | "
            f"{self.ciudad} | "
            f"base ${self.salario_base}"
        )


# 2. CLASES HIJAS
class EmpleadoPlanta(EmpleadoBase):
    """Empleado que recibe salario base más prestaciones."""

    def calcular_pago(self):
        """Calcula el salario con un 30 % adicional de prestaciones."""
        return self.salario_base * 1.30


class EmpleadoContratista(EmpleadoBase):
    """Empleado que recibe únicamente su salario base."""

    def calcular_pago(self):
        """Devuelve el salario sin prestaciones adicionales."""
        return self.salario_base


# 3. CREAR EL OBJETO SEGÚN EL TIPO DE EMPLEADO
def crear_empleado(nombre, tipo, salario_base, ciudad):
    """Crea el tipo de empleado correspondiente."""

    if tipo == "PLANTA":
        return EmpleadoPlanta(nombre, salario_base, ciudad)

    if tipo == "CONTRATISTA":
        return EmpleadoContratista(nombre, salario_base, ciudad)

    raise ValueError(f"Tipo desconocido '{tipo}'")


# 4. LECTURA DEL ARCHIVO EXCEL
def leer_empleados_excel(nombre_archivo):
    """Lee los empleados del Excel y devuelve una lista de objetos."""

    empleados = []

    try:
        df = pd.read_excel(nombre_archivo)
    except FileNotFoundError:
        print(f"[Error] No se encontró el archivo '{nombre_archivo}'.")
        return empleados
    except Exception as error:
        print(f"[Error] No fue posible leer el archivo: {error}")
        return empleados

    # Normalizar nombres de columnas
    df.columns = [str(columna).strip().lower() for columna in df.columns]

    columnas_necesarias = {"nombre", "tipo", "salario_base"}

    if not columnas_necesarias.issubset(df.columns):
        columnas_faltantes = columnas_necesarias - set(df.columns)
        print(f"[Error] Al Excel le faltan columnas: {columnas_faltantes}")
        return empleados

    for _, fila in df.iterrows():

        if (
            pd.isna(fila["nombre"])
            or pd.isna(fila["tipo"])
            or pd.isna(fila["salario_base"])
        ):
            print("[Aviso] Fila incompleta ignorada.")
            continue

        nombre = str(fila["nombre"]).strip()
        tipo = str(fila["tipo"]).strip().upper()
        salario = fila["salario_base"]

        ciudad = ""

        if "ciudad" in df.columns and not pd.isna(fila["ciudad"]):
            ciudad = str(fila["ciudad"]).strip()

        try:
            empleado = crear_empleado(
                nombre,
                tipo,
                salario,
                ciudad
            )

            empleados.append(empleado)

        except ValueError as error:
            print(f"[Aviso] Se ignoró {nombre}: {error}")

    return empleados


# 5. FUNCIÓN PROPIA
def empleado_mejor_pagado(empleados):
    """
    Busca y devuelve al empleado con el pago total más alto.
    """

    if not empleados:
        return None

    mejor_empleado = empleados[0]

    for empleado in empleados[1:]:
        if empleado.calcular_pago() > mejor_empleado.calcular_pago():
            mejor_empleado = empleado

    return mejor_empleado


# 6. FUNCIÓN PRINCIPAL
def ejecutar_quiz():
    """Ejecuta el programa principal de la nómina."""

    empleados = leer_empleados_excel("empleados.xlsx")

    print("\n--- NÓMINA DE EMPLEADOS ---")

    if not empleados:
        print("No hay empleados válidos para mostrar.")
        return

    for empleado in empleados:
        pago = empleado.calcular_pago()

        print(
            empleado.obtener_informacion(),
            "-> pago:",
            f"${pago:,.0f}"
        )

    mejor_empleado = empleado_mejor_pagado(empleados)

    if mejor_empleado is not None:
        print("\n--- EMPLEADO CON MAYOR PAGO ---")
        print(
            mejor_empleado.obtener_informacion(),
            "-> pago:",
            f"${mejor_empleado.calcular_pago():,.0f}"
        )


# INICIAR EL PROGRAMA
if __name__ == "__main__":
    ejecutar_quiz()