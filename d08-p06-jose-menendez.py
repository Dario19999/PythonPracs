#practica 06
#menendez gomez jose dario
#chavez romo jonathan eduardo
print("---------------------------");
print("practica 06");
print("menendez gomez jose dario");
print("chavez romo jonathan eduardo");
print("---------------------------\n");

#x-------------ejercicio-01--------------x
print("x-------------ejercicio-01--------------x\n")
def e01Mate():
    t1 = 30
    t2 = 75
    t3 = 85

    promExamen = 100*.2
    promTareas = ((t1+t2+t3)/3)*.8
    promFinalM = promExamen + promTareas

    print("materia: matematicas\n")
    print("promedio de examen: ",promExamen)
    print("promedio de tareas: ",promTareas)
    print("promedio final: ",promFinalM,"\n")
    print("x------------------------------------x\n")
    return promFinalM

def e01Fis():
    t1 = 30
    t2 = 75
    t3 = 85

    promExamen = 100*.15
    promTareas = ((t1+t2+t3)/3)*.85
    promFinalF = promExamen + promTareas

    print("materia: fisica\n")
    print("promedio de examen: ",promExamen)
    print("promedio de tareas: ",promTareas)
    print("promedio final: ",promFinalF,"\n")
    print("x------------------------------------x\n")
    return promFinalF

def e01Qui():
    t1 = 30
    t2 = 75
    t3 = 85
    t4 = 30
    t5 = 75
    t6 = 85
    promExamen = 100*.75
    promTareas = ((t1+t2+t3+t4+t5+t6)/6)*.25
    promFinalQ = promExamen + promTareas

    print("materia: quimica\n")
    print("promedio de examen: ",promExamen)
    print("promedio de tareas: ",promTareas)
    print("promedio final: ",promFinalQ,"\n")
    print("x------------------------------------x\n")
    return promFinalQ

def e01PromGeneral():
    promGeneral=(e01Mate()+e01Fis()+e01Qui())/3
    print("promedio general de las 3 materias mas dificiles:\n",promGeneral,"\n")
e01PromGeneral()

#x-------------ejercicio-02--------------x
print("x-------------ejercicio-02--------------x\n")
def e02Inversion():
    capital = 42000
    ganMensual = capital*.033
    print("ganancia mensual: $",ganMensual,"\n")
e02Inversion()

#x-------------ejercicio-03--------------x
print("x-------------ejercicio-03--------------x\n")
def e03Ganancias():
    sueldo = 6000
    v1 = 1500
    v2 = 1600
    v3 = 1850
    v4 = 3700
    v5 = 4700
    v6 = 4500
    v7 = 1000
    v8 = 1400
    v9 = 6700
    v10 = 1500
    comVentas = (v1+v2+v3+v4+v5+v6+v7+v8+v9+v10)*.15
    promComisiones = comVentas/12
    ganMensual = sueldo+promComisiones
    ganAnualT = (sueldo*12)+comVentas

    print("ganancia mensual sin comisiones: $",sueldo)
    print("ganancia mensual con comisiones: $",ganMensual)
    print("ganancia anual por comisiones: $",comVentas)
    print("ganancia anual total: $",ganAnualT,"\n")

e03Ganancias()

#x-------------ejercicio-04--------------x
print("x-------------ejercicio-04--------------x\n")
def e04Descuento():
    tCompra = 3500
    descuento = 3500*.165
    tPagar = tCompra-descuento
    print("total de compra: ",tCompra)
    print("descuento: ", descuento)
    print("total a pagar: ",tPagar,"\n")
e04Descuento()

#x-------------ejercicio-05--------------x
print("x-------------ejercicio-05--------------x\n")
def e05CalAlgoritmos():
    p1 = 100
    p2 = 100
    ef = 100
    tf = 30

    promParciales = ((p1+p2)/2)*.55
    promEf = ef*.3
    promTf = tf*.15
    promFinal = promParciales+promEf+promTf

    print("promedio final:\n", promFinal,"\n")
e05CalAlgoritmos()

#x-------------ejercicio-06--------------x
print("x-------------ejercicio-06--------------x\n")
def e06PromedioHM():
    h = 7
    m = 9
    tAlumnos = h+m
    promH = (h*100)/tAlumnos
    promM = (m*100)/tAlumnos
    print("% de hombres: ",promH,"%")
    print("% de mujeres: ",promM,"%\n")
e06PromedioHM()
