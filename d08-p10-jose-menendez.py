#practica 10
#menendez gomez jose dario
#chavez romo jonathan eduardo

from colorama import init, Style, Back, Fore, Cursor
init(autoreset=True)
import os, sys
from time import sleep
import msvcrt

def displayInfo():
    print(Cursor.POS(1,1)+Fore.GREEN+"x---------------------------x")
    print(Cursor.POS(1,2)+Fore.GREEN+"practica 10")
    print(Cursor.POS(1,3)+Fore.GREEN+"menendez gomez jose dario")
    print(Cursor.POS(1,4)+Fore.GREEN+"chavez romo jonathan eduardo")
    print(Cursor.POS(1,5)+Fore.GREEN+"x---------------------------x")
    print(Cursor.POS(1,25)+"[1] Cuadrado")
    print(Cursor.POS(1,26)+"[2] Rectangulo")
    print(Cursor.POS(1,27)+"[3] Triangulo")
    print(Cursor.POS(1,28)+"[X] Salir")
    print(Cursor.POS(23,25)+"[W] Arriba")
    print(Cursor.POS(23,26)+"[A] Izquierda")
    print(Cursor.POS(23,27)+"[S] Abajo")
    print(Cursor.POS(23,28)+"[D] Derecha")
	

def printCuadrado(color=Fore.WHITE, contx=0, conty=0, posx=5, posy=10):#funcion que imprime el cuadrado en la nueva posicion
    x = (posx-contx)
    y = (posy-conty)
    for i in range(7):
	    print(Cursor.POS(x, y+i)+color+".............", end="")


def printRectangulo(color=Fore.WHITE, contx=0, conty=0, posx=23, posy=10):#funcion que imprime el rectangulo en la nueva posicion
    x = (posx-contx)
    y = (posy-conty)
    for i in range(7):
	    print(Cursor.POS(x, y+i)+color+"........", end="")

def printTriangulo(color=Fore.WHITE, contx=0, conty=0, posx=35, posy=9):#funcion que imprime el triangulo en la nueva posicion
    x = (posx-contx)
    y = (posy-conty)
    for i in range(8):
	    sp=8-i
	    print(Cursor.POS(x, y+i)+color+" "*sp+". "*i, end="")

def moverCuadrado(color=Fore.WHITE, posxC=5, posyC=10, posxR=0, posyR=0,posxT=0,posyT=0): #funcion que mueve el cuadrado
    dir = ""
    while(dir != "2") & (dir != "3") & (dir != "x"):
	    displayInfo()
	    dir = msvcrt.getwch()
	    if(dir == "w"):
		    posyC += 1
		    os.system("cls")
		    printTriangulo(Fore.YELLOW,posxT,posyT)	
		    printRectangulo(Fore.RED,posxR,posyR)
		    printCuadrado(color,posxC,posyC)
		    
	    elif(dir == "s"):
		    posyC -= 1
		    os.system("cls")
		    printTriangulo(Fore.YELLOW,posxT,posyT)
		    printRectangulo(Fore.RED,posxR,posyR)
		    printCuadrado(color,posxC,posyC)
		    
	    elif(dir == "a"):
		    posxC += 1
		    os.system("cls")
		    printTriangulo(Fore.YELLOW,posxT,posyT)	
		    printRectangulo(Fore.RED,posxR,posyR)
		    printCuadrado(color,posxC,posyC)
		    
	    elif(dir == "d"):
		    posxC -= 1
		    os.system("cls")
		    printTriangulo(Fore.YELLOW,posxT,posyT)
		    printRectangulo(Fore.RED,posxR,posyR)
		    printCuadrado(color,posxC,posyC)
	    elif(dir == "x"):
		    os.system("cls")
		    print("Proceso finalizado...")
		    sys.exit()
	    
		    
    posx = posxC
    posy = posyC
    if(dir == "2"):
	    display(False,"2",contxC=posx,contyC=posy,contxR=posxR,contyR=posyR,contxT=posxT,contyT=posyT)
    elif(dir == "3"):
	    display(False,"3",contxC=posx,contyC=posy,contxR=posxR,contyR=posyR,contxT=posxT,contyT=posyT)
	    
