class Fraction:
    def __init__(self, numérateur, dénominateur):
        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self, n):
        """Indique si la fraction peut être appliquée à n."""
        return n % self.dénominateur == 0

    def valeur(self, n):
        """Retourne le résultat de l'application de la fraction à n."""
        quotient = n // self.dénominateur
        return self.numérateur * quotient


class Facteur:
    def __init__(self, facteurs):
        self.facteurs = facteurs

    def nombre(self, exposants):
        """Reconstruit un nombre à partir des exposants donnés."""
        resultat = 1
        for facteur, exposant in zip(self.facteurs, exposants):
            resultat *= facteur ** exposant
        return resultat

    def decomposition(self, n):
        """Retourne les exposants correspondant aux facteurs connus."""
        exposants = []
        for facteur in self.facteurs:
            exposant = 0
            while n % facteur == 0:
                n //= facteur
                exposant += 1
            exposants.append(exposant)
        return exposants


class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        """Exécute le programme jusqu'à ce qu'aucune fraction ne soit applicable."""
        index = 0
        while index < len(self.programme):
            fraction = self.programme[index]
            if fraction.est_entier(n):
                n = fraction.valeur(n)
                index = 0
            else:
                index += 1
        return n

    def suite(self, n, N):
        """Produit au maximum N valeurs successives du programme."""
        valeurs = [n]
        index = 0
        while index < len(self.programme) and len(valeurs) < N:
            fraction = self.programme[index]
            if fraction.est_entier(n):
                n = fraction.valeur(n)
                valeurs.append(n)
                index = 0
            else:
                index += 1
        return valeurs
