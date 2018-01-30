
from simpleai.search import CspProblem, backtrack, min_conflicts
import itertools
variables = [x for x in range(3)]

equipamientos = {
				'Assault cuirass':[0,5000], 
				'Battlefury':[1,500],
				'Cloak':[0,200],
				'Hyperstone':[0,2000],
				'Quelling blade':[0,200],
				'Shadow blade': [0,3000],
				'Veil of discord': [1,2000],
				 }

dominios = {variable: [equipamiento for equipamiento in equipamientos] for variable in variables}

restricciones = []

def no_supera_6000(variables, valores):
	suma = 0
	for valor in valores:
		suma += equipamientos[valor][1]
	return suma < 6000

restricciones.append((variables, no_supera_6000))

def pareja_valida_cartas(valores, carta1, carta2):
	if valores[0] == carta1 and valores[1] == carta2:
		return False
	if valores[0] == carta2 and valores[1] == carta1:
		return False
	return True
	

def no_hyperstone_shadow_blade(variables, valores):
	return pareja_valida_cartas(valores, 'Hyperstone','Shadow blade')	

def no_quelling_shadow(variables, valores):
	return pareja_valida_cartas(valores, 'Quelling blade', 'Shadow blade')

def no_cloak_veil_of_discord(variables, valores):
	return pareja_valida_cartas(valores, 'Cloak', 'Veil of discord')

def items_no_iguales(variables, valores):
	return valores[0]!=valores[1]

for carta_a, carta_b in itertools.combinations(variables, 2):
	restricciones.append(((carta_a, carta_b), no_hyperstone_shadow_blade))
	restricciones.append(((carta_a, carta_b), no_quelling_shadow))
	restricciones.append(((carta_a, carta_b), no_cloak_veil_of_discord))
	restricciones.append(((carta_a, carta_b), items_no_iguales))

def minimo_una_regenera_vida(variables, valores):
	count_regeneran = 0
	for valor in valores:
		if equipamientos[valor][0] == 1:
			count_regeneran += 1
	return count_regeneran > 0

restricciones.append((variables, minimo_una_regenera_vida))

print 'Backtrack',backtrack(CspProblem(variables, dominios, restricciones))
print 'Min Conflicts', min_conflicts(CspProblem(variables, dominios, restricciones), iterations_limit=10000)