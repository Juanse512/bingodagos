from src import bingo

carton1 = bingo.carton()

def test_num_rep():
    assert bingo.num_rep(carton1)
