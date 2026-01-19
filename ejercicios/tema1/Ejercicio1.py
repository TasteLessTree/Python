def analizar_calificaciones(calificaciones):
    # Comprobar si la lista está vacía -> Devolver None
    if len(calificaciones) == 0:
        return {
            "Resultados": None
        }
    
    # Si la lista no esta vacía, se ejecutará este código:

    # La suma de las calificaciones dividida por el número total de calificaciones
    promedio = sum(calificaciones) / len(calificaciones)
    # Redondear para que el promedio sea igual al PDF (redondedear a dos decimales)
    promedio = round(promedio, 2)

    # La calificación más alta
    maxima = max(calificaciones)

    # La calificación más baja
    minima = min(calificaciones)

    # Encontrar el número total de aprobados (calificaciones >= 5)
    aprobados = sum(1 for nota in calificaciones if nota >= 5)

    # Encontrar el número total de suspensos (calificaciones < 5)
    suspendidos = sum(1 for nota in calificaciones if nota < 5)

    return {
        "Promedio": promedio,
        "Máxima": maxima,
        "Mínima": minima,
        "Aprobados": aprobados,
        "Suspendidos": suspendidos
    }
    
# Datos de entrada
notas_clase_a = [8.5, 4.0, 10.0, 7.5, 5.0, 3.0, 9.0, 6.5]
notas_clase_b = [3.5, 4.0, 1.0]
notas_clase_c = []

# Salida
print("--- Clase A ---")
print(f'Notas: {notas_clase_a}')
for key, value in analizar_calificaciones(notas_clase_a).items():
    print(f'{key}: {value}')

# Espacio en blanco
print()

print("--- Clase B ---")
print(f'Notas: {notas_clase_b}')
for key, value in analizar_calificaciones(notas_clase_b).items():
    # Según el PDF, no se tienen que devolver estos valores, así que los ignoramos
    if key == "Máxima" or key == "Mínima" or key == "Suspendidos":
        continue

    print(f'{key}: {value}')

# Espacio en blanco
print()

print("--- Clase C ---")
print(f'Notas: {notas_clase_c}')
for key, value in analizar_calificaciones(notas_clase_c).items():
    print(f'{key}: {value}')