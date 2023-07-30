---
title: "Algorithmes avec piles et files"
tags:
    - info/algo
    - peda
    - -todo
---

## Présentation

...

## Problèmes classiques

Pour résoudre les problèmes suivants,
on dispose d'autant de piles que l'on veut,
et des structures classiques comme `Si` et `Tant_Que`...
mais pas aux listes par exemple.
On peut par exemple écrire:

```
P = nouvelle_pile()
Q = nouvelle_pile()
...
```

L'interface de ces piles est l'interface classique:
`empiler`, `dépiler`, `est_vide`.

Problème 0  
Longueur d'une pile.

Problème 0 bis  
Longueur d'une pile, mais sans modifier la pile.


Problème 1  
Présence d’une valeur dans une pile, sans altérer la pile.

On dispose d'une pile A qui contient des valeurs, et une valeur v.
Ecrire un algorithme qui indique si v est une valeur de A.
A la fin de l'exécution, A devra être revenue dans son état initial.

Votre algorithme était-il correct sur une pile vide?

Problème 2  
Retourner une pile.

On dispose d'une pile A qui contient des valeurs.
Ecrire un algorithme qui "retourne" la pile,
c'est-à-dire met les valeurs récentes en dessous et
les valeurs anciennes au dessus.

Votre algorithme était-il correct sur une pile vide?

Problème 3  
Séparer les pairs des impairs en les gardant dans l’ordre.

Problème 4  
Implémenter une File avec deux piles, une Pile avec deux files.
