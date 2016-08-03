# Deux programmes :
# 1. Apprendre
# 2. Reconnaissance

# Différents types de couches:
#   - Couche d'entrée:
#   - Couche(s) cachée(s):
#   - Couche de sortie:

import random
import numpy as np

class perceptron:
    def __init__(self):
        """Permet d'initialiser les bases du perceptron"""
        # On initialise a et b pour la fonction
        # (défini actuellement comme: ax + b)
        self.a = random.uniform(-50, 50)
        self.b = random.uniform(-5, 5)
        # On initialise le poids pour chaque entrée
        self.w = []
        for i in range(2)
            self.w.extend(random.uniform(-1, 1))
        # On initialise le biais
        self.bias = random.uniform(-1, 1)

    def f(x):
        """Permet de calculer une fonction f(x)"""
        # On défini la fonction que l'on va utiliser
        # Peut donc être facilement changeable
        return(self.a * x + self.b)

    def sigmoid(x):
        """Renvois la valeur de la fonction sigmoïde"""
        # On défini la fonction sigmoïde
        return(1.0 / (1 + np.exp(-x))

    def sumStep(inputs):
        """Permet de faire la somme de tout les poids
        C'est la seconde étape du processus d'un perceptron"""
        # On fait la somme de tous les poids
        sum = self.bias
        for i in range(inputs)
            sum += inputs[i] * self.w[i]
        return sum

    def activationStep():
        """Permet de """
        # On envoi en sortie la réponse de la fonction sigmoïde
