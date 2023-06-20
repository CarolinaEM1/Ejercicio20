# Hacer un programa donde el usuario digite dos cadenas y el programa indique cuál es la cadena más larga

cadena1 = input("Digite una cadena de caracteres: ")
cadena2 = input("Digite otra cadena de caracteres: ")

if len(cadena1) > len(cadena2):
    print(f"La cadena más larga es: {cadena1}")
elif len(cadena2) > len(cadena1):
    print(f"La cadena más larga es: {cadena2}")
else:
    print("Ambas cadenas son del mismo tamaño")

#Carolina EM


