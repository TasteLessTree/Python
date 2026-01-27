import sqlite3

import fastapi from APIRouter
from pydantic import BaseModel

router = fastapi.APIRouter()

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str
    clave: str

@router.get('/usuarios')
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
        return {'Usuarios': usuarios}
    except sqlite3.OperationalError:
        return {'Error': 'Error al abrir la base de datos. No se pudieren obtener los usuarios.'}

@router.get('/usuario/{id}')
async def get_usuario(user_id: int) -> dict[str, str]:
    try:
        conn = sqlite3.connect('prueba.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
        row = cursor.fetchone()

        if row is None:
            return {'No encontrado': f'No se ha encontrado el usuario con id: {user_id}.'}

        usuario = Usuario(
            id = row[0],
            nombre = row[1],
            email = row[2],
            clave = row[3],
        )

        conn.close()
        return {'Usuario': usuario}
    except sqlite3.OperationalError:
        return {'Error': f'Error al abrir la base de datos. No se pudo obtener el usuario con id: {user_id}.'}

@router.get('/get_usuario')
async def get_usuario(name: str, email: str) -> dict[str, str]:
    try:
        conn = sqlite3.connect('prueba.db')
        cursor = conn.cursor()

        if name is None and email is None:
            return {'Error': 'Por favor, introduzca ambos parámetros.'}

        elif name is not None and email is None:
            cursor.execute('SELECT * FROM usuarios WHERE nombre = ?', (name,))
            row = cursor.fetchone()

            if row is None:
                return {'Error': f'No existen usuarios con el nombre: \'{name}.\''}

        elif name is None and email is not None:
            cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
            row = cursor.fetchone()

            if row is None:
                return {'Error': f'No se ha encontrado el usuario con email: \'{email}\'.'}

        else:
            cursor.execute('SELECT * FROM usuarios WHERE nombre = ? AND email = &', (name, email,))
            row = cursor.fetchone()

            if row is None:
                return {'Error': f'No se han encontrado usuarios con nombre: \'{name}\' y email: \'{email}\'.'}

        usuario = Usuario(
            id = row[0],
            nombre = row[1],
            email = row[2],
            clave = row[3],
        )

        conn.close()
        return {'Usuario': usuario}
    except sqlite3.OperationalError:
        return {'Error': 'Error con la base de datos.'}