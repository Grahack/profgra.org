---
title: "Mémo shell"
tags:
    - info/lang/sh
---

## Pages

- [[shell/for]]
- [[shell/scp]]
- [[shell/sed]]

## Commandes diverses

### Recherche dans des fichiers

```sh
find . -type f -name "*.md*" -exec grep -il "truc" {} \;
```

### Recherche dans des fichiers avec contexte

```sh
find . -type f -exec grep -H -n -C2 --regexp="truc" {} \;
```
