import datetime
import locale

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

i = 1
while i <= 5:
    nombre = input(f'Introdu el nombre del invitado: {i}/5: ')
    ahora = datetime.datetime.now()

    i += 1