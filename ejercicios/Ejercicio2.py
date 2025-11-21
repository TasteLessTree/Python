import datetime
import locale
import random

try:
    # Para Linux
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
except locale.Error:
    # Para Windows
    try:
        locale.setlocale(locale.LC_TIME, "Spanish")
    except locale.Error:
        print("Incapaz de localizar locale. Se usa formato por defecto.")

registro_invitados = {}

print("--- REGISTRO DE INVITADOS A LA CENA DE NAVIDAD ---")
i = 1
while i <= 5:
    nombre = input(f'Introduce el nombre del invitado: {i}/5: ')
    fecha = datetime.datetime.now()
    dia = fecha.strftime("%d de %B")
    hora = fecha.strftime("%H:%M:%S")

    print(f'\t-> {nombre} ha sido añadido a las {hora}')

    registro_invitados.update(
        {
            i: {
                "nombre": nombre,
                "dia": dia,
                "hora": hora
            }
        }
    )
    i += 1

print("--- ¡Registro completado! ---")

print("--- LISTA ORDENADA (Por registro) ---")
lista_invitados_ordenada = []

print("--- LISTA DESORDENADA (Sorteo de asientos) ---")
lista_desordenada = lista_invitados_ordenada.copy()
random.shuffle(lista_desordenada)

print("--- ANÁLISIS DE LA LISTA ---")
print(f'Total de invitados apuntados: {len(registro_invitados)}')

datos = registro_invitados.values()