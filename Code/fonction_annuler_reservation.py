def annuler_reservation():
    try:
        with open("reservations.csv", "r") as f:
            reservations = list(csv.reader(f))
            entete = reservations[0]
            reservations = reservation[1:]
    
