from src import bingo

carton1 = bingo.carton()
def test_contar_celdas():
    assert bingo.contar_celdas(carton1)

def test_columnas():
    assert bingo.columnas(carton1)
def test_menor():
    assert bingo.menor(carton1)

def test_mayor():
    assert bingo.mayor(carton1)
