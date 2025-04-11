def reserver():
    nom_utilisateur = input("À quel nom est la réservation?")
    print("Choisissez une salle parmie les suivant.")
    with open("salles.txt", "r") as salles:
        liste_salles = salles.readlines()
        for nb_ligne, ligne in enumerate(liste_salles):
            if nb_ligne == 0:
                print(ligne)
            else:
                print(f"{nb_ligne}. {ligne}")
        nb_salle = int(input("Entrez son identifiant numérique de la salle."))
        for nb_ligne, ligne in enumerate(liste_salles):
            if nb_salle == nb_ligne:
                nom_salle = ligne.split("\t")[0]
    print(nom_salle)
reserver()
