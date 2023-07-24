#classe/NSI #peda/activite #info/lang/python

# Listes de nombres
1. Nombres consécutifs
    1. Écrire une instruction ou une suite d’instructions
       qui affiche les nombres entiers de 1 à 20, chacun
       sur une ligne.
   1. Écrire une expression (du code qui peut être
     écrit à droite d’une affectation) qui s’évalue en
     la liste des nombres entiers de 1 à 20 (sans
     préparation, ça doit être fait en une expression).
1. Idem avec les nombres pairs entre 1 et 20, puis
   avec les nombres impairs entre 1 et 20.
1. Écrire une fonction qui attend en paramètre
   une liste et teste si cette liste est la liste des
   nombres entiers de 1 à 20.

# Propositions
```python
for i in range(20):
    print(i+1)
for i in range(1, 21):
    print(i)

x = []
for i in range(20):
    x.append(i+1)
n  # est l’expression demandée

# mieux:
range(1, 21)  # en fait un itérateur
[i for i in range(1, 21)]  # vraie liste

for i in range(21):
    if i % 2:  # ajouter not ou ==0 pour les pairs
        print(i)

for i in range(1, 11):
    print(i*2)  # ajouter +1 pour les impairs

range(0, 21, 2)
range(1, 20, 2)
[x for x in range(1, 21) if x%2==0]
[2*x for x in range(1, 11)]  # ajouter +1...

```