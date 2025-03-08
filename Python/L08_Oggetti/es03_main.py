# Richieste:
# 1. Stampare tutte le ricette.
# 2. Stampare la lista di ricette di una categoria a scelta.
# 3. Visualizzare il numero totale di ricette per categoria.
# 4. Calcolare la quantità totale di ingredienti per una categoria.
# 5. Trovare le ricette con un ingrediente in comune.
# 6. Chiedere all'utente una serie di ingredienti e stampare le ricette che li usano.
# 7. Aggiungere una nuova ricetta.
# 8. Eliminare una ricetta.
# 9. Modificare gli ingredienti di una ricetta


from es03_classi import  Ricettacolo

ricetta = []
ricettacolo= Ricettacolo ("Risto Pub", ricetta )
ricettacolo.lettura_file("C:/Users/lordj/Desktop/DAITA24/L08_Oggetti/res/ricettacolo.csv")

def scelte ():
    scelta = input ("\nScegli una categoria tra Primi, Pizza e Drinks: ").casefold()
    if scelta == "primo" or scelta == "primi":
        scelta = "1"
       
    elif scelta == "pizza" or scelta == "pizze":
        scelta = "2"
        # n = 2
    elif scelta == "drink" or scelta == "drinks":
        scelta = "3"
        # n =  3 
    return scelta

menu = """
1. Stampare tutte le ricette.
2. Stampare la lista di ricette di una categoria a scelta.
3. Visualizzare il numero totale di ricette per categoria.
4. Calcolare la quantità totale di ingredienti per una categoria.
5. Trovare le ricette con un ingrediente in comune.
6. Chiedere all'utente una serie di ingredienti e stampare le ricette che li usano.
7. Aggiungere una nuova ricetta.
8. Eliminare una ricetta.
9. Modificare gli ingredienti di una ricetta"""

while True: 
    print(menu)
    cmd = input("INSERISCI COMANDO: ")
    print()
    match cmd:
        case "0":
            print("Termino programma")
            break
        case "1":
            for x in range(1,4):
                ricettacolo.mostra_ricette(str(x))
        case "2": 
            ricettacolo.mostra_ricette(scelte())
        case "3": 
            v =scelte()
            print(ricettacolo.mostra_ricette(v, n = int(v)))
        case "4":
            print (ricettacolo.mostra_q_igredienti(scelte()))
        case "5":
            ingrediente_comune = input("Inserisci l'ingrediente: ").capitalize()
            ricettacolo.igredienti_comuni(ingrediente_comune)
        case "6":
            var  = input("Scegli una serie di ingredienti separati da uno spazio: ").title()
            v= var.split()
            ricettacolo.ricette_comuni(v)
        case "7":
            # Aggiungere una nuova ricetta
            print ("Inserisci una ricetta: \n")
            tipo = input("Vuoi aggiungere un Primo, Pizza o un Drink: ")
            nome = input("Inserisci nome: ")
            quan = input ("Inserisci quantità: ")
            ingredienti = input ("Inserisci gli ingredienti: ")
            nuova_ricetta = [tipo, nome,quan,ingredienti]
            if nuova_ricetta[0] == "Primo":
                ricettacolo.aggiungi_ricetta(nuova_ricetta)