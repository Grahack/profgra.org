#info/lang/python 

# Comment utiliser Python

## Logiciels

Si vous préférez travailler en ligne de commande
pure, vous n’aurez pas besoin de cet article.
Dans le cas contraire vous aurez installé:
- soit uniquement le langage Python depuis
  [le site officiel](https://python.org)
  (ça me semble suffisant car IDLE sera compris),
- soit un logiciel qui intègre une zone d'édition
  de fichier et une zone pour la console interactive.

### Python et IDLE

L’éditeur IDLE est installé avec la plupart
des distributions minimales de Python.
Il est simple, sobre et efficace.
Au démarrage vous tombez dans la console interactive.
Je vous invite à ouvrir une fenêtre pour un nouveau
fichier (`ctrl+N`) et organiser votre écran
avec la console à droite et l’éditeur de fichiers à gauche :

```
+-------------------+  +-------------------+
+                   +  + Python 3.X.X ...  +
+                   +  + [???] on ???      +
+                   +  + Type "help", ...  +
+                   +  + >>>               +
+                   +  +                   +
+                   +  +                   +
+                   +  +                   +
+-------------------+  +-------------------+
```

### Autres logiciels

On peut citer :
- Spyder, qui est souvent installé avec des modules
  supplémentaires, voire comporte un gestionnaire de modules,
- des interpréteurs intégrés à une page web
  ([[Brython]], [[Python Tutor]]),
- personnellement je ne conseille pas Edupython.

## La console interactive

On la reconnait aux trois *chevrons* (trois signes
«supérieur») qui forment l'*invite de commande*
de Python dans TOUS les interpréteurs disponibles:

```python
>>> |
```

On y tape des expressions ou des instructions une
par une:

```python
>>> 2+2  # la valeur d'une expression est évaluée
4        # et affichée automatiquement, sans print
>>> # possible de taper des instructions sur
>>> # plusieurs lignes, dans ce cas «...» apparaît
>>> for i in range(3):
...     print(i)
0
1
2
```

À part avec un copié-collé, il n'est en général pas
possible de pouvoir enregistrer son travail.

La console interactive est tout de même pratique
pour des calculs uniques ou pour tester des petits
bouts de code en vue des les enregistrer dans un
fichier.

## Les scripts
On peut enregistrer un programme Python dans
un fichier (extension `.py`) en vue de le réutiliser.
On appelle ça un *script* ou même un *module*.

Lors de l'exécution, si le logiciel que vous utilisez
comporte une console interactive,
c'est là qu'auront lieu les interactions d’entrée et sortie:

- les *sorties* dues à `print`
- les *entrées* dues à `input`

Je répète : tout ça se fait dans la console.

## Compléments: doctest

#-todo
