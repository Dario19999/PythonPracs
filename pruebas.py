from msvcrt import getch

while True:
    
    dir = ord(getch())
    
    if dir == 72:
        print("arriba")
    elif dir == 75:
        print("izq")
    elif dir == 77:
        print("der")
    elif dir == 80:
        print("abajo")
    else:
    print(dir)