from pathlib import Path
import re
import subprocess
import sys


def test_partie_complete_en_ligne_de_commande():
    # Saisies invalides, un tir, son doublon, puis toutes les cases.
    reponses = ["bonjour", "-1", "8", "0", "non", "-1", "10", "0", "0", "0"]
    for ligne in range(8):
        for colonne in range(10):
            reponses.extend([str(ligne), str(colonne)])
    resultat = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("main.py"))],
        input="\n".join(reponses) + "\n",
        capture_output=True,
        text=True,
        check=True,
        timeout=10,
    )
    sortie = resultat.stdout
    assert resultat.stderr == ""
    assert sortie.startswith("Bataille navale\n" + "\n".join([".........."] * 8))
    assert sortie.count("Entrez un entier.") == 2
    assert sortie.count("Coordonnée hors limites.") == 4
    assert sortie.count("Cette case a déjà été jouée.") == 2
    assert sortie.count("Coulé :") == 4
    for nom, marque in [
        ("porte-avions", "🚢"),
        ("croiseur", "⛴"),
        ("torpilleur", "🚣"),
        ("sous-marin", "🐟"),
    ]:
        assert f"Coulé : {nom} {marque} !" in sortie
    coups = int(re.search(r"Bravo ! Flotte coulée en (\d+) coups\.", sortie)[1])
    assert 11 <= coups <= 80
    assert coups == sortie.count("À l'eau !") + sortie.count("Touché !") + 4
    derniere_grille = sortie.splitlines()[-9:-1]
    assert len(derniere_grille) == 8
    carte = "".join(derniere_grille)
    assert "💣" not in carte
    for marque, longueur in [("🚢", 4), ("⛴", 3), ("🚣", 2), ("🐟", 2)]:
        assert carte.count(marque) == longueur
