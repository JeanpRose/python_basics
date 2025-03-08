from datetime import datetime

class Persona:
    def __init__(self,  nominativo: str, anno_nascita: int, residenza: str):
        self.nominativo = nominativo
        self.anno_nascita = anno_nascita
        self.residenza = residenza
        self.eta = self.calcolo_eta(anno_nascita)
    
    def calcolo_eta(self, var):
        oggi = datetime.today()
        eta = oggi.year - var
        return eta

    def __str__(self):
        return f"Nominativo: {self.nominativo} | {self.eta} anni | Residente: {self.residenza}"
    

class Paziente(Persona):
    def __init__(self, nominativo: str, anno_nascita: int, residenza: str, patologia: str,ricovero: bool, giorni_ricovero: int, ticket: float, reparto_assegnato: str = None):
        super().__init__(nominativo, anno_nascita, residenza)
        self.patologia = patologia.capitalize()
        self.reparto_assegnato = self.assegno_reparto(patologia.capitalize())
        self.giorni_ricovero = giorni_ricovero
        self.ticket = ticket
        self.costo = self.costo_degenza()
        self.ricovero = ricovero

    def reparti (self, path):
        lista_righe1 = [] 
        lista_righe = [] 
        with open(path, "r", encoding= "utf-8") as file:
            lista_righe1 = file.read().splitlines()
        for riga in lista_righe1:
            b = riga.split(",") # Suddivide ogni riga in chiave e valore
            lista_righe.append(b)
        return lista_righe
    
    def assegno_reparto (self, pat):
        lista_reparti = self.reparti("C:/Users/lordj/Desktop/DAITA24/L08_Oggetti/res/reparti.txt")
        for x in lista_reparti: 
            if x[0] == pat:
                pat = x[1] 
        return pat    
    
    def costo_degenza(self):
        costo = self.giorni_ricovero * self.ticket
        return round(costo,2)
    
    def __str__(self):
        return f"""{"-"*50}\n{super().__str__()}
Patologia: {self.patologia} | Reparto assegnato: {self.reparto_assegnato} | {"Ricovero : si" if self.ricovero else ""}
Costo degenza: {self.costo}€ per {self.giorni_ricovero} giorni\n{"-"*50}"""


# x= Paziente("Light Yagami", 1970, "Milano","Mal di testa da programmazione",False ,3,30.31)
# print (x)


class Dottore (Persona):
    def __init__(self, nominativo: str, anno_nascita: int, residenza: str,reparto: str, anni_lavoro: int, tirocinante: bool, numero_interventi: int, interventi_riusciti: int ):
        super().__init__(nominativo, anno_nascita, residenza)
        self.reparto = reparto
        self.anni_lavoro = anni_lavoro
        self.tirocinante = tirocinante
        self.numero_interventi = numero_interventi
        self.interventi_riusciti = interventi_riusciti
        self.stipendio = self.stipendio_dot()
        self.dottore_buono = self.buon_dottore()
        

    def stipendio_dot(self):
        base = 1600
        stipendio = base + (self.anni_lavoro * 100 if self.reparto == "Pediatria" else self.anni_lavoro *200 if self.reparto == "Neurologia" else self.anni_lavoro *50)
        stipendio = stipendio/2 if self.tirocinante else stipendio
        stipendio = stipendio + (self.interventi_riusciti*10)
        stipendio = stipendio - ((self.numero_interventi-self.interventi_riusciti)* (-20) if self.reparto == "Pediatria" else (self.numero_interventi-self.interventi_riusciti)*50)
        return stipendio
    
    def buon_dottore(self):
        interventi_non_riusciti = self.numero_interventi-self.interventi_riusciti
        return f"""{"E' un dottore eccellente" if (self.interventi_riusciti > interventi_non_riusciti)
                    else "E' un dottore mediocre" if (self.interventi_riusciti == interventi_non_riusciti)
                    else "E' un dottore pessimo" if (self.interventi_riusciti < interventi_non_riusciti) else ""  }"""

    def __str__(self):
        return f"""{"-"*50}\n{super().__str__()}
| Reparto: {self.reparto} | Anni lavoro: {self.anni_lavoro} {"| Tirocinante : si" if self.tirocinante else ""}
| Numero interventi: {self.numero_interventi} | Interventi riusciti: {self.interventi_riusciti}
| Stipendio: {self.stipendio_dot()} 
| {self.buon_dottore()}\n{"-"*50}"""

# x = Dottore("Cristina Yang",1978,"Roma","Pediatria",10,True,50, 49)
# print (x)

