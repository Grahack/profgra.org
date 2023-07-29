---
title: "Activité rapide sur les tris de dictionnaires"
tags:
    - info
    - peda/actrapide
---

1. On considère une liste de dictionnaires :

```python
L = [{"prenom": "arthur", "nom": "truc"},
      "prenom": "john",   "nom": "bidule"}]
```

Que vaut `sorted(L)` ?

2. On a défini une fonction `f` :

```python
def f(d):
    return d['nom']
```

Que vaut `sorted(L, key=f)` ?
