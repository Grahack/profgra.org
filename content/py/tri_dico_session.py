>>> liste_de_dicos = []
>>> liste_de_dicos.append({"A":3, "B":1, "C":2, "D":1})
>>> liste_de_dicos.append({"A":2, "B":1, "C":4, "D":3})
>>> liste_de_dicos.append({"A":4, "B":2, "C":1, "D":4})
>>> liste_de_dicos.append({"A":1, "B":2, "C":3, "D":2})
>>> print(liste_de_dicos)
[{'A': 3, 'B': 1, 'C': 2, 'D': 1}, {'A': 2, 'B': 1, 'C': 4, 'D': 3}, {'A': 4, 'B': 2, 'C': 1, 'D': 4}, {'A': 1, 'B': 2, 'C': 3, 'D': 2}]
>>> for dico in liste_de_dicos:
	print(dico)

{'A': 3, 'B': 1, 'C': 2, 'D': 1}
{'A': 2, 'B': 1, 'C': 4, 'D': 3}
{'A': 4, 'B': 2, 'C': 1, 'D': 4}
{'A': 1, 'B': 2, 'C': 3, 'D': 2}
>>> def affiche(liste):
	for elt in liste:
	    print(elt)

>>> affiche(liste_de_dicos)
{'A': 3, 'B': 1, 'C': 2, 'D': 1}
{'A': 2, 'B': 1, 'C': 4, 'D': 3}
{'A': 4, 'B': 2, 'C': 1, 'D': 4}
{'A': 1, 'B': 2, 'C': 3, 'D': 2}
>>> l = [4, 3, 5, 2]
>>> l
[4, 3, 5, 2]
>>> sorted(l)
[2, 3, 4, 5]
>>> l
[4, 3, 5, 2]
>>> l.sort()
>>> l
[2, 3, 4, 5]
>>> affiche(sorted(liste_de_dicos))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    affiche(sorted(liste_de_dicos))
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> def clef(dictionnaire):
	return dictionnaire["A"]

>>> affiche(sorted(liste_de_dicos, key=clef))
{'A': 1, 'B': 2, 'C': 3, 'D': 2}
{'A': 2, 'B': 1, 'C': 4, 'D': 3}
{'A': 3, 'B': 1, 'C': 2, 'D': 1}
{'A': 4, 'B': 2, 'C': 1, 'D': 4}
>>> def valeur_en_B(dictionnaire):
	return dictionnaire["B"]

>>> affiche(sorted(liste_de_dicos, key=valeur_en_B))
{'A': 3, 'B': 1, 'C': 2, 'D': 1}
{'A': 2, 'B': 1, 'C': 4, 'D': 3}
{'A': 4, 'B': 2, 'C': 1, 'D': 4}
{'A': 1, 'B': 2, 'C': 3, 'D': 2}