class Ospedale:
    def __init__(self, nome: str, lista: list[Persona |Paziente | Dottore]):
        self.nome = nome 
        self.lista = lista

    def lettura_file(self, path: str):
        self.lista = [] 
        with open(path, "r", encoding= "utf-8") as file:
            lista_di_righe = file.read().splitlines()
    
        for riga_stringa in lista_di_righe:

            riga_lista = riga_stringa.split(",")
            # Dottore,Addison Montgomery,1989,Firenze,Ginecologia,5,True,20,18
            # Paziente,Light Yagami,1970,Milano,Gastrite,False,3,30

            if riga_lista[0] == "Paziente":
                paz = Paziente(riga_lista[1], int(riga_lista[2]), riga_lista[3], riga_lista[4], bool(riga_lista[5]), int(riga_lista[6]), float (riga_lista[7]))
                self.lista.append(paz)
            elif riga_lista[0] == "Dottore":
                dot = Dottore(riga_lista[1], int(riga_lista[2]), riga_lista[3], riga_lista[4],int (riga_lista[5]), bool(riga_lista[6]), int(riga_lista[7]), float (riga_lista[8]))
                self.lista.append(dot)
            if riga_lista[0] == "Dottore" or riga_lista[0] =="Paziente":
                per = Persona(riga_lista[1], int(riga_lista[2]), riga_lista[3])
                self.lista.append(per)

    def mostra_persone (self, variabile : str):
        if variabile == "Persona": 
            print ("\nPersone:\n")
            for persona in self.lista:
                    if persona.__class__ is Persona:
                        print(persona)
        if variabile == "Paziente":
            print ("\nPazienti:\n")                  
            for paziente in self.lista:
                    if paziente.__class__ is Paziente:
                        print (paziente) 
        if variabile == "Dottore":
            print ("\nDottori:\n")
            for dottore in self.lista:
                    if dottore.__class__ is Dottore:
                        print (dottore) 

    def dottori_varie (self, x):
        lista_doc = []
        for y in self.lista:
            if y.__class__ is Dottore:
                lista_doc.append(y)
            
        if x==1: 
            for dottore in lista_doc:
                print (dottore if dottore.anni_lavoro >= 10 else "")
        if x == 2:
            scelta = input("Scegli una città per visualizzare i dottori: ").capitalize()
            for dottore in lista_doc:
                if dottore.residenza == scelta:
                    print (dottore)
        if x == 3:
            stipendio_max = max (lista_doc, key= lambda x : x.stipendio)
            print (stipendio_max)
        if x == 4:
            stipendio_min = min (lista_doc, key= lambda x : x.stipendio)
            print (stipendio_min)
        if x == 5:
            somma = 0
            count = 0
            for dottore in lista_doc:
                somma += dottore.stipendio
                count += 1 
            print (f"La media degli stipendi dei dottori è {somma/count}€")

        if x == 6: 
            scelta = input ("Scegli un reparto per visualizzare lo stipendio medio: ").capitalize()
            somma = 0
            count = 0
            for dottore in lista_doc:
                if dottore.reparto == scelta:
                    somma += dottore.stipendio
                    count += 1 
            print (f"La media degli stipendi dei dottori in {scelta} è {round(somma/count, 2)}€")

        if x == 7:
            for dottore in lista_doc:
                print (dottore if "E' un dottore eccellente" in dottore.dottore_buono else "")
        if x == 8:
            dot_anziano = max (lista_doc, key= lambda x : x.eta)
            print (dot_anziano)
        if x == 10:
            diz: dict[str, int]= {
            "Neurologia" : 0,
            "Medicina generale" : 0,
            "Pediatria" : 0,
            "Pronto soccorso" : 0,
            "Chirurgia" : 0,
            "Ginecologia" : 0}

            for m in self.lista:
                if isinstance(m, Paziente):
                    diz[m.reparto_assegnato] += 1
            piu_affollato = max(diz, key= lambda d: diz[d])
            print (f"\n{piu_affollato} è il reparto con più pazienti, ne ha {diz[piu_affollato]}")
            print (f"Il resto dei reparti: \n")
            for k,v in diz.items():
                if k != piu_affollato:
                    print(f"{k}: {v}")
        if x == 11:
            somma = 0
            for dottore in lista_doc:
                somma += dottore.stipendio 
            print (f"La spesa totale che deve affrontare l'ospedale per i dottori è {round(somma,2)}€")
    
    def pazienti_vari (self, s):
        lista_paz = []
        for y in self.lista:
            if y.__class__ is Paziente:
                lista_paz.append(y)
        if s == 1:
            paz_giovane = min (lista_paz, key= lambda x : x.eta)
            print (paz_giovane)
        if s == 2:
            somma = 0 
            for paziente in lista_paz:
                somma += paziente.costo
            print (f"La somma che i pazienti devono all'ospedale è {round(somma,2)}€")







# 15 - Vedere la somma che i pazienti devono all'ospedale