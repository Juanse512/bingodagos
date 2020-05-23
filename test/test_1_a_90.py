from src import bingo
from src import originar_carton
carton1 = originar_carton.intentoCarton()
def test_uno_noventa():
    assert bingo.uno_noventa(carton1)
