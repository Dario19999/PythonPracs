#practica 12
#menendez gomez jose dario
#chavez romo jonathan eduardo

from colorama import init, Style, Back, Fore, Cursor
init(autoreset=True)
import os, sys, random

def printInfo():
    print(Cursor.POS(1,1)+Fore.RED+"x---------------------------x")
    print(Cursor.POS(1,2)+Fore.RED+"practica 12")
    print(Cursor.POS(1,3)+Fore.RED+"menendez gomez jose dario")
    print(Cursor.POS(1,4)+Fore.RED+"chavez romo jonathan eduardo")
    print(Cursor.POS(1,5)+Fore.RED+"x---------------------------x")

def printMenu():
    print(Cursor.POS(1,7)+"[1] Calendario")
    print(Cursor.POS(1,8)+"[S] Salir\n")
    
def printCalendarFrame(year, month):#funcion que imprime el marco del calendario
    os.system('cls')
    for superiorL in range(65):
        if(superiorL == 0):
            print(Fore.RED+"╔", end="")
        elif(superiorL == 64):
            print(Fore.RED+"╗")
        else:
            print(Fore.RED+"═", end="")
            
    for leftL in range(27):
        if(leftL == 0):
            print(Fore.RED+"║")
        elif(leftL == 1):
            print(Fore.RED+"╠")
        elif(leftL == 3):
            print("╠")
        elif(leftL == 7):
            print("╠")
        elif(leftL == 11):
            print("╠")
        elif(leftL == 15):
            print("╠")
        elif(leftL == 19):
            print("╠")
        elif(leftL == 23):
            print("╠")
        else:
            print("║")
            
    for inferiorL in range(65):
        if(inferiorL == 0):
            print("╚", end="")
        elif(inferiorL == 64):
            print("╝")
        else:
            print("═", end="")
            
    for rightL in range(27):
        if(rightL == 0):
            print(Cursor.POS(65,2+rightL)+Fore.RED+"║")
        elif(rightL == 1):
            print(Cursor.POS(65,3)+Fore.RED+"╣")
        elif(rightL == 3):
            print(Cursor.POS(65,5)+"╣")
        elif(rightL == 7):
            print(Cursor.POS(65,9)+"╣")
        elif(rightL == 11):
            print(Cursor.POS(65,13)+"╣")
        elif(rightL == 15):
            print(Cursor.POS(65,17)+"╣")
        elif(rightL == 19):
            print(Cursor.POS(65,21)+"╣")
        elif(rightL == 23):
            print(Cursor.POS(65,25)+"╣")
        else:
            print(Cursor.POS(65,2+rightL)+"║")
    
    colS = 9
    for col in range(6):
        for k in range(26):
            if(k == 25):
                print(Cursor.POS(2+colS,4+k)+"╩")
            else:
                print(Cursor.POS(2+colS,4+k)+"║")
        colS += 9
    rCount = 2
    colS = 9
    colI = 9
    for row in range(6):
        for j in range(63):
            if(j % 9 == 0) & (j != 0) & (row == 0):              
                print(Cursor.POS(2+colS,1+rCount)+Fore.RED+"╦",end="")
                colS += 9
            elif(row == 0):
                print(Cursor.POS(2+j,1+rCount)+Fore.RED+"═",end="")
            if(j % 9 == 0) & (j != 0):
                print(Cursor.POS(2+colI,3+rCount)+"╬",end="")
                colI += 9
            else:
                print(Cursor.POS(2+j,3+rCount)+"═")
        rCount += 4
        colI = 9
        colS = 9
    
    print(Cursor.POS(27,2)+Fore.YELLOW+month)
    print(Cursor.POS(40,2)+Fore.YELLOW+str(year))
    
    print(Cursor.POS(4,4)+Fore.CYAN+"LUNES")
    print(Cursor.POS(13,4)+Fore.CYAN+"MARTES")
    print(Cursor.POS(23,4)+Fore.CYAN+"MIER.")
    print(Cursor.POS(31,4)+Fore.CYAN+"JUEVES")
    print(Cursor.POS(39,4)+Fore.CYAN+"VIERNES")
    print(Cursor.POS(49,4)+Fore.CYAN+"SABADO")
    print(Cursor.POS(58,4)+Fore.CYAN+"DOMINGO")
    print(Cursor.POS(25,25))

