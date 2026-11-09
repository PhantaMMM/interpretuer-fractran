"""Deux exemples de la story « chevauchement »."""

from bateau import Bateau


def se_chevauchent(premier, second):
    for position in premier.positions():
        if position in second.positions():
            return True
    return False


if __name__ == "__main__":
    horizontal = Bateau(1, 1, 3)
    croisement = Bateau(0, 2, 3, True)
    loin = Bateau(3, 0, 2)
    print("Chevauchement :", se_chevauchent(horizontal, croisement))
    print("Chevauchement :", se_chevauchent(horizontal, loin))
