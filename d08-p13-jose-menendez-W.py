#practica 13
#menendez gomez jose dario
#chavez romo jonathan eduardo

from colorama import init, Style, Back, Fore, Cursor
init(autoreset=True)
import os, sys, subprocess
from msvcrt import getch

def printInfo():
    print(Cursor.POS(47,23)+Fore.RED+"x---------------------------x")
    print(Cursor.POS(55,24)+Fore.RED+"practica 13")
    print(Cursor.POS(48,25)+Fore.RED+"menendez gomez jose dario")
    print(Cursor.POS(47,26)+Fore.RED+"chavez romo jonathan eduardo")
    print(Cursor.POS(47,27)+Fore.RED+"x---------------------------x")
    
def menuSign():
    print(Cursor.POS(50,3)+Fore.GREEN+"___  ___                 ")
    print(Cursor.POS(50,4)+Fore.GREEN+"|  \/  |                 ")
    print(Cursor.POS(50,5)+Fore.GREEN+"| .  . | ___ _ __  _   _ ")
    print(Cursor.POS(50,6)+Fore.GREEN+"| |\/| |/ _ \ '_ \| | | |")
    print(Cursor.POS(50,7)+Fore.GREEN+"| |  | |  __/ | | | |_| |")
    print(Cursor.POS(50,8)+Fore.GREEN+"\_|  |_/\___|_| |_|\__,_|")
                         
def newFileSign():        
    print(Cursor.POS(31,3)+Fore.RED+" _____                        ___           _     _            ")
    print(Cursor.POS(31,4)+Fore.RED+"/  __ \                      / _ \         | |   (_)           ")
    print(Cursor.POS(31,5)+Fore.RED+"| /  \/_ __ ___  __ _ _ __  / /_\ \_ __ ___| |__  ___   _____  ")
    print(Cursor.POS(31,6)+Fore.RED+"| |   | '__/ _ \/ _` | '__| |  _  | '__/ __| '_ \| \ \ / / _ \ ")
    print(Cursor.POS(31,7)+Fore.RED+"| \__/\ | |  __/ (_| | |    | | | | | | (__| | | | |\ V / (_) |")
    print(Cursor.POS(31,8)+Fore.RED+" \____/_|  \___|\__,_|_|    \_| |_/_|  \___|_| |_|_| \_/ \___/ ")
                                                               
def editSign():
    pass

    
    
    
def menuInfo(selected = 1,fore = Fore.GREEN, back = Back.BLACK):
    if(selected == 1):
        print(Cursor.POS(46, 13)+Fore.GREEN+Back.WHITE+"          Nuevo Archivo         ")
    else:
        print(Cursor.POS(46, 13)+fore+back+"          Nuevo Archivo         ")
    if(selected == 2):
        print(Cursor.POS(46, 15)+Fore.GREEN+Back.WHITE+"      Mostrar/Editar Archivo    ")
    else:
        print(Cursor.POS(46, 15)+fore+back+"      Mostrar/Editar Archivo    ")
    if(selected == 3):
        print(Cursor.POS(46, 17)+Fore.GREEN+Back.WHITE+"              Salir             ")
    else:
        print(Cursor.POS(46, 17)+fore+back+"              Salir             ")
    print(Cursor.POS(28,28))
    
def menuFrame(color = Fore.GREEN):
    for superiorL in range(36):
        if(superiorL == 0):
            print(Cursor.POS(44,10)+color+"╔", end="")
        elif(superiorL == 35):
            print(Cursor.POS(79,10)+color+"╗")
        else:
            print(Cursor.POS(44+superiorL,10)+color+"═", end="")
            
    for leftL in range(10):
        print(Cursor.POS(44,11+leftL)+color+"║")

    for inferiorL in range(36):
        if(inferiorL == 0):
            print(Cursor.POS(44,21)+color+"╚", end="")
        elif(inferiorL == 35):
            print(Cursor.POS(79,21)+color+"╝")
        else:
            print(Cursor.POS(44+inferiorL,21)+color+"═", end="")
            
    for rightL in range(10):
        print(Cursor.POS(79,11+rightL)+color+"║")
    
def frame(color = Fore.GREEN):
    for superiorL in range(120):
        if(superiorL == 0):
            print(color+"╔", end="")
        elif(superiorL == 119):
            print(color+"╗")
        else:
            print(color+"═", end="")
            
    for leftL in range(27):
        print(color+"║")

    for inferiorL in range(120):
        if(inferiorL == 0):
            print(color+"╚", end="")
        elif(inferiorL == 119):
            print(color+"╝")
        else:
            print(color+"═", end="")
            
    for rightL in range(27):
        print(Cursor.POS(120,2+rightL)+color+"║")
    
    menuFrame(color)
    
def newFile(name):
    try:
        newFile = open(name, mode = "x")
        print(Cursor.POS(46, 13)+Fore.GREEN+'Archivo creado exitosamente...')
        print(Cursor.POS(46, 15)+Fore.GREEN+'Presione una tecla para ir al menu')
        getch()
        menu()
    except FileExistsError:
        print(Cursor.POS(46, 13)+Fore.GREEN+'Error: El archivo ya existe... \n')
        print(Cursor.POS(46, 15)+Fore.GREEN+'Presione una tecla para ir al menu')
        getch()
        menu()
        
def menu():
    os.system('cls')
    frame()
    printInfo()
    menuSign()
    menuInfo()
    step = 1
    while(True):
        opc = ord(getch())
        if(opc == 80):
            if(step == 3):
                step = 1
            else:
                step += 1
            menuInfo(step)
        elif(opc == 72):
            if(step == 1):
                step = 3     
            else:
                step -= 1
            menuInfo(step)
        
        if(opc == 13) & (step == 1):
            os.system('cls')
            frame(Fore.RED)
            newFileSign()
            print(Cursor.POS(46, 11)+Fore.GREEN+'Ingrese el nombre de su archivo: ')
            subprocess.run('', shell = True)
            print(Cursor.POS(46, 12)+Fore.GREEN+'-> \0337')
            name = input('\0338')
            
            newFile(name)
        if(opc == 13) & (step == 3):
            os.system('cls')
            print("Ha salido del programa...")
            os.system('PAUSE')
            exit()
menu()