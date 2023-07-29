---
title: "Xile"
tags:
    - classe/TNSI
    - peda/actrapide
    - info/POO
---

Un fou a inventé la structure de données `Xile`.

C’est comme une *pile* mais qu’on peut
transformer en *file* à la volée en appelant la
méthode `change` (sans argument). Un nouvel
appel à la méthode `change` repasse du
comportement *file* au comportement *pile*.

On sait de plus que les méthodes habituelles
`empile` et `enfile` ont été renommées en
`enxile`, et les méthodes `depile` et `defile`
en `dexile`.

1. Écrire des tests.
2. Écrire la classe `Xile` qui fait passer les tests
    de la première question.

Indices:

```python
L.append(valeur)  # ajoute valeur en queue de L
L.pop()   # retire et renvoie la valeur en queue de L
L.pop(0)  # retire et renvoie la valeur en tête de L
```

Exemples de tests:

```python
x = Xile()
x.enxile("A")
x.enxile("B")
assert x.dexile() == "B"
x.enxile("B")
x.change()
assert x.dexile()=="A"
```
