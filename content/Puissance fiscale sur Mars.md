---
title: "Puissance fiscale sur Mars"
tags:
    - classe/TNSI
    - peda/actrapide
    - info/POO
    - info/lang/python
---

Sur Mars, on calcule la puissance fiscale
des véhicules avec le produit $n×mˆ2$, où:
* $n$ est le nombre de roues du véhicule,
* $m$ est la masse du véhicule en tonnes.

1. Écrire une classe Python qui modélise un
   véhicule martien et qui fera passer les
   tests suivants:

```python
v = VM(3, 1.5)
assert v.puiss() == 6.75
# accident
v.roues = 2
v.masse = 1.2
assert v.puiss() == 2.88
```

2. Ajouter une méthode `nouvelle_puissance`
   (et faire les autres modifications nécessaires)
   pour que le code suivant fonctionne:

```python
def f(n, m):
    return n+m

v.nouvelle_puissance(f)
assert v.puiss() == 3.2
```
