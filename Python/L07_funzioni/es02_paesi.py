
with open ("./res/paesi.csv") as file1: 
    elemento_file = file1.readlines()
    
def elenco_paesi ():
    ris = []
    for elemento in elemento_file:
        j = elemento.split(",") 
        ris.append(j)
    for j in ris:
        print (f"{j[0]} | capitale: {j[1]} | n° abitanti: {int (j[2]):,} | ha come moneta: {j[4]} | religione: {j[5]} | {"E' un isola" if j[3]=="True"else "Non è un isola"}".replace(",", "."))

def monete ():
    lista_monete= []
    for elemento in elemento_file:
        j = elemento.split(",") 
        lista_monete.append(j[4])
    return lista_monete

def scelta_monete (scelta):
    if scelta in money: 
        for elemento in elemento_file:
            j = elemento.split(",") 
            if j[4] == scelta:
                print (j[0])


def isole():
    lista_isole = []
    for elemento in elemento_file:
        j1 = elemento.split(",") 
        if j1[3] == "True":
            lista_isole.append(j1[0])           
    return lista_isole

def isole_minor_abitanti ():
    def media ():
        somma = 0 
        for elemento in elemento_file:
            j = elemento.split(",")
            somma += int (j[2])
        media_totale = round(somma/len (elemento_file))
        return media_totale
    lista_isole_2 = []
    for elemento in elemento_file:
        j1 = elemento.split(",") 
        if j1[3] == "True" and int (j1[2]) <media():
            lista_isole_2.append(j1[0])
            lista_isole_2.append(int(j1[2])) 
    for elemento in range (0,len(lista_isole_2),2):
           for j in range(1,len(lista_isole_2),2):
               if lista_isole_2[elemento] == lista_isole_2[j-1] :                
                   print (f"{lista_isole_2[elemento]} ha {int(lista_isole_2[j]):,}".replace(",", "."))
    print (f"\nla media è {media():,}".replace (",", "."))

def popolazione ():
    dizionario_paesi = []
    for elemento in elemento_file:
        j = elemento.split(",")
        popolazione1 = {
            "Stato": j[0],
            "Capitale": j[1], 
            "Abitanti": int (j[2]),
            "Isola": j[3],
            "Moneta": j[4],
            "Religione": j[5][:-1]
        }
        dizionario_paesi.append(popolazione1)
    dizionario = sorted(dizionario_paesi, key=lambda x: x["Abitanti"])
    
    print ("Elenco dei paesi ordinati per popolazione")
    for i in dizionario:  
        print (f"Stato: {i["Stato"]} | Capitale: {i["Capitale"]} | Abitanti: {int(i["Abitanti"]):,} | Moneta: {i["Moneta"]} | Religione: {i["Religione"]} | {"è un isola." if i["Isola"]=="True"else ""}".replace (",","."))
    
def lista_religioni ():
    lista_religioni1= []
    for elemento in elemento_file:
        j = elemento.split(",") 
        lista_religioni1.append(j[5][:-1])
    return lista_religioni1

def religione_a_scelta (religione): 
    for elemento in elemento_file:
        j2 = elemento.split(",") 
        if religione in j2[5][:-1]:
            print (j2[0])


def somma_religione (scelta):
    somma = 0
    for elemento in elemento_file:
        j2 = elemento.split(",") 
        if scelta in j2[5][:-1]:
            somma += int(j2[2])
    print (f"{somma:,}".replace(",","."))

def paese_monete ():
    conteggio = {}
    for elemento in elemento_file:
        j = elemento.split(",")
        for elemento in j:
            if elemento == j[4]:    
                if elemento in conteggio:
                    conteggio[elemento] += 1
                else:
                    conteggio[elemento] = 1
    print(f"Numero dei paesi che usano la stessa moneta:")
    for i in conteggio: 
        print (f"{i} : {conteggio[i]}")

cmd = ""

while cmd != 0:
    print ("\nBenvenuto\n")
    with open ("./res/menu_paesi.txt") as file: 
        print (file.read())
    cmd = int (input ("Inserisci un numero da eseguire: "))
    if cmd == 1: 
        print()
        print("."*50)
        print ("\nL'elenco dei paesi è :\n")
        elenco_paesi()
        print("."*50)
    if cmd == 2:
        print()
        print("."*50)
        money =set(monete())
        print (f"Elenco monete:")
        print (*money, sep=", ")
        scelta_moneta = input(f"Scegli una moneta: ").capitalize()
        print (f"\nLa lista dei Paesi che hanno {scelta_moneta} è:\n")
        scelta_monete(scelta_moneta)
        print("."*50)
    if cmd == 3:
        print()
        print("."*50)
        print ("L'elenco dei paesi che sono isole:\n")
        print (*isole(),sep=", ")
        print("."*50)
    if cmd == 4:
        print()
        print("."*50)
        print ("\nL'elenco delle isole col numero di abitanti inferiore alla media totale:\n")
        isole_minor_abitanti()
        print("."*50)
    if cmd ==5:
        print()
        print("."*50)
        popolazione()
        print("."*50)
    if cmd == 6:
        print()
        print("."*50)
        religioni = set (lista_religioni())
        print("Scegli una religione tra:")
        print (*religioni, sep=", ")
        scelta_religione = input("** ").title()
        print (f"Elenco dei paesi di religione {"Cristiana" if scelta_religione == "Cristianesimo" else "Induista" if scelta_religione == "Induismo" else "shintoista e buddista" if scelta_religione == "Shintoismo e Buddhismo" else""}")
        religione_a_scelta(scelta_religione)
        print("."*50)
    if cmd == 7:
        print()
        print("."*50)
        religioni = set (lista_religioni())
        print("Scegli una religione tra:")
        print (*religioni, sep=", ")
        scelta = input("e ti darò la somma degli abitanti: ").title()
        print ()
        somma_religione(scelta)
        print("."*50)
    if cmd == 8:
        print()
        print("."*50)
        paese_monete()
        print("."*50)
    if cmd == 0:
        exit()