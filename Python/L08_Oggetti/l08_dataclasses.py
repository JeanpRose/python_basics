from dataclasses import dataclass

# scrivendo una classe in questo modo (con il decoratore)

@dataclass 
class Prodotto:
    nome:str
    prezzò : float 
    quant_disponibile : int

    def costo_totale (self):
        return self.prezzo * self.quant_disponibile


p1 = Prodotto("cioccolato", 2.5, 100 )

print(p1.costo_totale())