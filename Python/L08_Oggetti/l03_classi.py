class Persona:
    # costruttore
    def __init__(self, nominativo: str, eta:int):
        self.nominativo = nominativo.title()
        self.eta = int(eta)

    # rappresentazione in str dell'oggetto/istanza
    def __str__(self):
        return f"Nominativo: {self.nominativo} - età: {self.eta}"

class Automobile: 
    
    # metodo
    def __init__(self, marca: str, modello: str, prezzo_base : float, anno: int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.prezzo_base = prezzo_base
    
    def prezzo(self):
        prezzo = self.prezzo_base
        if self.marca.casefold()=="fiat":
            prezzo += 200
        elif self.marca.casefold()== "ferrari":
            prezzo *= 10
        
        if self.anno < 1980:
            prezzo /= 2 
        
        return prezzo
    
    def __str__(self):
        return f"""Marca : {self.marca}
Modello: {self.modello}  
Prezzo: {self.prezzo()}  
Anno: {self.anno} 
        
"""