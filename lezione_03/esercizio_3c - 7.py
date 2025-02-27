i = 0
testa = 0 
croce = 0 
percentuale_testa = 0 
percentuale_croce = 0
while i <= 7 :

    i += 1
    lancio = str(input(f"lancio numero {i} cosa è uscito ?"))

    match lancio :

        case lancio if lancio == "c" or lancio == "C" :
            croce += 1
        
        case lancio if lancio == "t" or lancio == "T" :
            testa +=1
            
        case _:
            print(f"hai digitato la lettera errata")

percentuale_testa = (testa*100)/i
percentuale_croce = (croce*100)/i

print(f" Totale testa : {testa} Percentuale :{percentuale_testa}")


print(f" Totale Croce : {croce} Percentuale : {percentuale_croce}")