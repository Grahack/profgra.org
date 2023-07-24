On a 27 semaines pour 5 séquences,
donc 5×5 sem + 2 sem. Avec 2h par semaine,
on arrive par séquence à 10h de cours/TD + 5h TP.

# Séquence 1

- Maths
  - Base Numération
  - division euclidienne
  (définition mathématique seulement et utilisation calculatrice)
- Algo
  - Le robot peut être envoyé à la maison avec
    «qu’en avez-vous pensé? que penser du robot?»
  - Utilisation de Python (IDLE pour les grands débutants)
  - opérations arithmétiques
  - variables
  - appels de fonctions (print, input, bin, hex, int)
    pas de littéral autre que str

Intro possible pour Utilisation de Python avec [[Le jeu des allumettes]],
pour détecter les niveaux des étudiants.

DS vendredi 7 octobre, réserver une salle
pour S1S2 et S3S4.

# Séquence 2

- Maths
  - logique des propositions (non, et, ou, tables de vérité,
    expressions, De Morgan)
- Algo
  - opérateurs booléens
  - suite de `assert` pour tables de vérité
  - définition de fonctions, une expr booléenne peut
    être implémentée par une fonction de $Bˆn$ dans B
  - structure conditionnelle `if`, `else`, `elif`
  - peut-être les prédicats (dont la correspondance
    en Python serait des fonctions dans B)

Exemples:

```python
def expr1(P, Q, R):
    return (P and Q) or R
```
Définir une fonction qui modélise l’implication,
elle doit passer les tests:

```python
assert impl(False, False) == True
assert impl(False, True)  == True
assert impl( True, False) == False
assert impl( True, True)  == True
```

Attention, on veut faire correspondre les
concepts mathématiques avec le code Python,
mais on ne veut pas qu’ils les mélange sur leurs copies.

DS vers le vendredi 2 décembre.

