from src import bingo
from src import originar_carton
c = originar_carton.intentoCarton()
def test_filas():
    assert bingo.filas(c)
