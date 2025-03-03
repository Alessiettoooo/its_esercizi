x = float(input(f"inserisci cordinata x"))
y = float(input(f"inserisci cordinata y"))

cordinate =(x,y)

match cordinate : 

    case cordinate if x == 0 and y == 0 :
        print(f"il punto {cordinate} si trova nell'origine")

    case cordinate if y == 0 :
        print (f"il punto {cordinate} si trova sull'asse X")

    case cordinate if x == 0 :
        print(f"il punto {cordinate} si trova sull'asse Y")

    case cordinate if x > 0 and y > 0 :
        print(f"il punto {cordinate} si trova nel primo quadrante")

    case cordinate if x < 0 and y < 0 :
        print(f"il punto {cordinate} si trova nel terzo quadrante")

    case cordinate if x > 0 and y < 0 :
        print(f"il punto {cordinate} si trova nel quarto quadrante")

    case _:
        print(f"nulla")