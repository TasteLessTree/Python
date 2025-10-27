"""
Dada las siguiente cadena, sustituye la palabra "canción" por "voz"
"""

cadena = "La canción que se oyó quedó muy bonita"

nueva_cadena = cadena.replace("canción", "voz")
print(cadena)
print(nueva_cadena)

"""
Pedir al usuario que introduzca su nombre y apellidos y los imprima
"""
nombre = input("Escribe tu nombre: ")
apellidos = input("Escribe tus apellidos: ")
print(f'Hola {nombre} {apellidos}, ¿Qué tal estás?')

"""
Escribe un programa que permita adivinar un personaje
De Marvel basado en tres preguntas:
1. ¿Pude volar?
2. ¿Es humano?
3. ¿Tiene máscara?

[ironman, capitana marvel, ronan el acusador, vision, spiderman, hulk, thanos, bolt]
"""

can_fly = True
is_human = True
has_mask = True

print("\n\n[ADIVINAR PERSONAJES DE MARVEL]")
puede_volar = input("¿Puede volar? (s/n): ")

if puede_volar == "s":
    can_fly = True

    es_humano = input("¿Es humano? (s/n): ")

    if es_humano == "s":
        is_human = True

        tiene_mascara = input("¿Tiene máscara? (s/n): ")

        if tiene_mascara == "s":
            has_mask = True
            print("Tu personaje es Ironman")

        else:
            has_mask = False
            print("Tu personaje es Capitana Marvel")

    else:
        is_human = False

        tiene_mascara = input("¿Tiene máscara? (s/n): ")

        if tiene_mascara == "s":
            has_mask = True
            print("Tu personaje es Ronan El Acusador")

        else:
            has_mask = False
            print("Tu personaje es Visión")
else:
    can_fly = False

    es_humano = input("¿Es humano? (s/n): ")

    if es_humano == "s":
        is_human = True

        tiene_mascara = input("¿Tiene máscara? (s/n): ")

        if tiene_mascara == "s":
            has_mask = True
            print("Tu personaje es Spiderman")

        else:
            has_mask = False
            print("Tu personaje es Hulk")

    else:
        is_human = False

        tiene_mascara = input("¿Tiene máscara? (s/n): ")

        if tiene_mascara == "s":
            has_mask = True
            print("Tu personaje es Thanos")

        else:
            has_mask = False
            print("Tu personaje es Bolt")