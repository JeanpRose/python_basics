
class Persona:
    def __init__(self, nome: str):
        self.set_nome(nome)

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome : str):
        if len(nome) >= 3: 
            self.nome = nome
        else: 
            self.nome = None 
        

p1 = Persona("c")
print (p1.nome)

