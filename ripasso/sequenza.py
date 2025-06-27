x : int = int(input('inserire un numero '))
pos = 0 
somma = 0 
if x % 1 == 0:
    lista = [] 
   
    while True :
        n = int(input("scrivi 0 se vuoi terminare l'inserimento dei numeri "))
        if n == 0 :
            break
        b = int(input("inserisci la sequenza di numeri "))
        if b % 1 == 0 and b > 0 :
            lista.append(b)

        else : 
            print(f"devi inserire un numero intero o positivo")

        

    print(f"la sequenza è {lista}")
    for a in lista :

        if x == a :


            pos = lista.index(a)
            continue

    for c in lista :

        if c != x :

            somma += c 


print(f"la posizione dell'elemento x ossia {x} nella lista {lista} è {pos}")
print(f"la somma dei valori della sequenza diversi da {x} è {somma}")