def dateCalc(year, month):#funcion que crea los diccionarios, realiza el calculo para determinar en que dia empieza cada mes e imprime los dias en el calendario
    
    monthDict = {
        1 : ['Enero', 31],
        2 : ['Febrero', 28],
        3 : ['Marzo', 31],
        4 : ['Abril', 30],
        5 : ['Mayo', 31],
        6 : ['Junio', 30],
        7 : ['Julio', 31],
        8 : ['Agosto', 31],
        9 : ['Septiembre', 30],
        10 : ['Octubre', 31],
        11 : ['Noviembre', 30],
        12 : ['Diciembre', 31]
    }
    leapMonthDict = { #diccionario de mese para año bisiesto
        1 : ['Enero', 31],
        2 : ['Febrero', 29],
        3 : ['Marzo', 31],
        4 : ['Abril', 30],
        5 : ['Mayo', 31],
        6 : ['Junio', 30],
        7 : ['Julio', 31],
        8 : ['Agosto', 31],
        9 : ['Septiembre', 30],
        10 : ['Octubre', 31],
        11 : ['Noviembre', 30],
        12 : ['Diciembre', 31]
    }
    
    yearDict = {}
    y = 0
    for i in range(1418):
        y = i + 1582
        yearDict[y] = monthDict
        if(y % 4 == 0) | (y % 400 == 0):
            yearDict[y] = leapMonthDict
            
    printCalendarFrame(year, monthDict[month][0])
    
    #aqui empieza el algoritmo para determinar el primer dia de cada mes
    a = 0
    b = 0
    c = 0
    d = 0
    e = 1
    if(year >= 1500) & (year <= 1599):
        a = 9
    elif(year >= 1600) & (year <= 1699):
        a = 7
    elif(year >= 1700) & (year <= 1799):
        a = 5
    elif(year >= 1800) & (year <= 1899):
        a = 3
    elif(year >= 1900) & (year <= 1999):
        a = 1
    elif(year >= 2000) & (year <= 2099):
        a = 0
    elif(year >= 2100) & (year <= 2199):
        a = -2
    
    lastDigits = int((str(year)[2] + str(year)[3]))
    b = (lastDigits//4) + lastDigits
    
    if(month == 1):
        d = 6
    elif(month == 2):
        d = 2
    elif(month == 3):
        d = 2
    elif(month == 4):
        d = 5
    elif(month == 5):
        d = 0
    elif(month == 6):
        d = 3
    elif(month == 7):
        d = 5
    elif(month == 8):
        d = 1
    elif(month == 9):
        d = 4
    elif(month == 10):
        d = 6
    elif(month == 11):
        d = 2
    elif(month == 12):
        d = 4
        
    if((year % 4 == 0) | (year % 400 == 0)) & (year % 100 != 0) & ((month == 1) | (month == 2)):
        c = -1
        
    day = (a + b + c + d + e)

    while(day >= 7):
        day -= 7
    
    selectedMonthDays = yearDict[year][month][1]
    
    #Se imprimen los dias segun el dia de la semana en el que cae
    dateC = 6
    if(day == 1):
        dateR = 8
        for i in range(selectedMonthDays):
            if(dateR == 71):
                dateR = 8
                dateC += 4
            print(Cursor.POS(dateR,dateC)+Fore.YELLOW+Style.BRIGHT+str(i+1), end="")
            dateR += 9
    elif(day == 2):
        dateR = 17
        for i in range(selectedMonthDays):
            if(dateR == 71):
                dateR = 8
                dateC += 4
            print(Cursor.POS(dateR,dateC)+Fore.YELLOW+Style.BRIGHT+str(i+1), end="")
            dateR += 9
    elif(day == 3):
        dateR = 26
        for i in range(selectedMonthDays):
            if(dateR == 71):
                dateR = 8
                dateC += 4
            print(Cursor.POS(dateR,dateC)+Fore.YELLOW+Style.BRIGHT+str(i+1), end="")
            dateR += 9      
    elif(day == 4):
        dateR = 35
        for i in range(selectedMonthDays):
            if(dateR == 71):
                dateR = 8
                dateC += 4
            print(Cursor.POS(dateR,dateC)+Fore.YELLOW+Style.BRIGHT+str(i+1), end="")
            dateR += 9      
    elif(day == 5):
        dateR = 44
        for i in range(selectedMonthDays):
            if(dateR == 71):
                dateR = 8
                dateC += 4
            print(Cursor.POS(dateR,dateC)+Fore.YELLOW+Style.BRIGHT+str(i+1), end="")
            dateR += 9      
    elif(day == 6):
        dateR = 53
        for i in range(selectedMonthDays):
            if(dateR == 71):
                dateR = 8
                dateC += 4
            print(Cursor.POS(dateR,dateC)+Fore.YELLOW+Style.BRIGHT+str(i+1), end="")
            dateR += 9      
    elif(day == 0):
        dateR = 62
        for i in range(selectedMonthDays):
            if(dateR == 71):
                dateR = 8
                dateC += 4
            print(Cursor.POS(dateR,dateC)+Fore.YELLOW+Style.BRIGHT+str(i+1), end="")
            dateR += 9            
    print(Cursor.POS(30,30))
    
def menu():#funcion del menu
    os.system('cls')
    printInfo()
    printMenu()
    
    opc = ""
    while(opc != "s") & (opc != "S"):
        opc = str(input("Ingrese la opcion: "))
        if(opc == "1"):
            os.system('cls')

            year = str(input("Ingrese el a"u"ñ""o: " ))
            while(year.isnumeric() == False):
                if(year.isnumeric() == False):
                    os.system('cls')
                    print("Ingrese numeros solamente")
                    year = str(input("Ingrese el a"u"ñ""o: " ))
            while(int(year) < 1582) | (int(year) > 2999):
                if(int(year) > 2999):
                    os.system('cls')
                    print("El a"u"ñ""o que busca no debe superar al 2999")
                    year = str(input("Ingrese el a"u"ñ""o: " ))           
                elif(int(year) < 1582):
                    os.system('cls')
                    print("El a"u"ñ""o que busca no debe ser menor al 1582")
                    year = str(input("Ingrese el a"u"ñ""o: " ))      

                
            month = str(input("Ingrese el numero de mes (1-12): "))     
            while(month.isnumeric() == False):
                if(month.isnumeric() == False):
                    os.system('cls')
                    print("Ingrese numeros solamente")
                    month = str(input("Ingrese el numero de mes (1-12): "))  
            while(int(month) < 1) | (int(month) > 12):
                if(int(month) < 1) | (int(month) > 12):
                    os.system('cls')
                    print("El mes no debe ser menor a 1 ni mayor a 12")
                    month = str(input("Ingrese el numero de mes (1-12): "))                
                      
            dateCalc(int(year),int(month))
            os.system('PAUSE')
            menu()
        elif(opc == "s"):
            os.system('cls')
            print("Ha salido del programa...")
            exit()
        else:        
            os.system('cls')
            printInfo()
            printMenu()
            opc = str(input("Ingrese la opcion: "))
    os.system('cls')   
    print("Ha salido del programa...")

menu() 