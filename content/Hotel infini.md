---
title: Hotel infini
tags:
  - maths
---

## Description de l'hôtel

Nous avons un hôtel tout à fait classique, avec des chambres numérotées avec des nombres entiers: 1, 2, 3... sauf qu’il est infini : la suite des chambres ne s’arrête pas.

C'est l'hôtel de Hilbert (1925), voir [WP](https://fr.wikipedia.org/wiki/H%C3%B4tel_de_Hilbert).

### FAQ

- Quel est le numéro de la dernière chambre ? Un symbole particulier ?  Il n’y a pas de dernière chambre.
- Ça existe un hôtel comme ça ? Non.

## Problème du voyageur

Un voyageur arrive, mais l'hôtel est complet. Comment lui trouver une place ?

Dans ce problème et les suivants, la réorganisation doit consister en un déplacement des clients. Vous devez leur indiquer dans quelle chambre aller. Aucun client ne peut effectuer de déplacement infini.

Si besoin, voir la FAQ concernant l'hôtel.

### Solution

Différentes façons d'expliquer la solution :

- Chaque client va dans la chambre suivante.
- Le client de la chambre $n$ va dans la chambre $n+1$.

```plain
[----------- . . . 
X [--------- . . . 
```

### Conclusion

Il y a autant de chambres dans cet hôtel que de chambres plus une. Si on note $\aleph$ ce nombre, on a $\aleph = \aleph + 1$.

On peut aussi dire qu’il y a autant de nombres dans $\mathbb N^*$ que dans $\mathbb N$.

## Problème des quarante-deux voyageurs

Un car de quarante-deux voyageurs arrive, mais l'hôtel est complet. Comment trouver une place à chacun des voyageurs ?

### Solution

Différentes façons d'expliquer la solution :

- Chaque client va dans la chambre 42 numéros après la sienne.
- Le client de la chambre $n$ va dans la chambre $n+42$.
- On répète 42 fois la solution du problème précédent.

Ainsi les 42 premières chambres sont libérées pour le car.

```plain
[---------------- . . .
X X ... X [------ . . .
\___42__/
```

### Conclusion

Il y a autant de chambres dans cet hôtel que de chambres plus 42. Si on note $\aleph$ ce nombre, on a $\aleph = \aleph + 42$.

## Problème du car infini

Un car infini arrive, mais l'hôtel est complet.

### Description du car

Il est numéroté comme l'hôtel, donc possède les mêmes propriétés mathématiques.

### Solution

Différentes façons d'expliquer une solution :

- Chaque client va dans la chambre double de la sienne.
- Le client de la chambre $n$ va dans la chambre $2×n$.

Ainsi les chambres impaires sont libérées pour le car.

Une autre façon d’imaginer la solution : les voyageurs sortent du car pour faire une file, les clients sortent de l’hôtel pour faire une file à côté des nouveaux arrivants, puis on prend une personne de chaque file pour aller dans une chambre sur deux.

### Conclusion

Comme le car et l’hôtel sont équivalents, on peut dire qu’il y a autant de chambres dans cet hôtel que de chambres dans deux de ces hôtels. Si on note $\aleph$ ce nombre, on a $\aleph = 2×\aleph$.

On peut aussi dire qu’il y a autant de nombres pairs (ou impairs) dans $\mathbb N$ que de nombres dans $\mathbb N$.

## Problème du car infini des deux côtés

Un car « infini des deux côtés » arrive, mais l'hôtel est complet.

### Description du car

Il est numéroté comme le car précédent, mais avec une place numérotée 0 et autant de places avec un numéro négatif que le car précédent.

### Solutions

#### Solution n°1

Le plus simple est de comprendre que ce problème est équivalent à la réorganisation du car précédent (infini « d’un seul côté »). En effet, en faisant deux files de voyageurs (par exemple avec les places positives et les places négatives) puis en prenant les voyageurs par deux, on obtient l’équivalent du car précédent (une place impaire, une place paire).

#### Solution n°2

On dispose les voyageurs en deux files comme précédemment, puis on demande aux clients de l’hôtel d’aller au triple de leur chambre.

### Conclusion

On peut aussi dire qu’il y a autant de nombres dans $\mathbb Z$ que dans $\mathbb N$.

## Quarante-deux cars infinis

Les cars sont tous identiques à celui du problème avec le car infini.

### Solution

On peut multiplier le numéro de chambre par 43 ou répéter la solution pour un seul car autant de fois qu’il faut.

## Une infinité de cars infinis

C’est là que ça commence à être drôle : une infinité de cars infinis arrivent. Les cars sont numérotés comme les chambres de l'hôtel, et dans chacun il y a des places numérotées comme les chambres de l'hôtel.

### Indices

- On peut commencer par vider l’hôtel (comme pour une des solutions précédentes) pour simplifier un peu le problème. Les clients formeraient ainsi un car supplémentaire, qui se fond dans l’infinité des cars (voir le tout premier problème !).
- L’espaces des voyageurs est un quart de plan, l’hôtel une demi-droite. Plutôt qu’essayer de « faire rentrer le quart de plan dans la demi-droite », on peut imaginer « dessiner la demi-droite dans le quart de plan ».

### Solution

En notant $x$ le numéro du car, $y$ le numéro de la place d’un voyageur, et $n$ le numéro de la chambre où ce voyageur doit aller, on peut utiliser :
$$n = \frac{x(x+1)}{2} + \left[ x(y+1) + \frac{(y-1)(y-2)}{2} \right]$$
La démonstration vous est laissée en exercice.

Nan bon allez OK on la fait.

On numérote les cases du quart de plan ainsi :

```plain
y \ x |  1 |  2 |  3 |  4 |  5 |  6
------+----+----+----+----+----+-----
   1  |  1 |  3 |  6 | 10 | 15 | 21
   2  |  2 |  5 |  9 | 14 | 20 |  .
   3  |  4 |  8 | 13 | 19 |  . |  .
   4  |  7 | 12 | 18 |  . |  . |  .
   5  | 11 | 17 |  . |  . |  . |  .
   6  | 16 |  . |  . |  . |  . |  .
 ...  |  . |  . |  . |  . |  . |  .
```

Dans la première ligne, on reconnaît les nombres triangulaires. Donc si $y=0$, on a :

$$ n = \frac{x(x+1)}{2} $$
C’est la première partie de la formule. Pour la partie entre crochets, on s’aperçoit que sur une même colonne on passe à la case d’en-dessous en ajoutant une valeur qui augmente de 1 en 1. Sauf que la première valeur à ajouter change à chaque fois, mais on la reconnaît : c’est $x$.

La valeur à ajouter aux valeurs de la première ligne est donc cette somme :

$$ x + (x+1) + (x+2) + ... + ? $$
On sait de plus que cette somme possède $y-1$ termes car c’est le nombre de sauts pour arriver à la ligne numéro $y$. On peut la calculer de deux façons : la formule générale ou le regroupement des $x$.

1. La formule générale donne $\frac{1}{2}(y-1)(x + (x + y - 2))$ car on connait le nombre de termes, le premier terme, et le dernier est $x + (y-2)$.
2. Le regroupement des $x$ donne d’abord $x(y-1)$, puis la somme de 0 à $y-2$, soit $\frac{(y-1)(y-2)}{2}$.

Et on a bien :
$$x(y-1) + \frac{(y-1)(y-2)}{2} = \frac{1}{2}(y-1)(x + (x + y - 2))$$

La démonstration par récurrence est laissée en exercice.