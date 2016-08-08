
"""Permet de générer des point aléatoire sur un plan 2D"""

# Les modules externe
import random

def generate_data(iteration, minc, maxc):
    """Permet de génerer des coordonnées sur un plan en 2D.
    Il renvoi un tableau contenant les coordonnées x et y"""

    # On vérifie si la valeur est bien un entier
    if not isinstance((iteration or minc or maxc), int):
        print("generate_data : Vous n'avez pas rentré de bonne valeur")
        quit()
    # On verifie si le maximum est plus grand que le minimum
    if maxc <= minc:
        print("generate_data : Le maximum doit être plus grand que votre \
minimum")
        quit()
    # On vérifie si notre itération est bien positive
    if iteration <= 0:
        print("generate_data : Votre nombre d'itération est incorrect.")
        quit()
    # On limite l'utilisateur en terme de valeur
    if not -9999 <= (iteration or minc or maxc) <= 9999:
        print("generate_data : Un des nombres que vous avez rentré en paramètre \
est trop petit ou trop grand.")
        quit()

    # Génère les coordonnées
    inputs = []
    for _ in range(iteration):
        inputs.extend([[random.randrange(minc, maxc) for _ in range(2)]])
    return inputs
