---
title: "Activité rapide du monstre"
tags:
    - info/POO
    - info/lang/python
    - peda/actrapide
---

Écrire une classe qui passe les tests suivants:

```python
>>> m = Monstre(18)  # nombre de têtes
>>> m.tetes
18
>>> m.ajouter_une_tete()
>>> m.tetes
19
>>> print("Le monstre crie", m.texte_du_cri(), ".")
le monstre crie aa...aa .  # avec 19 lettres "a"
```

Indices pour la création du cri :

```python
>>> "a" * 4
'aaaa'
>>> txt = ""
>>> for _ in range(4):
    txt = txt + "a"
>>> txt
'aaaa'
```
