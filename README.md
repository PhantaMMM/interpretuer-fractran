# Interpréteur FRACTRAN

Projet de programmation objet : implémentation d'un interpréteur FRACTRAN en Python.

Le projet est organisé autour de trois classes :
- Fraction : représente une fraction FRACTRAN et permet de tester si elle peut être appliquée à un entier.
- Facteur : permet de représenter un nombre à partir d'exposants de facteurs premiers et d'en retrouver la décomposition.
- Fractran : exécute un programme FRACTRAN et peut produire une suite de valeurs.

Le programme principal contient plusieurs exemples demandés dans le sujet : calcul de sommes, calcul de produits, suite de Fibonacci et recherche de nombres premiers avec le programme de Conway.

## Exécution

python main.py

## Tests

python -m pytest -v
