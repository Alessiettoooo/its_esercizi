def make_album(autore,album) : 

    diz = {"autore":autore, "album":album}
    return diz

chiamata = make_album("lazza","sirio")
print(chiamata)

chiamata = make_album("fedez","bella vita")
print(chiamata)

chiamata = make_album("givanotti","bello mio")
print(chiamata)

while True : 


    
    autore = input("inserisci nome autore ")
    album = input(f"inserisci nome album ") 
    chiamata = make_album(autore,album)
    print(chiamata)

    break 
