
from src.bingo import sumar
from src.bingo import restar

def test_sumar():
	assert sumar(1,2) == 3
	assert sumar(10,1) == 11

def test_restar():
	assert restar(4,2) == 2
	assert restar(3,1) == 2
