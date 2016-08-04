
# Les modules externe
import random
import math

class perceptron:
    def __init__(self):
        """Permet d'initialiser les bases du perceptron
        C'est la première étape du processus d'un perceptron"""

        # On défini le pas d'apprentissage
        self.lRate = 0.1

        # On défini le seuil
        self.threshold = 0.5

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

        # Pour éviter un OverflowError au niveau de 0
        # Car il arrondi à 1, mais pas pour les 10^-x
        try:
        # On défini la fonction sigmoïde
            res = 1 / (1 + math.exp(-x))
        except OverflowError:
            res = 0.0
        return res

    def sumStep(self, coor):
        """Permet de faire la somme de tout les poids
        C'est la seconde étape du processus d'un perceptron"""

        # On fait la somme de tous les poids
        sumw = 0.0
        for i in range(2):
            sumw += coor[i] * self.w[i]
        return sumw

    def activationStep(self, coor):
        """Permet d'envoyer la sortie du perceptron
        C'est la dernière étape du processus d'un perceptron"""

        # On envoi en sortie la réponse de la fonction sigmoïde
        if self.sigmoid(self.sumStep(coor)) >= self.threshold:
            return 1
        return -1

        # Cela peut être une autre solution pour apprendre :
        # La fonction de Heaviside
        # y = self.sumStep(coor) + self.bias
        # if y >= self.threshold:
        #     return 1
        # return -1

    def realAnswer(self, coor):
        """Permet d'obtenir le bon résultat
        Idéal pour faire apprendre au perceptron"""

        # Si y > f(x), alors le point est au-dessus
        if coor[1] > self.f(coor[0]):
            return 1
        return -1

    def adjustWeights(self, coor, intervalError):
        """Permet d'ajuster le poids de chaque entrée, afin de bien répondre"""

        for i in range(2):
            self.w[i] += coor[i] * intervalError * self.lRate


    def train(self, inputs):
        """Permet d'entraîner le perceptron pour un cas particulier
        La fonction train est en quelques sorte un professeur qui lui si oui
        ou non les réponses sont justes."""

        for iteration in range(100):
            globalError = 0
            for coor in inputs:
                # On compare la réponse du perceptron avec la vrai réponse
                intervalError = self.realAnswer(coor) - self.activationStep(coor)
                # On ajuste le poids pour corriger le perceptron
                # dans son apprentissage
                self.adjustWeights(coor, intervalError)
                globalError += abs(intervalError)
            # On regarde si il est totalement juste
            # print("iteration = {}\nglobalError = {}".format(iteration, globalError)) #TEST
            if globalError == 0:
                break

    def test(self, inputs):
        """Permet de tester les connaissances du perceptron"""

        globalError = 0
        for coor in inputs:
            intervalError = self.realAnswer(coor) - self.activationStep(coor)
            globalError += abs(intervalError)
        print("Nombre d'erreurs lors du test : ", globalError / 2)
