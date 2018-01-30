from simpleai.search import CspProblem, backtrack, min_conflicts
import itertools
variables = [x for x in range(3)]

equipamientos = {
				'a_madera':[1,800], 
				'a_hierro':[1,1000],
				'a_acero':[1,1300],
				'e_madera':[2,500],
				'e_hierro':[2,700],
				'e_acero': [2,1000],
				'g_madera': [2,1300],
				'p_fuego' : [0,1500],
				'p_hielo' : [0,800],
				'p_acido' : [0,1200]
				 }

dominios = {variable: [equipamiento for equipamiento in equipamientos] for variable in variables}

restricciones = []

def no_supera_3000(variables, valores):
	suma = 0
	for valor in valores:
		suma += equipamientos[valor][1]
	return suma < 3000

	

def no_armadura(variables, valores):
	suma1 = 0
	for valor in valores:
		if equipamientos[valor][0] == 1:
			suma1 += 1
	return suma1 ==1 

def no_espadas(variables, valores):
	suma2 = 0
	for valor in valores:
		if equipamientos[valor][0] == 2:
			suma2 += 1
	return suma2 ==1 

restricciones.append((variables, no_armadura))
restricciones.append((variables, no_espadas))
restricciones.append((variables, no_supera_3000))


print 'Backtrack',backtrack(CspProblem(variables, dominios, restricciones))
print 'Min Conflicts', min_conflicts(CspProblem(variables, dominios, restricciones), iterations_limit=10000)