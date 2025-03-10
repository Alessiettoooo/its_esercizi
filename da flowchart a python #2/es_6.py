x = float(input(f"inserisci valore di x"))
somma = 0
if x > 0 : 

    i = 0 

    while i != 10 :

        n = float(input(f"inserisci valore n"))

        if x % 2 == 0 and n > x / 2:

            somma = somma + n

        elif n < x : 

            somma = somma + n 

        i = i + 1

    print(f"la somma è {somma}")
else : 

    print(f"errore il numero {x} deve essere positivo ")