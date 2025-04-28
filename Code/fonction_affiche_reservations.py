import csv
def affiche_reservation():
    with open("C:\\Users\\samue\\OneDrive - Collège Universel\\H2025\\Programmation_II_-_Debogage_informatique\\Travaux\\Projet\\Code\\Projet_debugage_H2025\\Code\\Fichiers\\reservations.csv", "r") as fichier_reservations:
        liste_reservations = csv.reader(fichier_reservations)
        next(liste_reservations)
        liste_reservations = list(liste_reservations)
        print("ID\tNU\tNS\tDate\t\tHeure\tDuré\n")
        for ligne in liste_reservations:
            print(f"{ligne[0]}\t{ligne[1]}\t{ligne[2]}\t{ligne[3]}\t{ligne[4]}\t{ligne[5]}")
