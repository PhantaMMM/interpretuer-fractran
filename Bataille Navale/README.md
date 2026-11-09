# Bataille navale

Un jeu solo en Python, dans le terminal, pour travailler les classes, les listes
et l'héritage. Énoncé de référence : [Projet : bataille navale, cours de François
Brucker](https://francoisbrucker.github.io/cours_informatique/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-bataille-navale/).

## Jouer

Depuis ce dossier, avec Python 3.9 ou plus récent :

```bash
python3 main.py
```

Aucune bibliothèque externe n'est nécessaire pour jouer. La grille compte
8 lignes (`0` à `7`) et 10 colonnes (`0` à `9`). Saisir une ligne, puis une colonne.

| Symbole | Signification |
| --- | --- |
| `.` | Case inconnue, y compris un bateau encore caché |
| `x` | Tir dans l'eau |
| `💣` | Bateau touché, pas encore coulé |
| `🚢`, `⛴`, `🚣`, `🐟` | Bateau coulé, révélé en entier |

La flotte contient un porte-avions de longueur 4, un croiseur de longueur 3,
un torpilleur de longueur 2 et un sous-marin de longueur 2. Les lettres, les
coordonnées hors limites et les doublons ne comptent pas comme des coups.
La partie se termine après le quatrième naufrage et affiche le nombre de coups.

## Organisation et choix de programmation

- `grille.py` : stockage dans une liste, tirs, placement et affichage.
- `bateau.py` : classe de base et quatre sous-classes.
- `jeu.py` : préparation de la flotte et traitement d'un tir.
- `main.py` : saisie et boucle de jeu.
- `story_grille.py` : « Plouf dans l'eau », grille interactive de 5 × 8 ; `q` quitte.
- `story_bateau.py` : deux exemples de chevauchement, avec et sans collision.
- `test_grille.py`, `test_bateau.py`, `test_jeu.py`, `test_main.py`,
  `test_stories.py` : tests automatisés.
- `UML.md` : classes et déroulement d'un tir.

La case `(ligne, colonne)` se trouve à l'indice
`ligne * nombre_colonnes + colonne`. L'eau est stockée sous la forme `∿`, mais
s'affiche comme un point. L'affichage ne contient pas de retour à la ligne final.

Deux grilles ont des rôles séparés : `solution` garde le placement secret sans
être modifiée par les tirs ; `vue` contient seulement ce que le joueur a découvert.
Il n'est donc pas nécessaire de masquer les bateaux au moment de l'affichage.
La vue sert aussi à repérer les tirs déjà effectués, sans liste de tirs séparée.

Pour placer chaque bateau, on énumère les départs et les orientations qui le
font rentrer dans la grille. On conserve tous ceux dont les cases sont libres,
puis `random.choice` choisit un triplet `(ligne, colonne, vertical)`.
Il n'y a pas de boucle de tentatives aléatoires. `Grille.ajoute` vérifie toutes
les cases avant d'écrire : un refus ne laisse jamais un bateau à moitié placé.
Les positions sont calculées dans deux branches explicites, horizontale et
verticale. La story de chevauchement compare les coordonnées par appartenance,
sans intersection d'ensembles.

`Bateau.coulé(grille)` reconnaît les `x` de l'exercice et les `💣` du jeu.
Dans le jeu, cette vérification se fait sur `vue` avant de remplacer les impacts
par la marque du bateau coulé. La flotte reste complète ; un compteur indique
combien de bateaux restent à couler.

## Stories et vérifications

```bash
python3 story_grille.py
python3 story_bateau.py
```

Pour installer les outils de développement dans un environnement neuf :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest black
python -m pytest -v
python -m black --check *.py
```

Les tests reprennent les exemples exacts du cours, les limites et refus de
placement sans modification, les quatre sous-classes et les impacts. Ils
contrôlent aussi l'ensemble des placements proposés au tirage, vingt flottes
aléatoires, les deux stories et une vraie partie lancée dans un sous-processus.
Ce dernier essai fournit les 80 coordonnées possibles, des erreurs de saisie et
des doublons, puis vérifie la victoire, les quatre bateaux révélés et le compteur.
