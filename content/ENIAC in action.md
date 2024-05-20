---
title: ENIAC in action
tags:
  - -draft
---

[[ENIAC]]

## Introduction

- entonnoir à double sens

## 1 - Imagining ENIAC

- électricité commerciale 1880
- électronique radar fin 30s
- draft april 1943
- balistique au centième de seconde
- sur le terrain: pas efficace (ne tue pas assez de gens)
- "human computers"
- I/O électronique 1000× plus rapide que la version mécanique
- IBM en 1943?
- équations différencielles
- Irven Travis' digital diffence analyser 1940, clock problem not solved
- accumulator, multiplier (and adder)
- constant transmitter and recorder (I/O)
- complément à 10: -15 sur 4 chiffres stocké comme 9985
- les accumulateurs ont deux sorties: une pour le nombre et une pour son opposé
- accumulateurs à 10 chiffres car les erreurs de troncature (discrétisation temporelle) et d'arrondi (discrétisation de valeur) étaient prévues sur 5 chiffres et on voulait une précision de 5 chiffres

## 2 - Structuring ENIAC

- prototype à deux accumulateurs pour la faisabilité, besoin d'un élément coordinateur avant d'avoir bien réfléchi à la programmation
- décentralisation, encapsulation
- premier programme par Burks?
- vocabulaire : «programme»?
- intégration par pas de 2 dixièmes de seconde
- temps de calcul compté en "addition times"
- la multiplication prend qques unités
- parallélisation
- une trajectoire: 2000 étapes en 70s
- deux diagrammes (séquence et câblages) à convertir en à peu près 200 "program cards"
- l'encapsulation a permis d'obtenir une bonne longévité
- "master programmer" pour
  - conditions initiales
  - intégration
  - impression
  - vérifications (avec jeu de données maîtrisé)
- invention des registres pour séparer l'arithmétique du stockage
- 20 accumulateurs, 3 tables de fonctions, multiplieur, diviseur/extracteur de racine, transmetteur de constante, "unit cycle", imprimante, "master programmer"
- conditionnelles seulement en 1945 (ex: arrêter qd une variable dépasse une valeur)
- plus que les conditionnelles, les ingénieurs ont aussi réfléchi à enchaîner des jeux d'instruction plus complexes
- intégration tous les centièmes puis tous les millièmes de secondes quand on se rapproche de la seconde
- universel: peut simuler n'importe quel autre ordinateur
- d'abord basé sur le signe d'un accumulateur (stocké dans le registre PM)
- davantage de considération dans le "sequence programming", les conditionnelles ne seront finalement pas mises en place mais intégrées dans les capacités de comptage et de contrôle déjà requises par le master programmer
- description d'idées rejetées, comme le bifurcator, mais elles ressurgiront
- "program pulses" et "data pulses" sur deux réseaux différents, mais besoin de les faire communiquer pour les conditionnelles
- possibilité de sous-routine
- fin 1944, réflexion plus abstraite sur le contrôle
- dénomination: "sign discrimination", possible sans master programmer
- des détournements astucieux d'éléments existants ont permis de nouvelles fonctionnalités

## 3 - Bringing ENIAC to life

- le problème du matériel: difficulté de se le procurer en temps de guerre
- équipe de "production", surtout des femmes
- environ 18000 tubes fragile, donc peu de chances de finir un calcul!
- tubes testés et ENIAC peu éteint
- "testing table"
- le maillon lent: les entrées-sorties
- operators < programmers (to highlight the creative and mathematical aspects, and the deep understanding needed)
