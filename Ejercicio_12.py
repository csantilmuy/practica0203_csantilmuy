# Escribir un programa en el que se pregunte al usuario por una frase y una
# letra, y muestre por pantalla el número de veces que aparece la letra en
# la frase.
frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
veces = frase.count(letra)
print(f"La letra {letra} aparece {veces} veces en la frase")