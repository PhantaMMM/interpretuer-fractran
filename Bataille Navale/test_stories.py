from pathlib import Path
import subprocess
import sys

DOSSIER = Path(__file__).parent


def test_story_bateau():
    from bateau import Bateau
    from story_bateau import se_chevauchent

    horizontal = Bateau(1, 1, 3)
    assert se_chevauchent(horizontal, Bateau(0, 2, 3, True)) is True
    assert se_chevauchent(horizontal, Bateau(3, 0, 2)) is False
    resultat = subprocess.run(
        [sys.executable, str(DOSSIER / "story_bateau.py")],
        capture_output=True,
        text=True,
        check=True,
        timeout=10,
    )
    assert "Chevauchement : True" in resultat.stdout
    assert "Chevauchement : False" in resultat.stdout


def test_story_grille():
    resultat = subprocess.run(
        [sys.executable, str(DOSSIER / "story_grille.py")],
        input="bonjour\n-1\n0\n2\n3\nq\n",
        capture_output=True,
        text=True,
        check=True,
        timeout=10,
    )
    assert "Coordonnées invalides." in resultat.stdout
    assert "Case hors de la grille." in resultat.stdout
    assert "........\n........\n...x....\n........\n........" in resultat.stdout
