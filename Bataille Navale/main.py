"""Jouer seul dans le terminal : python main.py."""

from jeu import creer_partie, jouer_tir


def lire_coordonnee(question, limite):
    while True:
        try:
            valeur = int(input(question))
        except ValueError:
            print("Entrez un entier.")
            continue
        if 0 <= valeur < limite:
            return valeur
        print("Coordonnée hors limites.")


def main():
    solution, vue, flotte = creer_partie()
    restants = len(flotte)
    coups = 0
    print("Bataille navale")
    print(vue)
    while restants > 0:
        ligne = lire_coordonnee("Ligne (0 à 7) : ", 8)
        colonne = lire_coordonnee("Colonne (0 à 9) : ", 10)
        resultat, bateau = jouer_tir(solution, vue, flotte, ligne, colonne)
        if resultat == "déjà joué":
            print("Cette case a déjà été jouée.")
            continue
        coups += 1
        if resultat == "eau":
            print("À l'eau !")
        elif resultat == "touché":
            print("Touché !")
        elif resultat == "coulé":
            restants -= 1
            print(f"Coulé : {bateau.nom} {bateau.marque} !")
        print(vue)
    print(f"Bravo ! Flotte coulée en {coups} coups.")


if __name__ == "__main__":
    main()
