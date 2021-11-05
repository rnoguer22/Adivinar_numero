import random
num = random.randint(0,99)   # Numero aleatorio a adivinar

contador = 0   # En esta variable se almacenara el numero de intentos

while num:
    intento = int (input ("Introduzca un numero, entre 0 y 99, ambos incluidos: "))
    if 0 > intento > 99:
        print ("Introduzca un valor entre 0 y 99 por favor: ")
    