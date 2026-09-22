from fractran import Facteur, Fraction, Fractran

facteurs = Facteur([2, 3, 5])

# Sommes
programme_somme = Fractran([Fraction(3, 2)])
print("Sommes i + j, avec 1 <= i, j <= 10 :")
for i in range(1, 11):
    for j in range(1, 11):
        entrée = facteurs.nombre([i, j])
        sortie = programme_somme.run(entrée)
        somme = facteurs.decomposition(sortie)[1]
        print(f"{i} + {j} = {somme}")

# Produits
programme_produit = Fractran([
    Fraction(455, 33), Fraction(11, 13), Fraction(1, 11),
    Fraction(3, 7), Fraction(11, 2), Fraction(1, 3),
])
print("\nProduits i * j, avec 1 <= i, j <= 10 :")
for i in range(1, 11):
    for j in range(1, 11):
        entrée = facteurs.nombre([i, j])
        sortie = programme_produit.run(entrée)
        produit = facteurs.decomposition(sortie)[2]
        print(f"{i} * {j} = {produit}")

# Fibonacci
fibonacci = [
    Fraction(23, 95), Fraction(57, 23), Fraction(17, 39),
    Fraction(130, 17), Fraction(11, 14), Fraction(35, 11),
    Fraction(19, 13), Fraction(1, 19), Fraction(35, 2),
    Fraction(13, 7), Fraction(7, 1),
]
valeurs = Fractran(fibonacci).suite(3, 1000)
facteurs_fibonacci = Facteur([2, 3])
suite_fibonacci = []
for valeur in valeurs:
    decomposition = facteurs_fibonacci.decomposition(valeur)
    if valeur == facteurs_fibonacci.nombre(decomposition):
        suite_fibonacci.append(decomposition)
print("\nCouples d'exposants de Fibonacci :")
print(suite_fibonacci)

# Programme de Conway pour les nombres premiers
programme_premiers = [
    Fraction(17, 91), Fraction(78, 85), Fraction(19, 51),
    Fraction(23, 38), Fraction(29, 33), Fraction(77, 29),
    Fraction(95, 23), Fraction(77, 19), Fraction(1, 17),
    Fraction(11, 13), Fraction(13, 11), Fraction(15, 14),
    Fraction(15, 2), Fraction(55, 1),
]
valeurs = Fractran(programme_premiers).suite(2, 100000)
facteur_deux = Facteur([2])
nombres_premiers = []
for valeur in valeurs:
    decomposition = facteur_deux.decomposition(valeur)
    if valeur == facteur_deux.nombre(decomposition):
        exposant = decomposition[0]
        if exposant > 1:
            nombres_premiers.append(exposant)
print("\nNombres premiers obtenus :")
print(nombres_premiers)
