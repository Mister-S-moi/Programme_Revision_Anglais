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

#remplirBDD(listeCategories)

#print(choixRevision(listeCategories))

typeRevision, estSemaineAvant, choix = choixRevision(listeCategories)
print("test="+choix)
liste_fr, liste_ang = recupDonneesRevision(typeRevision, estSemaineAvant, choix)
print(liste_fr)
print(liste_ang)


#ISSUE : quand on valide rien pour le choix de la catégorie ça ne soulève pas d'erreur
#En fait il n'y a l'air d'avoir aucune vérif sur ce que j'entre

#le récup des données avec les semaines à l'air de fonctionné mais pas par rapport aux catégories
#C'est parce qu'il y a des guillemets en trop lorsque que je remplie les catégories de ma BDD (je n'ai pas 'Pollution' mais "'Pollution'")