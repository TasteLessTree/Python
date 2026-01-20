# Ejemplo con fastAPI y una mini base de datos
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str
    clave: str

@app.get('/usuarios')
async def get_usuarios() -> dict[str, list[Usuario]] | dict[str, str]:
    try:
        conn = sqlite3.connect('prueba.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        rows = cursor.fetchall()

        usuarios = [
            Usuario(
                id = rows[0],
                nombre = rows[1],
                email = rows[2],
                clave = rows[3],
            )
        ]

        conn.close()
        return {'usuarios': usuarios}
    except sqlite3.OperationalError:
        return {'error': 'Error al abrir la base de datos. No se pudieren obtener los usuarios.'}

@app.get('/usuarios/{id}')
async def get_usuario(id: int) -> dict[str, str]:
    try:
        conn = sqlite3.connect('prueba.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
        row = cursor.fetchone()

        usuario = Usuario(
            id = row[0],
            nombre = row[1],
            email = row[2],
            clave = row[3],
        )

        conn.close()
        return {'usuario': usuario}
    except sqlite3.OperationalError:
        return {'error': f'Error al abrir la base de datos. No se pudo obtener el usuario con id: {id}.'}

"""@app.post('/crear_usuario')
async def crear_usuario(usuario: Usuario):
    try:
        conn = sqlite3.('prueba.db')
        cursor = conn.cursor()

        cursor.execute('''
        ''')"""