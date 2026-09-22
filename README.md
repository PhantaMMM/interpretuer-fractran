# Interpréteur FRACTRAN

Ce projet contient une implémentation en Python d'un interpréteur FRACTRAN.

Le principe est simple : on part d'un entier et on parcourt les fractions du programme dans l'ordre. Dès qu'une fraction peut être appliquée et donne encore un entier, elle est utilisée, puis on recommence au début de la liste. Si aucune fraction n'est applicable, le calcul s'arrête.

## Les fichiers

- `fractran.py` : contient les trois classes du projet (`Fraction`, `Facteur` et `Fractran`)
- `test_fractran.py` : contient les tests des différentes classes et méthodes
- `main.py` : contient les exemples FRACTRAN demandés dans le projet

Dans `main.py`, on trouve notamment :
- le calcul de sommes ;
- le calcul de produits ;
- la suite de Fibonacci ;
- le programme de Conway permettant de rechercher des nombres premiers.

Pour Fibonacci, seules les valeurs pouvant s'écrire sous la forme `2^a * 3^b` sont conservées. Les exposants correspondent alors aux termes successifs de la suite.

Pour le programme de Conway, les puissances de 2 sont recherchées parmi les premières valeurs produites. Lorsqu'une valeur est une puissance de 2, son exposant correspond à un nombre premier (en excluant le cas `p = 1`).

## Lancer le programme

Depuis le dossier du projet :

```bash
python main.py
```

## Lancer les tests

Pour exécuter les tests :

```bash
python -m pytest -v
```

