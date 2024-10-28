---
title: Hotel infini
tags:
  - -draft
  - maths
---

## Description de l'hôtel

Ch numerotees avec ces nombres entiers: 1, 2, 3...

C'est l'hôtel de Hilbert, voir WP.

FAQ

- Dernière chambre? Pas de dernière chambre.
- Ça existe ? Non.

## Un voyageur

Un voyageur arrive, mais l'hôtel est complet. Comment lui trouver une place?

Dans ce problème et les suivants, la reorganisation doit consister en un déplacement des clients. Vous devez leur indiquer dans quelle chambre aller.

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

## Quarante-deux voyageurs

Un car de quarante-deux voyageurs arrivent, mais l'hôtel est complet. Comment leur trouver une place à chacune et chacun?

Vous devez réorganiser l'hôtel et donner une chambre à chaque voyageur.

### Solution

Différentes façons d'expliquer la solution :

- Chaque client va dans la chambre 42 numéros après la sienne.
- Le client de la chambre $n$ va dans la chambre $n+42$.

Ainsi les 42 premières chambres sont libérées pour le car.

```plain
[---------------- . . .
X X ... X [------ . . .
```

### Conclusion

Il y a autant de chambres dans cet hôtel que de chambres plus une. Si on note $\aleph$ ce nombre, on a $\aleph = \aleph + 42$.

## Un car infini

Même numérotation que l'hôtel.

## Un car infini des deux côtés

Places négatives

## Quarante-deux cars infinis

Un seul côté, le PB est équivalent.

## Une infinité de cars infinis

Cars numérotés comme l'hôtel, avec places numerotées comme l'hôtel.

$$n = \frac{x(x+1)}{2} + \left[ x(y+1) + \frac{(y-1)(y-2)}{2} \right]$$
La démonstration vous est laissée en exercice.
