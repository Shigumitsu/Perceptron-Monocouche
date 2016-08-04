
# Les modules externe
import random

def generateData(iteration, minc, maxc):
    """Permet de génerer des coordonnées sur un plan en 2D.
    Il renvoi un tableau contenant les coordonnées x et y"""

    # On vérifie si la valeur est bien un entier
    if not isinstance((iteration or minc or maxc), int):
        print("generateData : Vous n'avez pas rentré de bonne valeur")
        quit()
    # On verifie si le maximum est plus grand que le minimum
    if maxc <= minc:
        print("generateData : Le maximum doit être plus grand que votre \
minimum")
        quit()
    # On vérifie si notre itération est bien positive
    if iteration <= 0:
        print("generateData : Votre nombre d'itération est incorrect.")
        quit()
    # On limite l'utilisateur en terme de valeur
    if not -9999 <= (iteration or minc or maxc) <= 9999:
        print("generateData : Un des nombres que vous avez rentré en paramètre \
est trop petit ou trop grand.")
        quit()

    # Génère les coordonnées
    inputs = []
    for i in range(iteration):
        inputs.extend([[random.randrange(minc, maxc) for j in range(2)]])
    return (inputs)
