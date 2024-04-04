---
title: "Termux"
tags:
    - -draft
    - info
---
Appli Android qui fournit un terminal et un gestionnaire de paquets pour pouvoir disposer de nos commandes [[Shell]] préférées.

## Intérêt

Je l'utilise principalement pour:

- des [[Backups]] plus commodes avec [[rsync]],
- la synchro et la public de mon coffre [[Obsidian]] qui est dans un dépôt [[git]].

## Basic install

```shell
termux-setup-storage

apt update
# dl.bintra.com/grimler/science-packages-24 no Release file
# same with game-packages-24

apt upgrade
# use the new conf file for openssl and bash

pkg install vim git python  # and openssh if github needed
cp dotfiles/* .
mkdir .vim-tmp
```

## Github

```
pkg install openssh
# creates some key pairs
ssh-keygen -t ed25519 -C "your_email@example.com"
# fingerprint EIdKDiH4TUhx...
eval "$(ssh-agent -s)"  # ?

# copy the public key to github

ssh -T git@github.com  # OK, add to known_hosts

git clone git@github.com:Grahack/profgra.org.git .
```

