class Negozio:
    def __init__(self, nome, lista_videogiochi=None, lista_fumetti= None):
        self.nome = nome
        self.lista_videogiochi = lista_videogiochi if lista_videogiochi else []
        self.lista_fumetti = lista_fumetti if lista_fumetti else []

    def mostra_videogiochi(self):
        print("Videogiochi disponibili:")
        for v in self.lista_videogiochi:
            print(Videogame(*v))

    def mostra_fumetti(self):
        print("Fumetti disponibili:")
        for f in self.lista_fumetti:
            print(Fumetti(*f))

class Fumetti : 
    

    def __init__(self, titolo: str, casa_editrice: str, scrittore: str, disegnatore: str, n_pagine: int):
        self.titolo = titolo
        self.casa_editrice = casa_editrice
        self.scrittore = scrittore
        self.disegnatore = disegnatore
        self.n_pagine = int(n_pagine)
    def __str__(self):
        return f"""
Titolo: {self.titolo}
casa editrice: {self.casa_editrice}
scrittore: {self.scrittore}
disegnatore: {self.disegnatore}
numero pagine: {self.n_pagine}    

"""
    @property
    def titolo(self):
        return self.__titolo

    @titolo.setter
    def titolo(self, titolo):
        if not titolo.strip(): 
            print ("!","."*40,"!")
            print("Il titolo non può essere una stringa vuota")
            print ("."*44)
            exit()
        self.__titolo = titolo

    @property
    def casa_editrice(self):
        return self.__casa_editrice

    @casa_editrice.setter
    def casa_editrice(self, casa_editrice):
        if not casa_editrice.strip():
            print ("!","."*40,"!")
            print("La casa editrice non può essere una stringa vuota.")
            print ("."*44)
            exit()
            self.__casa_editrice = None
        self.__casa_editrice = casa_editrice

    @property
    def scrittore(self):
        return self.__scrittore

    @scrittore.setter
    def scrittore(self, scrittore):
        if not scrittore.strip():
            print ("!","."*40,"!")
            print("Lo scrittore non può essere una stringa vuota.")
            print ("."*44)
            exit()
            self.__scrittore = None
        self.__scrittore = scrittore

    @property
    def disegnatore(self):
        return self.__disegnatore

    @disegnatore.setter
    def disegnatore(self, disegnatore):
        if not disegnatore.strip():
            print ("!","."*40,"!")
            print("Il disegnatore non può essere una stringa vuota.")
            print ("."*44)
            exit()
            self.__disegnatore = None
        self.__disegnatore = disegnatore

    @property
    def n_pagine(self):
        return self.__n_pagine

    @n_pagine.setter
    def n_pagine(self, n_pagine):
        if n_pagine <= 0:
            print ("!","."*40,"!")
            print("Il numero di pagine deve essere maggiore di zero.")
            print ("."*44)
            exit()
            self.__n_pagine = None
        self.__n_pagine = n_pagine
    def stampa_file(self):
        return f"\n{self.titolo},{self.casa_editrice},{self.scrittore},{self.disegnatore},{self.n_pagine}"



class Videogame: 
    def __init__(self, titolo: str, console: str, genere: str, studio_sviluppo: str, voto_critica: int):
        self.titolo = titolo
        self.console = console
        self.genere = genere
        self.studio_sviluppo = studio_sviluppo
        self.voto_critica = int(voto_critica)

    @property
    def titolo(self):
        return self.__titolo
    
    @titolo.setter
    def titolo(self, titolo):
        if not titolo.strip():   
            print ("!","."*40,"!")
            print("Il titolo non può essere una stringa vuota")
            print ("."*44)
            exit()
        self.__titolo = titolo
        
    @property
    def console(self):
        return self.__console

    @console.setter
    def console(self, console):
        if not console.strip():
            print ("!","."*40,"!")
            print("La console non può essere una stringa vuota.")
            print ("."*44)
            exit()
            self.__console = None
        self.__console = console

    @property
    def genere(self):
        return self.__genere

    @genere.setter
    def genere(self, genere):
        if not genere.strip():
            print ("!","."*40,"!")
            print("Il genere non può essere una stringa vuota.")
            print ("."*44)
            exit()
            self.__genere = None
        self.__genere = genere

    @property
    def studio_sviluppo(self):
        return self.__studio_sviluppo

    @studio_sviluppo.setter
    def studio_sviluppo(self, studio_sviluppo):
        if not studio_sviluppo.strip():
            print ("!","."*40,"!")
            print("Lo studio di sviluppo non può essere una stringa vuota.")
            print ("."*44)
            exit()
            self.__studio_sviluppo = None
        self.__studio_sviluppo = studio_sviluppo

    @property
    def voto_critica(self):
        return self._voto_critica

    @voto_critica.setter
    def voto_critica(self, voto_critica):
        if not (0 <= voto_critica <= 100):
            print ("!","."*40,"!")
            print("Il voto della critica deve essere compreso tra 0 e 100.")
            print ("."*44)
            exit()
            self._voto_critica = None
        self._voto_critica = voto_critica

    def stampa_file(self):
        return f"\n{self.titolo},{self.console},{self.genere},{self.studio_sviluppo},{self.voto_critica}"

    def __str__(self):
        return f"""
Titolo: {self.titolo}
console : {self.console}
genere : {self.genere }
studio_sviluppo: {self.studio_sviluppo}
voto_critica: {self.voto_critica}
       
"""







