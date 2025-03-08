# definire una classe Drink con i segueti attributi
# nome: str, quantità: int, ingredienti: list 

# definire una classe Pizza con i seguenti attributi
# nome: str, quantità: int, ingredienti: list

# definire una classe Primo con i seguenti attributi
# nome: str, quantità: int, ingredienti: list

# Definire la classe Ricettacolo con i seguenti attributi
# nome: str, ricette: list

from dataclasses import dataclass

@dataclass
class Drink:
    nome: str
    quantita: int
    ingredienti: list[str]

@dataclass
class Pizza:
    nome: str
    quantita: int
    ingredienti: list[str]

@dataclass
class Primo:
    nome: str
    quantita: int
    ingredienti: list[str]

@dataclass
class Ricettacolo:
    nome: str
    ricette: list[Drink | Pizza | Primo]

    def mostra_ricette(self, categoria: str = ""):

        if not categoria:
            print(*self.ricette, sep= "\n")
            # print("\n".join(map(str,r.ricette))) # modo 1a
            # print("\n".join([str(x) for x in r.ricette])) # modo 1b
            # for ric in r.ricette: # modo 2
            #     print(ric)
        else:
            # globals() è un dizionario che raccoglie tutte le variabili che 
            # durante l'esecuzione del programma vengono salvate in memoria
            # quindi posso utilizzarlo per prendere i valori di quelle variabili
            # a partire dal loro nome
            # in questo caso specifico vado a prendere il valore associato
            # alla stringa nomeClasse (es. "Primo")
            # questo valore è la classe stessa (Primo)(quello che di solito è in verde)
            classe = globals()[categoria.title()]
            for ricetta in self.ricette:
                if isinstance(ricetta, classe):
                    print(ricetta)
            # for r in self.ricette:
            #     if categoria == "Primo" and isinstance(r, Primo):
            #         print(r)
            #     elif categoria == "Pizza" and isinstance(r, Pizza):
            #         print(r)
            #     elif categoria == "Drink" and isinstance(r, Drink):
            #         print(r)

    def lettura_file(self, path: str):
        self.ricette = [] # prima di leggere il file svuoto la lista per evitare problemi di duplicati

        with open(path, "r", encoding= "utf-8") as file:
            lista_righe = file.read().splitlines()

        for riga_stringa in lista_righe:
            # Primo,Puttanesca,230,Pomodoro-Acciughe-Capperi-Olive-Peperoncino
            riga_lista = riga_stringa.split(",")
            # print(riga_lista)
            lista_ingredienti_riga = riga_lista[3].split("-")

            if riga_lista[0] == "Primo":
                pr = Primo(riga_lista[1], int(riga_lista[2]), lista_ingredienti_riga)
                self.ricette.append(pr)
            elif riga_lista[0] == "Pizza":
                pi = Pizza(riga_lista[1], int(riga_lista[2]), lista_ingredienti_riga)
                self.ricette.append(pi)
            elif riga_lista[0] == "Drink":
                dr = Drink(riga_lista[1], int(riga_lista[2]), lista_ingredienti_riga)
                self.ricette.append(dr)

    def n_ricette_categoria(self):
        diz: dict[str, int]= {
            "Primo" : 0,
            "Drink" : 0,
            "Pizza" : 0
        }

        stringa = ""
        for r in self.ricette:
            if isinstance(r, Primo):
                diz["Primo"] += 1
            elif isinstance(r, Drink):
                diz["Drink"] += 1
            elif isinstance(r, Pizza):
                diz["Pizza"] += 1


        for k, v in diz.items():
            stringa += k + " - " + str(v) + "\n"
        return stringa
    
    def n_ingredienti_categoria(self, categoria: str):
        numero: int = 0
        # globals() è un dizionario che raccoglie tutte le variabili che 
        # durante l'esecuzione del programma vengono salvate in memoria
        # quindi posso utilizzarlo per prendere i valori di quelle variabili
        # a partire dal loro nome
        # in questo caso specifico vado a prendere il valore associato
        # alla stringa nomeClasse (es. "Primo")
        # questo valore è la classe stessa (Primo)(quello che di solito è in verde)
        classe = globals()[categoria.title()]
        for r in self.ricette:
            if isinstance(r, classe):
                numero += len(r.ingredienti)
        return numero
    
    def ricette_ingrediente(self, ingrediente: str):
        for r in self.ricette:
            if ingrediente in r.ingredienti:
                print(r)


    def ricette_ingredienti_multipli(self, ingredienti: str):
        lista_ingredienti = ingredienti.split("-")
        for r in self.ricette:
            check = True
            for i in lista_ingredienti:
                if i not in r.ingredienti:
                    check = False
                    break
            if check == True:
                print(r.nome)

    def aggiungi_ricetta(self, path:str, categoria: str, nome: str,
                          quantita: int, ingredienti: str):
        with open(path, "a", encoding="utf-8") as file:
            file.write(f"\n{categoria},{nome},{quantita},{ingredienti}")
            
        
        self.lettura_file(path) # modo 1: rileggo il file dopo la modifica

        # # modo 2: creo l'oggetto e lo inserisco nella self.ricette (lista_ricette)
        # classe = globals()[categoria.title()]
        # t = classe(nome, quantita, ingredienti.split("-"))
        # self.ricette.append(t

    def elimina_ricetta(self, path: str, nome: str):

        with open(path, "r", encoding= "utf-8") as file:
            lista_righe = file.read().splitlines()

            for riga in lista_righe.copy():
                if nome.title() == riga.split(",")[1]:
                    lista_righe.remove(riga)
                
            
            stringa_file = "\n".join(lista_righe)

        with open(path, "w", encoding= "utf-8") as file:
            file.write(stringa_file)
        
        self.lettura_file(path)
        # for ricetta in self.ricette.copy():
        #     if nome == ricetta.nome:
        #         self.ricette.remove(ricetta)
            
    def modifica_ricetta(self, path: str, nome: str, ingredienti: str):
        lista_ingredienti = ingredienti.split("-")
        stringa_file = ""
        for ricetta in self.ricette:
            if ricetta.nome == nome.title():
                ricetta.ingredienti = lista_ingredienti

        for ricetta in self.ricette:
            if isinstance(ricetta, Primo):
                stringa_file += f"Primo,{ricetta.nome},{str(ricetta.quantita)},{"-".join(ricetta.ingredienti)}\n"
            elif isinstance(ricetta, Pizza):
                stringa_file += f"Pizza,{ricetta.nome},{str(ricetta.quantita)},{"-".join(ricetta.ingredienti)}\n"
            elif isinstance(ricetta, Drink):
                stringa_file += f"Drink,{ricetta.nome},{str(ricetta.quantita)},{"-".join(ricetta.ingredienti)}\n"

        with open(path, "w", encoding= "utf-8") as file:
            file.write(stringa_file[:-1])


        

