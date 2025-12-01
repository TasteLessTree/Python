import json

datos_json = """
[
{"id": 1, "nombre": "Laptop", "precio": 1000.0, "stock": 5},
{"id": 2, "nombre": "Ratón", "precio": 25.0, "stock": 10},
{"id": 3, "nombre": "Teclado", "precio": 45.0, "stock": 15}
]
"""

datos = json.loads(datos_json)
print(f'--- 1. Recibiendo datos JSON ---')
print(f'Tipo de dato convertido: {type(datos)}')
print(f'Productos actuales: {len(datos)}')

print(f'--- 2. Modificando datos ---')
for item in datos:
    if item["nombre"] == "Laptop":
        item["precio"] = item["precio"] - 100 # Reducir un 10 por ciento
        print(f'Precio de Laptop actualizado: 1000.0 -> 900.0')

    elif item["nombre"] == "Ratón":
        item["stock"] = 0
        item.update({"disponible": False}) # Añadir una nueva clave
        print(f'El Ratón se ha marcado como agotado.')

print(f'--- 3. Añadiendo producto ---')
auriculares = {
    "id": 4,
    "nombre": "Auriculares",
    "precio": 50.0,
    "stock": 20
}
datos.append(auriculares)
print(f'Auriculares añadidos al inventario.')

print(f'--- 4. Generando nuevo JSON ---')
nuevo_json = json.dumps(datos, indent=4, sort_keys=True, ensure_ascii=False)
print(nuevo_json)