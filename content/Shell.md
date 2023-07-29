---
title: "Mémo shell"
tags:
    - info/lang/sh
---

## Recherche dans des fichiers

```sh
find . -type f -name "*.md*" -exec grep -il "truc" {} \;
```

## Recherche dans des fichiers avec contexte

```sh
find . -type f -exec grep -H -n -C2 --regexp="truc" {} \;
```
