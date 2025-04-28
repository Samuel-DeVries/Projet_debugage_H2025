import csv
from fonction_saisie_date import saisie_date
from fonction_dispo import dispo
from fonction_saisie_salle import saisie_salle
def reserver():
    with open("C:\\Users\\samue\\OneDrive - Collège Universel\\H2025\\Programmation_II_-_Debogage_informatique\\Travaux\\Projet\\Code\\Projet_debugage_H2025\\Code\\Fichiers\\reservations.csv", "r") as fichier_reservations:
        reservations = csv.reader(fichier_reservations)
        next(reservations)
        reservations = list(reservations)
        try:
            id_reservation = int(reservations[-1][0])+1
        except IndexError:
            id_reservation = 1
    nom_utilisateur = input("À quel nom est la réservation?")
    print("Choisissez une salle parmie les suivant.")
    nom_salle = saisie_salle()
    date = saisie_date()
    heures = dispo(date, nom_salle)
    try:
        heure = int(input("Pour quelle heure sohautez-vous faire la réservation? (format : hh)"))
        if heure>23:
            raise ValueError("Le format de l'heure n'a pas été respecté")
        for h, d in heures.items():
            if int(h) == heure:
                if not d:
                    raise ValueError("Cette heure est indisponible")
        dure = int(input("Donnez la durée de votre réservation. Notez que la réservation doit être d'un minimum d'une heure. La durée se fait en incrément d'une heure."))
        if 24-heure<dure:
            raise ValueError("Le format de la duré n'a pas été respecté ou la duré entrée implique une fin de réservation qui serait dans une journée future.")
        for h, d in heures.items():
            if heure < int(h) < heure+dure:
                if not d:
                    raise ValueError("Une des heures de inclue dans cette réservation est indisponible.")
    except ValueError as e:
        print("Erreur de valeur : ", e)
        try:
            heure = int(input("Pour quelle heure sohautez-vous faire la réservation? (format : hh)"))
            if heure>23:
                raise ValueError("Le format de l'heure n'a pas été respecté")
            for h, d in heures.items():
                if int(h) == heure:
                    if not d:
                        raise ValueError("Cette heure est indisponible")
            dure = int(input("Donnez la durée de votre réservation. Notez que la réservation doit être d'un minimum d'une heure. La durée se fait en incrément d'une heure."))
            if 24-heure<dure:
                raise ValueError("Le format de la duré n'a pas été respecté ou la duré entrée implique une fin de réservation qui serait dans une journée future.")
            for h, d in heures.items():
                if heure < int(h) < heure+dure:
                    if not d:
                        raise ValueError("Une des heures de inclue dans cette réservation est indisponible.")
        except ValueError as e:
            print("Erreur de valeur : ", e)
            quit()
    reservation = [id_reservation,nom_utilisateur,nom_salle,date,heure,dure]
    with open("reservations.csv", "w", newline="") as fichier_reservation:
        ecrivain = csv.writer(fichier_reservation)
        ecrivain.writerow(["ID","Nom d'utilisateur","Nom de la salle","Date","Heure","Dure"])
        if reservations!=[]:
            ecrivain.writerows(reservations)
        ecrivain.writerow(reservation)
    print("La réservation à été effectuée avec succès. Prenez note de votre identifiant de réservation, soit le", id_reservation)
