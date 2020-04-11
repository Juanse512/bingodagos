from src.bingo import carton

def test_contar_celdas():
    carton1 = carton()
    contador = 0
    for fila in carton1:
        for celda in fila:
            contador = contador + celda

    assert contador == 15
