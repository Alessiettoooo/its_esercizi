from abc import ABC,abstractmethod
class FormaGenerica : 

    @abstractmethod 
    def draw(self) : 
        pass

    def setShape(self,shape) : 

        if shape:

            self.shape = shape

        else : 
            print(f"errore !!! la shape non può essere una stringa vuota ")

    def getShape(self):

        return self.shape