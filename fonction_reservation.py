import csv
def reserver():
    with open("reservations.csv", "r") as fichier_reservations:
        reservations = csv.reader(fichier_reservations)
        next(reservations)
        reservations = list(reservations)
        try:
            id_reservation = reservations[-1][0]+1
        except IndexError:
            id_reservation = 1
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
    date = input("Pour quelle date souhaitez-vous faire la réservation? (format : AAAA-MM-JJ)")
    heure = int(input("Pour quelle heure sohautez-vous faire la réservation? (fromat : hh)"))
    dure = int(input("Donnez la duré de votre réservation. Notez que la réservation doit être d'un minimum d'une. La duré se fait en incrément d'une heure."))
    reservation = [id_reservation,nom_utilisateur,nom_salle,date,heure,dure]
    with open("reservations.csv", "w") as fichier_reservation:
        ecrivain = csv.writer(fichier_reservation)
        
        ecrivain.writerow(reservation)
reserver()
