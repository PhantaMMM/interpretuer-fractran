import random

import pytest


def test_placement_choisit_parmi_toutes_les_possibilites(monkeypatch):
    import jeu
    from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

    listes = []

    def choisir(possibilites):
        listes.append(possibilites.copy())
        return possibilites[0]

    monkeypatch.setattr(jeu.random, "choice", choisir)
    solution, vue, flotte = jeu.creer_partie()
    assert (solution.nombre_lignes, solution.nombre_colonnes) == (8, 10)
    assert [type(b) for b in flotte] == [PorteAvion, Croiseur, Torpilleur, SousMarin]
    assert solution is not vue
    assert solution.matrice.count(solution.vide) == 69
    assert vue.matrice == [vue.vide] * 80
    occupees = []
    for bateau, possibilites in zip(flotte, listes):
        attendues = []
        for ligne in range(8):
            for colonne in range(10):
                for vertical in (False, True):
                    essai = type(bateau)(ligne, colonne, vertical)
                    positions = essai.positions()
                    if all(
                        0 <= l < 8 and 0 <= c < 10 and (l, c) not in occupees
                        for l, c in positions
                    ):
                        attendues.append((ligne, colonne, vertical))
        assert sorted(possibilites) == sorted(attendues)
        occupees.extend(bateau.positions())


@pytest.mark.parametrize("graine", range(20))
def test_flottes_aleatoires_valides(graine, monkeypatch):
    import jeu

    monkeypatch.setattr(jeu.random, "choice", random.Random(graine).choice)
    solution, vue, flotte = jeu.creer_partie()
    positions = [case for bateau in flotte for case in bateau.positions()]
    assert len(positions) == len(set(positions)) == 11
    assert all(solution.case_valide(*case) for case in positions)
    for bateau in flotte:
        for ligne, colonne in bateau.positions():
            assert solution.matrice[solution.indice(ligne, colonne)] == bateau.marque
    assert str(vue) == "\n".join([".........."] * 8)


def test_tir_eau_touche_coule_et_doublons():
    from bateau import Torpilleur
    from grille import Grille
    from jeu import jouer_tir

    solution, vue = Grille(2, 3), Grille(2, 3)
    bateau = Torpilleur(1, 0)
    solution.ajoute(bateau)
    secret = solution.matrice.copy()
    assert jouer_tir(solution, vue, [bateau], -1, 0) == ("hors grille", None)
    assert vue.matrice == [vue.vide] * 6
    assert jouer_tir(solution, vue, [bateau], 0, 2) == ("eau", None)
    assert str(vue) == "..x\n..."
    assert jouer_tir(solution, vue, [bateau], 0, 2) == ("déjà joué", None)
    assert jouer_tir(solution, vue, [bateau], 1, 0) == ("touché", bateau)
    assert str(vue) == "..x\n💣.."
    assert jouer_tir(solution, vue, [bateau], 1, 0) == ("déjà joué", None)
    assert jouer_tir(solution, vue, [bateau], 1, 1) == ("coulé", bateau)
    assert str(vue) == "..x\n🚣🚣."
    assert jouer_tir(solution, vue, [bateau], 1, 1) == ("déjà joué", None)
    assert solution.matrice == secret
