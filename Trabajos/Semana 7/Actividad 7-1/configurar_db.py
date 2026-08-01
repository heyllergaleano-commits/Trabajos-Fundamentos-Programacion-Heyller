import sqlite3

# Crear conexión con la base de datos
conexion = sqlite3.connect("quantum_wallet.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    nit TEXT
)
""")

# Crear tabla wallets
cursor.execute("""
CREATE TABLE IF NOT EXISTS wallets (
    id_wallet INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo REAL NOT NULL DEFAULT 0,
    id_propietario INTEGER,
    FOREIGN KEY (id_propietario)
        REFERENCES usuarios(id_usuario)
)
""")

# Insertar usuarios
cursor.execute("""
INSERT INTO usuarios (nombre, email, nit)
VALUES ('Ana Torres', 'ana@quantum.com', NULL)
""")

cursor.execute("""
INSERT INTO usuarios (nombre, email, nit)
VALUES ('Bancolombia', 'contacto@bancolombia.com', '890903938')
""")

# Insertar wallets
cursor.execute("""
INSERT INTO wallets (saldo, id_propietario)
VALUES (150000.50, 1)
""")

cursor.execute("""
INSERT INTO wallets (saldo, id_propietario)
VALUES (5000000.00, 2)
""")

# Guardar cambios
conexion.commit()

# Mostrar información
print("Base de datos creada correctamente.\n")

cursor.execute("""
SELECT usuarios.nombre, wallets.saldo
FROM usuarios
JOIN wallets
ON usuarios.id_usuario = wallets.id_propietario
""")

for usuario in cursor.fetchall():
    print(f"Usuario: {usuario[0]} - Saldo: ${usuario[1]}")

# Cerrar conexión
conexion.close()