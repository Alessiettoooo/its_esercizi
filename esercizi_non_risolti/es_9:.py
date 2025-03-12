risultato = 1

def cambio_segno(target:str = "3.14") : 

    segno: int = 1
    pi : float = 0
    den: int = 1
    counter = 0
    

    while True: 

        pi += segno * (4/den)
        

       #risultato = risultato * segno, pi/den
        segno *= -1
        den += 2
        counter += 1

        
        if str(pi)[:len(target)] == target:

            print(f"le iterazioni per raggiungere {target} sono {counter}")

            break
cambio_segno(target="3.14") 
cambio_segno(target="3.141")        
cambio_segno(target="3.1415")               
cambio_segno(target="3.14159")  
     













    


