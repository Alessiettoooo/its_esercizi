nome = input(f"inserisci il nome")
ruolo =(input(f"inserisci il ruolo es Admin/Moderatore/Utente Adulto/Minorenne/Opsite"))
età  = int(input(f"inserisci l'età"))

diz = {"nome":nome,"ruolo":ruolo,"età":età}


    
match diz : 

    case diz if diz["ruolo"] == "admin" :
        print(f" il nome è {nome}") 
        print(f" il ruolo è {ruolo} ")
        print(f" l'età è {età} ")
        print(f" Accesso completo a tutte le funzionalità")

    case diz if ruolo == "moderatore" :
        print(f" il nome è {nome}") 
        print(f" il ruolo è {ruolo} ")
        print(f" l'età è {età} ")
        print(f" Salve {nome} può gestire i contenuti ma non modificare le impostazioni ")

    case diz if ruolo == "Utente adulto" and età >= 18  :
        print(f" il nome è {nome}") 
        print(f" il ruolo è {ruolo} ")
        print(f" l'età è {età} ")
        print(f" Accesso standard a tutti i servizi")

    case diz if ruolo == "Utente minorenne" and età <= 18  :
        print(f" il nome è {nome}") 
        print(f" il ruolo è {ruolo} ")
        print(f" l'età è {età} ")
        print(f" Accesso Limitato! solo visualizzazione dei contenuti")

    case _:

        print(f"Attenzione! Ruolo non riconosciuto! Accesso negato")