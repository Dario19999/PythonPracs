#practica 11
#menendez gomez jose dario
#chavez romo jonathan eduardo

from colorama import init, Style, Back, Fore, Cursor
init(autoreset=True)
import os, sys, random
from time import sleep 
from msvcrt import getch

def printInfo():
    print(Cursor.POS(1,1)+Fore.GREEN+"x---------------------------x")
    print(Cursor.POS(1,2)+Fore.GREEN+"practica 11")
    print(Cursor.POS(1,3)+Fore.GREEN+"menendez gomez jose dario")
    print(Cursor.POS(1,4)+Fore.GREEN+"chavez romo jonathan eduardo")
    print(Cursor.POS(1,5)+Fore.GREEN+"x---------------------------x")

def printMenu():
    print(Cursor.POS(1,7)+"[1] Convertir Frase")
    print(Cursor.POS(1,8)+"[S] Salir al menu\n")
    
def initLetts(): #funcion que inicializa las listas que contienen los caracteres para formar las letras
    a = [
        "  ##    ",    
        " #  #   ",   
        "######  ",  
        "#    #  ",  
        "#    #  \n"]
    b = [
        "#####   ",
        "#    #  ",
        "#####   ",
        "#    #  ",
        "#####   \n"]
    c = [       
        " #####  ",
        "#       ",
        "#       ",
        "#       ",
        " #####  \n"]
    d = [
        "#####   ", 
        "#    #  ",
        "#    #  ",
        "#    #  ",
        "#####   \n"]
    e = [
        "######  ",
        "#       ",
        "#####   ",
        "#       ",
        "######  \n"]
    f = [       
        "######  ",
        "#       ",
        "#####   ",
        "#       ",
        "#       \n"]
    g = [
        " #####  ",
        "#       ",
        "#   ##  ",
        "#    #  ",
        " #####  \n"]
    h = [
        "#    #  ",
        "#    #  ",
        "######  ",
        "#    #  ",
        "#    #  \n"]
    i = [ 
        "#####   ",
        "  #     ",
        "  #     ",
        "  #     ",
        "#####   \n"]
    j = [
        " #####  ",
        "   #    ",
        "   #    ",
        "#  #    ",
        " ##     \n"]
    k = [
        "#    #  ",
        "#   #   ",
        "####    ",
        "#   #   ",
        "#    #  \n"]
    l = [
        "#       ",
        "#       ",
        "#       ",
        "#       ",
        "######  \n"]
    m = [
        "#    #  ",
        "##  ##  ",
        "# ## #  ",
        "#    #  ",
        "#    #  \n"]
    n = [
        "#    #  ",
        "##   #  ",
        "# #  #  ",
        "#  # #  ",
        
        "#   ##  \n"]
    nh = [ 
        " ####   ",
        "##   #  ",
        "# #  #  ",
        "#  # #  ",
        "#   ##  \n"]
    o = [
        " ####   ",
        "#    #  ",
        "#    #  ",
        "#    #  ",
        " ####   \n"]
    p =[ 
        "#####   ",
        "#    #  ",
        "#####   ",
        "#       ",
        "#       \n"]
    q = [
        " ####   ",
        "#    #  ",
        "#  # #  ",
        "#   ##  ",
        " #### # \n"]
    r = [
        "#####   ",
        "#    #  ",
        "#####   ",
        "#   #   ",
        "#    #  \n"]
    s = [
        " #####  ",
        "#       ",
        " ####   ",
        "     #  ",
        "#####   \n"]
    t = [ 
        "#####   ",
        "  #     ",
        "  #     ",
        "  #     ",
        "  #     \n"]
    u = [
        "#    #  ",   
        "#    #  ",   
        "#    #  ",   
        "#    #  ",   
        " ####   \n"]
    v = [
        "#    #  ",
        "#    #  ",
        "#    #  ",
        " #  #   ",
        "  ##    \n"]
    w = [
        "#    #  ",
        "#    #  ",
        "#    #  ",
        "# ## #  ",
        "##  ##  \n"]    
    x = [
        "#    #  ",
        " #  #   ",
        "  ##    ",
        " #  #   ",
        "#    #  \n"]
    y = [
        "#    #  ",
        " #  #   ",
        "  ##    ",
        "  #     ",
        " #      \n"]
    z = [
        "#####   ",
        "   #    ",
        "  #     ",
        " #      ",
        "#####   \n"]
    sp = [
	    "     ",
        "     ",
        "     ",
        "     ",
        "     "]

    letters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,nh,o,p,q,r,s,t,u,v,w,x,y,z,sp]    
    return letters

