---
title: "Obsidian workflow"
tags:
    - obsidian
    - -todo
---

## Install

### Community plugins

* Homepage (pour prendre la place de l’utilisateur
  qui arrive sur mon site) avec la page
  `index.md` ouverte en mode « Vue ».  
  En fait un signet fait l'affaire.
* Customizable sidebar (pour la simplifier)
* ...

### Configuration

- Editor
  - Defaults to src
  - Strict line breaks ON (original MD)
  - Line wrap OFF (maîtrise des retours à la ligne)
  - Use tabs OFF
- Files & links
  - Auto update internal links ON
- Core plugins
  - Daily notes OFF
  - File recovery OFF
  - Starred OFF
  - Templates in tpl
  - Word count OFF
- File explorer with recent on top
    - easier to follow up
    - review from ancient files

## Sync

Dépôts git (termux, github, ordi perso)

## Sous répertoires

### Extensions

- `gif`
- `ods`
- `odt` (avec le pdf généré)
- `pdf` (seulement si je n’ai pas la version modifiable)
- `py`, `shell` (langages)
- exception : `img` pour les `.jpg`. et `.png`, `vid` pour les videos

### Autres sous-dossiers

- `bookmarks` (marque pages)
- `sng` (chansons)
- `std` (standards)
- `theorie` (des exemples pour chaque élément de théorie musicale)
- `tpl` (templates Obsidian)

## Tags

Les statuts commencent par un tiret:

* `-draft` pour les idées juste jetées, sans structure
* `-todo` la structure est présente mais la page a besoin d’être complétée,
  souvent où on voit des `...`.

Les autres tags sont des sujets, avec utilisation massive des sous-tags
(le séparateur est le `/`).

* bookmarks (pages au sujet des signets ou marque-pages, dont parfois certaines dans le dossier `bookmarks`)
* info
* info/POO
* info/algo
* info/archi
* info/fonctionnel
* info/hardware
* info/lang (pour les pages où on parle de plusieurs langages)
* info/lang/haskell (pour les pages en rapport avec ce langage)
* info/lang/python
* info/lang/sh
* info/outils
* info/outils/editeurs
* livre
* logique
* maths
* musique
* musique/basse
* musique/batterie
* musique/batterie/rudiments
* musique/clavier
* musique/exo
* musique/guitare
* musique/impro
* musique/meshuggah
* musique/metronome
* musique/outil
* musique/oreille (mettre la vid de max)
* musique/piano -> clavier
* musique/rythme
* musique/standard (pas de s)
* musique/theorie
* musique/triadpairs
* obsidian -> outil/obsidian??
* peda (pas la peine de remettre s’il y a déjà un tag classe/X)
* peda/actrapide
* peda/activite
* NSI (la discipline au lycée), vs les classes classe/1NSI
* prog (programmation)
* test
* viz

Idée du «portail» à creuser (tag portail?).

## Noms de fichiers

Il y a des conventions pour le nommage des fichiers.

* les classes (avec tags correspondants):
  * 1NSI.md classe/1NSI
  * TNSI.md classe/TNSI
  * STS_SIO.md classe/SIO (oui on mélange les deux niveaux)
* les leçons de youtubers: leurs initiales préfixent le nom du fichier
  * DF  Darryn Farrugia
  * EK  Espen Kraft
  * JD  Jazz Duets
  * JK  Jason Klubnak
  * JPB JP Bouvet
  - JN  Jeff Schneider
  * LK  Laurent Kremer
  * NGD Stephen Clark (Non Glamorous Drummer)
  * NS  Nate Smith (80/20 drummer)
  * OS  Open Studio
  * OWS Our Worship Sound
  * PNT Pianote
  * PT  Paul Thompson
  * QD  Quincy Davis
  * RC  Ross Campbell
  * RB  Rich Brown
  - ST  Stephen Taylor ([YT channel](https://www.youtube.com/@StephenTaylorDrums))
  * SVS Sir Valor Sax
  * WK  Wayne Krantz
  * ZG  Zack Grooves
