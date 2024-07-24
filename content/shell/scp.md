---
title: scp
tags:
    - info/lang/sh
---

```shell
# from distant to local current dir, one file
scp -P 8022 chri@192.168.1.108:/abs/path_to_file .
# from distant to local current dir, glob
scp -P 8022 chri@192.168.1.108:/path/*.txt .
# multiple files from local to distant
# the local and the distant are often inverted
scp files from local chri@192.168.1.158:/home/chri/
```