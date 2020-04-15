from src.bingo import carton

def test_filas():
    c = carton()
    contador = 0
    for x in range(3):
        for j in range(9):
            if c[x][j] == 1:
                contador = contador + 1
                break
    assert contador == 3            
