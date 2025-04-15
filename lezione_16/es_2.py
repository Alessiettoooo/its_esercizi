def compoundinterest(m,t) : 

    if t == 0 : 

        return m 
    
    else :

        return compoundinterest(m * 1.005,t - 1)
    
print(compoundinterest(3, 4))
