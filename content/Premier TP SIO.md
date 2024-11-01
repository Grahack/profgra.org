---
title: Premier TP SIO
tags:
  - SIO
  - info/lang/python
---

Le but de la séance est de :

- prendre en main [[Idle]]
- se familiariser avec les appels de fonctions (fonctions prédéfinies seulement) ;
- utiliser des variables et l’affectation ;
- découvrir les types de valeurs `int` et `str`.

Je tape le programme devant les étudiants et j’explique au fur et à mesure (voir les commentaires, que je tape aussi).

Voici le document que je distribue à la fin de la séance : [[odt/premier_TP_SIO.odt|odt]] et [[odt/premier_TP_SIO.pdf|pdf]].

## Premier programme version 1

```python
print("hello world")  # voir wikipedia

age = 14   # affectation de 14 à la variable age
print("votre age", age)

age_bin = bin(age)  # appel de la fonction
                    # bin avec pour argument
                    # la variable age
print("votre age en binaire", age_bin)

# inspection des types:
print(type(age), type(age_bin))
# int pour integer (nombre entier)
# str pour string (chaine de caractères)
```

## Premier programme version 2

Je reprends le même programme pour remplacer la ligne où 14 est « codé en dur » (« hardcodé »). On va plutôt interroger l’utilisateur ou l’utilisatrice.

```python
print("tapez votre age SVP")

age_txt = input()     # appel de fonction input
                      # sans argument
print(type(age_txt))    # inspection de la valeur
age = int(age_txt, 10)  # conversion str -> int
print("votre age", age)
  
age_bin = bin(age)  # appel de la fonction
                    # bin avec pour argument
                    # la variable age
print("votre age en binaire", age_bin)
```

## Bilan

Retenir :

- le caractère # indique un *commentaire* sur le reste de la ligne
- pour *appeler une fonction*, on tape son nom puis des parenthèses
- les *arguments* à cet appel de fonction se mettent dans les parenthèses
 - une fonction peut admettre aucun argument, ou un seul, ou plusieurs, ou même un nombre variable d’arguments (comme print) 
- le caractère = réalise une *affectation* d’une valeur à une *variable*
- la première affectation sur une variable est appelée *initialisation*

## Exercice

Il y a 6 types de conversion à connaître, et voici les fonctions Python correspondantes :

```plain
             D
           ^/ \^
int(?, 2) //   \\
         //     \\ int(?, 16)
        // bin   \\
       //     hex \\
      /v           v\
     B ============= H
```

Notez bien que `bin` et `hex` attendent un `int` et que `int` attend une `str`.

Le premier programme effectuait la conversion de D à B, écrivez les 5 programmes restants.

Finir à la maison et tester avec une installation de [[Python]].

La correction en [[odt/correc_programmes_conversions.odt|odt]] et en [[odt/correc_programmes_conversions.pdf|pdf]].