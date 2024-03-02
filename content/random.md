---
title: random
tags:
  - -draft
  - python
---

```python
>>> import random
>>> animaux = ["les souris", "le lion", "l’éléphant", "le ver de terre"]
>>> "%s mange %s" % (random.choice(animaux), random.choice(animaux))
'les souris mange l’éléphant'
```
