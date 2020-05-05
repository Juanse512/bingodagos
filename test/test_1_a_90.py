from src import bingo

def test_uno_noventa():
    carton1 = bingo.carton()
    assert bingo.uno_noventa(carton1)
