import sqlite3
from pathlib import Path


# Ubicar la base de datos creada en la Actividad 7-1
RUTA_ACTUAL = Path(__file__).resolve().parent
RUTA_DB = RUTA_ACTUAL.parent / "Actividad 7-1" / "quantum_wallet.db"


def conectar():
    """Abre la conexión con la base de datos y activa las llaves foráneas."""
    conexion = sqlite3.connect(RUTA_DB)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def crear_tabla_contactos():
    """Crea la tabla contactos si todavía no existe."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
            apodo TEXT NOT NULL,
            numero TEXT NOT NULL,
            id_usuario INTEGER NOT NULL,
            FOREIGN KEY (id_usuario)
                REFERENCES usuarios(id_usuario)
        )
    """)

    conexion.commit()
    conexion.close()
    print("Tabla 'contactos' creada o verificada correctamente.")


def preparar_datos_prueba():
    """
    Limpia los contactos anteriores para que la práctica siempre
    empiece con los identificadores del 1 al 5.
    """
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM contactos")
    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name = ?",
        ("contactos",)
    )

    conexion.commit()
    conexion.close()


# CREATE: insertar cinco contactos para el usuario 1
def crear_contactos():
    conexion = conectar()
    cursor = conexion.cursor()

    contactos = [
        ("Mama", "3001112233", 1),
        ("Papa", "3002223344", 1),
        ("Hermana", "3003334455", 1),
        ("Trabajo", "6044445566", 1),
        ("Universidad", "6045556677", 1),
    ]

    cursor.executemany("""
        INSERT INTO contactos (apodo, numero, id_usuario)
        VALUES (?, ?, ?)
    """, contactos)

    conexion.commit()
    conexion.close()
    print("CREATE: Se insertaron 5 contactos para el usuario 1.")


# READ: consultar los contactos del usuario 1
def leer_contactos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_contacto, apodo, numero
        FROM contactos
        WHERE id_usuario = ?
        ORDER BY id_contacto
    """, (1,))

    contactos = cursor.fetchall()

    print("\nREAD: Contactos del usuario 1")
    print("-" * 48)

    if contactos:
        for id_contacto, apodo, numero in contactos:
            print(
                f"ID: {id_contacto} | "
                f"Apodo: {apodo} | "
                f"Número: {numero}"
            )
    else:
        print("No se encontraron contactos.")

    conexion.close()


# UPDATE: cambiar el apodo del contacto con id 1
def actualizar_contacto():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE contactos
        SET apodo = ?
        WHERE id_contacto = ?
    """, ("Mamita", 1))

    conexion.commit()

    if cursor.rowcount > 0:
        print("\nUPDATE: El apodo 'Mama' fue cambiado por 'Mamita'.")
    else:
        print("\nUPDATE: No se encontró el contacto indicado.")

    conexion.close()


# DELETE: eliminar el contacto con id 2
def eliminar_contacto():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM contactos
        WHERE id_contacto = ?
    """, (2,))

    conexion.commit()

    if cursor.rowcount > 0:
        print("\nDELETE: El contacto con id 2 fue eliminado.")
    else:
        print("\nDELETE: No se encontró el contacto con id 2.")

    conexion.close()


def main():
    print("=== PRÁCTICA CRUD - QUANTUM CORE ===\n")

    crear_tabla_contactos()
    preparar_datos_prueba()

    crear_contactos()

    print("\n--- ESTADO INICIAL: 5 CONTACTOS ---")
    leer_contactos()

    actualizar_contacto()

    print("\n--- DESPUÉS DE ACTUALIZAR ---")
    leer_contactos()

    eliminar_contacto()

    print("\n--- ESTADO FINAL: CONTACTO 2 ELIMINADO ---")
    leer_contactos()

    print("\nPráctica CRUD finalizada correctamente.")


if __name__ == "__main__":
    main()