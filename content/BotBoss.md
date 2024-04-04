---
title: BotBoss
tags:
  - musique/midi
  - musique/batterie
  - musique/basse
---

BotBoss est le patron des robots. Il joue du synthé-basse avec son bras gauche, et de la batterie avec ses trois autres membres. C'est un duo basse-batt à lui tout seul.

## Inception

- Xavier Tribolet sur un morceau de techno à la fin d'un concert de Clarika (fin 2007 début 2008?)
- Josh Dion, Nate Wood (deux [[Batteurs]] jouant du clavier en même temps que de la batterie)
- 25 septembre 2023 au lycée, une démo que j’ai eu à faire tout seul, merci COVID19

## Idées

- Click charley
- Sustain qui kick, ou qui sustain les deux kbds
- Ajouter du kick en parallèle de la basse
- Sustain pour basse le temps d'un fill monstrueux

## Équipement

- [[Raspberry Pi]] 3 + [[Pisound]]
- Novation [[Launchkey]] MK3
- [[MidiChief]], un client ALSA scriptable en [[Lua]]
- batterie hybride électro-acoustique

## Mémo canaux

```plain
ch info | ch humain | émission vers| recept. depuis
--------+-----------+--------------+---------------
   0    |     1     |     DAW*     |      DAW1
   1    |     2     |     NTS      |       LK
   2    |     3     |  Fluid (alt) |      alt
   3    |     4     |  Fluid (LK)  |       LK
   9    |    10     |  Fluid (dr)  | batt elec, LK ou alt
  15    |    16     |     DAW**    |      DAW2
```
-  `DAW1` le [[Launchkey]] envoie des infos (pads)
-  `DAW2` le [[Launchkey]] envoie des infos (pots)
- `DAW*` LEDs statiques pour le [[Launchkey]]
- `DAW**` LEDs clignotantes pour le [[Launchkey]] et passage en mode DAW
- `NTS` [[NTS|le petit synthé tout mignon]]
- `Fluid (alt)` souvent un son de piano, orgue, cordes, depuis le [[Keystation]] main droite
- `Fluid (LK)` souvent un son de basse depuis le [[Launchkey]] main gauche
- `Fluid (dr)` le canal percussions habituel
