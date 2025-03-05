def make_shirt(taglia = "Large",scritta = "I love Python") : 

    riassunto = print(f"la taglia è {taglia} e la scritta è {scritta}")
    return riassunto

risultato = make_shirt()
risultato = make_shirt(taglia = "Medium")
risultato = make_shirt(taglia = "small", scritta = "I hate Python")



