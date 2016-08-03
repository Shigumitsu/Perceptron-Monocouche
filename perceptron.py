
# Les modules externe
import random
import numpy as np

class perceptron:
    def __init__(self):
        """Permet d'initialiser les bases du perceptron
        C'est la première étape du processus d'un perceptron"""

        # On défini le pas d'apprentissage
        self.lRate = 0.5

        # On initialise le poids pour chaque entrée
        self.w = []
        for i in range(2):
            self.w.append(random.uniform(-1, 1))

        # On initialise le biais
        self.bias = random.uniform(-1, 1)

    def f(self, x):
        """Permet de calculer une fonction f(x)"""

        # On défini la fonction que l'on va utiliser
        # Peut donc être facilement changeable
        try :
            self.a
            self.b
        except AttributeError:
            self.a = random.uniform(-50, 50)
            self.b = random.uniform(-5, 5)
        return(self.a * x + self.b)

    def sigmoid(self, x):
        """Renvoi la valeur de la fonction sigmoïde"""

        # On défini la fonction sigmoïde
        return 1.0 / (1 + np.exp(-x))

    def sumStep(self, coor):
        """Permet de faire la somme de tout les poids
        C'est la seconde étape du processus d'un perceptron"""

        # On fait la somme de tous les poids
        sumw = self.bias
        for i in range(2):
            sumw += coor[i] * self.w[i]
        return sumw

    def activationStep(self, coor):
        """Permet d'envoyer la sortie du perceptron
        C'est la dernière étape du processus d'un perceptron"""

        # On envoi en sortie la réponse de la fonction sigmoïde
        return self.sigmoid(self.sumStep(coor))

    def realAnswer(self, coor):
        """Permet d'obtenir le bon résultat
        Idéal pour faire apprendre au perceptron"""

        # Si y > f(x), alors le point est au-dessus
        if coor[1] > self.f(coor[0]):
            return 1
        return 0

    def adjustWeights(self, coor, intervalError):
        """Permet d'ajuster le poids de chaque entrée, afin de bien répondre"""

        for i in range(2):
            self.w[i] += coor[i] * intervalError * self.lRate


    def train(self, inputs):
        """Permet d'entraîner le perceptron pour un cas particulier
        La fonction train est en quelques sorte un professeur qui lui si oui
        ou non les réponses sont justes."""

        for iteration in range(10000000000000):
            globalError = 0.0
            for coor in inputs:
                # On compare la réponse du perceptron avec la vrai réponse
                intervalError = self.realAnswer(coor) - self.activationStep(coor)
                # On ajuste le poids pour corriger le perceptron
                # dans son apprentissage
                self.adjustWeights(coor, intervalError)
                globalError += abs(intervalError)
            # On regarde si il est totalement juste
            print("iteration = {}\nglobalError = {}".format(iteration, globalError)) #TEST
            if globalError == 0.0:
                break
