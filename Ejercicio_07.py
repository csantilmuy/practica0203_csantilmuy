# Escribir un programa que pida al usuario un número entero y muestre por
# pantalla un triángulo rectángulo como el de más abajo, de altura el número
# introducido.
# *
# **
# ***
# ****
# *****
número = int(input("Escribe un número entero: "))
for i in range(1, número + 1):
    print("*" * i)