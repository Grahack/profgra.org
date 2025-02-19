import sqlite3
con = sqlite3.connect('test.db')
cur = con.cursor()

# lecture
if True:
    for row in cur.execute('''SELECT * FROM contacts
                              ORDER BY mois_naiss'''):
        print(row)
else:
# Pour afficher joliment:
    for row in cur.execute('''SELECT * FROM contacts
                              ORDER BY mois_naiss'''):
        print(row[0], row[1],
              "(", row[2], "/", row[3], "/", row[4], ")")
        print("{0} {1} ({2}/{3}/{4})".format(row[0],
                                        row[1],
                                        row[2],
                                        row[3],
                                        row[4]))
        print("{0}, {1} ({2}/{3}/{4})".format(*row))
        print()

# Essayez d'insérer un contact depuis Python
