def test_init():
    from grille import Grille

    grille = Grille(2, 3)
    assert grille.nombre_lignes == 2
    assert grille.nombre_colonnes == 3
    assert grille.vide == "∿"
    assert grille.matrice == ["∿"] * 6


def test_tirs_et_affichage_du_cours():
    from grille import Grille

    grille = Grille(5, 8)
    assert str(grille) == "........\n........\n........\n........\n........"
    assert grille.indice(2, 3) == 19
    assert grille.tirer(2, 3) is True
    assert str(grille) == "........\n........\n...x....\n........\n........"
    assert grille.tirer(0, 7, "💣") is True
    assert grille.matrice[7] == "💣"
    avant = grille.matrice.copy()
    for ligne, colonne in [(-1, 0), (0, -1), (5, 0), (0, 8)]:
        assert grille.case_valide(ligne, colonne) is False
        assert grille.tirer(ligne, colonne) is False
    assert grille.matrice == avant


def test_placement_complet_ou_aucune_modification():
    from bateau import Bateau
    from grille import Grille

    grille = Grille(2, 3)
    assert grille.ajoute(Bateau(1, 0, 2)) is True
    assert grille.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]
    avant = grille.matrice.copy()
    for bateau in [
        Bateau(1, 0, 2, True),
        Bateau(1, 0, 4, True),
        Bateau(0, 2, 2),
        Bateau(-1, 0),
        Bateau(0, -1),
        Bateau(0, 1, 2, True),
    ]:
        assert grille.ajoute(bateau) is False
        assert grille.matrice == avant


def test_chevauchement_tardif_ne_place_pas_le_debut():
    from bateau import Bateau
    from grille import Grille

    grille = Grille(3, 4)
    assert grille.ajoute(Bateau(2, 2))
    avant = grille.matrice.copy()
    assert grille.ajoute(Bateau(0, 2, 3, True)) is False
    assert grille.matrice == avant
