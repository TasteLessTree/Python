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

def crear_tabla(conn):
    # Crea la tabla de alumnos si no existe
    cursor = conn.cursor()
    # SQLite no tiene tipo BOOL nativo, usa INTEGER (0 o 1). Python lo adapta automáticamente.
    sql = '''
    CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    curso TEXT,
    asignatura TEXT,
    nota REAL,
    aprobado INTEGER
    );
    '''
    cursor.execute(sql)
    conn.commit() # Guardar cambios estructurales

# --- C.R.U.D. OPERATIONS ---
def crear_alumno(conn, alumno):
    """
    (C)REATE: Inserta un nuevo alumno de forma segura.
    alumno: tupla con (nombre, apellidos, curso, asignatura, nota, aprobado)
    """
    sql = ''' INSERT INTO alumnos(nombre, apellidos, curso, asignatura, nota, aprobado)
    VALUES(?,?,?,?,?,?) '''
    cursor = conn.cursor()
    # ¡SEGURIDAD! Pasamos los datos como segundo argumento, no dentro del string SQL
    cursor.execute(sql, alumno)
    conn.commit()
    print(f"Alumno {alumno[0]} guardado con ID: {cursor.lastrowid}")

def leer_alumnos(conn):
    """
    (R)EAD: Lee todos los alumnos.
    """
    sql = "SELECT * FROM alumnos"
    cursor = conn.cursor()
    cursor.execute(sql)
    filas = cursor.fetchall()
    print("\n--- LISTA DE ALUMNOS ---")
    for fila in filas:
        # fila es una tupla: (id, nombre, apellidos, curso, asignatura, nota, aprobado)
        estado = "Aprobado" if fila[6] else "Suspenso"
        print(f"ID: {fila[0]} | {fila[1]} {fila[2]} - Nota: {fila[5]} ({estado})")
    print("------------------------\n")

def actualizar_nota(conn, id_alumno, nueva_nota):
    """
    (U)PDATE: Actualiza la nota y recalcula si está aprobado.
    """
    # Determinamos si aprueba (True si nota >= 5.0)
    nuevo_estado = True if nueva_nota >= 5.0 else False
    sql = ''' UPDATE alumnos
    SET nota = ?,
    aprobado = ?
    WHERE id = ?'''
    cursor = conn.cursor()
    # De nuevo, usamos ? para evitar inyecciones
    cursor.execute(sql, (nueva_nota, nuevo_estado, id_alumno))
    conn.commit()
    print(f"Nota del alumno {id_alumno} actualizada a {nueva_nota}.")

def borrar_alumno(conn, id_alumno):
    """
    (D)ELETE: Borra un alumno por su ID.
    """
    sql = 'DELETE FROM alumnos WHERE id = ?'
    cursor = conn.cursor()
    cursor.execute(sql, (id_alumno,))
    conn.commit()
    print(f"Alumno {id_alumno} eliminado.")

# --- BLOQUE PRINCIPAL DE EJECUCIÓN ---
if __name__ == '__main__':
    # 1. Conexión
    conn = conectar()
if conn:
    # 2. Inicialización
    crear_tabla(conn)
    # 3. CREATE (Insertar datos de prueba)
    # Nota: SQLite almacena True como 1 y False como 0
    crear_alumno(conn, ("Ana", "García", "1º Bach", "Matemáticas", 8.5, True))
    crear_alumno(conn, ("Luis", "Pérez", "1º Bach", "Matemáticas", 5.2, False))
    crear_alumno(conn, ("Rosa", "Pérez", "1º Bach", "Matemáticas", 4.6, False))
    crear_alumno(conn, ("Mateo", "Pérez", "1º Bach", "Matemáticas", 9.7, True))
    crear_alumno(conn, ("Felix", "Pérez", "1º Bach", "Matemáticas", 2.5, False))
    # 4. READ (Leer datos)
    leer_alumnos(conn)
    # 5. UPDATE (Actualizar nota de Luis, ID probable 2)
    # Supongamos que Luis recuperó y sacó un 6
    actualizar_nota(conn, 2, 6.0)
    # 6. DELETE (Borrar a Ana, ID probable 1)
    borrar_alumno(conn, 1)
    # Verificamos estado final
    leer_alumnos(conn)
    # 7. Cerrar conexión (Muy importante)
    conn.close()