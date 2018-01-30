from simpleai.search import CspProblem, backtrack, min_conflicts

rey = 1
nada = 0
soldado = 2

ancho = 7
largo = 7

variables = [(x,y) for x in range(ancho) for y in range(largo)]

dominio = {variable: [nada, rey, soldado] for variable in variables}

restricciones = []

def no_adyacentes(variables, valores):
    contador_reyes = 0
    for valor in valores:
        if valor == rey:
            contador_reyes += 1
    return contador_reyes <= 1

def cantidad_valida(variables, valores):
    cantidad_reyes = 0
    cantidad_soldados = 0
    for valor in valores:
        if valor == rey:
            cantidad_reyes += 1
        elif valor == soldado:
            cantidad_soldados += 1
    return cantidad_soldados > cantidad_reyes and cantidad_soldados < cantidad_reyes * 2

for casilla in variables:
    arriba = (casilla[0]-1,casilla[1])
    if arriba[0]<0:
        arriba = (-1,-1)
    abajo = (casilla[0]+1, casilla[1])
    if abajo[0] >= largo:
        abajo = (-1,-1)
    derecha = (casilla[0], casilla[1]+1)
    if derecha[1] >= ancho:
        derecha = (-1,-1)
    izquierda = (casilla[0], casilla[1]-1)
    if izquierda[1] < 0:
        izquierda = (-1,-1)
    restricciones.append(((arriba, abajo, izquierda, derecha), no_adyacentes))

restricciones.append((variables,cantidad_valida))

def imprimir_tablero(resultado):
    print '-'*40
    for fila in range(largo):
        fila_print = ''
        for columna in range(ancho):
            fila_print += '|%i' %resultado[(fila, columna)]
        print fila_print

        print '\n'

print 'Backtrack'
imprimir_tablero(backtrack(CspProblem(variables,dominio,restricciones)))

print 'Min conflicts'
imprimir_tablero(min_conflicts(CspProblem(variables,dominio,restricciones), iterations_limit=5000))