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
    print(Cursor.POS(1,8)+"[S] Salir \n")
    
def initLetts():
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

def getPhrase(phrase):
    
    letters = initLetts()
    newPhrase = []
    
    for i in phrase:
        if(i == "a") | (i == "A"):
            newPhrase.append(letters[0])
            #return letters[0]
        elif(i == "b") | (i == "B"):
            newPhrase.append(letters[1])
            #return letters[1]
        elif(i == "c") | (i == "C"):
            newPhrase.append(letters[2])  
            #return letters[2]
        elif(i == "d") | (i == "D"):
            newPhrase.append(letters[3])
            #return letters[3]
        elif(i == "e") | (i == "E"):
            newPhrase.append(letters[4])
            #return letters[4]
        elif(i == "f") | (i == "F"):
            newPhrase.append(letters[5])
            #return letters[5]
        elif(i == "g") | (i == "G"):
            newPhrase.append(letters[6])
            #return letters[6]
        elif(i == "h") | (i == "H"):
            newPhrase.append(letters[7])
            #return letters[7]
        elif(i == "i") | (i == "I"):
            newPhrase.append(letters[8])
            #return letters[8]
        elif(i == "j") | (i == "J"):
            newPhrase.append(letters[9])
            #return letters[9]
        elif(i == "k") | (i == "K"):
            newPhrase.append(letters[10])
            #return letters[10]
        elif(i == "l") | (i == "L"):
            newPhrase.append(letters[11])
            #return letters[11]
        elif(i == "m") | (i == "M"):
            newPhrase.append(letters[12])
            #return letters[12]
        elif(i == "n") | (i == "N"):
            newPhrase.append(letters[13])
            #return letters[13]
        elif(i == u"ñ") | (i == u"Ñ"):
            newPhrase.append(letters[14])
            #return letters[14]
        elif(i == "o") | (i == "O"):
            newPhrase.append(letters[15])
            #return letters[15]
        elif(i == "p") | (i == "P"):
            newPhrase.append(letters[16])
            #return letters[16]
        elif(i == "q") | (i == "Q"):
            newPhrase.append(letters[17])
            #return letters[17]
        elif(i == "r") | (i == "R"):
            newPhrase.append(letters[18])
            #return letters[18]
        elif(i == "s") | (i == "S"):
            newPhrase.append(letters[19])
            #return letters[19]
        elif(i == "t") | (i == "T"):
            newPhrase.append(letters[20])
            #return letters[20]
        elif(i == "u") | (i == "U"):
            newPhrase.append(letters[21])
            #return letters[21]
        elif(i == "v") | (i == "V"):
            newPhrase.append(letters[22])
            #return letters[22]
        elif(i == "w") | (i == "W"):
            newPhrase.append(letters[23])
            #return letters[23]
        elif(i == "x") | (i == "X"):
            newPhrase.append(letters[24])
            #return letters[24]
        elif(i == "y") | (i == "Y"):
            newPhrase.append(letters[25])
            #return letters[25]
        elif(i == "z") | (i == "Z"):
            newPhrase.append(letters[26])
            #return letters[26]
        elif(i == " "):
            newPhrase.append(letters[27])
            #return letters[27]
    return newPhrase


def printNewPhrase(phrase):
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
                if(contP == 0):
                    print(Cursor.POS(2+contP,10+cont+contT)+color+j, end="")
                else:
                    print(Cursor.POS(2+contP,10+cont+contT)+j, end="")
            contP += 8
            
        select(phrase, newPhrase)

        
def select(phrase, newPhrase):
    dir = ""
    dir = ord(getch())
    contR = 0
    contL = 0
    contP = 0
    contT = 0
    
    if dir == 77:
        contR += 1
        contP += 8
            
    for k in phrase:
        color = randColor()
        cont = 0
        contP = 0
        contT = 0
        index = phrase.index(k)
        if(index == contR):
            for i in range(len(phrase)):
                color = randColor()
                cont = 0
                for j in newPhrase[i+contR-1]:		    		    		    
                    if(contP >= 120):
                        contP = 0
                        contT = 6
                    cont += 1
                    if(newPhrase.index(newPhrase[i]) == i+contR-1):
                        print(Cursor.POS(2+contP,10+cont+contT)+color+j, end="")
                contP += 8
        else:
            for i in range(len(phrase)):
                color = randColor()
                cont = 0
                for j in newPhrase[i]:		    		    		    
                    if(contP >= 120):
                        contP = 0
                        contT = 6
                    cont += 1 
                    print(Cursor.POS(2+contP,10+cont+contT)+j, end="")
                contP += 8


            
        
        
def randColor():
    colors = {Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE}
    rand = random.randint(0,6)
    
    color = list(colors)[rand]
    
    return color

def menu():
    os.system('cls')
    printInfo()
    printMenu()
    
    opc = str(input("Ingrese la opcion: "))

    while(opc != "s") & (opc != "S"):
        if(opc == "1"):
            os.system('cls')
            printInfo()
            phrase = str(input("Ingrese su frase: "))
            if(phrase.isalpha()):
                printNewPhrase(phrase)
            else:
                print("No se aceptan numeros ni espacios vacios")
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
    










    

