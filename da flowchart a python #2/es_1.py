max_posti = input(f"inserisci posti massimi")
liberi = max_posti

while True :

    opzione = input(f"inserisci opzione ingresso-uscita-stato-esci")


    match opzione : 

        case "ingresso" : 

            if liberi > 0 :

                liberi = liberi - 1

            else : 

                print(f"non ci sono posti disponibili")

        case"uscita" : 

            if liberi < max_posti :

                liberi = liberi + 1

            else : 

                print(f"tutti i posti sono gia disponibili")

        case "stato" :

            print(f"i posti liberi sono {liberi}")
            print(f"i posti occupati sono {max_posti-liberi}")

        case "esci" :

            break

        case _:

            print(f"comando non valido")
