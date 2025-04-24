import csv
def affiche_dispo():
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
    with open("reservations.csv", "r") as fichier_reservations:
        liste_reservations = csv.reader(fichier_reservations)
        next(liste_reservations)
        liste_reservations = list(liste_reservations)
        reservations_a_date = []
        for reservation in liste_reservations:
            if reservation[3] == date:
                reservations_a_date.append(reservation)
    #reservations_a_date.sort(key=lambda x: int(x[4]))
    for ir in range(len(reservations_a_date)):
        reservations_a_date[ir].append(int(reservations_a_date[ir][4])+int(reservations_a_date[ir][5]))#Ajout de l'heure de fin
    heures = {}
    for h in range(24):
        heures[str(h)]=True
    for reservation in reservations_a_date:
        for heure, dispo in heures.items():
            if dispo == True:
                if int(reservation[4])<=int(heure)<=int(reservation[6]):
                    heures[heure] = False
    print("Voici la disponibilité pour cette journée : ")
    for heure, disponible in heures.items():
        if disponible:
            print(f"{heure} : Disponible")
        else:
            print(f"{heure} : Indisponible")
affiche_dispo()
