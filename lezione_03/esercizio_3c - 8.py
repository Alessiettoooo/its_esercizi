cont = ""
i = 0 
frase = str(input(f"inserisci una frase "))

for cont in frase : 

    i +=1

match frase : 

    case frase if frase[-1] == "?" and i % 2 == 0 :
        print(f"si")  
    
    case frase if frase[-1] == "?" and i % 2 == 1 :
        print(f"No")

    case frase if frase[-1] == "!" : 
        print(f"WoW")

    case _:
        print(f" tu dici  \"{frase}\" ") 

    


