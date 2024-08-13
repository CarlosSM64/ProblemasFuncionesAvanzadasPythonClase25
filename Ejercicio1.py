from random import randint

def adivina_el_numero():
    numero_secreto = randint(1,100)
    intentos = 0

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        distancia = abs(numero_secreto - intento)
    
        if intento < numero_secreto:
            if distancia<=10:
                print("Demasiado bajo, pero caliente e intenta de nuevo")
            else:
                print("Demasiado bajo, pero frío e intentalo de nuevo")
        elif intento > numero_secreto:
            if distancia<=10:
                print("Demasiado alto, pero caliente e intentalo de nuevo")
            else:
                print("Demasiado alto, pero frío e intentalo de nuevo")
        else:
            print(f"Ganaste, adivinaste el numero en {intentos} intento/s")
            break
        
adivina_el_numero()
