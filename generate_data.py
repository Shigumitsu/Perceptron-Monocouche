
# Les modules externe
import random

def generateData(iteration, minc, maxc):
    """Permet de génerer des coordonnées sur un plan en 2D.
    Il renvoi un tableau contenant les coordonnées x et y"""

    # Verification si la valeur est bien un entier
    if not isinstance(iteration, int) or not isinstance(minc, int) \
    or not isinstance(maxc, int):
        print("generateData : Vous n'avez pas rentrer de bonne valeur")
        return 0
    if maxc < minc:
        print("generateData : Le maximum doit être plus grand que votre \
        minimum")

    # Génère les coordonnées
    inputs = []
    for i in range(iteration):
        inputs.extend([[random.randrange(minc, maxc) for j in range(2)]])
    return (inputs)
