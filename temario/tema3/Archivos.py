import os

with open("errores.txt", "w") as file:
    file.write("--- INICIO DEL REGISTRO DE ERRORES ---\n")

with open("errores.txt", "a") as file:
    for i in range(3):
        error = input(f'Introduce el error {i+1}/3: ')
        file.write(error + "\n")

    file.write("--- FINAL DEL REGISTRO DE ERRORES ---")

with open("errores.txt", "r") as file:
    contenido = file.read()
    print(contenido)

borrar = input("\n¿Quieres borrar el archivo? (s/n): ")
if borrar == 's':
    os.remove("errores.txt")
    print("Archivo eliminado con éxito")
else:
    print("El archivo se ha conservado")