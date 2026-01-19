alumnos = []

while True:
    nombre = input("Introduce el nombre del alumno (o escribe 'fin' para salir): ")
    if nombre.lower().strip() != "fin":
        alumnos.append(nombre)
    else:
        # Salir del bucle cuando se escriba 'fin'
        break

print(f'Lista original: {alumnos}')

# Convertir a lista a set (no duplicados)
alumnos_set = set(alumnos)
print(f'Set (sin duplicados): {alumnos_set}')

# Convertir el set a una tupla (valores fijos)
alumnos_tupla = tuple(alumnos_set)
print(f'Tupla final: {alumnos_tupla}')

# Verificar si existe un alumno
nombre = input("Escribe el nombre del alumno que desea buscar: ")
if nombre in alumnos_tupla:
    print(f'{nombre} se encuentra entre los alumnos')
else:
    print(f'{nombre} no es un alumno')