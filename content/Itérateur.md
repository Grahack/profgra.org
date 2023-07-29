---
title: "Itérateur"
tags:
    - peda/actrapide
    - classe/TNSI
    - info/POO
    - info/lang/python
---

Définir une classe pour des objets de type
«itérateur» (comme un compteur).

On doit pouvoir fournir au constructeur un nombre
noté `n`, et l’objet aura une méthode `prochain`
qui ne prend pas d’argument mais retourne tour à
tour les nombres 0, puis 1, puis 2… jusqu’à `n`.
Après, la méthode `prochain` retournera `None`.

Exemple d’utilisation:

```python
compteur = Iterateur(3)
assert compteur.prochain() == 0
assert compteur.prochain() == 1
assert compteur.prochain() == 2
assert compteur.prochain() == 3
assert compteur.prochain() == None
assert compteur.prochain() == None
```

Quelles autres méthodes peut-on imaginer pour ce type d’objet?
