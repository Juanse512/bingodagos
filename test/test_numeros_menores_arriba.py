from src import bingo

def test_num_menores_arriba():
    carton1 = bingo.carton()
    assert bingo.num_menores_arriba(carton1)
