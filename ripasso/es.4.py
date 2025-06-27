def verifica(x,y,z) : 

    if (x == True )and y == True or z == True : 

        return "azione permessa"
    
    else :

        return "azione negata"
    
x = True 
y = False
z = False

print(verifica(x,y,z))