class Dico:
    # méthode 1
    L_des_clefs = []
    L_des_valeurs = []
    # méthode 2
    L_paires_kv = []
    # méthode 3
    ...
    
    def keys(self):
        return ...
    
    def __setitem__(self):
        ...

dict_a_tester = dict  # à remplacer par Dico

d = dict_a_tester()  # instanciation
assert list(d.keys()) == []  # liste des clés

d.__setitem__("nom", "gragnic")  # ajouter k-v
assert list(d.keys()) == ["nom"]
assert d.__getitem__("nom") == "gragnic"  # récup
                                          # d["nom"]

d.__setitem__("prenom", "christophe")
assert list(d.keys()) == ["nom", "prenom"]
assert d.__getitem__("prenom") == "christophe"

d.__setitem__("nom", "autre")  # modifier k-v
assert d.__getitem__("nom") == "autre"  # récup


