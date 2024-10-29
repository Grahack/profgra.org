# Voici le code du programme de la momie !
from random import randint

points_de_vie = 1
score = 0

while points_de_vie > 0:
    porte_momie = randint(1, 3)
    print("Trois portes devant toi. Laquelle ouvrir : 1, 2, ou 3 ?")
    porte_choisie = int(input())
    if porte_choisie == porte_momie:
        print("Une momie te dévore !")
        points_de_vie = 0
    else:
        print("La pièce est vide, tu entres.")
        score = score + 1

print("Le jeu est fini, ton score est", score)
