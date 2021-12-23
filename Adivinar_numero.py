import random
maximo = int (input ("Introzuca el valor maximo del numero aleatorio: "))   # Pedimos al usuario el valor maximo del numero aleatorio
minimo = int (input ("Introzca el valor minimo del numero aleatorio: "))   # Pedimos al usuario el valor minimo dle numero aleatorio
num = random.randint(minimo, maximo)   # Numero aleatorio a adivinar, entre los dos valores que nos ha dado el usuario

contador = 0   # En esta variable se almacenara el numero de intentos

while num:
    intento = int (input ("Introduzca un numero, entre " + str(minimo) + " y " + str(maximo) + " ambos incluidos: "))   # Le pedimos al usuario que introduzca un numero para adivinar el numero aleatorio
    if minimo > intento or intento > maximo:   # Nos aseguramos de que el numero esta comprendido dentro del rango que queremos
        print ("Introduzca un valor entre" + str(minimo) + " y " + str(maximo) + " por favor")
    elif intento < num and maximo > intento > minimo:
        print ("Demasiado pequeño")
        contador += 1
    elif intento > num and maximo > intento > minimo:
        print ("Demasiado grande")
        contador += 1
    elif intento == num and maximo > intento > minimo:
        print ("¡Ha ganado! ✌")
        contador += 1
        num = False   # Cerramos el bucle while
        print ("Ha necesitado ", contador, " intentos para conseguirlo")

# Comentario de prueba