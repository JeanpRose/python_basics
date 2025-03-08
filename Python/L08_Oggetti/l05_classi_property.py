
class Persona : 
    def __init__(self, nome: str, cognome: str, eta : int):
        self.nome = nome
        self.cognome= cognome
        self.eta = eta

    def get_nome(self):
        return self.__nome
    
    def set_nome (self, nome):
        if len(nome) >= 3: 
            self.__nome = nome
        else: 
            self.__nome = None 
    

    def get_cognome (self):
        return self.__cognome
    
    def set_cognome (self, cognome):
        if len(cognome) >= 3: 
            self.__cognome = cognome
        else: 
            self.__cognome = None 

    def get_eta(self):
        return self.__eta

    def set_eta(self, eta):
        if eta >0: 
            self.__eta = eta
        else :
            self.__eta = None

    nome = property(get_nome, set_nome)
    cognome = property(get_cognome, set_cognome)
    eta = property(get_eta, set_eta)




p1 = Persona("RO", "T", 0)
print (p1.eta)