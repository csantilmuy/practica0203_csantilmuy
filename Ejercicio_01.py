# Escribir un programa que almacene la cadena de caracteres contraseña en una
# variable, pregunte al usuario por la contraseña e imprima por pantalla si la
# contraseña introducida por el usuario coincide con la guardada en la
# variable sin tener en cuenta mayúsculas y minúsculas.
contraseña = "pañuelo"
peticióncontraseña = input("Escriba su contraseña: ")
if contraseña == peticióncontraseña.lower():
    print("La contraseña coincide con la guardada")
else:
    print("La contraseña no coincide con la guardada")