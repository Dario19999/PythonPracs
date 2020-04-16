#practica 09
#menendez gomez jose dario
#chavez romo jonathan eduardo

import os
    
#x-------------ejercicio-01--------------x
def e1():
    infinite = [1, 2, 3, 4]
    pTicket = 80
    print("Precio del boleto: $80")
    tDisc1 = 0
    tDisc2 = 0
    tDisc3 = 0
    tDisc4 = 0
    tDisc5 = 0
    cont = 0
    for loop in infinite:
        ans = str(input("Desea comprar un boleto? (s/n) "))
        if(ans == 's'):
            cont = cont + 1
            age = int(input("Ingrese su edad: "))

            if(age < 5):
                print("No se le permite la entrada a menores de 5 años.")
            elif(age >= 5) & (age <= 14):
                disc1 = pTicket*.35
                tDisc1 = tDisc1 + disc1 
                print("El descuento es de: $", disc1)
                print("El boleto costara:$", pTicket - disc1)
            elif(age >= 15) & (age <= 19):
                disc2 = pTicket*.25
                tDisc2 = tDisc2 + disc2
                print("El descuento es de: $", disc2)
                print("El boleto costara: $", pTicket - disc2)
            elif(age >= 20) & (age <= 45):
                disc3 = pTicket*.1
                tDisc3 = tDisc3 + disc3
                print("El descuento es de: $", disc3)
                print("El boleto costara: $", pTicket - disc3)
            elif(age >= 46) & (age <= 65):
                disc4 = pTicket*.25
                tDisc4 = tDisc4 + disc4
                print("El descuento es de: $", disc4)
                print("El boleto costara: $", pTicket - disc4)
            elif(age >= 66) & (age <= 150):
                disc5 = pTicket*.35
                tDisc5 = tDisc5 + disc5
                print("El descuento es de: $", disc5)
                print("El boleto costara: $", pTicket - disc5)
            else:
                print("O usted no ha nacido o ya esta muerto.")
                print("Edad no valida")
        elif(ans == 'n'):
            infinite.clear()
        else:
            print("Datos invalidos")
        infinite.append(loop)
    
    print("\nDinero no percibido en la categoria 1: $", tDisc1)
    print("Dinero no percibido en la categoria 2: $", tDisc2)
    print("Dinero no percibido en la categoria 3: $", tDisc3)
    print("Dinero no percibido en la categoria 4: $", tDisc4)
    print("Dinero no percibido en la categoria 5: $", tDisc5)
    print("\nTotal de dinero no percibido: $", tDisc1+tDisc2+tDisc3+tDisc4+tDisc5)
    print("Total de personas que ingresaron al teatro:", cont)

#x-------------ejercicio-02--------------x
def e2():
    cant = int(input("Cuantos vehiculos hay? "))
    mMt = 0
    mAt = 0
    if( cant == 0):
        print("No hay autos")
    elif(cant < 0):
        print("Datos no validos")
    else:
        for i in range(cant):
            print("El vehiculo", i+1, "es automovil o motocicleta? (a/m) ")
            ans = str(input())

            if(ans == 'a'):
                p = float(input("Ingrese la presion de la llanta: "))
                v = float(input("Ingrese el volumen de la llanta: "))
                t = float(input("Ingrese la temperatura: "))
                if(v == 0.0):
                    print("Datos erroneos")
                else:
                    m = (p*v)/(.37*(t+460))
                    mt = m*4
                    mAt = mAt + mt
                    print("La masa de aire total del vehículo", i+1, "es:",mt)
            elif(ans == 'm'):
                p = float(input("Ingrese la presion de la llanta: "))
                v = float(input("Ingrese el volumen de la llanta: "))
                t = float(input("Ingrese la temperatura: "))
                if(v == 0.0):
                    print("Datos erroneos")
                else:
                    m = (p*v)/(.37*(t+460))
                    mt = m*2     
                    mMt = mMt + mt       
                    print("La masa de aire total del vehículo", i+1, "es:",mt) 

        prom = (mAt+mMt)/cant
        print("\nEl promedio de masa de aire de", cant, "vehiculos es:", prom)

