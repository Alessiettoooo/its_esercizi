from formagenerica import FormaGenerica 

class Rettangolo(FormaGenerica):

    #inizializzare un oggetto della classe rettagolo

    def __init__(self):
        super().__init__()
                
        self.setShape("rettangolo")


    def draw(self):
        print(f"\n{self.getShape()}\n")

        # outer for 
        for i in range(5):

            for j in range(5*2):

                #lato a e b del rettangolo

                if i == 0 or i == 5-1:

                    print("*", end =" ")  

                elif j == 0 or j ==(5**2)-1:
                    print("*", end=" ")

                else : 
                    print(" ", end=" ")

            print("\n",end="")  