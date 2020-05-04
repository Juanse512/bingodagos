from src.bingo import carton

def test_num_rep():
    carton1 = carton()
    var = [0] * 100
    for columna in range(0,3):
        for fila in range(0,9):
            if carton1[columna][fila] > 0 and carton1[columna][fila] <= 90:
                assert var[carton1[columna][fila]] == 0
                var[carton1[columna][fila]] = var[carton1[columna][fila]] + 1
