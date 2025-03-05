def describe_city(città, paese = "italia") :
    
    risultato = print(f"{città} è in {paese}")
    return risultato 

chiamata = describe_city(città = "roma")
chiamata = describe_city(città = "Napoli")
chiamata = describe_city(città = "lloret de mar", paese = "spagna")
