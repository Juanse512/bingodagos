import random
import math
from jinja2 import Template

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





def func():
    while(1 > 0):
        carton1 = intentoCarton()
        if  carton_valido(carton1) == True:
            break
    return carton1;


def tres_x_nueve(carton1):
    countx = 0
    county = 0
    check = True
    for columna in carton1:
        for fila in columna:
            countx = countx + 1
        if countx != 9:
            check = False
        countx = 0
        county = county + 1
    check = check and county == 3
    return check;

def tres_ceros(carton1):
    check = 0
    valid = True
    for columna in range(0,3):
        for fila in range(0,9):
            if carton1[columna][fila] == 0:
                check = check + 1
            else:
                check = 0
            if check >= 3:
                valid = False
                break
        check = 0
    return valid;

def tres_nums(carton1):
    check = 0
    valid = True
    for columna in range(0,3):
        for fila in range(0,9):
            if carton1[columna][fila] != 0:
                check = check + 1
            else:
                check = 0
            if check >= 3:
                valid = False
                break
        check = 0
    return valid;

def num_rep(carton1):
    var = [0] * 100
    ver = True
    for columna in range(0,3):
        for fila in range(0,9):
            if carton1[columna][fila] > 0 and carton1[columna][fila] <= 90:
                if var[carton1[columna][fila]] != 0:
                    ver = False
                var[carton1[columna][fila]] = var[carton1[columna][fila]] + 1
    return ver;

def num_menores_arriba(carton1):
    var = 0
    ver = True
    for fila in range(0,9):
        for num in range(0,3):
            if carton1[num][fila] != 0:
                if var != 0:
                    if var > carton1[num][fila]:
                        ver = False
                var = carton1[num][fila]
        var = 0
    return ver;

def uno_noventa(carton1):
    for fila in range(0,3):
        for columna in range(0,9):
            celda = carton1[fila][columna]
            if celda < 0 or celda > 90:
                return False
    return True

def contar_celdas(carton1):
    contador = 0
    for fila in carton1:
        for celda in fila:
            if celda != 0:
                contador = contador + 1
    return contador == 15

def columnas(carton1):
    contador = 0
    for x in range(9): #Recorro las filas
        for j in range(3): #Recorro las columnas
            if carton1[j][x] != 0: #Si encuentro un carton
                contador = contador + 1  #Sumo 1 al contador
                break #Salgo del for y paso a la otra columna

    return contador == 9

def menor(carton1):
    contador = 0
    for fila in carton1:
        for celda in fila:
            if celda != 0:
                contador = contador + 1

    res = contador < 15
    return res == False

def mayor(carton1):
    contador = 0
    for fila in carton1:
        for celda in fila:
            if celda != 0:
                contador = contador + 1

    res = contador > 15
    return res == False


def fila_menor_derecha(carton1):
    var = 0
    for columna in range(0,3):
        for num in range(0,9):
            if carton1[columna][num] != 0:
                if var != 0:
                    if var >= carton1[columna][num]:
                        return False
                var = carton1[columna][num]
        var = 0
    return True

def filas(c):
    contador = 0
    for x in range(3):
        for j in range(9):
            if c[x][j] != 0:
                contador = contador + 1
                break
    return contador == 3

def diez_en_diez(c):
    com = 1
    fin = 9
    for i in range(9):
        for j in range(3):
            if c[j][i] != 0:
                if c[j][i] < com or c[j][i] > fin:
                    return False;
        com = fin + 1
        fin = fin + 10
    return True;
def carton_valido(carton1):
    if tres_x_nueve(carton1) == True and tres_ceros(carton1) == True and  tres_nums(carton1) == True and  num_rep(carton1) == True and  num_menores_arriba(carton1) == True and  uno_noventa(carton1) == True and  contar_celdas(carton1) == True and  columnas(carton1) == True and  menor(carton1) == True and  mayor(carton1) == True and  fila_menor_derecha(carton1) == True and  filas(carton1) == True and diez_en_diez(carton1) == True:
        return True
    else:
        return False

template = Template(open('plantilla.j2').read())

print(template.render(tabla = func()))
