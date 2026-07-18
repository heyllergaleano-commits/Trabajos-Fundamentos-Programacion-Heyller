# quiz_empresas.py
# Quiz 1 - Fundamentos de programacion (Programacion Estructurada + POO)
# Tu tarea: completar todos los bloques marcados con "# TODO".
# Cada linea de empresas.txt tiene:  nombre, sector, num_empleados, ingresos_anuales
# Para ejecutar:  python quiz_empresas.py
#
# CONSEJO: ve completando un TODO a la vez y ejecuta el archivo para ver como
#          se va llenando la salida. Al inicio veras resultados vacios o en cero.


# 1) LA CLASE: representa UNA empresa (datos + comportamiento juntos)
# quiz_empresas.py

class Empresa:
    """Representa UNA empresa: encapsula sus datos y su comportamiento."""

    def __init__(self, nombre, sector, num_empleados, ingresos_anuales):
        self.nombre = nombre
        self.sector = sector
        self.num_empleados = int(num_empleados)
        self.ingresos_anuales = int(ingresos_anuales)

    def obtener_informacion(self):
        return f"{self.nombre} | {self.sector} | {self.num_empleados} empleados | ${self.ingresos_anuales}"


def leer_empresas(nombre_archivo):
    empresas = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, sector, num_empleados, ingresos_anuales = linea.strip().split(",")

            if int(num_empleados) > 0:
                empresa = Empresa(nombre, sector, num_empleados, ingresos_anuales)
                empresas.append(empresa)

    return empresas


def calcular_total_ingresos(empresas):
    total = 0

    for empresa in empresas:
        total += empresa.ingresos_anuales

    return total


def filtrar_por_sector(empresas, sector):
    lista_filtrada = []

    for empresa in empresas:
        if empresa.sector == sector:
            lista_filtrada.append(empresa)

    return lista_filtrada


def empresa_con_mas_empleados(empresas):
    if len(empresas) == 0:
        return None

    mayor = empresas[0]

    for empresa in empresas:
        if empresa.num_empleados > mayor.num_empleados:
            mayor = empresa

    return mayor


def promedio_empleados(empresas):
    if len(empresas) == 0:
        return 0

    total_empleados = 0

    for empresa in empresas:
        total_empleados += empresa.num_empleados

    promedio = total_empleados / len(empresas)

    return round(promedio, 2)


def ejecutar_quiz():
    empresas = leer_empresas("empresas.txt")

    print("--- Empresas registradas ---")
    for empresa in empresas:
        print(empresa.obtener_informacion())

    print("\nTotal de ingresos:", calcular_total_ingresos(empresas))

    print("\n--- Empresas del sector TECNOLOGIA ---")
    for empresa in filtrar_por_sector(empresas, "TECNOLOGIA"):
        print(empresa.obtener_informacion())

    mejor = empresa_con_mas_empleados(empresas)
    if mejor is not None:
        print("\nEmpresa con mas empleados:", mejor.obtener_informacion())

    print("\nPromedio de empleados:", promedio_empleados(empresas))


ejecutar_quiz()