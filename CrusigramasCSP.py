import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts
import re
text= set(re.sub(r'[^\w] ', '', '''n general, a learning problem considers a set of n samples of data and then tries to predict properties of unknown data. If each sample is more than a single number and, for instance, a multi-dimensional entry (aka multivariate data), it is said to have several attributes or features.
We can separate learning problems in a few large categories:
supervised learning, in which the data comes with additional attributes that we want to predict (Click here to go to the scikit-learn supervised learning page).This problem can be either:
classification: samples belong to two or more classes and we want to learn from already labeled data how to predict the class of unlabeled data. An example of classification problem would be the handwritten digit recognition example, in which the aim is to assign each input vector to one of a finite number of discrete categories. Another way to think of classification is as a discrete (as opposed to continuous) form of supervised learning where one has a limited number of categories and for each of the n samples provided, one is to try to label them with the correct category or class.
regression: if the desired output consists of one or more continuous variables, then the task is called regression. An example of a regression problem would be the prediction of the length of a salmon as a function of its age and weight.
unsupervised learning, in which the training data consists of a set of input vectors x without any corresponding target values. The goal in such problems may be to discover groups of similar examples within the data, where it is called clustering, or to determine the distribution of data within the input space, known as density estimation, or to project the data from a high-dimensional space down to two or three dimensions for the purpose of visualization (Click here to go to the Scikit-Learn unsupervised learning page).
''').lower().split())

 
variables = ['1H','1V','2H','2V','3V','4H','4V','5H','6V','7H','7V','8H','8V','9V', '10H', '11H',]
dominios = {
	'1H':[x for x in text if len(x)==2],
	'1V':[x for x in text if len(x)==2],
	'2V':[x for x in text if len(x)==2],
	'2H':[x for x in text if len(x)==3],
	'3V': [x for x in text if len(x)==3],
	'4H':[x for x in text if len(x)==2],
	'4V':[x for x in text if len(x)==2],
	'5H':[x for x in text if len(x)==2],
	'6V':[x for x in text if len(x)==3],
	'7H':[x for x in text if len(x)==2],
	'7V':[x for x in text if len(x)==2],
	'8H':[x for x in text if len(x)==2],
	'8V':[x for x in text if len(x)==2],
	'9V':[x for x in text if len(x)==2],
	'10H':[x for x in text if len(x)==3],
	'11H':[x for x in text if len(x)==2],
}

restricciones = []

def misma_letra_inicio(variables, valores):
	return valores[0][0]==valores[1][0]

restricciones.append((('1H','1V'), misma_letra_inicio))
restricciones.append((('2V','2H'), misma_letra_inicio))
restricciones.append((('4H','4V'), misma_letra_inicio))
restricciones.append((('8H','8V'), misma_letra_inicio))
restricciones.append((('7H','7V'), misma_letra_inicio))

def son_distintas(variables, valores):
	return valores[0]!=valores[1]

for palabra_a, palabra_b in itertools.combinations(variables,2):
	restricciones.append(((palabra_a,palabra_b),son_distintas))
	
print min_conflicts(CspProblem(variables, dominios,restricciones), iterations_limit=5000)