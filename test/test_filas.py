from src import bingo

def test_filas():
    c = bingo.carton()
    assert bingo.filas(c)
