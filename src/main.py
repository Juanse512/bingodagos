import bingo
import originar_carton


while(1 > 0):
    carton1 = originar_carton.intentoCarton()
    if bingo.tres_x_nueve(carton1) == True and bingo.tres_ceros(carton1) == True and bingo.tres_nums(carton1) == True and bingo.num_rep(carton1) == True and bingo.num_menores_arriba(carton1) == True and bingo.uno_noventa(carton1) == True and bingo.contar_celdas(carton1) == True and bingo.columnas(carton1) == True and bingo.menor(carton1) == True and bingo.mayor(carton1) == True and bingo.fila_menor_derecha(carton1) == True and bingo.filas(carton1) == True:
        originar_carton.imprimirCarton(carton1)
        break
