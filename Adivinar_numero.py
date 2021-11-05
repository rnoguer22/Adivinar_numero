import random
num = random.randint(0,99)   # Numero aleatorio a adivinar

contador = 0   # En esta variable se almacenara el numero de intentos

while num:
    intento = int (input ("Introduzca un numero, entre 0 y 99, ambos incluidos: "))   # Le pedimos al usuario que introduzca un numero para adivinar el numero aleatorio
    if 0 > intento > 99:   # Nos aseguramos d que el numero esta comprendido dentro del rango que queremos
        print ("Introduzca un valor entre 0 y 99 por favor: ")
    elif intento < num:
        print ("Demasiado pequeño: ")
        contador += 1
    elif intento > num:
        print ("Demasiado grande")
        contador += 1
    else:
        print ("¡Ha ganado! ✌")
        contador += 1
        num = False   # Cerramos el bucle while
        print ("Ha necesitado ", contador, " intentos para conseguirlo")