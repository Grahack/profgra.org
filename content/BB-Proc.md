---
title: BBProc, le bébé processeur
tags:
  - -draft
  - info/archi
  - info/algo
  - classe/1NSI
---

## Présentation sur un premier exemple

Après avoir vu :
- le binaire et l’hexadécimal,
- quelques circuits électriques implémentant les fonctions logiques ET et OU,
- quelques montages avec des transistors implémentant d’autres fonctions logiques comme NOT et XOR, des bascules, des compteurs et des mémoires…

…on montre un diagramme séquentiel trouvé « dans la nature », afin d’expliquer ce qu’est une horloge et de donner quelques exemples de fréquences.

À chaque clic d’horloge, en combinant des opérations logiques élémentaires, le processeur effectue les opérations suivantes :

1. lecture de la valeur dans le registre PC (pour Program Counter), qui vaut `00` à l’initialisation ;
2. chargement de l’instruction située à l’adresse PC depuis la mémoire vive (RAM) dans le registre CI (pour Current Instruction) ;
3. « décodage » de l’instruction, ici ProkPap décode les trois quartets de l’instruction, notés I, J et K : I indique le type d’opération à effectuer et le couple JK représente souvent un emplacement dans la RAM (voir le tableau ci-dessous) ;
4. exécution de cette instruction (ne pas passer à l’étape 5 s’il faut s’arrêter !) ;
5. si l’instruction ne résulte pas par un saut ou un arrêt, ajouter 1 à PC.

Plus simplement :

1. où en est-on ?
2. que doit-on faire (récupération) ?
3. que doit-on faire (décodage) ?
4. faisons-le !
5. passons à la suite !

Voici une représentation schématique de la RAM avec un premier programme, sans doute le plus simple que l’on puisse écrire. Chaque « case mémoire » est repérée par l’abscisse K et l’ordonnée J (dirigée vers le bas) et peut stocker 12 chiffres binaires (donc 3 quartets).

```plain
J \ K |  0  |  1  |  2  | ...
------+-----+-----+-----+-----
   0  | A00 | ??? | ??? | ...
   1  | ??? | ??? | ??? | ...
   2  | ??? | ??? | ??? | ...
   .  .  .  .  .  .  .  .
   .  .  .  .  .  .  .  .
```

### Questions

- Combien y a-t-il d’emplacements dans la RAM ?
- Quelle est la taille de la mémoire en octets ?

Voici une représentation des registres. Chacun peut stocker 12 bits, sauf `O` qui en stocke un seul  et `PC` qui en stocke 8.

```plain
num | nom |   description          | valeur
----+-----+------------------------+--------
 0  |  R  | sorte de carrefour     | ???
 1  |  A  | sert aux ops. arithm.  | ???
 2  |  B  | idem                   | ???
 3  |  O  | dépassement (overflow) |   ?
 4  |  PC | Program Counter        |  00
 5  |  CI | Current Instruction    | ??? (notés IJK)
```

Les trois quartets de `CI` sont notés `IJK`, le `I` correspondant à une des instructions du tableau ci-dessous (chercher dans la colonne `I`) et le `J` et le `K` servant souvent à désigner une adresse dans la RAM (ligne `J` et colonne `K`).

```plain
 I | ASM |  Action ( -> signifie «est copié dans» )
---+-----+------------------------------------------
 0 |  LD | @JK -> R (la valeur à l’adresse JK dans la RAM est copiée dans R)
 1 | STO | R -> @JK (la valeur dans R est copiée à l’adresse JK dans la RAM)
 2 | MOV | Reg J -> Reg K (le registre num J est copiée dans le reg num K)
 3 | ADD | A+B -> R (somme des registres A et B copiée dans R, voir note (1))
 4 | SUB | A-B -> R (idem avec différence, voir note (2))
 5 | JMP | JK -> PC (la valeur JK est copiée dans PC, c’est un saut)
 6 | JPZ | Si R=0 alors JK -> PC (si la condition est vraie, on saute)
 7 | JPO | Si O=1 alors JK -> PC (idem)
 8 |  IN | User -> R (entrée d’une valeur par l’utilisatrice-teur)
 9 | OUT | R -> affichage
 A | END | arrêt du déroulement du programme

(1) si la somme A+B dépasse la capacité de R, le registre O vaut 1, 0 sinon
(2) si la différence A-B est négative, le registre O vaut 1, 0 sinon
```

`LD` pour « load », `STO` pour « store », `MOV` pour « move », `ADD` et `SUB` pour addition et soustraction, `JMP` ou `JP?` pour « jump », `IN` et `OUT` pour « entrée » et « sortie » et `END` pour « fin » (ou arrêt).

Exécutons le premier programme !

- Combien vaut PC ? `00`.
- À l’adresse `00` (J=0 et K=0) on trouve l’instruction `A00` que l’on charge dans CI.
- On a pour cette instruction I=A, J=0 et K=0, et d’après le tableau ci-dessous (dans la dernière ligne) il faut arrêter le programme.

> [!note]
> - Un registre est un type de mémoire rapide et « proche » du processeur.
> - PC est aussi parfois appelé IC pour Instruction Counter.
> - Le « décodage » se fait « mécaniquement » ou plutôt électroniquement avec les fonctions logiques qui ont été combinées.
> - Techniquement l’étape 4 fait partie de l’étape 3 car elle est réalisée directement.
> - Pour I=7 (`IN`) on peut imaginer que le processeur fait une pause pour qu’on ait le temps de lui communiquer la valeur.

Pour donner une image simplifiée d’un processeur qui « décode », on peut imaginer un circuit intégré branché de cette façon :

```plain
           12 bits de CI
            I    J    K    _________ connexion à la RAM (LD et STO) + I/O
          |||| |||| ||||  /
         +--------------+
  12 ---+|              |+===
bits ---+|              |+=== 8 bits
  de ---+|              |+=== de PC
   R ---+|              |+===
         +--------------+
           |||| ||||  |   \_________ connexion à l’horloge
             A    B   O
```

À vous d’écrire vos premiers programme :
 - afficher zéro et s’arrêter,
 - afficher « HELLO » et s’arrêter,
 - demander une valeur à l’utilisateur et afficher cette valeur plus un.

## Deuxième exemple

> [!note]
> Liste de tous les `MOV` :
> - 201 : R -> A
> - 202 : R -> B
> - 210 : A -> R
> - 212 : A -> B
> - 220 : B -> R
> - 221 : B -> A

Exécutez ce programme :

```plain
010 201 011 202 400 612 A00 ... ...
042 013 900 A00 ... ... ... ... ...
```

Idem en remplaçant 042 et 013 par 036 et 036.

Quel est le rôle de ce programme ?

## Exercices

- Afficher la plus grande de deux valeurs dans la RAM.
- Compte à rebours de la valeur à l’adresse `FF` jusqu’à zéro.

## TODO

Assembleur, assemblage, organise la mémoire à partir des mnémoniques, des labels…

Parler un peu de calculabilité.

V2, processeur de plus haut niveau, avec :
- Boutons
- PWS
- ALU

## Origine et remerciements

BB-Proc est le digne successeur d'[[OrdiPapier]], qui avait quelques défauts. BB-Proc a des entrées et sorties plus simples et utilise de l’hexadécimal.

Merci à Bordeaux (Philippe?), stagiaire et formation NSI.

