# definire una classe Drink con i segueti attributi
# nome: str, quantità: int, ingredienti: list 

# definire una classe Pizza con i seguenti attributi
# nome: str, quantità: int, ingredienti: list

# definire una classe Primo con i seguenti attributi
# nome: str, quantità: int, ingredienti: list

# Definire la classe Ricettacolo con i seguenti attributi
# nome: str, ricette: list

class Drink:
    def __init__(self, nome: str, quantità: int, ingredienti: list):
        self.nome: str [str]= nome
        self.quantità = quantità
        self.ingredienti = ingredienti

    def __str__(self):
       return f"Drink: {self.nome}, Quantità: {self.quantità}, Ingredienti: {self.ingredienti}"


class Pizza:
    def __init__(self, nome: str, quantità: int, ingredienti: list):
        self.nome = nome
        self.quantità = quantità
        self.ingredienti = ingredienti

    def __str__(self):
        return f"Pizza: {self.nome}, Quantità: {self.quantità}, Ingredienti: {self.ingredienti}"


class Primo:
    def __init__(self, nome: str, quantità: int, ingredienti: list):
        self.nome = nome
        self.quantità = quantità
        self.ingredienti = ingredienti

    def __str__(self):
        return f"Primo: {self.nome}, Quantità: {self.quantità}, Ingredienti: {self.ingredienti}"


class Ricettacolo:
    def __init__(self, nome: str, ricette: list[Drink | Primo | Pizza]):
        self.nome = nome
        self.ricette = ricette  # Lista di oggetti (Drink, Pizza, Primo, ecc.)

    def aggiungi_ricetta(self, ricetta):
        self.ricette.append(ricetta)

    def mostra_ricette(self, variabile= None, n:int = None):
        count_drink = 0
        count_primo = 0
        count_pizza = 0
        if variabile == "1": 
            print ("\nPrimi:\n")if n == None else ""
            for ricetta in self.ricette:
                    if ricetta.__class__ is Primo:
                        print(ricetta) if n == None else ""
                        count_primo += 1
            return f"Il numero di primi è {count_primo}" if n == 1 else ""
        if variabile == "2":
            print ("\nPizza:\n") if n == None else ""                   
            for ricetta in self.ricette:
                    if ricetta.__class__ is Pizza:
                        print (ricetta) if n == None else ""
                        count_pizza += 1
            return f"Il numero di pizze è {count_pizza}" if n == 2 else ""
        if variabile == "3":
            count_drink = 0
            print ("\nDrink:\n")if n == None else ""  
            for ricetta in self.ricette:
                    if ricetta.__class__ is Drink:
                        print (ricetta) if n == None else ""
                        count_drink += 1
            return f"Il numero di drink è {count_drink}" if n == 3 else ""
    def mostra_q_igredienti (self, variabile):
        quantita_primo = 0
        quantita_pizze = 0
        quantita_drnk = 0
        if variabile == "1": 
            for ricetta in self.ricette:
                    if ricetta.__class__ is Primo:
                        x = ricetta.ingredienti.split("-")
                        quantita_primo += len(x)
            return f"la quantità totale di ingredienti per i primi è {quantita_primo}" 
        if variabile == "2": 
            for ricetta in self.ricette:
                    if ricetta.__class__ is Pizza:
                        x = ricetta.ingredienti.split("-")
                        quantita_pizze += len(x)
            return f"la quantità totale di ingredienti per le pizze è {quantita_pizze}"
        if variabile == "3": 
            for ricetta in self.ricette:
                    if ricetta.__class__ is Drink:
                        x = ricetta.ingredienti.split("-")
                        quantita_drnk += len(x)
            return f"la quantità totale di ingredienti per i primi è {quantita_drnk}"
    def igredienti_comuni (self, variabile):
         for ricetta in self.ricette:
              if variabile in ricetta.ingredienti:
                   print (ricetta)
    def ricette_comuni (self, variabile):
         for ricetta in self.ricette:
            x = ricetta.ingredienti.split("-")
            j = True
            for ingrediente in variabile:
                if ingrediente not in x:
                        j = False
                        break  
            if j:
                print (ricetta)
         

    def __str__(self):
        return f"Ricettacolo: {self.nome}\nRicette:\n{self.ricette}" 

    def lettura_file(self, path):
        with open(path, encoding='utf-8') as file:
            elementi_file = file.read().splitlines()
            for elemento in elementi_file:
                dati = elemento.split(',')
                if dati[0] == "Drink":
                    self.ricette.append(Drink(dati[1],dati[2],dati[3]))
                elif dati[0] == "Primo":
                    self.ricette.append(Primo(dati[1],dati[2],dati[3]))
                elif dati[0] == "Pizza" : 
                    self.ricette.append(Pizza(dati[1],dati[2],dati[3]))









## cercare globals ()