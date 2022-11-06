class Truc:
    "doc"
    def __str__(self):
        return "ceci est ma représentation textuelle"

t = Truc()
print(t)

class Compteur:
    "doc"
    valeur = 0
    def __str__(self):
        return str(self.valeur)

c = Compteur()
print(c.valeur)
print(c)

