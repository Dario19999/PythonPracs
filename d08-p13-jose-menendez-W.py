#practica 13
#menendez gomez jose dario
#chavez romo jonathan eduardo

from colorama import init, Style, Back, Fore, Cursor

init(autoreset=True)
import os, sys, subprocess
from msvcrt import getch
from collections import defaultdict

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
    
    print(Cursor.POS(85,13)+Fore.GREEN+"[FLECHA-ARRIBA] Mover Arriba")
    print(Cursor.POS(85,14)+Fore.GREEN+"[FLECHA-ABAJO] Mover Abajo")
    print(Cursor.POS(85,15)+Fore.GREEN+"[ENTER] Seleccionar")                    
    
def newFileSign():        
    print(Cursor.POS(31,3)+Fore.RED+" _____                        ___           _     _            ")
    print(Cursor.POS(31,4)+Fore.RED+"/  __ \                      / _ \         | |   (_)           ")
    print(Cursor.POS(31,5)+Fore.RED+"| /  \/_ __ ___  __ _ _ __  / /_\ \_ __ ___| |__  ___   _____  ")
    print(Cursor.POS(31,6)+Fore.RED+"| |   | '__/ _ \/ _` | '__| |  _  | '__/ __| '_ \| \ \ / / _ \ ")
    print(Cursor.POS(31,7)+Fore.RED+"| \__/\ | |  __/ (_| | |    | | | | | | (__| | | | |\ V / (_) |")
    print(Cursor.POS(31,8)+Fore.RED+" \____/_|  \___|\__,_|_|    \_| |_/_|  \___|_| |_|_| \_/ \___/ ")
                                                               
def editSign():
    print(Cursor.POS(47,2)+Fore.CYAN+"___  ___          _                    _______    _ _ _             ")
    print(Cursor.POS(47,3)+Fore.CYAN+"|  \/  |         | |                  / /  ___|  | (_) |            ")
    print(Cursor.POS(47,4)+Fore.CYAN+"| .  . | ___  ___| |_ _ __ __ _ _ __ / /| |__  __| |_| |_ __ _ _ __ ")
    print(Cursor.POS(47,5)+Fore.CYAN+"| |\/| |/ _ \/ __| __| '__/ _` | '__/ / |  __|/ _` | | __/ _` | '__|")
    print(Cursor.POS(47,6)+Fore.CYAN+"| |  | | (_) \__ \ |_| | | (_| | | / /  | |__| (_| | | || (_| | |   ")
    print(Cursor.POS(47,7)+Fore.CYAN+"\_|  |_/\___/|___/\__|_|  \__,_|_|/_/   \____/\__,_|_|\__\__,_|_|   ")
    
def menuInfo(selected = 1,fore = Fore.GREEN, back = Back.BLACK):
    if(selected == 1):
        print(Cursor.POS(46, 13)+Fore.RED+Back.WHITE+"          Nuevo Archivo         ")
    else:
        print(Cursor.POS(46, 13)+fore+back+"          Nuevo Archivo         ")
    if(selected == 2):
        print(Cursor.POS(46, 15)+Fore.RED+Back.WHITE+"      Mostrar/Editar Archivo    ")
    else:
        print(Cursor.POS(46, 15)+fore+back+"      Mostrar/Editar Archivo    ")
    if(selected == 3):
        print(Cursor.POS(46, 17)+Fore.RED+Back.WHITE+"              Salir             ")
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

def editFrame():
    for superiorL in range(77):
        if(superiorL == 0):
            print(Cursor.POS(3,11)+Fore.CYAN+"╔", end="")
        elif(superiorL == 76):
            print(Cursor.POS(118,11)+Fore.CYAN+"╗")
        else:
            print(Cursor.POS(42+superiorL,11)+Fore.CYAN+"═", end="")
            
    for superiorL2 in range(40):   
        if(superiorL2 == 0):
            print(Cursor.POS(3,2)+Fore.CYAN+"╔", end="")
        elif(superiorL2 == 39):
            print(Cursor.POS(42,2)+Fore.CYAN+"╗")
        else:
            print(Cursor.POS(3+superiorL2,2)+Fore.CYAN+"═", end="") 
             
    for leftL in range(26):
        print(Cursor.POS(3,3+leftL)+Fore.CYAN+"║")
        
    for midL in range(26):
        if(midL == 8):
            print(Cursor.POS(42,11)+Fore.CYAN+"╠")
        else:
            print(Cursor.POS(42,3+midL)+Fore.CYAN+"║")
            
    for inferiorL in range(117):
        if(inferiorL == 0):
            print(Cursor.POS(3,28)+Fore.CYAN+"╚", end="")
        elif(inferiorL == 116):
            print(Cursor.POS(118,28)+Fore.CYAN+"╝")
        elif(inferiorL == 39):
            print(Cursor.POS(42, 28)+Fore.CYAN+"╩")
        else:
            print(Cursor.POS(3+inferiorL,28)+Fore.CYAN+"═", end="")
                        
    for rightL in range(16):
        print(Cursor.POS(118,12+rightL)+Fore.CYAN+"║")

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
    
