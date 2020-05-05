
def carton():
    carton = (
        (1,0,2,3,4,0,5,0,6),
        (0,7,8,9,0,10,11,12,0),
        (13,14,0,0,15,0,0,0,0)
    )
    return carton;

def num_rep(carton1):
    var = [0] * 100
    ver = True
    for columna in range(0,3):
        for fila in range(0,9):
            if carton1[columna][fila] > 0 and carton1[columna][fila] <= 90:
                if var[carton1[columna][fila]] != 0:
                    ver = False
                var[carton1[columna][fila]] = var[carton1[columna][fila]] + 1
    return ver;

def num_menores_arriba(carton1):
    var = 0
    ver = True
    for fila in range(0,9):
        for num in range(0,3):
            if carton1[num][fila] != 0:
                if var != 0:
                    if var > carton1[num][fila]:
                        ver = False
                var = carton1[num][fila]
        var = 0
    return ver;

def uno_noventa(carton1):
    for fila in range(0,3):
        for columna in range(0,9):
            celda = carton1[fila][columna]
            if celda < 0 or celda > 90:
                return False
    return True

def contar_celdas(carton1):
    contador = 0
    for fila in carton1:
        for celda in fila:
            if celda != 0:
                contador = contador + 1
    return contador == 15

def columnas(carton1):
    contador = 0
    for x in range(9): #Recorro las filas
        for j in range(3): #Recorro las columnas
            if carton1[j][x] != 0: #Si encuentro un carton
                contador = contador + 1  #Sumo 1 al contador
                break #Salgo del for y paso a la otra columna

    return contador == 9

def menor(carton1):
    contador = 0
    for fila in carton1:
        for celda in fila:
            if celda != 0:
                contador = contador + 1

    res = contador < 15
    return res == False

def mayor(carton1):
    contador = 0
    for fila in carton1:
        for celda in fila:
            if celda != 0:
                contador = contador + 1

    res = contador > 15
    return res == False

from src.bingo import carton

def fila_menor_derecha(carton1):
    var = 0
    for columna in range(0,3):
        for num in range(0,9):
            if carton1[columna][num] != 0:
                if var != 0:
                    if var >= carton1[columna][num]:
                        return False
                var = carton1[columna][num]
        var = 0
    return True

def filas(c):
    contador = 0
    for x in range(3):
        for j in range(9):
            if c[x][j] != 0:
                contador = contador + 1
                break
    return contador == 3
