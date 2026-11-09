# Diagrammes UML

## Classes

```mermaid
classDiagram
    class Grille {
        +int nombre_lignes
        +int nombre_colonnes
        +list matrice
        +str vide = "∿"
        +__init__(nombre_lignes, nombre_colonnes)
        +indice(ligne, colonne) int
        +case_valide(ligne, colonne) bool
        +tirer(ligne, colonne, touche="x") bool
        +ajoute(bateau) bool
        +__str__() str
    }
    class Bateau {
        +int ligne
        +int colonne
        +int longueur = 1
        +bool vertical = False
        +str marque = "⛵"
        +__init__(ligne, colonne, longueur=1, vertical=False)
        +positions() list
        +coulé(grille) bool
    }
    class PorteAvion {
        +str marque = "🚢"
        +str nom = "porte-avions"
        +__init__(ligne, colonne, vertical=False)
    }
    class Croiseur {
        +str marque = "⛴"
        +str nom = "croiseur"
        +__init__(ligne, colonne, vertical=False)
    }
    class Torpilleur {
        +str marque = "🚣"
        +str nom = "torpilleur"
        +__init__(ligne, colonne, vertical=False)
    }
    class SousMarin {
        +str marque = "🐟"
        +str nom = "sous-marin"
        +__init__(ligne, colonne, vertical=False)
    }
    Bateau <|-- PorteAvion : longueur 4
    Bateau <|-- Croiseur : longueur 3
    Bateau <|-- Torpilleur : longueur 2
    Bateau <|-- SousMarin : longueur 2
    Grille ..> Bateau : ajoute lit positions et marque
    Bateau ..> Grille : coulé lit les impacts
```

`solution` et `vue` sont deux objets `Grille`, et non deux classes différentes.
Les fonctions `creer_partie` et `jouer_tir` sont définies dans `jeu.py`.

## Un tir sur un bateau

```mermaid
sequenceDiagram
    actor Joueur
    participant Main as main.py
    participant Jeu as jouer_tir
    participant Solution as solution : Grille
    participant Vue as vue : Grille
    participant Navire as bateau : Bateau
    Joueur->>Main: ligne et colonne
    Main->>Jeu: coordonnées et grilles
    Jeu->>Vue: contrôler limites et absence de tir précédent
    Jeu->>Solution: lire la case secrète
    Jeu->>Vue: tirer(ligne, colonne, "💣")
    Jeu->>Navire: coulé(vue)
    Navire->>Vue: lire toutes les cases du bateau
    alt toutes les cases touchées
        Jeu->>Vue: remplacer les impacts par la marque
        Jeu-->>Main: coulé, bateau
        Main->>Main: diminuer le nombre de bateaux restants
    else bateau encore à flot
        Jeu-->>Main: touché, bateau
    end
    Main-->>Joueur: message et affichage de vue
```
