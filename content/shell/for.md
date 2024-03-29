---
title: "for"
tags:
    - info/lang/sh
---

## Iterates of files in a directory

```sh
for file in /dir/*
do
  echo "$file"
done
```

Same but in one line:

```sh
for f in *; do echo "$f";done
```
