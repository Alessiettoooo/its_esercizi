def sum(n :int) -> int : 

    if n < 0 : 

        print(f"errore")

    else : 
        
        sum = 0 
        while n : 

        
            sum += n 
            n = n - 1

        return int(sum)

print(sum(5))
