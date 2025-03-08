
# si usa in base al valore di una variabile

# esempio
# chiediamo all'utente di inserire la sua professione
# il programma dovrà rispondere con il suo stipendio

professione = input("Qual è la tua professione? ").casefold()

risposta = "Stipendio: "

# if professione == "programmatore":
#     risposta += "1300€"
# elif professione == "meccanico":
#     risposta += "1800€"
# elif professione == "elettricista": 
#     risposta += "2000€"
# else:
#     risposta += "800€"

# print (risposta)

## MATCH-CASE

# SINTASSI
# prima di tutto varibile da controllare
# match variabile : 
#       case valore1 : # il valore deve essere dello stesso tipo della variabile
#                        è come se fosse un if
#            blocco di codice del primo case
#       case valore2 : 
#            blocco di codice
#       case valore3 : 
#            blocco di codice
#       case _ : 
#            blocco di codice

# è come se fosse un if-else
# case _ è utilizzato per definire l'else
# 
# è uguale all'if commentat sopra
if len(professione) > 0: 
    match professione : 
        case "programmatore" | "professore": 
            risposta += "1300€"
        case "elettricista" : 
            risposta += "2000€"
        case "meccanico": 
            risposta += "1800€"
        case _ : 
            risposta += "800€"
else: 
    risposta = "professione non definita"
print (len(professione))
print (risposta)

# per utilizzare l'operatore logico 'or' si usa '|'
# | --> or
# & --> and 


# altro esempio

mese = int (input("Inserisci un mese, indicando il numero: "))
if 0 < mese < 13:
    match mese: 
        case 1: 
            print ("Gennaio")
        case 2: 
            print ("febbraio")
        case 3: 
            print ("Marzo")
        case _ : 
            print ("altri mesi ")
else: 
    print ("Mese non riconosciuto ")

risposta = " "
giorni = int (input("Inserisci i giorni totali per capire che mese è: "))

if 28 <= giorni <= 31:
    match giorni: 
        case 28 | 29: 
            risposta = f"Il mese che presenta {giorni} giorni è: Febbraio"
        case 30: 
            risposta = f"I mesi che presentano {giorni} giorni sono: Aprile, Giugno, Settembre e Novembre"
        case _ : 
            risposta = f"I mesi che presentano {giorni} giorni sono: Gennaio, Marzo, Maggio, Luglio, Agosto, Ottobre e Dicembre"
else : 
    print ("Inserisci un numero da 28 a 31")

print (risposta)