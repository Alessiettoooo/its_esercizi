
def show_message(lista) : 

    for i in lista :
        print(i)

def send_messages(lista):
    
    sent_messages =[] 

    while len(lista) > 0:
        message = lista.pop(0)
        print(message)
        sent_messages.append(message)

    return sent_messages

messageList =["ciao",  "come ti chiami ? "]
messageList_new = messageList.copy()
show_message(messageList) 

sent_messages = send_messages(messageList)

print(messageList)
print(sent_messages)

print(messageList)
print(messageList_new)
'''
messaggio = "scrivi un messaggio "



s = show_message(lista)
print(*s)

t = send_messages(messaggio)
print(*t)
'''