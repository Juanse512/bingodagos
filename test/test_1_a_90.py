from src.bingo import carton

def test_uno_noventa():
    carton1 = carton()
    contador = 0
    for fila in range(0,3):
        for columna in range(0,9):
            celda = carton1[fila][columna]
            assert celda >= 0 and celda <= 90