def moverRectangulo(color=Fore.WHITE,posxR=20, posyR=10,posxC=0,posyC=0,posxT=0,posyT=0): #funcion que mueve el rectangulo
    dir = ""
    while(dir != "3") & (dir != "1")& (dir != "x"):
	    displayInfo()
	    dir = msvcrt.getwch()
	    
	    if(dir == "w"):
		    posyR += 1
		    os.system("cls")
		    printTriangulo(Fore.RED,posxT,posyT)					
		    printCuadrado(Fore.YELLOW,posxC,posyC)			
		    printRectangulo(color,posxR,posyR)
	    elif(dir == "s"):
		    posyR -= 1
		    os.system("cls")
		    printTriangulo(Fore.RED,posxT,posyT)					
		    printCuadrado(Fore.YELLOW,posxC,posyC)			
		    printRectangulo(color,posxR,posyR)
	    elif(dir == "a"):
		    posxR += 1
		    os.system("cls")
		    printTriangulo(Fore.RED,posxT,posyT)
		    printCuadrado(Fore.YELLOW,posxC,posyC)			
		    printRectangulo(color,posxR,posyR)		
	    elif(dir == "d"):
		    posxR -= 1
		    os.system("cls")
		    printTriangulo(Fore.RED,posxT,posyT)	
		    printCuadrado(Fore.YELLOW,posxC,posyC)		    
		    printRectangulo(color,posxR,posyR)
	    elif(dir == "x"):
		    os.system("cls")
		    print("Proceso finalizado...")
		    sys.exit()

    posx = posxR
    posy = posyR
    if(dir == "1"):
	    display(False,"1",contxC=posxC,contyC=posyC,contxR=posx,contyR=posy,contxT=posxT,contyT=posyT)
    if(dir == "3"):
	    display(False,"3",contxC=posxC,contyC=posyC,contxR=posx, contyR=posy,contxT=posxT,contyT=posyT)

def moverTriangulo(color=Fore.WHITE, posxT=35,posyT=9,posxC=0,posyC=0, posxR=0, posyR=0): #funcion que mueve el triangulo
    dir = ""
    while(dir != "1") & (dir != "2")& (dir != "x"):
	    displayInfo()
	    dir = msvcrt.getwch()
	    if(dir == "w"):
		    posyT += 1
		    os.system("cls")					
		    printTriangulo(color,posxT,posyT)		
		    printCuadrado(Fore.RED,posxC,posyC)
		    printRectangulo(Fore.YELLOW,posxR,posyR)
	    elif(dir == "s"):
		    posyT -= 1
		    os.system("cls")						
		    printTriangulo(color,posxT,posyT)		
		    printCuadrado(Fore.RED,posxC,posyC)
		    printRectangulo(Fore.YELLOW,posxR,posyR)
	    elif(dir == "a"):
		    posxT += 1
		    os.system("cls")
		    printTriangulo(color,posxT,posyT)		
		    printCuadrado(Fore.RED,posxC,posyC)
		    printRectangulo(Fore.YELLOW,posxR,posyR)		
	    elif(dir == "d"):
		    posxT -= 1
		    os.system("cls")
		    printTriangulo(color,posxT,posyT)		
		    printCuadrado(Fore.RED,posxC,posyC)
		    printRectangulo(Fore.YELLOW,posxR,posyR)
	    elif(dir == "x"):
		    os.system("cls")
		    print("Proceso finalizado...")
		    sys.exit()
    posx = posxT
    posy = posyT		
    if(dir == "1"):
	    display(False,"1",contxC=posxC,contyC=posyC,contxR=posxR,contyR=posyR,contxT=posx,contyT=posy)
    if(dir == "2"):
	    display(False,"2",contxC=posxC,contyC=posyC,contxR=posxR,contyR=posyR,contxT=posx,contyT=posy)


def display(shw=True,fig="",contxC=0,contyC=0,contxR=0,contyR=0,contxT=0,contyT=0):#funcion que cambia los colores de seleccion e imprine las figuras en la posicion actual
    os.system("cls")
    selected = Fore.GREEN
    nonSelectedY = Fore.YELLOW
    nonSelectedR = Fore.RED
    print(fig)
    while(fig != "x"):
	    if(shw == True):#se imprime el menu principal y se captura la seleccion de figura
		    printCuadrado(Fore.WHITE,contxC,contyC)
		    printRectangulo(Fore.WHITE,contxR,contyR)
		    printTriangulo(Fore.WHITE,contxT,contyT)
		    displayInfo()
		    fig = msvcrt.getwch()
	    os.system("cls")
	    if(fig == "1"):#se compara la variable de seleccion de figura para colorear la figura seleccionada y las no seleccionadas
		    printTriangulo(nonSelectedY,contxT,contyT)
		    printCuadrado(selected,contxC,contyC)
		    printRectangulo(nonSelectedR,contxR,contyR)
		    displayInfo()
		    moverCuadrado(selected,contxC,contyC,contxR,contyR,contxT,contyT)
	    elif(fig == "2"):
		    printTriangulo(nonSelectedR,contxT,contyT)
		    printRectangulo(selected,contxR,contyR)
		    printCuadrado(nonSelectedY,contxC,contyC)
		    displayInfo()
		    moverRectangulo(selected,contxR,contyR,contxC,contyC,contxT,contyT)
	    elif(fig == "3"):
		    printTriangulo(selected,contxT,contyT)
		    printRectangulo(nonSelectedY,contxR,contyR)
		    printCuadrado(nonSelectedR,contxC,contyC)
		    displayInfo()
		    moverTriangulo(selected,contxT,contyT,contxC,contyC,contxR,contyR)
    print("Proceso finalizado...")
	
display()


