
# Ce fichier permet de faire des tests sur le programme

# Mes modules
import perceptron
import generate_data

# On met les coordonnées dans des tableaux
# Les inputs_train sont les coordonnées sur lesquels notre programme va apprendre
inputs_train = generate_data.generateData(50, -10, 10)
# Les inputs_work sont les coordonnées sur lesquels notre programme va s'exercer
inputs_work = generate_data.generateData(999, -10, 10)

# On va créer notre perceptron
# Il a pour option (dans l'ordre) le pas d'apprentissage et le seuil
p = perceptron.perceptron(0.1, 0.01)

# On entraîne notre perceptron avec les inputs_train
p.train(inputs_train)

# On test ensuite ses capacitées à travailler seul
p.test(inputs_work)
