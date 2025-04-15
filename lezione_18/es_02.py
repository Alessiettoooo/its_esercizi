def validate_password(password="ciaone") : 

    lista_caratteri =["*","!",",",".","-","_","&","%"]
    cont_caratteri = 0  
    cont_maiuscole = 0 
    for i in password : 

        if i in lista_caratteri :

            cont_caratteri += 1

        elif i == i.upper() :

            cont_maiuscole += 1

        
    if len(password) == 20 and cont_caratteri >= 3 and cont_maiuscole >= 3 :

        print(f"la password è {password}")

    else : 

        raise InvalidPasswordError(f" la password non soddisfa i requisiti")
    
validate_password()

        

    



