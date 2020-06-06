[![Build Status](https://travis-ci.com/Juanse512/bingodagos.svg?branch=master)](https://travis-ci.com/Juanse512/bingodagos)
[![Coverage Status](https://coveralls.io/repos/github/Juanse512/bingodagos/badge.svg)](https://coveralls.io/github/Juanse512/bingodagos)
# Bingo

Código en Python que genera un cartón de bingo.
Escrito para Adaptación Del Ambiente De Trabajo, Instituto Politécnico Superior "Gral. San Martín", 2020.
Juan Segundo Valero 6to Info
## Reglas
Se considara un cartón válido al que cumple con las siguientes condiciones:
* Cada carton es una matrix de 3 x 9.
* Los números del carton se encuentran en el rango 1 a 90.
* Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton tiene 15 celdas ocupadas.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* No pueden existir columnas vacias.
* No pueden existir columnas con sus tres celdas ocupadas.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.

## Uso
Para clonar el repositorio:
```
git clone https://github.com/Juanse512/bingodagos.git
```

Para ejecutar el código:
```
python src/bingo.py
```
Nota: para distribuciones basadas en Debian utilizar `python3`

Para más información sobre cómo instalar o actualizar Python visite https://www.python.org/

## Ejemplo de salida
```
$ python src/bingo.py 
0 14 23 0 41 50 0 0 86 

1 0 0 30 48 0 0 79 87 

4 17 0 34 0 57 66 0 0 

```
