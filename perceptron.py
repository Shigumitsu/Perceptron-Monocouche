
# Les modules externe
import random
import math
import matplotlib.pyplot as plt
import numpy as np

class perceptron:
    def __init__(self, lRate, threshold):
        """Permet d'initialiser les bases du perceptron
        C'est la première étape du processus d'un perceptron"""

        # On défini le pas d'apprentissage
        if 0.0 <= lRate <= 1.0:
            self.lRate = lRate
        else:
            print("Vous devez mettre un pas d'apprentissage entre 0.0 et 1.0")
            (quit)

        # On défini le seuil
        if 0.0 <= threshold <= 1.0:
            self.threshold = threshold
        else:
            print("Vous devez mettre un seuil entre 0.0 et 1.0")
            quit()

        # On initialise le poids pour chaque entrée
        self.w = []
        for i in range(2):
            self.w.append(random.uniform(-1, 1))

        # On initialise le biais
        self.bias = random.uniform(-1, 1)

        # On défini a et b de la fonction f(x)
        self.a = random.randrange(-50, 50)
        self.b = random.randrange(-5, 5)

    def f(self, x):
        """Permet de calculer une fonction f(x)"""

        # On défini la fonction que l'on va utiliser
        # Peut donc être facilement changeable
        # /!\ ATTENTION /!\ : Le perceptron ne peut que gérer les
        # fonctions linéaires !
        return(self.a * x + self.b)

    def sigmoid(self, x):
        """Renvoi la valeur de la fonction sigmoïde"""

        # Pour éviter un OverflowError au niveau de 0
        # Car il arrondi à 1, mais pas 0 (pour les 10^-x)
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
        return self.sigmoid(self.sumStep(coor))

        # On envoi en sortie la réponse de la fonction sigmoïde en fonction du seuil
        # if self.sigmoid(self.sumStep(coor)) >= self.threshold:
        #     return 1
        # return 0

        # Cela peut être une autre solution pour apprendre :
        # La fonction de Heaviside
        # y = self.sumStep(coor) + self.bias
        # if y >= self.threshold:
        #     return 1
        # return 0

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

        # Tableau pour connaitre l'évolution des erreurs global
        globalErrortab = np.array([])
        for iteration in range(1000):
            globalError = 0
            for coor in inputs:
                # On compare la réponse du perceptron avec la vrai réponse
                intervalError = self.realAnswer(coor) - self.activationStep(coor)
                # On ajuste le poids pour corriger le perceptron
                # dans son apprentissage
                self.adjustWeights(coor, intervalError)
                globalError += abs(intervalError)
            # On regarde si il est totalement juste
            globalErrortab = np.append(globalErrortab, globalError)
            if globalError <= 0.1:
                break

        print ("Le nombre global d'erreur pendant l'entrainment est de : ", globalError)
        print ("Nombre d'itération durant l'entrainement : ", iteration)

        # Calcul de la pente de la fonction
        print ("La pente de la fonction est de : ", (self.f(1) - self.f(0)))

        # On cherche la pente du perceptron, afin de prouver
        # que notre perceptron marche
        for y in range(2):
            for x in np.arange(-50.0, 51.0, 0.0001):
                # print(self.activationStep([x, y]))
                if 0.495 <= self.activationStep([x, y]) <= 0.505:
                    if y == 0:
                        xa = x
                    else:
                        xb = x
                    break

        # On affiche les résultats
        print ("La pente devinée est de : ", 1 / (xb - xa))

        # Permet de tracer un graphique du nbr global d'erreur / nbr d'itération
        plt.plot(np.arange(iteration + 1), globalErrortab)
        plt.title("Nbr global d'erreur pdt l'entrainement en fct du \
nbr d'itération")
        plt.xlabel("Nbr d'itération")
        plt.ylabel("Nbr d'erreur global")
        plt.show()

    def test(self, inputs):
        """Permet de tester les connaissances du perceptron"""

        globalError = 0
        globalErrortab = np.array([])
        for coor in inputs:
            intervalError = self.realAnswer(coor) - self.activationStep(coor)
            globalError += abs(intervalError)
            globalErrortab = np.append(globalErrortab, globalError)
        print("Nombre d'erreurs lors du test : ", globalError)

        # Permet de tracer un graphique du nbr global d'erreur / nbr d'itération
        plt.plot(np.arange(len(inputs)), globalErrortab)
        plt.title("Nbr global d'erreur pdt les tests en fct du \
nbr d'itération")
        plt.xlabel("Nbr d'itération")
        plt.ylabel("Nbr d'erreur global")
        plt.show()
