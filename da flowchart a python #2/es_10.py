eta = int(input(f"inserisci eta "))

if eta >= 18 and eta <= 65 : 

    print(f"può partecipare all'attività")

elif eta < 18 : 

    print(f"non puoi partecipare all'attività perchè non hai raggiunto l'età minima richiesta")

else : 

    print(f"non puoi partecipare all'attività perchè hai superato l'eta massima consentita")