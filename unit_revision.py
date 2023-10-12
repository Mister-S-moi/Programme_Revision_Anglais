


"""Fonction qui demande à l'utilisateur s'il souhaite réviser une catégorie, une semaine et/ou un ensemble de catégorie ou de semaine
NOTE : attention, la fonction retourne 3 string dont choixSemaine qu'il faudra convertir en entier
NOTE : on pourra ajouter une catégorie de révision par rapport à ce qui n'est pas bien appris"""
def choixRevision(listeCategories):
    typeRevision = input("\nVoulez vous réviser par rapport aux semaines (1) ou par rapport aux carégories (2) : ")
    
    if typeRevision == "1":
        choixRevisionSemaine = input("\nVoulez vous aussi réviser les semaines d'avant ? o/n : ")
        
        semaineCorrecte = False
        while not(semaineCorrecte):
            choixSemaine = input("Choisissez le numéro de la semaine : ")
            if (int(choixSemaine) > 0) and (int(choixSemaine) < 42):
                semaineCorrecte = True
        if choixRevisionSemaine != "o":
            return "revisionSemaine", "semaineUnique", choixSemaine
        else:
            return "revisionSemaine", "semaineAvant", choixSemaine
        
    else:
        print("\nVeuillez choisir la catégorie du mot : ")
        for loop in range(len(listeCategories)):
            print(loop + 1, " : ", listeCategories[loop])
        
        categorieCorrecte = False
        while not(categorieCorrecte):
            choixCategorie = input("\nEntrez le chiffre de la catégorie : ")
            if (int(choixCategorie) > 0) and (int(choixCategorie) < len(listeCategories) + 1):
                categorieCorrecte = True
        choixCategorie = listeCategories[int(choixCategorie)-1]
        return "revisionCategorie", "", choixCategorie
    

def recupDonneesRevision(typeRevision, estSemaineAvant, choix):    
    
    #on définit le bout d'instruction SQL qui nous permettra de récupérer ce que l'on veut réviser
    match typeRevision:
        case "revisionSemaine":
            match estSemaineAvant:
                case "semaineUnique":
                    conditionSQL = " WHERE semaine="+choix
                case "semaineAvant":
                    conditionSQL = " WHERE semaine<="+choix
        case "revisionCategorie":
            conditionSQL = " WHERE categorie="+choix
    
    
    #renvoie une liste de tuple que l'on ramenera à des CdC (ex : [('un',), ('deux',), ... ])
    cur.execute("SELECT francais FROM contenu"+conditionSQL)
    listeFrancais = cur.fetchall()
    #on remet la liste de tuple en liste de string
    for i in range(len(listeFrancais)):
        listeFrancais[i] = ''.join(listeFrancais[i])
    
    cur.execute("SELECT anglais FROM contenu"+conditionSQL)
    listeAnglais = cur.fetchall()
    #on remet la liste de tuple en liste de string
    for j in range(len(listeAnglais)):
        listeAnglais[j] = ''.join(listeAnglais[j])

    return listeFrancais, listeAnglais

