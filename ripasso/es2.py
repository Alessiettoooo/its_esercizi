def esercizio1(lista : list[int]  ) -> dict : 

    diz : dict = {}
    lista1 =[]
    lista2 =[]  
    for numero in lista :

        if numero  >= 0 :

            lista1.append(numero) 
            diz[0].append(lista1)

        else : 

            lista2.append(numero)
            diz[1].append(lista2)

       
        
    
    
        return diz

lista=[2,4,6,44,3] 

print(esercizio1(lista))

    
    


