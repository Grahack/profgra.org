---
title: Numération
tags:
  - -draft
  - classe/SIO
  - -todo
  - maths/numération
---

## Activité introductive

### Énoncé

Un fainéant en a assez de devoir utiliser beaucoup 
de chiffres pour écrire de grands nombres. Aidez-le
à inventer d'autres chiffres et un système pour les
utiliser.

### Plénière de régulation 

On se met d'accord sur ces chiffres: A, B, C, D...

### Bilan

Tant qu'on a des chiffres disponibles, on utilise ces chiffres
(dans l'ordre). Une fois qu'on a plus de chiffre disponible
on repart à zéro et on met une retenue dans la colonne de
gauche, en propageant la retenue si besoin.

## Hexadécimal

16 chiffres

Puissances de 16

## Binaire

Deux chiffres, compatible avec l'hexadécimal

## Conversions

il y en a 6 à connaître:

- bin>hex et hex>bin triviales
- bin>dec et hex>dec avec tableau puissances
- dec>bin et dec>hex
  - de g à d avec tab puiss ou
  - de d à g avec div euc

Feuille [[Quartets et octets célèbres]]

## Opérations

Savoir mettre en place l'addition, la soustraction
et la multiplication.

## Complément à 2

### Énoncé 

On dispose de 8 bits. On sait qu'on peut coder 256
valeurs, comment peut-on s'organiser pour coder
des nombres entiers négatif, zéro, et des nombres
positifs?

### Plénière de régulation 

Élaguer puis proposer d'additionner -1 et 1.

### Bilan

#### Idée

Jusqu'à 126, c'est comme d'habitude et pour
les négatifs on prend le nombre dont la somme
avec l'opposé fait 256. Comme ça si on ne
tient pas compte de la retenue la somme
est nulle.

#### Autres formulations ou calculs
