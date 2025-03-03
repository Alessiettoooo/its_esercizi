n = int(input("inserisci il numero"))

if n < 2 :

    print(f"il numero non è primo")
    
    
else : 

    div = 2

    while div <= n**0.5 :

        if n % div == 0 :

            print(f"il numero non è primo")

        else : 

            div = div + 1

    else : 

        print(f"il numero è primo")