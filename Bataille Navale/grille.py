"""Une grille rectangulaire représentée par une seule liste."""


class Grille:
    vide = "∿"

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)

    def indice(self, ligne, colonne):
        return ligne * self.nombre_colonnes + colonne

    def case_valide(self, ligne, colonne):
        return 0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes

    def tirer(self, ligne, colonne, touche="x"):
        if not self.case_valide(ligne, colonne):
            return False
        self.matrice[self.indice(ligne, colonne)] = touche
        return True

    def ajoute(self, bateau):
        # Préparer tous les indices avant de toucher à la liste.
        indices = []
        for ligne, colonne in bateau.positions():
            if not self.case_valide(ligne, colonne):
                return False
            indice = self.indice(ligne, colonne)
            if self.matrice[indice] != self.vide:
                return False
            indices.append(indice)
        for indice in indices:
            self.matrice[indice] = bateau.marque
        return True

    def __str__(self):
        texte = ""
        for ligne in range(self.nombre_lignes):
            if ligne > 0:
                texte += "\n"
            for colonne in range(self.nombre_colonnes):
                case = self.matrice[self.indice(ligne, colonne)]
                texte += "." if case == self.vide else case
        return texte
