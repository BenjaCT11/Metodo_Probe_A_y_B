
#Version 1.1.2
print("Version 1.1.2")
print("En esta version se añadio un print() y un archivo style.css")


#import para leer archivos en formato csv
import csv

#impor para operaciones matematicas
import math



#creamos la clase que crea los nodos
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None



#creamos la clase para formar la cabeza de la lista enlazada
class listaEnlazada:
    def __init__(self):
        self.cabeza = None #inicializamos la cabeza en nulo



        # Define una función llamada consultaLista en una clase que representa una lista enlazada
    def consultaLista(self):
        actual = self.cabeza  # Inicializa una variable actual para apuntar al primer nodo de la lista
        while actual is not None:  # Inicia un bucle mientras actual no sea None (es decir, mientras haya nodos en la lista)
            print(actual.dato)  # Imprime el valor almacenado en el nodo actual
            actual = actual.next  # Avanza al siguiente nodo en la lista estableciendo actual en el nodo siguiente
        print("\n") #salto de linea



        # Funcion para insertar nuevos nodos al final de la lista
    def insertarNodoAlFinal(self, valor):
        
        if self.cabeza is None:
            # Si la lista está vacía (la cabeza es None), crea un nuevo nodo con el valor proporcionado.
            nuevoNodo = Nodo(valor)
            # Establece el nuevo nodo como la cabeza de la lista.
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.next is not None:
                actual = actual.next
                # Recorre la lista hasta encontrar el último nodo (cuando el siguiente nodo es None).
            nuevoNodo = Nodo(valor)
            # Crea un nuevo nodo con el valor proporcionado.
            actual.next = nuevoNodo
            # Enlaza el último nodo con el nuevo nodo, extendiendo así la lista.



#funciones para calcular Probe
def calcularProbe(listaX, listaY, n, valorE):

    #creamos nuevas listas para almacenar los resultados
    xCuadrada = listaEnlazada() #valores de X^2
    yCuadrada = listaEnlazada() #valores de Y^2
    xPory = listaEnlazada() #valores de X*Y

    #ubicamos la cabeza de ambas listas
    nodoX = listaX.cabeza
    nodoY = listaY.cabeza

    #Inicializamos variables
    sumaX = 0.0
    sumaY = 0.0
    sumaXCuadrada = 0.0
    sumaYCuadrada = 0.0
    sumaXporY = 0.0

    mediaX = 0.0
    mediaY = 0.0

    
    while nodoX is not None and nodoY is not None:

        # Realiza la operación deseada entre los valores de los nodos y agrega el resultado a la nueva lista
        valor1 = nodoX.dato * nodoY.dato
        valor2 = nodoX.dato**2
        valor3 = nodoY.dato**2


        xPory.insertarNodoAlFinal(valor1) #multiplicamos X*Y
        xCuadrada.insertarNodoAlFinal(valor2) #Elevamos X al cuadrado
        yCuadrada.insertarNodoAlFinal(valor3) #Elevamos Y al cuadrado

        
        #se calculan las sumatorias y la media de X y Y para hacer las operaciones
        sumaX = sumaX + nodoX.dato
        sumaY = sumaY + nodoY.dato
        sumaXCuadrada = sumaXCuadrada + valor2
        sumaYCuadrada = sumaYCuadrada + valor3
        sumaXporY = sumaXporY + valor1
        
        #calculamos la media de los valores de las listas X y Y
        mediaX = sumaX/n
        mediaY = sumaY/n


        # Avanza al siguiente nodo en cada lista
        nodoX = nodoX.next
        nodoY = nodoY.next

    #Calcular el valor de B1 y B0
    parametro1 = sumaXporY - (n * mediaX * mediaY)
    parametro2 = sumaXCuadrada - (n * (mediaX **2) )

    variableB1 = parametro1 / parametro2
    variableB0 = mediaY - variableB1 * mediaX


    #Calcular el valor de r
    parametro1DeR = (n * sumaXporY) - (sumaX * sumaY)
    parametro2DeR = math.sqrt(((n * sumaXCuadrada) - (sumaX **2)) * ((n * sumaYCuadrada) - (sumaY **2)))
    
    variableR = parametro1DeR / parametro2DeR
    variableRCuadrada = variableR **2


    #Calcular el valor de P
    variableP = variableB0 + variableB1 * valorE


    print(" Valor de B1:",variableB1,"\n", "Valor de B0:", variableB0,"\n", "Valor de R:", variableR,"\n","Valor de R^2:", variableRCuadrada,"\n", "Valor de P:", variableP,"\n")
    confiabilidad(variableRCuadrada)


    
