from src import bingo
carton1 = [
    [0,3,2,5,5,5,0,4,91, 0, 12],
    [1,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
carton2 = [
    [1,1,1,1,1,1,1,4,91, 0, 12],
    [1,2,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0]
]
def test_not_num_rep():
    assert not(bingo.num_rep(carton1))
def test_not_filas():
    assert not(bingo.filas(carton1))
def test_not_uno_noventa():
    assert not(bingo.uno_noventa(carton1))

def test_not_contar_celdas():
    assert not(bingo.contar_celdas(carton1))

def test_not_columnas():
    assert not(bingo.columnas(carton1))
def test_not_menor():
    assert not(bingo.menor(carton1))

def test_not_mayor():
    assert not(bingo.mayor(carton2))

def test_not_tres_0():
    assert not(bingo.tres_ceros(carton1))

def test_not_tres_nums():
    assert not(bingo.tres_nums(carton1))

def test_not_tres_por_nueve():
    assert not(bingo.tres_x_nueve(carton1))
def test_not_fila_menor_derecha():
    assert not(bingo.fila_menor_derecha(carton1))
def test_not_num_menores_arriba():
    assert not(bingo.num_menores_arriba(carton1))
def test_not_diez_en_diez():
    assert not(bingo.diez_en_diez(carton1))
def test_not_imprimir_carton():
    assert not(bingo.imprimirCarton(carton1))
