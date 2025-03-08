

class Persona: 
    def __init__(self, nome: str, cognome: str, eta : int):
        self.nome = nome
        self.cognome= cognome
        self.eta = eta

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if len(nome) >= 3: 
            self.__nome = nome
        else: 
            self.__nome = None

    @property
    def cognome (self):
        return self.__cognome
    
    @nome.setter
    def cognome (self, cognome):
        if len(cognome) >= 3: 
            self.__cognome = cognome
        else: 
            self.__cognome = None 
    @property
    def eta(self):
        return self.__eta
    
    @eta.setter
    def eta(self, eta):
        if eta >0: 
            self.__eta = eta
        else :
            self.__eta = None

if __name__ == "__main__":
    p1 = Persona ("C","rossi",12)
    
    print (p1.nome)