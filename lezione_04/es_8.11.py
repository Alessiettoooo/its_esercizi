
def show_message(lista) : 

    for i in lista :
        print(i)

def send_messages(lista) :
    
    sent_messages =[] 

    for i in lista :
        print(i)
        sent_messages.append(i)
        lista.remove(i)

    return sent_messages

messageList =["ciao",  "come ti chiami ? "]
show_message(messageList) 

sent_messages = send_messages(messageList)

print(messageList)
print(sent_messages)
'''
messaggio = "scrivi un messaggio "



s = show_message(lista)
print(*s)

t = send_messages(messaggio)
print(*t)
'''