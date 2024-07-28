---
title: Les trois programmes
tags:
  - peda
  - info/lang/python
  - 1NSI
  - exercice
---

Voici trois « programmes » qui travaillent sur la même liste. Le but de l’exercice est de comprendre ce qu’ils font.

1. Après lecture du code, pouvez-vous dire ce que fait chacun des trois programmes ? Si oui, donnez un titre à chacun.
1. Si non, traduisez chaque ligne de code en français et relisez cette traduction. Est-ce plus clair ?
1. Toujours pas ? Alors jouez le rôle de l’ordinateur, de tête ou à l’aide d’un papier et d’un crayon. Après avoir « fait tourner » les programmes, pouvez-vous donner un titre à chacun ?
1. Toujours pas ? Alors copiez-collez-les dans l’interpréteur Python de votre choix et exécutez-les. Est-ce plus clair ?

```python
L = [-5, 13, 3.2, 7, -2, 5.13, 52, -10, 12, -7]

# programme 1
i = 0
R = 0
while i < 10:
    if L[i] < 10:
        R = R + 1
    i = i + 1
print(R)

# programme 2
i = 0
R = 0
while i < 10:
    if L[i] > R:
        R = L[i]
    i = i + 1
print(R)

# programme 3
i = 0
R = 0
while i < 10:
    R = R + L[i]
    i = i + 1
print(R)
```