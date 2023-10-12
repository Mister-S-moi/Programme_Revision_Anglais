exec(open("./unit_bdd.py").read())
exec(open("./unit_revision.py").read())

import sqlite3
from datetime import datetime

#Toujours se connecter à la BDD
#connexion vers notre BDD avec une création implicite si elle n'existe pas
con = sqlite3.connect("souillard.db")

#création d'un curseur nécessaire à l'envoi de requête SQLite
cur = con.cursor()
print("Connexion réussie")

#Attention, s'il faut changer le nom d'une catégorie déjà existante dans la BDD il faudra être prudent
listeCategories = ["'Units and measures'",
                    "'Common abbreviations'",
                    "'Acronyms and abbreviations'",
                    "'Expressions de liaison'",
                    "'False friends'",
                    "'Idioms'",
                    "'Prepositions'",
                    "'Technology and basic engineering'",
                    "'Employment'",
                    "'Information technology'",
                    "'Pollution'",]

#Début réel du prgramme

remplirBDD(listeCategories)

print(choixRevision(listeCategories))

recupDonneesRevision(choixRevision(listeCategories))