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
                nom_salle = ligne.split("\t")[0]
    try:
        date = input("Pour quelle date souhaitez-vous faire la réservation? (format : AAAA-MM-JJ)")
        if len(date)!=10 or len(date.split("-")[0])!=4 or len(date.split("-")[1])!=2 or len(date.split("-")[2])!=2:
            raise ValueError("La date entrée ne respecte pas le format AAAA-MM-JJ")
        if int(date.split("-")[1]) not in range(1, 13):
            raise ValueError("Le mois entrée ne correspond pas à un mois du calendrier")
        if (int(date.split("-")[1]) in (1,3,5,7,8,10,12) and int(date.split("-")[2]) not in range(1,32)) or (int(date.split("-")[1]) in (4,6,9,11) and int(date.split("-")[2]) not in range(1,31)) or (int(date.split("-")[1])==2 and int(date.split("-")) not in range(1,30)):
            raise ValueError("La journée entrée ne correspond pas à une journée du calendrier.")
    except ValueError as e:
        print("Erreur de valeur : ", e)
        try:
            date = input("Pour quelle date souhaitez-vous faire la réservation? (format : AAAA-MM-JJ)")
            if len(date)!=10 or len(date.split("-")[0])!=4 or len(date.split("-")[1])!=2 or len(date.split("-")[2])!=2:
                raise ValueError("La date entrée ne respecte pas le format AAAA-MM-JJ")
            if int(date.split("-")[1]) not in range(1, 13):
                raise ValueError("Le mois entrée ne correspond pas à un mois du calendrier")
            if (int(date.split("-")[1]) in (1,3,5,7,8,10,12) and int(date.split("-")[2]) not in range(1,32)) or (int(date.split("-")[1]) in (4,6,9,11) and int(date.split("-")[2]) not in range(1,31)) or (int(date.split("-")[1])==2 and int(date.split("-")) not in range(1,30)):
                raise ValueError("La journée entrée ne correspond pas à une journée du calendrier.")
        except ValueError as e:
            print("Erreur de valeur : ", e)
            quit()
    heure = int(input("Pour quelle heure sohautez-vous faire la réservation? (format : hh)"))
    dure = int(input("Donnez la duré de votre réservation. Notez que la réservation doit être d'un minimum d'une heure. La duré se fait en incrément d'une heure."))
    reservation = [id_reservation,nom_utilisateur,nom_salle,date,heure,dure]
    with open("reservations.csv", "w") as fichier_reservation:
        ecrivain = csv.writer(fichier_reservation)
        
        ecrivain.writerow(reservation)
reserver()
