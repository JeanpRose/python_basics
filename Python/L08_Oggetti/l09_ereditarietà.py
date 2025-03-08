# Persona -- nome, cognome
# Studente -- [nome, cognome], voto
# Insegnante -- [nome, cognome], materia


class Persona:
    def __init__(self, nome: str, cognome: str):
        self.nome = nome
        self.cognome = cognome
    
    def iniziali(self):
        return f"{self.nome[0]} {self.cognome[0]}"
    
    # __str__ è un metodo già presente in object(classe da cui deriva tutto)
    # attraverso questa definizione stiamo andando a ridefinirne
    # il funzionamento in questa classe -> OVERRIDE
    # Override del metodo
    def __str__(self):
        return f"Nominativo: {self.nome} {self.cognome}"
    
    # se voglio un doppio init
    # con @classmethod andro a creare dei metodi che sono indipendenti
    # dalle istanze. i metodi saranno richiamabili direttamente con la
    # . notatiom sul nome della classe
    # cls viene sostituita in base alla classe da cui 
    # richiamiamo il metodo
    @classmethod
    def persona_from_stringa(cls, dati: str):
        lista_dati = dati.split(",")
        return cls (lista_dati[0], lista_dati[1])
    @classmethod #decoratore
    def from_lista (cls, lista: list):
        return cls(lista[0], lista[1])


class Insegnante (Persona):
    def __init__(self, nome: str, cognome: str, materia: str):
        #con super().__init__(par), par2, ..., par_n
        # è una funzione che serve a richiamare gli attributi e 
        # i metodi della classe padre
        super().__init__(nome, cognome)

        self.materia = materia

    # ovveride del metodo
    # per quanto riguarda gli insegnati se io chiamo il metodo iniziali
    # verrà cercato prima nella classe stessa se non lo trova va a cercare
    # nella classe "padre"
    # l'override mi permette quindi di sovrascrivere il metodo della classe padre
    # con uno più specifico per la classe figlia

    def iniziali(self):
        return f"Prof: {super().iniziali()}"
    


class Studente(Persona):
    __next_matricola = 1

    def __init__(self, nome: str, cognome: str, voto: int):
        super().__init__(nome, cognome)
        self.voto = voto
        self.__matricola = Studente.__next_matricola
        Studente.__next_matricola +=1
    def iniziali(self):
        return f"{super().iniziali()}"
    
    def __str__(self):
        return f"\n{super().__str__()} -- voto: {self.voto} -- Matricola: {self.__matricola} "
    
    # metodo di classe che mi restituisce il numero di matricola del prossimo studente
    @classmethod
    def next_matricola(cls):
        return cls.next_matricola
    


    # con @staticmethod andiamo a creare dei metodi che non hanno bisogno
    # di classi o istanze per funzionare. Spesso vengono usati per effettuare
    # controlli dei valori che ricevono. Potremmo usarli per definire una 
    # classe utility che contiene varie tipologie di controlli
    @staticmethod
    def grafica_voto(voto):
        if voto >= 6:
            return str(voto)
        else:
            return "Insufficiente"








p = Persona.persona_from_stringa("Filippo, Pavanello")
print (p)


p1 = Persona.from_lista(["Filippo", "Pava"])
print(p1)


i = Insegnante("Mario", "Cognome", "Italiani")
print (i.iniziali())


s = Studente("Luigi", "Verdi", 9)
print (s.iniziali())
print (s)


print(Studente.grafica_voto(5))







