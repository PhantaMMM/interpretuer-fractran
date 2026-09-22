from fractran import Facteur, Fraction, Fractran


def test_fraction_init():
    fraction = Fraction(1, 2)
    assert fraction.numérateur == 1
    assert fraction.dénominateur == 2


def test_fraction_est_entier():
    assert Fraction(1, 2).est_entier(2)
    assert not Fraction(1, 3).est_entier(2)


def test_fraction_valeur():
    fraction = Fraction(3, 2)
    assert fraction.valeur(4) == 6


def test_facteur_init():
    facteur = Facteur([2, 3, 7])
    assert facteur.facteurs == [2, 3, 7]


def test_facteur_nombre():
    facteur = Facteur([2, 3, 7])
    assert facteur.nombre([1, 2]) == (2 ** 1) * (3 ** 2)
    assert facteur.nombre([1, 2, 3]) == (2 ** 1) * (3 ** 2) * (7 ** 3)


def test_facteur_decomposition():
    facteur = Facteur([2, 3, 7])
    assert facteur.decomposition(1) == [0, 0, 0]
    assert facteur.decomposition((2 ** 3) * (3 ** 2) * 7) == [3, 2, 1]


def test_fractran_init():
    programme = [Fraction(3, 10), Fraction(4, 3)]
    assert Fractran(programme).programme == programme


def test_fractran_run():
    programme = Fractran([Fraction(3, 10), Fraction(4, 3)])
    assert programme.run(14) == 14
    assert programme.run(15) == 8


def test_fractran_suite():
    programme = Fractran([Fraction(3, 10), Fraction(4, 3)])
    assert programme.suite(15, 10) == [15, 20, 6, 8]
    assert programme.suite(15, 2) == [15, 20]
