import sqlite3

def conectar():
    # Conecta a la base de datos (crea el archivo si no existe)
    try:
        # Esto creará un archivo 'escuela.db' en la misma carpeta
        conn = sqlite3.connect('escuela.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error conectando: {e}")
        return None