def confiabilidad(r2):
    if 0.9 <= r2:
        print( "Confiabilidad Predictiva: Se puede usar con mucha confianza\n")
    elif 0.7 <= r2 < 0.9:
        print( "Confiabilidad Fuerte: Se puede usar para planificar\n")
    elif 0.5 <= r2 < 0.7:
        print( "Confiabilidad Adecuada para planificación, pero usar con precaución\n")
    elif r2 < 0.5:
        print( "No es confiable para fines de planificación\n")
    


#creamos las diferentes listas
miListaA = listaEnlazada() #Tamaño de proxy estimado
miListaB = listaEnlazada() #Tamaño agregado y modificado del plan
miListaC = listaEnlazada() #Tamaño agregado y modificado real
miListaD = listaEnlazada() #Horas de desarrollo real

#Abrimos el archivo csv
with open('C:\\AppServ\\www\\archivos_python\\Metodo Probe\\lecturas.csv', mode='r') as archivo_csv:
    #creamos un lector que leera fila por fila del archivo csv
    lector_csv = csv.reader(archivo_csv)
    
    # Saltar la primera fila (encabezados)
    next(lector_csv)

    valorN = 0 #Esta variable almacenara el valor de "n"
    

    #Iteramos la lectura de las filas (para cada fila en lector_csv)
    for fila in lector_csv:

        #print(fila) #Aqui podremos vizualizar los valores de cada fila y su posicion del archivo csv

        #Agregamos el valor de la fila dependiendo su posicion a una nueva variable para 
        # insertar en el nodo de la lista
        valor_A = float(fila[1])
        valor_B = float(fila[2])
        valor_C = float(fila[3])
        valor_D = float(fila[4])


        # Agrega los valores a las listas enlazadas correspondientes
        miListaA.insertarNodoAlFinal(valor_A) #Tamaño de proxy estimado
        miListaB.insertarNodoAlFinal(valor_B) #Tamaño agregado y modificado del plan
        miListaC.insertarNodoAlFinal(valor_C) #Tamaño agregado y modificado real
        miListaD.insertarNodoAlFinal(valor_D) #Horas de desarrollo real


        valorN +=1 #valor de "n" aumenta dependiendo cuantas filas haya en el archivo csv
    
    




while True:
    print("\nSelecciona una Opcion a calcular:")
    print("1.- Estimacion de Tamaño con Probe A.\n2.- Estimacion de Tamaño con Probe B.\n3.- Estimacion de Tiempo con Probe A.\n4.- Estimacion de Tiempo con Probe B.\n5.- Salir")

    try:
        opcion = int(input("Digite su opcion: "))
        # El código aquí se ejecutará si la entrada del usuario es un número entero válido.

        if opcion == 1:
            # Opción 1: Estimacion de Tamaño con Probe A

            print("\nEstimacion de tamaño con Probe A.")
            valorE = float(input("Digite el valor de E: "))
            print(" ") #Salto de linea

            calcularProbe(miListaA, miListaC, valorN, valorE) #Llamada a la funcion para calcular Probe


            break  # Sale del bucle while después de una opción válida
        elif opcion == 2:
            # Opción 2: Estimacion de Tamaño con Probe B

            print("\nEstimacion de tamaño con Probe B.")
            valorE = float(input("Digite el valor de E: "))
            print(" ") #Salto de linea

            calcularProbe(miListaB, miListaC, valorN, valorE) #Llamada a la funcion para calcular Probe


            break  # Sale del bucle while después de una opción válida
        elif opcion == 3:
            # Opción 3: Tiempo con Probe A

            print("\nEstimacion de Tiempo con Probe A.")
            valorE = float(input("Digite el valor de E: "))
            print(" ") #Salto de linea

            calcularProbe(miListaA, miListaD, valorN, valorE) #Llamada a la funcion para calcular Probe


            break  # Sale del bucle while después de una opción válida
        elif opcion == 4:
            # Opción 4: Tiempo con Probe B

            print("\nEstimacion de Tiempo con Probe A.")
            valorE = float(input("Digite el valor de E: "))
            print(" ") #Salto de linea

            calcularProbe(miListaB, miListaD, valorN, valorE) #Llamada a la funcion para calcular Probe


            break  # Sale del bucle while después de una opción válida
        elif opcion == 5:
            # Opción 5: Salir del programa

            print("Saliendo del programa.")


            break  # Sale del bucle while y termina el programa
        else:

            print("Opción no válida. Por favor, elija un numero del 1 al 4.")
            print("\n")


    except ValueError:
        # El código aquí se ejecutará si el usuario ingresa algo que no puede ser convertido a un número entero.
        print("Entrada inválida. Debe ingresar un número entero (1 al 4).")
        print("\n")
