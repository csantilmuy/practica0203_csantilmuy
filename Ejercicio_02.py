# Escribir un programa que pida al usuario dos números y muestre por pantalla
# su división. Si el divisor es cero el programa debe mostrar un error.
dividendo = float(input("Escriba el dividendo: "))
divisor = float(input("Escriba el divisor: "))
if divisor == 0:
    print("Error, el divisor debe ser distinto a 0")
else:
    print(dividendo / divisor)