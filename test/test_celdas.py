from src import bingo
carton1 = bingo.func()
def test_contar_celdas():
    assert bingo.contar_celdas(carton1)

def test_columnas():
    assert bingo.columnas(carton1)
def test_menor():
    assert bingo.menor(carton1)

def test_mayor():
    assert bingo.mayor(carton1)

def test_tres_0():
    assert bingo.tres_ceros(carton1)

def test_tres_nums():
    assert bingo.tres_nums(carton1)

def test_tres_por_nueve():
    assert bingo.tres_x_nueve(carton1)
