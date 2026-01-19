# Ejemplo con fastAPI

from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/calcular/{param1}/{param2}")
async def calcular(param1: int, param2: int) -> int:
    total: int = param1 + param2
    return total