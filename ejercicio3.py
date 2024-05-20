def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    
    for letra in frase:
        if letra in vocales:
            contador += 1
    
    return contador

# Solicitar frase al usuario
frase = input("Introduce una frase: ")

numero_vocales = contar_vocales(frase)
print(f"El número de vocales en la frase es: {numero_vocales}")
