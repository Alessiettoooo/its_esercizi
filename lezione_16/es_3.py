def recursivefactorial(n) : 

    if n == 0 : 

        return 0 
    elif n == 1 : 

        return 1 
    elif n > 1:

        return recursivefactorial(n*(n-1))
    
recursivefactorial(5)