# x-------------ejercicio-03--------------x
def e3():
    cant = int(input("Cuantas gallinas hay? "))
    calT = 0
    if( cant == 0):
        print("No hay gallinas")
    elif(cant < 0):
        print("Datos no validos")
    else:
        for i in range(cant):
            print("Ingrese el peso de la gallina", i+1)
            p = float(input())
            print("Ingrese la altura de la gallina", i+1)
            h = float(input())
            print("Ingrese la cantidad de huevos que pone la gallina", i+1)
            e = int(input())
            if(p <= 0) | (h <= 0) | (e <= 0):
                print("Uno de los datos esta mal. ningun numero puede ser cero")

            calidad = (p*h)/e
            print("\nLa calidad de la gallina", i+1, "es:", calidad)
            calT = calT + calidad

        promCal = calT/cant
        print("\nLa calidad total de sus gallinas es:", calT)
        print("El promedio de calidad de sus gallinas es:", promCal)

        if(calT >= 15):
            pHuevo = 1.2*promCal
        elif(calT > 8) & (calT < 15):
            pHuevo = 1*promCal
        elif(calT <= 8):
            pHuevo = .8*promCal

        print("\nEl precio determinado para el kilo de huevo es:", pHuevo)

#x-------------ejercicio-04--------------x
def e4():#Esta funcion es sobre la encuesta sobre el tratado de libre comercio
    print("x---Tratado de libre comercio---x\n")
    na=0#Variables para las opciones
    ne=0
    ni=0
    contra=100
    for i in range(contra):
        contra=int(input("-Estas en contra o a favor?(si=1/no=2/me abstengo=3)"))
        if contra == 1:
            na=na+1
        elif contra == 2:
            ne=ne+1
        elif contra == 3:
            ni=ni+1        
        cont=int(input(("Desea seguir la encuesta?(1=si/2=no): ")));#Opcion para seguir la encuesta
        if cont == 1:
            contra=int(input("-Estas en contra o a favor?(si=1/no=2/me abstengo=3)"))
        elif cont > 1:
            tdip=na+ne+ni#Suma de todos los diputados
            por=100/tdip#Division para sacara el porcentaje de cada diputado
            print("Numero de diputados encuestados: ",tdip)
            print("Porcentaje de los",na,"diputados a favor: ", na*por,"%")
            print("Porcentaje de los",ne,"diputados en contra: ", ne*por,"%")
            print("Porcentaje de los",ni,"diputados que se abstienen: ", ni*por,"%")

#x-------------ejercicio-05--------------x
def e5():
    num = int(input("Ingrese el numero para la suma regresiva en Hex: "))
    hnums = []
    if(num <= 0):
        print("Datos erroneos. El numero o puede ser igual o menor a 0.")
    else:
        for i in range(num, 0, -2):
            hnums.append(hex(i))
        hnums.append(hex(0))
        print("Secuencia de numeros en hexadecimal hasta 0:")
        print(hnums)

        for j in range(len(hnums)-1):
            hnum1 = int(hnums[j], 16)
            hnum2 = int(hnums[j+1], 16)
            hnums[j+1] = hex(hnum1 + hnum2)

        print("La suma de estos numeros es: ", hnums[-1])

#x-------------ejercicio-06--------------x
def e6():#esta funcion es sobre la captura de las calificaciones sobre programando con python con Profesor Campos
    cant = int(input("Cuantos alumnos desea capturar? "))
    ni=1 #Todas las variabes utilizadas
    f=0
    g= 0
    prom=ni
    if(cant <= 0):
        print("Datos incorrectos")
    else:
        for i in range(cant):
            if(cant <= 0):
                print("Datos incorrectos")
                cant = int(input("Ingrese nuevamente la cantidad de alumnos: "))   
            elif(ni <= cant):
                print("Ingrese las calificaciones del alumno", ni)
                cal = int(input("Calificacion 1: "))
                if(cal < 0) & (cal > 100):
                    print("Calificacion no valida")
                cal2 = int(input("Calificacion 2: "))
                if(cal2 < 0) & (cal2 > 100):
                    print("Calificacion no valida")
                cal3 = int(input("Calificacion 3: "))
                if(cal3 < 0) & (cal3 > 100):
                    print("Calificacion no valida")
                ni = ni+1#Datos para sacar el nunmero de alumno
                prom=(cal+cal2+cal3)/3
                if f < prom:
                    f=prom #Aqui esta para sacar el mejor promedio
                    g=ni-1 #Aqui para sacar cual fue
                print("Su promedio fue: ",prom)       
        print("El promedio del mejor alumno fue: ",f)
        print("El mejor alumno fue el alumno: ",g)

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