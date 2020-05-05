from src import bingo

carton1 = bingo.carton()
def test_fila_menor_derecha():
    assert bingo.fila_menor_derecha(carton1)
