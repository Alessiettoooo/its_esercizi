max = float(input(f"inserisci il valore massimo"))
cont = 1

while True : 

    cont += 1
    n = float(input(f"inserisci il numero"))

    if n > max :
        
        max = n 
        
    if cont == 4 :
        
        print(f"il valore massimo è {max}")

        break


    
