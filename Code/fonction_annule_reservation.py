import csv
def annule_reservation():
        with open("Fichiers\\reservations.csv", "r") as f:
                reservations = list(csv.reader(f))
        try:
                identifiant = int(input("Saisissez l'identifiant de la réservation que vous souhaitez annuler."))
                ids = []
                for ligne in reservations:
                        if ligne[0] == "ID":
                                continue
                        else:
                                ids.append(ligne[0])
                if str(identifiant) not in ids:
                        raise ValueError("Aucune réservation existante avec cette identifiant.")
                for ligne in range(len(reservations)):
                        if ligne == 0:
                                continue
                        elif reservations[ligne][0] == str(identifiant):
                                del reservations[ligne]
                                break
                with open("Fichiers\\reservations.csv", "w", newline="") as fw:
                        ecrivain = csv.writer(fw)
                        ecrivain.writerows(reservations)
                print("Suppression effectuée avec succès.")
        except ValueError as e:
                print("Erreur de valeur : ", e)