def getPhrase(phrase):#funcion que retorna una lista con las letras de la frase
    
    letters = initLetts()
    newPhrase = []
    
    for i in phrase:
        if(i == "a") | (i == "A"):
            newPhrase.append(letters[0])
        elif(i == "b") | (i == "B"):
            newPhrase.append(letters[1])
        elif(i == "c") | (i == "C"):
            newPhrase.append(letters[2])  
        elif(i == "d") | (i == "D"):
            newPhrase.append(letters[3])
        elif(i == "e") | (i == "E"):
            newPhrase.append(letters[4])
        elif(i == "f") | (i == "F"):
            newPhrase.append(letters[5])
        elif(i == "g") | (i == "G"):
            newPhrase.append(letters[6])
        elif(i == "h") | (i == "H"):
            newPhrase.append(letters[7])
        elif(i == "i") | (i == "I"):
            newPhrase.append(letters[8])
        elif(i == "j") | (i == "J"):
            newPhrase.append(letters[9])
        elif(i == "k") | (i == "K"):
            newPhrase.append(letters[10])
        elif(i == "l") | (i == "L"):
            newPhrase.append(letters[11])
        elif(i == "m") | (i == "M"):
            newPhrase.append(letters[12])
        elif(i == "n") | (i == "N"):
            newPhrase.append(letters[13])
        elif(i == u"ñ") | (i == u"Ñ"):
            newPhrase.append(letters[14])
        elif(i == "o") | (i == "O"):
            newPhrase.append(letters[15])
        elif(i == "p") | (i == "P"):
            newPhrase.append(letters[16])
        elif(i == "q") | (i == "Q"):
            newPhrase.append(letters[17])
        elif(i == "r") | (i == "R"):
            newPhrase.append(letters[18])
        elif(i == "s") | (i == "S"):
            newPhrase.append(letters[19])
        elif(i == "t") | (i == "T"):
            newPhrase.append(letters[20])
        elif(i == "u") | (i == "U"):
            newPhrase.append(letters[21])
        elif(i == "v") | (i == "V"):
            newPhrase.append(letters[22])
        elif(i == "w") | (i == "W"):
            newPhrase.append(letters[23])
        elif(i == "x") | (i == "X"):
            newPhrase.append(letters[24])
        elif(i == "y") | (i == "Y"):
            newPhrase.append(letters[25])
        elif(i == "z") | (i == "Z"):
            newPhrase.append(letters[26])
        elif(i == " "):
            newPhrase.append(letters[27])
    return newPhrase

def printNewPhrase(phrase, shift=0):#funcion que imprime la nueva frase
    os.system('cls')
    printInfo()
    print("\n[S] Salir")
    print("\nSu frase:",phrase) 
    
    dir = ""
    newPhrase = getPhrase(phrase)
    while(dir != 115) & (dir != 83):  
        contP = 0
        contT = 0
        for i in range(len(phrase)):
            color = randColor()
            cont = 0
            for j in newPhrase[i]:		    		    		    
                if(contP >= 120):
                    contP = 0
                    contT = 6
                cont += 1
                if(phrase == "psicodelico"):#easter egg
                        print(Cursor.POS(2+contP,10+cont+contT)+color+j, end="")
                else:
                    if(contP == shift):                  
                        print(Cursor.POS(2+contP,10+cont+contT)+color+j, end="")
                    else:
                        print(Cursor.POS(2+contP,10+cont+contT)+j, end="")
            contP += 8
        if(phrase == "psicodelico"):
            pass
        else:
            changeColor(phrase, shift)

def changeColor(phrase, shift):#funcion que mueve los colores
    dir = ""
    dir = ord(getch())
    
    max = (len(phrase)-1)*8
    if dir == 77:
        if(shift >= max):
            shift = 0
        else:
            shift += 8
        printNewPhrase(phrase, shift)
    if dir == 75:
        if(shift <= 0):
            shift = max
        else:
            shift -= 8
        printNewPhrase(phrase, shift)
    if dir == 115 or dir == 83:
        menu()
        
def randColor():#funcion que retorna un color aleatorio
    colors = {Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN}
    rand = random.randint(0,5)
    
    color = list(colors)[rand]
    
    return color

def menu():#funcion del menu
    os.system('cls')
    printInfo()
    printMenu()
    
    opc = str(input("Ingrese la opcion: "))

    while(opc != "s") & (opc != "S"):
        if(opc == "1"):
            os.system('cls')
            printInfo()
            phrase = str(input("Ingrese su frase: "))
            printNewPhrase(phrase)
            pre = str(input("\nDesea ingresar una nueva frase? (y/n):"))
            if(pre == "y"):
                continue
            elif(pre == "n"):
                opc = "s"
                os.system('cls')
        elif(opc == "s"):
            os.system('cls')
            print("Ha salido del programa...")
            return
        else:        
            os.system('cls')
            printInfo()
            printMenu()
            opc = str(input("Ingrese la opcion: "))
        
    print("Ha salido del programa...")

menu() 
    










    

