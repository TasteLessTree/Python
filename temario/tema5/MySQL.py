import mysql.connector

CONFIG = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

def conectar_servidor():
    try:
        return mysql.connector.connect(**CONFIG)
    except mysql.connector.Error as error:
        print(f'Error al conectar al servidor: {error}')
        return None

def conectar_basedatos():
    try:
        config_db = CONFIG.copy()
        config_db['database'] = 'escuela'
        return mysql.connector.connect(**config_db)
    except mysql.connector.Error as error:
        print(f'Error al conectar a la base de datos: {error}')
        return None

def inicializar_conexion():
    conexion = conectar_servidor()

    if conexion is not None:
        cursor = conexion.cursor()

        # Crear la base de datos
        cursor.execute('CREATE DATABASE IF NOT EXISTS escuela')

        # Usar la base de datos
        cursor.execute('USE escuela')

        # Crear una tabla
        sql = '''CREATE TABLE IF NOT EXISTS alumnos (id INT AUTO_INCREMENT PRIMARY KEY, 
                 nombre VARCHAR(100) NOT NULL,
                 apellidos VARCHAR(100) NOT NULL,
                 curso VARCHAR(50),
                 asignatura VARCHAR(100),
                 nota FLOAT,
                 aprobado BOOLEAN,
                 )'''
        cursor.execute(sql)
        print("Base de datos y tablas verificadas")
        cursor.close()

# Operaciones CRUD
def crear_alumno(alumno):
    conexion = conectar_basedatos()

    if conexion is not None:
        cursor = conexion.cursor()
        sql = '''INSERT INTO alumnos (nombre, apellidos, curso, asignatura, nota, aprobado) VALUES (%s, %s, %s, %s, %s, %s)'''

        try:
            cursor.execute(sql, alumno)
            conexion.commit()
            print(f'Alumno: {alumno[0]} creado. ID: {cursor.lastrowid}')
        except mysql.connector.Error as error:
            print(f'Error al crear alumno: {error}')
        finally:
            cursor.close()
            conexion.close()

def leer_alumnos():
    conexion = conectar_basedatos()

    if conexion is not None:
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM alumnos')

        filas = cursor.fetchall()

        print(f'Listando MySQL')
        for fila in filas:
            # fila -> id, nombre, apellidos, curso, asignatura, nota, aprobado (1 -> true o 0 -> false)
            estado = "Aprobado" if fila[6] == 1 else "Suspenso"
            print(f'ID: {fila[0]} |\n\t{fila[1]} {fila[2]} {fila[3]} |\n\t - Nota: {fila[5]} - [{estado}]')
        print('-' * 30)
        cursor.close()
        conexion.close()

def actualizar_nota(id_alumno, nueva_nota):
    conexion = conectar_basedatos()

    if conexion is not None:
        cursor = conexion.cursor()

        es_aprobado = True if nueva_nota >= 5.0 else False

        sql = '''UPDATE alumnos SET nota = %s, aprobado = %s WHERE id = %s'''
        cursor.execute(sql, (nueva_nota, es_aprobado, id_alumno))
        conexion.commit()
        print(f'Nota actualizada para ID {id_alumno}')
        cursor.close()
        conexion.close()


def borrar_alumno(id_alumno):
    conexion = conectar_basedatos()

    if conexion is not None:
        cursor = conexion.cursor()
        sql = '''DELETE FROM alumnos WHERE id = %s'''
        cursor.execute(sql, (id_alumno,))
        conexion.commit()
        print(f'Alumno borrada con ID {id_alumno}')
        cursor.close()
        conexion.close()

# Ejecución
if __name__ == "__main__":
    # 1. Preparar el terreno (Crear DB si es la primera vez)
    inicializar_conexion()
    # 2. Insertar datos (CREATE)
    # Nota: MySQL maneja True/False como 1/0, pero Python lo convierte automáticamente
    crear_alumno(("Carlos", "Ruiz", "3º ESO", "Historia", 4.5, False))
    crear_alumno(("Elena", "Nito", "3º ESO", "Historia", 9.2, True))
    # 3. Leer (READ)
    leer_alumnos()
    # 4. Actualizar (UPDATE) - Supongamos que Carlos hizo un trabajo extra
    actualizar_nota(1, 5.0)  # Asumimos que Carlos es el ID 1
    # 5. Borrar (DELETE) - Borramos a Elena (ID 2)
    borrar_alumno(2)
    # Ver final
    leer_alumnos()