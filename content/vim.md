---
title: "vim"
tags:
    - info/outils/editeurs
---

```
set fileencoding=utf8
:w
```

## Remove duplicates

```
:sort u
:g/^\(.*\)$\n\1/d  # without sorting
                   # but removes blank lines
```
