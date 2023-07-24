Écrire une classe qui passe les tests suivants:

ˋˋˋpython
>>> m = Monstre(18)  # nombre de têtes
>>> m.tetes
18
>>> m.ajouter--une--tete()
>>> m.tetes
19
>>> print("Le monstre crie", m.texte--du--cri(), ".")
le monstre crie aa...aa .  # avec 19 lettres "a"
ˋˋˋ

Indices pour la création du cri:

ˋˋˋpython
>>> "a" * 4
'aaaa'
>>> txt = ""
>>> for -- in range(4):
    txt = txt + "a"
>>> txt
'aaaa'
