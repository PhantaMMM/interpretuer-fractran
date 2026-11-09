"""Les bateaux connaissent leurs coordonnées, mais ne possèdent pas de grille."""


class Bateau:
    marque = "⛵"

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        cases = []
        if self.vertical:
            for ligne in range(self.ligne, self.ligne + self.longueur):
                cases.append((ligne, self.colonne))
        else:
            for colonne in range(self.colonne, self.colonne + self.longueur):
                cases.append((self.ligne, colonne))
        return cases

    def coulé(self, grille):
        impacts = 0
        for ligne, colonne in self.positions():
            case = grille.matrice[grille.indice(ligne, colonne)]
            if case in ("x", "💣"):
                impacts += 1
        return impacts == self.longueur


class PorteAvion(Bateau):
    marque = "🚢"
    nom = "porte-avions"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)


class Croiseur(Bateau):
    marque = "⛴"
    nom = "croiseur"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)


class Torpilleur(Bateau):
    marque = "🚣"
    nom = "torpilleur"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)


class SousMarin(Bateau):
    marque = "🐟"
    nom = "sous-marin"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
