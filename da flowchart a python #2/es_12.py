n = int(input(f"insersci n "))
i = 0 

while i != n : 

    x = int(input(f"insersci valore x "))
    y = int(input(f"insersci valore y "))

    if x > 0 and y > 0 : 

        result = x * y 
        print(f"il risultato è {result} ")

    elif x < 0 and y < 0 : 

        print(f"errore")

    else : 

        result = x - y
        print(f"il risultato è {result}")

    i = i + 1 