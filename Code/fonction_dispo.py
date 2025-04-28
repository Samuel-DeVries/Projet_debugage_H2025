import csv
def dispo(date, nom_salle):
    with open("C:\\Users\\samue\\OneDrive - Collège Universel\\H2025\\Programmation_II_-_Debogage_informatique\\Travaux\\Projet\\Code\\Projet_debugage_H2025\\Code\\Fichiers\\reservations.csv", "r") as fichier_reservations:
        liste_reservations = csv.reader(fichier_reservations)
        next(liste_reservations)
        liste_reservations = list(liste_reservations)
        reservations_a_date = []
        for reservation in liste_reservations:
            if reservation[2] == nom_salle and reservation[3] == date:
                reservations_a_date.append(reservation)
    reservations_a_date.sort(key=lambda x: int(x[4]))
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
    return heures

