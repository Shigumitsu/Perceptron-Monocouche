
"""Ce fichier permet de créer et de tester un perceptron"""

# Les modules externe
import random
import math

# # A décommenter uniquement si vous voulez prouver l'efficacité du programme
# import matplotlib.pyplot as plt
# import numpy as np

class Perceptron(object):
    """Objet qui a pour but d'être un perceptron"""

    def __init__(self, l_rate, threshold):
        """Permet d'initialiser les bases du perceptron
        C'est la première étape du processus d'un perceptron

        -----
        l_rate: Learning Rate | Pas d'apprentissage
        Valeurs: Entre 0.0 et 1.0

        -----
        threshold: Threshold | Seuil
        Valeurs: Entre 0.0 et 1.0
        /!\\ Option inutile lorsque votre fonction d'activation est un sigmoide ! /!\\"""

        # On vérifie les valeurs rentrées
        if not isinstance((l_rate or threshold), float):
            print("perceptron : Vous n'avez pas rentré de bonne valeur")
            quit()

        # On défini le pas d'apprentissage
        if 0.0 <= l_rate <= 1.0:
            self.__l_rate = l_rate
        else:
            print("perceptron : Vous devez mettre un pas d'apprentissage entre 0.0 et 1.0")
            quit()

        # On défini le seuil
        if 0.0 <= threshold <= 1.0:
            self.__threshold = threshold
        else:
            print("perceptron : Vous devez mettre un seuil entre 0.0 et 1.0")
            quit()

        # On initialise le poids pour chaque entrée
        self.__weights = []
        for _ in range(2):
            self.__weights.append(random.uniform(-1, 1))

        # On initialise le biais
        self.__bias = random.uniform(-1, 1)

        # On défini a et b de la fonction f(x)
        self.__a_values = random.randrange(-50, 50)
        self.__b_values = random.randrange(-5, 5)

    def func_f(self, x_values):
        """Permet de calculer une fonction f(x)"""

        # On défini la fonction que l'on va utiliser
        # Peut donc être facilement changeable
        # /!\ ATTENTION /!\ : Le perceptron ne peut que gérer les
        # fonctions linéaires !
        return self.__a_values * x_values + self.__b_values

    @classmethod
    def sigmoid(cls, x_values):
        """Renvoi la valeur de la fonction sigmoïde"""

        # Pour éviter un OverflowError au niveau de 0
        # Car il arrondi à 1, mais pas 0 (pour les 10^-x)
        try:
        # On défini la fonction sigmoïde
            res = 1 / (1 + math.exp(-x_values))
        except OverflowError:
            res = 0.0
        return res

    def sum_step(self, coor):
        """Permet de faire la somme de tout les poids
        C'est la seconde étape du processus d'un perceptron"""

        # On fait la somme de tous les poids
        sumw = 0.0
        for i in range(2):
            sumw += coor[i] * self.__weights[i]
        return sumw

    def activation_step(self, coor):
        """Permet d'envoyer la sortie du perceptron
        C'est la dernière étape du processus d'un perceptron"""

        # On envoi en sortie la réponse de la fonction sigmoïde
        return self.sigmoid(self.sum_step(coor))

        # On envoi en sortie la réponse de la fonction sigmoïde en fonction du seuil
        # if self.sigmoid(self.sum_step(coor)) >= self.__threshold:
        #     return 1
        # return 0

        # Cela peut être une autre solution pour apprendre :
        # La fonction de Heaviside
        # y = self.sum_step(coor) + self.__bias
        # if y >= self.__threshold:
        #     return 1
        # return 0

    def real_answer(self, coor):
        """Permet d'obtenir le bon résultat
        Idéal pour faire apprendre au perceptron"""

        # Si y > f(x), alors le point est au-dessus
        if coor[1] > self.func_f(coor[0]):
            return 1
        return 0

    def adjust_weights(self, coor, intervalerror):
        """Permet d'ajuster le poids de chaque entrée, afin de bien répondre"""

        for _ in range(2):
            self.__weights[_] += coor[_] * intervalerror * self.__l_rate


    def train(self, inputs):
        """Permet d'entraîner le perceptron pour un cas particulier
        La fonction train est en quelques sorte un professeur qui lui si oui
        ou non les réponses sont justes."""

        # Tableau pour connaitre l'évolution des erreurs global
        # globalerrortab = np.array([])
        iteration = 0
        for iteration in range(1000):
            globalerror = 0
            for coor in inputs:
                # On compare la réponse du perceptron avec la vrai réponse
                intervalerror = self.real_answer(coor) - self.activation_step(coor)
                # On ajuste le poids pour corriger le perceptron
                # dans son apprentissage
                self.adjust_weights(coor, intervalerror)
                globalerror += abs(intervalerror)
            # globalerrortab = np.append(globalerrortab, globalerror)
            # On regarde si il est totalement juste
            # Nombre global d'erreur avant que le programme d'entrainement s'arrête
            # Avec les fonctions qui renvoi des réponses binaires
            # if globalerror <= 0.0:
            # Avec les fonctions qui renvoi des réponses floats
            if globalerror <= 0.1:
                break

        print("Le nombre global d'erreur pendant l'entrainment est de : ", globalerror)
        print("Nombre d'itération durant l'entrainement : ", iteration)

#         # Ralenti le programme, mais permet de prouver que notre perceptron marche
#         # Décommentez aussi l.131 et l.142
#         # Calcul de la pente de la fonction
#         print("La pente de la fonction est de : ", (self.func_f(1) - self.func_f(0)))
#
#         # On cherche la pente du perceptron, afin de prouver
#         # que notre perceptron marche
#         for y_values in range(2):
#             for x_values in np.arange(-50.0, 51.0, 0.0001):
#                 # print(self.activation_step([x, y]))
#                 if 0.495 <= self.activation_step([x_values, y_values]) <= 0.505:
#                     if y_values == 0:
#                         xa_values = x_values
#                     else:
#                         xb_values = x_values
#                     break
#
#         # On affiche les résultats
#         print("La pente devinée est de : ", 1 / (xb_values - xa_values))
#
#         # Permet de tracer un graphique du nbr global d'erreur / nbr d'itération
#         plt.plot(np.arange(iteration + 1), globalerrortab)
#         plt.title("Nbr global d'erreur pdt l'entrainement en fct du \
# nbr d'itération")
#         plt.xlabel("Nbr d'itération")
#         plt.ylabel("Nbr d'erreur global")
#         plt.show()

    def test(self, inputs):
        """Permet de tester les connaissances du perceptron"""

        globalerror = 0
        # globalerrortab = np.array([])
        for coor in inputs:
            intervalerror = self.real_answer(coor) - self.activation_step(coor)
            globalerror += abs(intervalerror)
            # globalerrortab = np.append(globalerrortab, globalerror)
        print("Nombre d'erreurs lors du test : ", globalerror)

#         # Ralenti le programme, mais permet de prouver que notre perceptron marche
#         # Décommentez aussi l.186 et l.190
#         # Permet de tracer un graphique du nbr global d'erreur / nbr d'itération
#         plt.plot(np.arange(len(inputs)), globalerrortab)
#         plt.title("Nbr global d'erreur pdt les tests en fct du \
# nbr d'itération")
#         plt.xlabel("Nbr d'itération")
#         plt.ylabel("Nbr d'erreur global")
#         plt.show()
