from fonction_reservation import *
from fonction_affiche_dispo import *
from fonction_affiche_reservations import *
from fonction_annule_reservation import *
while True:
    print("==== Reserver avec SFNJ ====")
    print("            Menu           ")
    print("1. Réserver une salle")
    print("2. Afficher les disponibilités")
    print("3. Annuler une réservation")
    print("4. Lister toutes les réservation actuelles")
    print("5. Quitter")
    action = int(input("Entrez le chiffre de l'action voulue: "))
    if action == 1:
        reserver()
    elif action == 2:
        affiche_dispo()
    elif action == 3:
        annule_reservation()
    elif action == 4:
        affiche_reservations()
    elif action == 5:
        print("Merci d'avoir utilisé SFNJ. Au revoir!")
        quit()
    else:
        raise ValueError("Veuillez choisir une option entre 1 et 5")
