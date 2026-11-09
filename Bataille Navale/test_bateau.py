def test_positions_et_valeurs_par_defaut():
    from bateau import Bateau

    simple = Bateau(2, 3)
    assert (simple.ligne, simple.colonne, simple.longueur, simple.vertical) == (
        2,
        3,
        1,
        False,
    )
    assert simple.positions() == [(2, 3)]
    assert simple.marque == "⛵"
    assert Bateau(2, 3, 3).positions() == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, 3, True).positions() == [(2, 3), (3, 3), (4, 3)]


def test_coule_exige_toutes_les_cases_touchees():
    from bateau import Bateau
    from grille import Grille

    for impact in ("x", "💣"):
        grille = Grille(3, 4)
        bateau = Bateau(0, 2, 3, True)
        grille.ajoute(bateau)
        assert bateau.coulé(grille) is False
        grille.tirer(0, 2, impact)
        grille.tirer(1, 2, impact)
        assert bateau.coulé(grille) is False
        grille.tirer(2, 2, impact)
        assert bateau.coulé(grille) is True


def test_quatre_types_et_placement_des_marques():
    from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin
    from grille import Grille

    for classe, longueur, marque in [
        (PorteAvion, 4, "🚢"),
        (Croiseur, 3, "⛴"),
        (Torpilleur, 2, "🚣"),
        (SousMarin, 2, "🐟"),
    ]:
        for vertical in (False, True):
            bateau = classe(0, 0, vertical)
            assert isinstance(bateau, Bateau)
            assert bateau.longueur == longueur
            assert bateau.marque == marque
            assert bateau.vertical == vertical
            grille = Grille(4, 4)
            assert grille.ajoute(bateau)
            assert grille.matrice.count(marque) == longueur
            for ligne, colonne in bateau.positions():
                assert grille.matrice[grille.indice(ligne, colonne)] == marque
