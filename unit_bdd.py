#importation de la bibliothèque pour gérer les BDD
import sqlite3

"""Fonction permettant la création d'une BDD nommée souillard.db qui est la version simple du projet
NOTE : si jamais vous venez à changer le code de creationBDD() il faut supprimer l'ancienne BDD avant de relancer la fonction"""

def creationBDD():
    #connexion vers notre BDD avec une création implicite si elle n'existe pas
    con = sqlite3.connect("souillard.db")

    #création d'un curseur nécessaire à l'envoi de requête SQLite
    cur = con.cursor()
    print("Connexion réussie")
    
    instructionCreationBDD_1 = '''  CREATE TABLE "contenu" (
                                        "francais"	TEXT NOT NULL,
                                        "anglais"	TEXT NOT NULL,
                                        "categorie"	TEXT NOT NULL,
                                        "semaine"	INTEGER NOT NULL,
                                        FOREIGN KEY("francais") REFERENCES "revision"("francais") ON UPDATE CASCADE,
                                        PRIMARY KEY("francais","anglais"),
                                        FOREIGN KEY("anglais") REFERENCES "revision"("anglais") ON UPDATE CASCADE
                                    );'''
    
    cur.execute(instructionCreationBDD_1)
    
    instructionCreationBDD_2 = '''  CREATE TABLE "revision" (
                                        "francais"	TEXT NOT NULL,
                                        "anglais"	TEXT NOT NULL,
                                        "nb_vrais"	INTEGER NOT NULL,
                                        "nb_faux"	INTEGER NOT NULL,
                                        "date_derniere_revision"	TEXT,
                                        "nb_vrais_sucessifs"	INTEGER NOT NULL,
                                        PRIMARY KEY("francais","anglais")
                                    );'''
                                
    cur.execute(instructionCreationBDD_2)

    print("Création réussie")
    
    
    
creationBDD()
