#Algorimo adaptado de:
# https://github.com/vicmagv/bingo-card-generator
import random
import math
def intentoCarton():
    contador = 0
    carton = (
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    )
    numerosCarton = 0

    while (numerosCarton < 15):
      contador = contador + 1
      if (contador == 50):
        return intentoCarton()
      numero = random.randint(1,90)

      columna = math.floor(numero / 10)
      if (columna == 9):
          columna = 8
      huecos = 0
      for i in range(3):
        if (carton[i][columna] == 0):
          huecos = huecos + 1
        if (carton[i][columna] == numero):
          huecos = 0
          break
      if (huecos < 2):
        continue
      fila = 0
      for j in range(3):
        huecos = 0
        for i in range(9):
          if (carton[fila][i] == 0):
              huecos = huecos + 1
        if (huecos < 5 or carton[fila][columna] != 0):
          fila = fila + 1
        else:
          break
      if (fila == 3):
        continue
      carton[fila][columna] = numero
      numerosCarton = numerosCarton + 1
      contador = 0
    for x in range(9):
      huecos = 0
      for y in range(3):
        if (carton[y][x] == 0):
            huecos = huecos + 1
      if (huecos == 3):
        return intentoCarton()
    return carton

def imprimirCarton(carton):
    for columna in range(3):
        for fila in range(9):
            print(carton[columna][fila], end = " ")
        print('\n')


imprimirCarton(intentoCarton())
