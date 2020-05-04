from src.bingo import carton

def test_fila_menor_derecha():
    carton1 = carton()
    var = 0
    for columna in range(0,3):
        for num in range(0,9):
            if carton1[columna][num] != 0:
                if var != 0:
                    assert var < carton1[columna][num]
                var = carton1[columna][num]
        var = 0
