---
title: Racines
tags:
  - peda
  - maths
---

## Racine carrée

Voici trois opérations (ou fonctions) : ajouter 12, multiplier par 3, mettre au carré. Pour chacune d’elle, quelle est l’opération inverse ? Autrement dit, si le résultat est 16, quel était le nombre de départ ?

Pour le carré, il y a deux solutions : 4 et -4.

Pour tout nombre $a$ positif, $\sqrt{a}$ est le nombre positif dont le carré vaut $a$.

Autrement dit on a pour $a$ positif : $(\sqrt{a})^2 = a$.

Mais on a aussi $\sqrt{a^2} = a$, pourquoi ? Et si $a$ est négatif, que peut-on dire de $\sqrt{a^2}$ ?

### Relations avec les autres opérations

Pour tous nombres $a$ et $b$ positifs, on a $\sqrt{a}×\sqrt{b} = \sqrt{ab}$. Pourquoi ?

Trouver un contre-exemple à $\sqrt{a}+\sqrt{b} = \sqrt{a+b}$

### Valeurs approchées

D’après ce tableau donnant les carrés parfaits, on peut avoir une idée de la
valeur approchée de $\sqrt a$ en plaçant $a$ au bon endroit dans la colonne de
droite et en regardant la correspondance dans la colonne de gauche.

```plain
  n | n²
----+----
  0 |  0
  1 |  1
  2 |  4
  3 |  9
  4 | 16
  5 | 25
  6 | 36
```

C’est en fait l’algorithme de dichotomie, que l’on peut continuer pour obtenir
des décimales.

Notez qu’aucun nombre décimal ne peut convenir pour $\sqrt 2$.

### Simplification

En calculant $(2\sqrt 2)^2$ on réalise que $\sqrt 8 = 2 \sqrt 2$.

On aurait pu aussi l’expliquer en écrivant :

$$
\begin{align*}
 \sqrt 8 & = \sqrt{2^2 × 2} \\
 \sqrt 8 & = \sqrt{2^2} × \sqrt{2} \\
 \sqrt 8 & = 2 \sqrt 2
\end{align*}
 $$
