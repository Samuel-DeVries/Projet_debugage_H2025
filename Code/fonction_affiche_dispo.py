from fonction_dispo import dispo
from fonction_saisie_date import saisie_date
from fonction_saisie_salle import saisie_salle
def affiche_dispo():
    date = saisie_date()
    print("Entrez le nom de la salle dont vous souhaitez vérifier la disponibilité.")
    nom_salle = saisie_salle()
    heures = dispo(date, nom_salle)
    print("Voici la disponibilité pour cette journée : ")
    for heure, disponible in heures.items():
        if disponible:
            print(f"{heure} : Disponible")
        else:
            print(f"{heure} : Indisponible")
