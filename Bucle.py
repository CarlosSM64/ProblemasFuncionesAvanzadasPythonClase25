# contador = 1
# while contador < 10:
#     print(contador)
#     contador +=1
    
def contar_vocales(palabra):
    vocales = "aeiou"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador
    
palabra = input("Ingresa una palabra: ").lower()
print("Número de vocales:", contar_vocales(palabra))    
