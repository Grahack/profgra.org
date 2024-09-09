---
title: Binaire et héxadécimal
tags:
  - info
  - NSI
---

Voir le [[premier_tableau_bin_hexa.odt|doc élève]].

Il y a 6 types de conversion à connaître :

```plain
    D
  // \\
 B === H
```

- Les deux horizontales sont les plus faciles (quartet après quartet, voir plus loin).
- Viennent ensuite les deux vers le haut, qui utilisent le tableau des puissances de 2 ou 16 et des additions.
- Les deux vers le bas sont les plus difficiles, et chacune des deux peut se faire de gauche à droite ou de droite à gauche.
  - D->B de gauche à droite : on met un 1 dans la plus grande puissance de 2 qui est inférieure au nombre à convertir, puis on continue avec le reste.
  - D->H de gauche à droite : après avoir trouvé la plus grande puissance de 16 inférieure au nombre à convertir, on effectue la division, puis on continue avec le reste.
  - D->B et D->H de droite à gauche : on divise par 2 ou 16, le reste donne le chiffre à écrire à droite et on continue avec le quotient.

$$16^n = 16×16×…×16 = 2^4 × 2^4 × … × 2^4 = 2^{4n}$$

Donc les puissances de 16 sont aussi des puissances de 2 : toutes les 4 colonnes dans le tableau des puissances de 2 on trouve une puissance de 16.

```plain
  8192 |   4096 ||  2048 |  1024 |   512 |   256 ||  128 |   64 |   32 |   16 || 8 | 4 | 2 | 1
2×16^3 | 1×16^3 || 8×256 | 4×256 | 2×256 | 1×256 || 8×16 | 4×16 | 2×16 | 1×16 ||
8 | 4 | 2 | 1
           4096 ||                           256 ||                        16 ||             1
```
