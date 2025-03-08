class Persona:
    #di base le classi hanno questo costruttore
    # def __init__(self):
    #     pass

    """_summary_
            Classe che descrive una persona
            con nome cognome e età
        Returns:
            _type_: _description_
            __init__: restiuisce gli attributi nome,cognome, età
           __scheda__ : restituisce la scheda (è un metodo)
           _cambia_nome_ : serve per cambiare nome e cognome
           
        """
    # costruttore
    def __init__(self, nome: str, cognome: str, eta:int):
        self.nome = nome.capitalize()
        self.cognome = cognome
        self.eta = int(eta)
    
    # metodo istanza
    def scheda (self):
        return f"Nome: {self.nome} - Cognome: {self.cognome} - età: {self.eta}"
    # metodo istanza
    def cambia_nome (self, nome : str, cognome: str):
        self.nome = nome
        self.cognome = cognome

    # rappresentazione in str dell'oggetto/istanza
    def __str__(self):
        return f"Nome: {self.nome} - Cognome: {self.cognome} - età: {self.eta}"





p1 = Persona("CASA", "PANE",2)
print (p1.scheda())

print ()

# se cè str non cè bisogno di creare un metodo wchedq
p2 = Persona("Giovanni", "Rana", 70)
print (p2)

p2.cambia_nome("Mario", "Rossi")

print (p2)