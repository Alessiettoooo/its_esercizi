max = float(input(f"inserisci massimo"))
cont = 1

while cont < 4 :

    cont += 1
    n = float(input(f"inserisci il numero"))

    if n > max :

        max = n

print(f"il numero massimo è {max}")

