invitados = []

for i in range(3):
    invitado = input("Escribe el nombre de un invitado: ")
    invitados.append(invitado)

print(invitados)

verificar = input("\n¿A quién quieres buscar en la lista?: ")

if invitados.__contains__(verificar):
    print(f'{verificar} está en la lista')
else:
    print(f'{verificar} no fue invitado')

confirmar = input("\n¿Quieres eliminar a alguien de la lista? (si/no): ")

if confirmar == "si":
    eliminar = input("Escribe el nombre: ")
    invitados.remove(eliminar)
    print(invitados)
else:
    print("Ok")