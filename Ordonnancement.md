#classe/NSI #-draft 

# Ordonnancement

1. Observation de processus avec `ps aux`.
1. Définition de processus.

```
(nouveau) -1-> PRÊT <-3-2-> ÉLU -> (terminé)
                ˆ            |
                5-- BLOQUÉ <-4
```

1. Un nouveau processus arrive dans l’ensemble des
  processus «prêts».
1. Suivant une certaine stratégie, l’ordonnanceur
  choisit un processus parmi les «prêts». Il passe
  ainsi en statut «élu» et l’ordinateur pourra
  «travailler dessus».
1. Un autre processus a été choisi et «passe devant»
  le processus qui été élu.
1. Le processus a besoin d’une ressource, il est
  alors «bloqué» et sera débloqué quand la ressource
  sera disponible.
1. Ressource disponible, le processus repasse
  dans l’ensemble des processus «prêts».
1. Un processus est «terminé» quand il n’y a plus
  de travail à faire, donc l’état juste précédent était
  «élu».

Remarque: «nouveau» et «terminé» ne sont pas
vraiment des états car les processus n’y restent pas.

Questions:

1. Imaginer des stratégies pour le choix des
  processus prêts.

Indices:

1. Ce que l’on peut imaginer savoir sur les processus:
  date d’arrivée, durée d’exécution estimée, …