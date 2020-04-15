from src.bingo import carton

def test_contar_celdas():
    carton1 = carton()
    contador = 0
    for fila in carton1:
        for celda in fila:
            contador = contador + celda
    assert contador == 15

def test_columnas():
    carton1 = carton()
    contador = 0
    for x in range(9): #Recorro las filas
        for j in range(3): #Recorro las columnas
            if carton1[j][x] == 1: #Si encuentro un carton
                contador = contador + 1  #Sumo 1 al contador
                break #Salgo del for y paso a la otra columna

    assert contador == 9

def test_menor():
    carton1 = carton()
    contador = 0
    for fila in carton1:
        for celda in fila:
            contador = contador + celda

    res = contador < 15
    assert res == False

def test_mayor():
    carton1 = carton()
    contador = 0
    for fila in carton1:
        for celda in fila:
            contador = contador + celda

    res = contador > 15
    assert res == False
