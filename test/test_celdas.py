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
    for x in range(9):
        for j in range(3):
            if carton1[j][x] == 1:
                contador = contador + 1
                break

    assert contador == 9
