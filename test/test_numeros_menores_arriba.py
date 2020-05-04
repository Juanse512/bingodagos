from src.bingo import carton

def test_num_menores_arriba():
    carton1 = carton()
    var = 0
    for fila in range(0,9):
        for num in range(0,3):
            if carton1[num][fila] != 0:
                if var != 0:
                    assert var < carton1[num][fila]
                var = carton1[num][fila]
        var = 0
