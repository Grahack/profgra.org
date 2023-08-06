---
title: "Activité rapide: listes aléatoires"
tags:
    - info/lang/python
    - peda/actrapide
---

## Rappels

### Nombres aléatoires

```python
import random
random.randint(1, 6)  # génère un nombre aléatoire entre 1 et 6 compris
```
### Ajouter (concaténation) une valeur à une liste

```python
L.append(v)  # ajoute la valeur v à la fin de la liste L
```

## Questions

1. Écrire une fonction qui attend un nombre `N` en paramètre et retourne
   une liste de `N` nombres aléatoires entre 1 et 6.
2. Écrire une fonction qui calcule la moyenne des valeurs d’une liste.
3. Utiliser la réponse aux deux questions précédentes pour estimer la valeur
   moyenne d’un lancer de dés.

