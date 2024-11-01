liste_de_dicos = []
liste_de_dicos.append({"A":3, "B":1, "C":2, "D":1})
liste_de_dicos.append({"A":2, "B":1, "C":4, "D":3})
liste_de_dicos.append({"A":4, "B":2, "C":1, "D":4})
liste_de_dicos.append({"A":1, "B":2, "C":3, "D":2})

def affiche(liste):
    for elt in liste:
        print(elt)

affiche(liste_de_dicos)

# 1. Trier suivant la somme des valeurs
def somme(d):
    return d['A'] + d['B'] + d['C'] + d['D']

affiche(sorted(liste_de_dicos, key=somme))

# 2. Trier suivant B puis A
def score(d):
    return d['B'], d['A']

affiche(sorted(liste_de_dicos, key=score))
