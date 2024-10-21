---
title: Complément à deux
tags:
  - NSI
  - info/encodage
---

# Mise en place

On peut introduire l’idée en classe en proposant aux élèves d’inventer un moyen d’encoder les nombres entiers relatifs sur 8 bits.

# À savoir

- introduit par Von Neumann en 1945
- taille des mots $N$ à fixer
- principe
  - positifs comme d’habitude
  - $n + (-n) = 0$ avec retenue ignorée
- trucs à savoir
  - bit de signe à la place du bit le plus fort
  - inversion puis +1
  - inversion à gauche du premier 1 en partant de la droite
  - 0 est en fait $2^N$, donc $-n = 256 - n$