def newFile(name):
    try:
        if(name.endswith(".txt")):
            newFile = open(name, mode = "x")
        else:
            name = name + ".txt"
            newFile = open(name, mode = "x")
        newFile.close()
        print(Cursor.POS(46, 14)+Fore.GREEN+'Archivo creado exitosamente...')
        print(Cursor.POS(46, 15)+Fore.RED+'Presione una tecla para regresar')
        getch()
        menu()
    except FileExistsError:
        print(Cursor.POS(46, 14)+Fore.RED+'Error: El archivo ya existe...')
        print(Cursor.POS(46, 15)+Fore.RED+'Presione una tecla para regresar')
        getch()
        menu()

def editFile(fileName, txtFiles):
    print(Cursor.POS(43,12)+Fore.CYAN+"Seguro que desea editar el archivo '"+fileName+"'?")
    print(Cursor.POS(43,13)+Fore.CYAN+"Presione ENTER para aceptar o ESC para regresar a la seleccion...")
    
    opc = ord(getch())
    if(opc == 27):
        os.system('cls')
        frame(Fore.CYAN)
        editFrame()
        editSign()
        selectFile(txtFiles)
    elif(opc == 13):
        os.system('cls')
        frame(Fore.CYAN)
        editFrame()
        editSign()
        print(Cursor.POS(43,10)+Fore.CYAN+"[ENTER] Guardar y salir")
        print(Cursor.POS(43,12)+Fore.CYAN+"Escriba el texto que desea agregar al archivo "+fileName)
        subprocess.run('', shell = True)
        print(Cursor.POS(43,13)+Fore.CYAN+"-> \0337")
        newInfo = str(input('\0338'))
        
        thisFile = open(fileName, mode="a", encoding="utf-8")
        thisFile.write(newInfo+" ")
        thisFile.close()
        
        os.system('cls')
        frame(Fore.CYAN)
        editFrame()
        editSign()
        print(Cursor.POS(43,12)+Fore.CYAN+"El archivo '"+fileName+"' ha sido editado correctamente")
        print(Cursor.POS(43,13)+Fore.RED+"Presione ENTER para editar un nuevo archivo o ESC para regresar al menu")
        opc = ord(getch())
        
        if(opc == 13):
            os.system('cls')
            frame(Fore.CYAN)
            editFrame()
            editSign()
            print(Cursor.POS(43,10)+Fore.CYAN+"[ESC] Salir al menu")
            selectFile(txtFiles)
        elif(opc == 27):
            menu()

def selectFile(txtFiles,selected = 0,fore = Fore.CYAN, back = Back.BLACK):

    if(len(txtFiles) == 0):
        print(Cursor.POS(5,4)+Fore.CYAN+"No hay archivos para mostrar")
        print(Cursor.POS(5,5)+Fore.CYAN+"Primero debe crear un archivo")
    else:
        cont = 0
        tab = 0
        for t in txtFiles:
            cont += 1
            if(cont-1 == selected):
                print(Cursor.POS(5+tab,3+cont)+fore+Back.WHITE+t)
            else:
                print(Cursor.POS(5+tab,3+cont)+Fore.CYAN+Back.BLACK+t)
            if(cont == 14):
                cont = 0
                tab += 25
        
def menu():
    os.system('cls')
    frame()
    menuFrame()
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
            menuFrame(Fore.RED)
            newFileSign()
            print(Cursor.POS(46, 11)+Fore.GREEN+'Ingrese el nombre de su archivo: ')
            subprocess.run('', shell = True)
            print(Cursor.POS(46, 12)+Fore.GREEN+'-> \0337')
            name = str(input('\0338'))
            
            newFile(name)
                        
        if(opc == 13) & (step == 2):
            os.system('cls')
            frame(Fore.CYAN)
            editFrame()
            editSign()
            print(Cursor.POS(43,10)+Fore.CYAN+"[ESC] Salir al menu")
            
            files = os.listdir('.')
            txtFiles = []
            for f in files:
                if f.endswith('.txt'):
                    txtFiles.append(f)
            
            step = 0
            selectFile(txtFiles,step)
            
            while(True):
                opc = ord(getch())
                if(opc == 80):
                    if(step == len(txtFiles)-1):
                        step = 0
                    else:
                        step += 1
                    selectFile(txtFiles,step)
                elif(opc == 72):
                    if(step == 0):
                        step = len(txtFiles)-1   
                    else:
                        step -= 1
                    selectFile(txtFiles,step)
                elif(opc == 13):
                    editFile(txtFiles[step], txtFiles)
                elif(opc == 27):
                    menu()
        if(opc == 13) & (step == 3):
            os.system('cls')
            print("Ha salido del programa...")
            os.system('PAUSE')
            exit()
menu()