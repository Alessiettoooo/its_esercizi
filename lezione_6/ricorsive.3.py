def suminrange(a,b) -> int : 

    if a > b :

        temp = a 
        a = b 
        b = temp

    sum = 0 

    while b >= a : 

        sum = sum + b 
        b = b - 1 

    return int(sum)

print(suminrange(a = 5,b = 10))