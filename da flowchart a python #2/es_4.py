n_tutor = 10
attesa = 0 

while n_tutor != 0 and attesa < 50 : 
    
    studente = input(f"inserisci studente")

    if n_tutor > 0 :

        attesa = attesa + 1
        print(f"studente in attesa")

    else :

        n_tutor = n_tutor-1
        print(f"tutor assegnato con successo")


     