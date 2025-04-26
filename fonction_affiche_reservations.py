import csv
def affiche_reservation():
    with open("reservations.csv", "r") as fichier_reservations:
        liste_reservations = csv.reader(fichier_reservations)
        next(liste_reservations)
        liste_reservations = list(liste_reservations)
        print("ID\tNU\tNS\tDate\t\tHeure\tDuré\n")
        for ligne in liste_reservations:
            print(f"{ligne[0]}\t{ligne[1]}\t{ligne[2]}\t{ligne[3]}\t{ligne[4]}\t{ligne[5]}")
affiche_reservation()
