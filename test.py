
"""Ce fichier permet de faire des tests sur le programme"""

# Les modules externe
from matplotlib.pylab import *

# Mes modules
import perceptron
import generate_data

# On met les coordonnées dans des tableaux
# Les inputs_train sont les coordonnées sur lesquels notre programme va apprendre
inputs_train = generate_data.generateData(80)
# Les inputs_work sont les coordonnées sur lesquels notre programme va s'exercer
inputs_work = generate_data.generateData(20)

# On va créer notre perceptron
p = perceptron.perceptron

# On entraîne notre perceptron avec les inputs_train
p.train(inputs_train)

# On test ensuite ses capacitées à travailler seul
p.test(inputs_work)

# On affiche ensuite les résultats sur un graphique
