num = 4
str1 = "rojo"
str2 = str1
verda = True

print(num, str1, str2, verda)

x = 5
y = 7

#      5 + 7,   5 - 7    5 * 7    7 / 5    7 % 5   7^5
print((x + y), (x - y), (x * y), (y / x), (y % x), (y ** x))

"""
x = int(input("Escribe un número: "))
print(x)
"""

texto = "Este texto es muy bonito"
texto = "Aquel" + texto[4:] # cadena[empiece:final]
print(texto)

# Longitud
print(len(texto))

# Separar por espacios
print(texto.split())

# Tipo de variable
print(type(texto))
print(type(texto.split()))

# Si comienza con "algo"
print(texto.startswith("Este"))

# Encuentra una sub-string
print(texto.find("s m"))

# Devuelve la posición de una sub-string
print(texto.index("muy"))

# Cuenta cuantas veces aparece
print(texto.count("o"))

# Pone cada palabra con mayúscual
print(texto.title())

# Pone cada palabra en minúscula
print(texto.lower())

# Interpolar cadenas
nombre = "Pepito"
edad = 34
print(f'Mi nombre es {nombre} y tengo {edad} años')