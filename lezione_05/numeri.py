def prime_factors(n: int) -> list[int]:
    lista = []
    result = 1
    c = 2
    while c == 1 : 
        
        if n % c == 0 :
            
            ris = n / c
            lista.append(c)
            
        elif n % 3 == 1 : 
            
            c = 3
            ris = n / c 
            lista.append(c)
            
        elif n % 5 == 1 : 
            
            c = 5
            ris = n / c 
            lista.append(c)
            
        elif n % 7 == 1 : 
            
            c = 7
            ris = n / c 
            lista.append(c)
            
        else : 
            
            break
            
    for n in lista :
        
        result *= n
        
        
        if result == n : 
            
            return lista
        
        
        
print(prime_factors(60))