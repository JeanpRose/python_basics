'''
Scrivi un programma che permetta a due giocatori di sfidarsi in un gioco di "Carta, Forbice, Sasso".
Il programma deve svolgere le seguenti operazioni:

Chiedere all'utente di inserire il nome del primo giocatore e il nome del secondo giocatore.
chiedere al primo giocatore di scegliere tra carta (c), forbice (f) o sasso (s) fino a quando non viene inserita una scelta valida.
chiedere al secondo giocatore di fare lo stesso fino a quando non viene inserita una scelta valida.
Determinare il vincitore basandosi sulle scelte dei giocatori secondo le seguenti regole:
Carta batte sasso
Forbice batte carta
Sasso batte forbice
Stampare il nome del vincitore e il messaggio relativo alla combinazione delle scelte (ad esempio, "Carta batte sasso").
Se entrambi i giocatori scelgono lo stesso simbolo, stampare "Pareggio".
Gestire correttamente le situazioni in cui un giocatore inserisce una scelta non valida (non c, f o s).
Far giocare i giocatori finchÃ¨ non decidono di uscire dal programma

'''

giocatori = 2
nome= []

for giocatore in range (giocatori):
    nome.append(input (f"Inserisci il nome del giocatore n° {(giocatore+1)}: ").capitalize())

scelta = " "
lista_scelte= []

gioco = " "

while gioco !="esci":
    lista_scelte= []
    print ()
    print ("Benvenuto al gioco di carta forbice e sasso")
    
    for name in nome: 
        menu = f"""
    {name} scegli tra: 
    1. Carta
    2. Forbice
    3. Sasso
    """
        while scelta != "0": 
            print (menu)
            scelta = input ("Inserisci una variabile o scrivi esci se non vuoi più giocare: ").casefold()
            if scelta == "sasso" or scelta =="s": 
                lista_scelte.append(scelta)
                break

            elif scelta == "forbice" or scelta =="f":
                lista_scelte.append(scelta)
                break

            elif scelta == "carta" or scelta == "c":
                lista_scelte.append(scelta)
                break
            elif scelta == "esci" or scelta == "exit":
                print ("Grazie per aver giocato")
                exit()
            else:
                print(f"Comando errato: {nome} inserisci sasso, carta o forbice se vuoi giocare")

    for i in range(len(lista_scelte)):
        for j in range (i+1, len(lista_scelte)):
            if lista_scelte[i] == lista_scelte[j]: 
                print ()
                print (f"{nome[0]} e {nome[1]} hanno la stessa scelta, prareggio")
                print ()

            elif lista_scelte[i]== "carta" and lista_scelte[j]=="sasso" or lista_scelte[j]== "carta" and lista_scelte[i]=="sasso":
                if lista_scelte[i] == "carta":
                    print ()
                    print (f"Carta batte sasso, {nome[i]} ha vinto")
                    print()
                elif lista_scelte[j] == "carta":
                    print ()
                    print (f"Carta batte sasso, {nome[j]} ha vinto")
                    print ()

            elif lista_scelte[i]== "carta" and lista_scelte[j]=="forbice" or lista_scelte[j]== "carta" and lista_scelte[i]=="forbice":
                if lista_scelte[i] == "forbice":
                    print ()
                    print (f"Forbice batte carta, {nome[i]} ha vinto")
                    print ()
                elif lista_scelte[j] == "forbice":
                    print ()
                    print (f"Forbice batte carta, {nome[j]} ha vinto")
                    print ()

            elif lista_scelte[i]== "forbice" and lista_scelte[j]==" sasso" or lista_scelte[i] == "sasso" and lista_scelte[j] == "forbice":
                if lista_scelte[i] == "sasso":
                    print ()
                    print (f"Sasso batte forbice, {nome[i]} ha vinto")
                    print ()
                elif lista_scelte[j] == "sasso":
                    print ()
                    print (f"Sasso batte forbice, {nome[j]} ha vinto")
                    print ()
        
