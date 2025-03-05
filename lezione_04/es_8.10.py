lista = ["ciao come ti chiami ? "]

def show_message(lista) : 

    return lista



messaggio = input(f"scrivi un messaggio ")

def send_messages(messaggio) :
    
    send_messages =[messaggio] 

    return send_messages

s = show_message(lista)
print(*s)

t = send_messages(messaggio)
print(*t)