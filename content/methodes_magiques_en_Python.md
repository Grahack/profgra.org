---
title: "Méthodes magiques en Python"
tags:
    - info/POO
    - info/lang/python
---

Elles sont de la forme `__XXX__` et permettent, entre autres, de donner un comportement à vos objets lorsqu’ils sont par exemple face à un opérateur, comme `+`.

```python
>>> class Truc:
...    pass
...
>>> o1 = Truc()
>>> o2 = Truc()
o1 + o2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    o1 + o2
TypeError: unsupported operand type(s) for +: 'Truc' and 'Truc'
class Truc:
    def __add__(self, other):
        return "ça fonctionne"

o1 = Truc()
o2 = Truc()
o1 + o2
'ça fonctionne'
```

Les plus utiles sont `__repr__` ou `__str__`.
