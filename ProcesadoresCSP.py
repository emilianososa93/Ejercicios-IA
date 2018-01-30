from simpleai.search import CspProblem, backtrack, min_conflicts
import itertools
Detalle = [(2,10),(5,20),(2,14),(1,1),(2,2),(2,8)]




Variables = [0,1,2,3,4,5]
Procesadores = ['T','G','B']
Dominios = {x : Procesadores
            for x in Variables }

Dominios[2] = ['G']

def controlar_todo(variables, valores):
    contadorRAMT = contadorPROCT = contadorRAMG = contadorPROCG = contadorRAMB =  contadorPROCB = 0
    for var in variables:
        if valores[var] == 'T':
            contadorRAMT += Detalle[var][1]
            contadorPROCT += Detalle[var][0]
        if valores[var] == 'G':
            contadorRAMG += Detalle[var][1]
            contadorPROCG += Detalle[var][0]
        if valores[var]== 'B':
            contadorRAMB += Detalle[var][1]
            contadorPROCB += Detalle[var][0]
    if (((contadorRAMT <= 32) and (contadorPROCT <= 8)) and ((contadorRAMG <= 16) and (contadorPROCG <= 4)) and ((contadorRAMB <= 16) and (contadorPROCB <= 4))):
        return True
    else:
        return False
restricciones = []
restricciones.append(((Variables),controlar_todo))

print 'Backtrack',backtrack(CspProblem(Variables, Dominios, restricciones))
print 'Min Conflicts', min_conflicts(CspProblem(Variables, Dominios, restricciones), iterations_limit=10000)