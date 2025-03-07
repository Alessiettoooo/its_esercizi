liberi = 20


while True :

    opzione = input(f"inserisci opzione prenota-libera-visualizza-esci")


    match opzione : 

        case "prenota" : 

            if liberi > 0 :

                liberi = liberi - 1

            else : 

                print(f"non ci sono posti disponibili")

        case"libera" : 

            if liberi < 20 :

                liberi = liberi + 1

            else : 

                print(f"tutti i posti sono gia disponibili")

        case "visualizza" :

            print(f"i posti liberi sono {liberi}")
            print(f"i posti occupati sono {20-liberi}")

        case "esci" :

            break

        case _:

            print(f"comando non valido")
