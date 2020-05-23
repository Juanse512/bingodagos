from src import bingo
from src import originar_carton
carton1 = originar_carton.intentoCarton()

def test_num_rep():
    assert bingo.num_rep(carton1)
