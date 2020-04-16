#practica 08
#menendez gomez jose dario
#chavez romo jonathan eduardo

import os 

#x-------------ejercicio-01--------------x
def e1():
    Radio=int(input("Introduzca el Radio de la esfera: "));
    print("\n")
    Area=4*3.1416*(Radio*Radio)
    while Radio <= 0:
        print("ERROR: El radio debe ser mayor que cero.")
        Radio=int(input("Introduzca el Radio de la esfera: "));
    print("El Area de una esfera de", Radio, "es: ",Area)

#x-------------ejercicio-02--------------x
def e2():
    Arista=int(input("Introduzca la arista e un cubo: "));
    N=0
    while Arista > 0:
        print("El volumen del cubo de arista", Arista, "es: ",Arista*Arista*Arista)
        N=N+1
        print("Aristas calculadas: ",N)
        Arista=int(input("Introduzca la arista de un cubo: "));
    print("ERROR: La arista debe ser mayor que 0.")

#x-------------ejercicio-03--------------x
def e3():
    n = int(input("Escriba el numnero de la tabla de multiplicar que desea mostrar: "))
    while(n < 0):
        print("No puede ser una cifra negativa")
        n = int(input("Ingrese nuevamente el numero: "))
    m = n
    while(n >= 0):
        print(m, "x", n, "=", m*n)
        n = n-1

#x-------------ejercicio-04--------------x
def e4():
    cant = int(input("Cuantos numeros desea convertir? "))
    while(cant < 0):
        print("No puede ser una cifra negativa")
        cant = int(input("Ingrese nuevamente la cantidad de numeros: "))    
    nums = [] #arreglo de numeros originales
    nnums =[] #arreglo de numeros simetricos a los originales
    i = 1
    while(i <= cant):
        print("Ingrese el numero", i)
        num = int(input())
        nums.append(num)
        nnums.append(num*-1)#se multiplican los originales por -1 para obtener los simetricos
        i = i+1

    print("Numeros originales:",nums)
    print("Simetricos:", nnums)

#x-------------ejercicio-05--------------x
def e5():
    cant = int(input("Ingrese la cantidad de alumnos: "))
    while(cant < 0):
        print("No puede ser una cifra negativa")
        cant = int(input("Ingrese nuevamente la cantidad de alumnos: "))
    alum = [] #arreglo de alumnos
    alumOrd = [] #arreglo de alumnos ordenado para saber la cal. mayor
    i = 0
    j = 0
    k = 0
    n = 0
    suma = 0 #variable de suma para sacar la media
    while(i < cant):
        print("Ingrese la calificacion del alumno", i+1)
        cal = float(input())
        while(cal < 0) | (cal > 100):
            print("La calificacion no debe ser mayor a 100 ni menor a 0")
            print("Ingrese de nuevo la calificacion del alumno", i+1)
            cal = float(input())
        alum.append(cal) #se agregan las calificaciones a lois arreglos 1 a 1
        alumOrd.append(cal)
        suma = suma+cal
        i = i+1

    print("La media de calificaciones es: ", suma/cant)

    #ordenando arreglo para saber el numero mayor
    while(k < cant-1):
        while(j < cant-1):
            if(alumOrd[j]>alumOrd[j+1]):
                temp = alumOrd[j]
                alumOrd[j] = alumOrd[j+1]
                alumOrd[j+1] = temp
            j = j+1
        k= k+1
    numM = alumOrd[cant-1] #numero mayor
    
    #buscano la posicion del numero mayo en el arreglo no ordenado
    while(n < cant):
        if(alum[n] == numM):
            alumM = n+1
        n = n+1    

    print("El alumno con mayor calificacion es el alumno", alumM, "(",numM,")")

#x-------------ejercicio-06--------------x
def e6():
    cant = int(input("Ingrese la cantidad de vehiculos: "))
    while(cant < 0):
        print("No puede ser una cifra negativa")
        cant = int(input("Ingrese nuevamente la cantidad de vehiculos: "))
    placas = [] #arreglo que contiene las placas ingresadas
    i = 0
    #variables contadoras de calcomanias
    amarillas = 0
    rojas = 0
    rosas = 0
    verdes = 0
    azules = 0
    while(i < cant):
        print("Ingrese las placas (alfanumericas) del vehiculo", i+1)
        placa = str(input())
        placas.append(placa)
        while(placa[-1].isalpha()):#se valida que el ultimo digito sea un numero
            print("Placas erroneas")
            print("Ingrese nuevamente las placas del vehiculo", i+1)
            placa = str(input())
        #comparaciones para aumentar cada color de calcomania
        if(placa[-1] == '1') | (placa[-1] == '2'):
            amarillas = amarillas+1
        elif(placa[-1] == '3') | (placa[-1] == '4'):
            rosas = rosas+1
        elif(placa[-1] == '5') | (placa[-1] == '6'):
            rojas = rojas+1
        elif(placa[-1] == '7') | (placa[-1] == '8'):
            verdes = verdes+1
        elif(placa[-1] == '9') | (placa[-1] == '0'):
            azules = azules+1

        i = i+1

    print("Placas de", cant, "vehiculos:", placas)
    print("Calcomanias amarillas: ", amarillas)
    print("Calcomanias rosas: ", rosas)
    print("Calcomanias rojas: ", rojas)
    print("Calcomanias verdes: ", verdes)
    print("Calcomanias azules: ", azules)

#x-------------ejercicio-07--------------x
def menu():
    opc = ''
    while(opc != 's') & (opc != 'S'):
        print("---------------------------")
        print("practica 08")
        print("menendez gomez jose dario")
        print("chavez romo jonathan eduardo")
        print("---------------------------\n")
        print("-----Menu------")
        print("[1] e1")
        print("[2] e2")
        print("[3] e3")
        print("[4] e4")
        print("[5] e5")
        print("[6] e6")
        print("[s] Salir")
        opc = str(input("Ingrese el numero del ejercicio a evaluar: "))
        os.system('cls')

        if(opc == '1'):
            e1()
            os.system('PAUSE')
            os.system('cls')
        elif(opc == '2'):
            e2()
            os.system('PAUSE')
            os.system('cls')
        elif(opc == '3'):
            e3()
            os.system('PAUSE')
            os.system('cls')
        elif(opc == '4'):
            e4()
            os.system('PAUSE')
            os.system('cls')
        elif(opc == '5'):
            e5()
            os.system('PAUSE')
            os.system('cls')
        elif(opc == '6'):
            e6()            
            os.system('PAUSE')
            os.system('cls')
    os.system('cls')
    print("Usted ha escapado de la simulacion")

menu()