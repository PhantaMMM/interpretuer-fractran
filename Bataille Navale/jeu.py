"""Le placement secret et la carte du joueur restent deux grilles distinctes."""

import random

from bateau import Croiseur, PorteAvion, SousMarin, Torpilleur
from grille import Grille


def creer_partie():
    solution = Grille(8, 10)
    vue = Grille(8, 10)
    flotte = []
    for classe in (PorteAvion, Croiseur, Torpilleur, SousMarin):
        possibilites = []
        longueur = classe(0, 0).longueur
        for vertical in (False, True):
            # Ces bornes garantissent que le bateau entre en entier.
            lignes = 8 - longueur + 1 if vertical else 8
            colonnes = 10 if vertical else 10 - longueur + 1
            for ligne in range(lignes):
                for colonne in range(colonnes):
                    essai = classe(ligne, colonne, vertical)
                    cases = essai.positions()
                    if all(
                        solution.matrice[solution.indice(l, c)] == solution.vide
                        for l, c in cases
                    ):
                        possibilites.append((ligne, colonne, vertical))
        ligne, colonne, vertical = random.choice(possibilites)
        bateau = classe(ligne, colonne, vertical)
        solution.ajoute(bateau)
        flotte.append(bateau)
    return solution, vue, flotte


def jouer_tir(solution, vue, flotte, ligne, colonne):
    if not vue.case_valide(ligne, colonne):
        return "hors grille", None
    indice = vue.indice(ligne, colonne)
    if vue.matrice[indice] != vue.vide:
        return "déjà joué", None
    if solution.matrice[indice] == solution.vide:
        vue.tirer(ligne, colonne)
        return "eau", None

    vue.tirer(ligne, colonne, "💣")
    for bateau in flotte:
        if (ligne, colonne) in bateau.positions():
            if bateau.coulé(vue):
                for l, c in bateau.positions():
                    vue.tirer(l, c, bateau.marque)
                return "coulé", bateau
            return "touché", bateau
