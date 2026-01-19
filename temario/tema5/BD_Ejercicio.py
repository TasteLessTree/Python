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

def generar_reporte(conn):
    cursor = conn.cursor()

    # Calcular nota media
    cursor.execute("select avg(nota) from alumnos")
    resultado_media = cursor.fetchone()
    media = resultado_media[0] if resultado_media[0] is not None else 0.0

    # Contar aprobados
    cursor.execute("select count(*) from alumnos where aprobado = 1")
    total_aprobado = cursor.fetchone()[0]

    # Contar suspensos
    cursor.execute("select count(*) from alumnos where aprobado = 0")
    total_suspensos = cursor.fetchone()[0]

    # Mostrar resultados
    total_alumnos = total_suspensos + total_aprobado
    print(f'Total de alumnos: {total_alumnos}')
    print('-' * 30)

    print(f'Nota media de la clase: {media:.2f}') # ':.2f' Para mostrar dos decimales
    print(f'Total de aprobados: {total_aprobado}')
    print(f'Total suspensos: {total_suspensos}')

    # EXTRA para calcular el porcentaje de éxito
    if total_alumnos > 0:
        procentaje_aprobados = (total_aprobado / total_alumnos) * 100
        print(f'Porcentaje de éxtio: {procentaje_aprobados:.1f}%')

if __name__ == '__main__':
    conn = conectar()

    if conn:
        generar_reporte(conn)

    conn.close()