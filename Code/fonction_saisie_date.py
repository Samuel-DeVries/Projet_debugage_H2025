def saisie_date():
    try:
        date = input("Saisissez la date (format : AAAA-MM-JJ)")
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
    return date
