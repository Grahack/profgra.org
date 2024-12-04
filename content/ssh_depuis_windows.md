---
title: "ssh depuis Windows"
tags:
    - info/git
---

## Key pair generation

In git bash :

```shell

$ ssh-keygen -t ed25519 -C "email@mail.com"
```


## Install and start ssh agent

In an admin elevated powershell :

```shell
> Get-Service ssh-agent | Set-Service -StartupType Automatic -PassThru | Start-Service
...
> start-ssh-agent.cmd
...
> ssh-add.exe ..\..\Users\XXX\.ssh\id_ed25519
```


# Configure git bash

```shell
ssh-add ~/.ssh/id_ed25519  # if not done previously
git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe
cat ~/.ssh/id_ed25519  # to add to https://github.com/settings/keys
```