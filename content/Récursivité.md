---
title: Récursivité
tags:
  - info/rec
  - classe/TNSI
---

```python
def listes_bool(taille):
    print("on demande la taille", taille)
    if taille == 0:
        return [[]]
    else:
        L = []
        for l in listes_bool(taille-1):
            L.append(l+[False])
            L.append(l+[True])
        return L
```
