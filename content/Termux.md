---
title: "Termux"
tags:
    - -draft
    - info
---

## Purpose

I mainly use Termux on Android for:

- easier [[Backups]],
- sync of my [[Obsidian]] git repository.

## Basic install

```shell
termux-setup-storage

apt update
# dl.bintra.com/grimler/science-packages-24 no Release file
# same with game-packages-24

apt upgrade
# use the new conf file for openssl and bash

apt install vim git python
cp dotfiles/* .
mkdir .vim-tmp
```

## Github

```
apt install openssh
# creates some key pairs
ls ~/.ssh
ssh-keygen -t ed25519 -C "your_email@example.com"
# fingerprint EIdKDiH4TUhx...
eval "$(ssh-agent -s)"

# copy the public key to github

ssh -T git@github.com  # OK

# ?? ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

git clone git@github.com:Grahack/ProfGra.git .
# ? git clone ssh://username@domain.example/P.git .
```

