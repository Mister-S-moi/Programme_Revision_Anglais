


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
            return("revisionSemaine", "semaineUnique", choixSemaine)
        else:
            return("revisionSemaine", "semaineAvant", choixSemaine)
        
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
        return("revisionCategorie", "", choixCategorie)
    
    
