from src import bingo
from src import originar_carton
carton1 = originar_carton.intentoCarton()
def test_fila_menor_derecha():
    assert bingo.fila_menor_derecha(carton1)
