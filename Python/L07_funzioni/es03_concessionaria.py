with open ("./res/macchine.csv") as file:
    elementi_file = file.readlines()

lista_dizionario = []
for diz in elementi_file:
    j = diz.split(",")
    dizionario={"modello": j[0],
               "marca": j[1],
               "colore": j[2],
               "carburante":j[3],
               "cilindrata": int (j[4]),
               "prezzo": int(j[5]),
               "nPortiere": j[6],
               "cabrio": "True" if j[7][:-1]=="Cabrio"else "False"}
    lista_dizionario.append(dizionario)

def funzione_print(x):
    ris = [f"{ele["marca"]} - {ele["modello"]} - cilindrata: {ele ["cilindrata"]} - colore: {ele["colore"]} - prezzo: {ele["prezzo"]}" for ele in x]
    return ris
def media ():
    somma = 0 
    for elemento in lista_dizionario:
        somma += int (elemento ["cilindrata"])
    media_totale = round(somma/len (lista_dizionario))
    return media_totale

cmd = ""
while cmd != 0:

    with open ("./res/menu_macchine.txt") as file:
        print(file.read())

    cmd = int(input("Inserisci un numero: "))
    match cmd:
        case 1: 
            print ("-"*40)
            print ("\nElenco di tutte le macchine:\n")
            macchine = funzione_print(lista_dizionario)
            print (*macchine, sep="\n")
            print ("-"*40)
        case 2:
            print ("-"*40)
            print ("\nElenco delle macchine cabrio:\n")
            macchine_cabrio = list (filter(lambda x : x["cabrio"]=="True", lista_dizionario))
            print (*funzione_print(macchine_cabrio), sep ="\n")
            print ("-"*40)
        case 3:
            print ("-"*40)
            print ("\nMacchina a benzina meno costosa\n")
            macchina_benzina= list (filter(lambda x : x["carburante"]=="benzina", lista_dizionario))
            minore1=min(elemento["prezzo"] for elemento in macchina_benzina)
            minore = [macchina for macchina in macchina_benzina if macchina["prezzo"] == minore1]
            print (*funzione_print(minore), sep = "\n")
            print ("-"*40)
        case 4:
            print ("-"*40)
            print ("\nElenco delle macchine che hanno un prezzo superiore a 25000 e 5 porte\n")
            macchine_5_porte= list (filter(lambda x : x["nPortiere"]=="5", lista_dizionario))
            macchine_sup_25000  = list (filter(lambda x : x["prezzo"]>=25000, macchine_5_porte)) 
            print (*funzione_print(macchine_sup_25000), sep="\n")
            print ("-"*40)
        case 5:
            print ("-"*40)
            print ("\nElenco di tutte le ibride rosse\n")
            macchine_rosse= list (filter(lambda x : x["colore"]=="rosso", lista_dizionario))
            macchine_ibride_rosse= list (filter(lambda x : x["carburante"]=="ibrido", lista_dizionario))
            print (*funzione_print(macchine_ibride_rosse), sep="\n")
            print ("-"*40)
        case 6:
            print ("-"*40)
            print ("\nElenco delle macchina in ordine decrescente per prezzo\n")
            ordine_decresente= sorted (lista_dizionario, key = lambda x : x["prezzo"], reverse = True)
            print (*funzione_print(ordine_decresente), sep="\n")
            print ("-"*40)
        case 7:
            print ("-"*40)
            print ("\nElenco delle macchine a benzina con cilindrata superiore alla media, in ordine alfabetico in base al modello\n")
            macchina_benzina= list (filter(lambda x : x["carburante"]=="benzina", lista_dizionario))
            macchina_benzina_cili_sup = list (filter(lambda x : x["cilindrata"]>media(), macchina_benzina))
            ordine_alfabetico= sorted (macchina_benzina_cili_sup, key = lambda x : x["modello"])
            print (*funzione_print(ordine_alfabetico), sep="\n")
            print ("-"*40)
        case 8:
            print ("-"*40)
            print ("\nElenco delle macchine non bianche\n")
            macchina_non_bianche= list (filter(lambda x : x["colore"]!="bianco", lista_dizionario))
            print (*funzione_print(macchina_non_bianche), sep="\n")
            print ("-"*40)
        case 0:
            exit()
        case _:
            print ("!","-"*20,"ERRORE","-"*20,"!")
            print ("Inserisci un numero presente nella LISTA")
            print("-" * 52)