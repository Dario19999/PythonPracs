# from msvcrt import getch
import os
# dir = ord(getch())
# print(dir)
# if dir == 72:
#     print("arriba")
# elif dir == 75:
#     print("izq")
# elif dir == 77:
#     print("der")
# elif dir == 80:
#     print("abajo")


def dateDict():
    os.system('cls')
    monthDict = {
        'enero' : [1, 31],
        'febrero' : [2, 28],
        'marzo' : [3, 31],
        'abril' : [4, 30],
        'mayo' : [5, 31],
        'junio' : [6, 30],
        'julio' : [7, 31],
        'agosto' : [8, 31],
        'septiembre' : [9, 30],
        'octubre' : [10, 31],
        'noviembre' : [11, 30],
        'diciembre' : [12, 31]
    }
    leapMonthDict = {
        'enero' : [1, 31],
        'febrero' : [2, 29],
        'marzo' : [3, 31],
        'abril' : [4, 30],
        'mayo' : [5, 31],
        'junio' : [6, 30],
        'julio' : [7, 31],
        'agosto' : [8, 31],
        'septiembre' : [9, 30],
        'octubre' : [10, 31],
        'noviembre' : [11, 30],
        'diciembre' : [12, 31]
    }
    yearDict = {}
    year = 0
    for i in range(539):
        year = str(i + 1582)
        yearDict[year] = monthDict
        if(int(year) % 4 == 0) | (int(year) % 400 == 0):
            yearDict[year] = leapMonthDict

    print( yearDict["2019"]['febrero'])
    
    
dateDict()