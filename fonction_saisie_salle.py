def saisie_salle():
    with open("salles.txt", "r") as salles:
        liste_salles = salles.readlines()
        for nb_ligne, ligne in enumerate(liste_salles):
            if nb_ligne == 0:
                print(ligne)
            else:
                print(f"{nb_ligne}. {ligne}")
        try:
            nb_salle = int(input("Entrez l'identifiant numérique de la salle."))
            if nb_salle<1 or nb_salle>len(liste_salles)-1:
                raise ValueError("Cette entrée ne correspond pas à l'identifiant d'une des salles.")
        except ValueError as e:
            print("Erreur de valeur : ",e)
            try:
                nb_salle = int(input("Entrez l'identifiant numérique de la salle à nouveau."))
                if nb_salle<1 or nb_salle>len(liste_salles)-1:
                    raise ValueError("Cette entrée ne correspond pas encore une fois à l'identifiant d'une des salles.")
            except ValueError as e:
                print("Erreur de valeur : ",e)
                quit()
        for nb_ligne, ligne in enumerate(liste_salles):
            if nb_salle == nb_ligne:
                return ligne.split("\t")[0]
    
