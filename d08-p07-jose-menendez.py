#practica 07
#menendez gomez jose dario
#chavez romo jonathan eduardo
print("---------------------------")
print("practica 07")
print("menendez gomez jose dario")
print("chavez romo jonathan eduardo")
print("---------------------------\n")

#x-------------ejercicio-01--------------x
print("x-------------ejercicio-01--------------x\n")

def e1():
    cal = int(input("Introduzca su calificacion: "))
    print("\n")

    if (cal > 80) & (cal <= 100):
        print("Aprobado, mijo")
    elif (cal <= 80) & (cal >= 0):
        print("Reprobado, mijo")
    else:
        print("Datos no validos")

#x-------------ejercicio-02--------------x
print("x-------------ejercicio-02--------------x\n")

def e2():
    sueldo = int(input("Ingrese su sueldo: "))
    print("\n")
    print("Su sueldo:", sueldo)

    if(sueldo < 20000) & (sueldo >= 0):
        aumento = sueldo*.30
        sueldo = sueldo+aumento
        print("Su sueldo + aumento del 30%: $", sueldo)
    elif(sueldo <= 23000) & (sueldo >= 0):
        aumento = sueldo*.15
        sueldo = sueldo+aumento   
        print("Su sueldo + aumento del 15%: $", sueldo)   
    elif(sueldo <= 25000) & (sueldo >= 0):
        aumento = sueldo*.05
        sueldo = sueldo+aumento 
        print("Su sueldo + aumento del 5%: $", sueldo)
    elif(sueldo > 25000):
        print("Su sueldo:", sueldo)
        print("No necesita aumento")
    else:
        print("Datos invalidos")

#x-------------ejercicio-03--------------x
print("x-------------ejercicio-03--------------x\n")

def e3():
    horas = int(input("Ingrese las horas trabajadas esta semana: "))
    print("\n")
    sueldoH = 150
    sueldoS = sueldoH*40   
    print("Sueldo por 40 horas trabajadas a la semana: $", sueldoS)

    if(horas > 40) & (horas <= 48):
        horasE = horas - 40
        sueldoE = sueldoH*2*horasE
        sueldoT = sueldoS + sueldoE
        print("Bono por", horasE, "hora(s) extra: $",sueldoE)
        print("Sueldo por", horas, "horas trabajadas esta semana $",sueldoT)
    elif(horas > 48):
        horasTr = horas - 48
        horasE = horas - 40
        sueldoE = (sueldoH*2*8) + (sueldoH*3*horasTr)
        sueldoT = sueldoS + (sueldoH*2*8) + sueldoE
        print("Bono por", horasE, "hora(s) extra: $",sueldoE)
        print("Sueldo por", horas, "horas trabajadas esta semana $",sueldoT)
    elif(horas <= 40) & (horas >=0):
        horasE = 0
        sueldoE = 0
        sueldoT = horas*sueldoH
        print("Bono por", horasE, "hora(s) extra: $",sueldoE)
        print("Sueldo por", horas, "horas trabajadas esta semana $",sueldoT)
    else:
        print("Datos no validos")

#x-------------ejercicio-04--------------x
print("x-------------ejercicio-04--------------x\n")

def e4():
    cantH = int(input("Ingrese la cantidad de hijos que tiene: "))
    cantE = int(input("Ingrese la cantidad de hijos en edad escolar que tiene: "))
    viuda = str(input("La madre de familia es viuda? (s/n): "))
    sub = 0

    if(cantE > cantH):
        print("No puede tener", cantE, "hijos en edad escolar si solo tiene", cantH)
    else:
        if(cantH <= 2) & (cantH >= 0):
            sub = sub + 70
        elif(cantH >= 3) & (cantH <= 5):
            sub = sub + 90    
        elif(cantH >= 6):
            sub = sub + 120

        sub = sub + (cantE*10)

        if(viuda == 's'):
            sub = sub + 20

        print("El total de apoyo para su familia es: $", sub)
#x-------------ejercicio-05--------------x
print("x-------------ejercicio-05--------------x\n")

def e5():
    diaN = int(input("Ingresar dia de nacimiento: "))
    mesN = int(input("Ingresar mes de nacimiento (numero): "))
    añoN = int(input("Ingresar anio de nacimiento: "))
    grado = str(input("Ingrese su grado: "))
    grupo = str(input("Ingrese su grupo: "))
    promedio = int(input("Ingrese su promedio hasta el ultimo semestre: "))
    horario = str(input("Ingrese su horario de preferencia (xx:xx - xx:xx): "))
    print("\n")

    edad = 2020 - añoN

    if(edad > 18) & (promedio >= 60):
        print("Podras formar parte del equipo de natacion en el horario:", horario,)
        print("Fecha de nacimiento:", diaN,"/",mesN,"/",añoN)
        print("Edad: ", edad)
        print("Pomedio: ", promedio)
        print("Grado y grupo:", grado, grupo)
    
    if(edad < 18) & (edad >= 0) | (promedio < 60):
        print("Lo sentimos pero no podras formar parte del equipo de natacion")
        print("Edad: ", edad)
        print("Pomedio: ", promedio)
        print("Edad requerida: 18+")
        print("Promedio requerido: 60+")

#x-------------ejercicio-06--------------x
print("x-------------ejercicio-06--------------x\n")

def e6():
    placas = int(input("Ingrese sus placas (numericas): "))
    millas = int(input("Ingresar millas/h recorridas: "))
    kilometros = int(input("Ingresar kilometros recorridos: "))
    kmGas = int(input("Ingrese los Km. por Lt. de gasolina (10 a 16): "))
    print("\n")
    print("Las placas del auto son:", placas)
    if(millas > 80):
        print("Esta arriba del limite de velocidad")
    elif(millas < 0):
        print("Usted va en reversa")

    if(kilometros > 200) & (kilometros < 350):
        print("Hace falta mantenimiento al auto")
    elif(kilometros < 0):
        print("Dato de kilometros recorridos erroneo")

    if(kmGas >=14) & (kmGas <= 16):
        print("Consume poca gasolina")
    elif(kmGas >=10) & (kmGas <= 13):
        print("Consume algo de gasolina")
    elif(kmGas < 0):
        print("Dato de Km. x Lt. de gasolina erroneo")


#x-------------ejercicio-07--------------x
print("x-------------ejercicio-07--------------x\n")

def e7():
    numJ = int(input("Ingrese el numero del jugador: "))
    anot = int(input("Ingrese los tiros anotados: "))
    fallos = int(input("Ingrese los tiros fallidos: "))
    pts = int(input("Ingrese los puntos marcados: "))
    print("\n")
    totT = anot + fallos

    if(pts >=3) & (pts <= 6):
        print("El jugador", numJ,"Anoto pocos puntos")
    elif(pts >= 7) & (pts <= 15):
        print("El jugador", numJ,"Anoto puntos aceptables")
        tirosTr = pts//3
        print("En promedio anoto", tirosTr, "tiros de 3 puntos")
    elif(pts >= 16) & (pts <= 22):
        print("El jugador", numJ,"Felicidades por sus anotaciones")
        tirosTr = pts/3
        print("En promedio anoto", tirosTr, "tiros de 3 puntos")
    elif(pts < 0):
        print("Dato de puntos erroneo")
    
    print("Tiros anotados:", anot)
    print("Tiros fallidos:", fallos)
    print("Total de tiros:", totT)
    
def grito_de_guerra():
    e4()

grito_de_guerra()