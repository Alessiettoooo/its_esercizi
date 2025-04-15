import random 

posizione_ini = 1 
energia_iniziale = 100 
energia_lepre = energia_iniziale
energia_tartaruga = energia_iniziale
lunghezza = 70 


posizione_tart = posizione_ini
posizione_lep = posizione_ini


def visualizza(posizione_tart,posizione_lep) : 

    t = 0 
    l = 0 
    pista =["_"] * lunghezza
    posizione_tart = pista * t
    posizione_lep = pista * l


    return pista,posizione_tart,posizione_lep

def m_tart(t) :
    
    numero = input(random(1,11))

    if numero >= 1 and numero <= 5 : 

        t += 3 

    elif numero == 6 or numero == 7 : 

        t -= 6 

    else : 

        t += 1 

def m_lepre(l) : 

    numero = input(random(1,11))

    if numero == 1 or numero == 2 : 

        l = l

    elif numero == 3 or numero == 4 :

        l += 9 

    elif numero == 5 : 

        l -= 12

    elif numero >= 6 and numero <= 8 : 

        l += 1 

    else : 

        l -= 2 

m_tart()
m_lepre()
print(visualizza(posizione_lep,posizione_tart))

