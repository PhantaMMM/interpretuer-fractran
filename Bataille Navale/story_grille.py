"""Story « Plouf dans l'eau » : tirer sur une grille de 5 × 8."""

from grille import Grille


if __name__ == "__main__":
    grille = Grille(5, 8)
    while True:
        print(grille)
        reponse = input("Ligne de 0 à 4 (q pour quitter) : ")
        if reponse.strip().lower() == "q":
            break
        try:
            ligne = int(reponse)
            colonne = int(input("Colonne de 0 à 7 : "))
        except ValueError:
            print("Coordonnées invalides.")
            continue
        if not grille.tirer(ligne, colonne):
            print("Case hors de la grille.")
