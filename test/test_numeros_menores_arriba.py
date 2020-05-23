from src import bingo
from src import originar_carton
carton1 = originar_carton.intentoCarton()
def test_num_menores_arriba():
    assert bingo.num_menores_arriba(carton1)
