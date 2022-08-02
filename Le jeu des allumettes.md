#-draft 
#info/lang/python #peda/activite #classe/SIO

# Le jeu des allumettes

## Jouer

Utilisation éditeur de code, par ex [[Idle]].
Charger le fichier et l'exécuter.

```python
# le jeu des allumettes
tour = 1
N, p = 20, 3
joueurs = ["joueur A", "joueur B"]
prises = []
print("Bienvenue dans le jeu des allumettes!")

def reste_de_la_division_par_2(n):
    return n % 2

def num_joueur(n):
    r = reste_de_la_division_par_2(n)
    return 1 - r

while N > 1:
    print("Il y a " + str(N) + " allumettes.")
    print(joueurs[num_joueur(tour)],
          "combien en prenez-vous?")
    prise_str = input()
    prises.append(prise_str)
    N = N - int(prise)
    tour = tour + 1
    
if N == 1:
    print("Gagné !")
elif N == 0:
    print("Perdu !")
else:
    print("C'est trop !")
    
print("Prises:")
for p in range(len(prises)):
    print(prises[p], end=" - ")

```

## Améliorer

Lister les améliorations possibles.

Debrief en plénière.

1. Demander les noms des joueurs.
1. Demander nbre total et prise max.
1. Meilleur affichage final des prises.
1. Contrôle des prises.
1. ...
1. Jouer contre ordinateur.

Pour les rapides: programmer
[[Le jeu du plus ou moins]].
