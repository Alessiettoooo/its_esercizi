pari = 0 
dispari = 0 
cont = 0 

for cont in range (1,10 + 1) :

    n = float(input(f"inserisci numero"))

    if n % 2 == 0 :

        pari = pari + 1

    else :

        dispari = dispari + 1 

    cont = cont + 1

print(f"i numeri pari sono : {pari}")
print(f"i numeri dispari sono : {dispari }")

