
"""Ce fichier permet de faire des tests sur le programme perceptron.py"""

# Mes modules
import perceptron
import generate_data

# On met les coordonnées dans des tableaux
# Les inputs_train sont les coordonnées sur lesquels notre programme va apprendre
INPUTS_TRAIN = generate_data.generate_data(500, -100, 100)
# Les inputs_work sont les coordonnées sur lesquels notre programme va s'exercer
INPUTS_WORK = generate_data.generate_data(999, -100, 100)

# On va créer notre perceptron
# Il a pour option (dans l'ordre) le pas d'apprentissage et le seuil
P = perceptron.Perceptron(0.1, 0.5)

# On entraîne notre perceptron avec les inputs_train
P.train(INPUTS_TRAIN)

# On test ensuite ses capacitées à travailler seul
P.test(INPUTS_WORK)
