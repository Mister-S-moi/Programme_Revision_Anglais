#importation de la bibliothèque pour gérer les BDD
import sqlite3
from datetime import datetime

"""Fonction permettant la création d'une BDD nommée souillard.db qui est la version simple du projet
NOTE : si jamais vous venez à changer le code de creationBDD() il faut supprimer l'ancienne BDD avant de relancer la fonction"""

def creationBDD():
    
    instructionCreationBDD_1 = '''  CREATE TABLE "contenu" (
                                        "francais"	TEXT NOT NULL,
                                        "anglais"	TEXT NOT NULL,
                                        "categorie"	TEXT NOT NULL,
                                        "semaine"	INTEGER NOT NULL,
                                        "dateAjout" INTEGER NOT NULL,
                                        PRIMARY KEY("francais","anglais")
                                    );'''
    
    cur.execute(instructionCreationBDD_1)
    
    instructionCreationBDD_2 = '''  CREATE TABLE "revision" (
                                        "francais"	TEXT NOT NULL,
                                        "anglais"	TEXT NOT NULL,
                                        "etatReussite"	TEXT NOT NULL,
                                        "dateRevision"	TEXT NOT NULL,
                                        PRIMARY KEY("francais","anglais"),
                                        FOREIGN KEY("francais") REFERENCES "contenu"("francais") ON UPDATE CASCADE,
                                        FOREIGN KEY("anglais") REFERENCES "contenu"("anglais") ON UPDATE CASCADE
                                    );'''
                                
    cur.execute(instructionCreationBDD_2)

    print("Création réussie")
    
    
    
"""Fonction qui permet de remplir la table contenu avec des entrées utilisateur
NOTE : attention, si vous avez changé le nom de la BDD il faudra aussi l'éditer ici
NOTE : cette fonction permet de remplir la BDD dans sa version simple"""

def remplirBDD():
    motFrancais = input("\nVeuillez entrer le mot français : ")
    motAnglais = input("\nVeuillez entrer le mot anglais : ")
    
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
    
    print("\nVeuillez choisir la catégorie du mot : ")
    for loop in range(len(listeCategories)):
        print(loop + 1, " : ", listeCategories[loop])
    
    categorieCorrecte = False
    while not(categorieCorrecte):
        categorie = input("\nEntrez le chiffre de la catégorie : ")
        categorie = int(categorie)
        if (categorie > 0) and (categorie < len(listeCategories) + 1):
            categorieCorrecte = True
    
    print("\nVeuillez choisir la semaine du mot : ")
    
    semaineCorrecte = False
    while not(semaineCorrecte):
        semaine = input("Entrez la semaine du mot : ")
        semaine = int(semaine)
        if (semaine > 0) and (semaine < 42):
            semaineCorrecte = True
            
    #instruction SQLite pour mettre les données dans la table contenu
    cur.execute("""INSERT INTO contenu (francais, anglais, categorie, semaine, dateAjout) VALUES (?,?,?,?,?)""",(motFrancais, motAnglais, listeCategories[categorie-1], semaine, datetime.today().strftime('%Y-%m-%d')))
    con.commit()    #Nécessaire avec l'instruction INSERT
    
def rien2():
    return 0




    
#Toujours se connecter à la BDD
#connexion vers notre BDD avec une création implicite si elle n'existe pas
con = sqlite3.connect("souillard.db")

#création d'un curseur nécessaire à l'envoi de requête SQLite
cur = con.cursor()
print("Connexion réussie")
#Début réel du prgramme
creationBDD()
remplirBDD()
