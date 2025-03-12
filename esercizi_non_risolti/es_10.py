'''
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

    acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
    calcolare e visualizzare la somma di tutti i numeri pari inseriti;
    calcolare e visualizzare la media di tutti i numeri dispari inseriti;
    determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
    se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
'''

pari = 0 
dispari = 0 
cont = 1
somma = 0 

while True :

    n = int(input(f"inserisci un numero (0 per terminare): "))

    if n % 2 == 0 : 

        pari = pari + n 

    if n % 2 == 1 : 

        somma = somma + n
        cont += 1

    if n == 0 : 
        
        dispari = somma / cont
        break

print(f"la somma dei numeri pari è {pari}")
print(f"la media dei numeri dispari è {dispari}")

