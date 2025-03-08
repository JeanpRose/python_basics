from es02_classi import Fumetti, Videogame, Negozio

with open ("./res/fumetti.csv") as file: 
    lista_fumetti = file.read().splitlines()
with open ("./res/videogames.csv") as file: 
    lista_videogames = file.read().splitlines()

lista_liste = []
for elemento in lista_fumetti:
    j= elemento.split(",")
    lista_liste.append(j)
lista_liste2= []
for elemento in lista_videogames:
    j= elemento.split(",")
    lista_liste2.append(j)

def media(): 
    somma = 0
    count = 0
    for elemento in lista_liste:
        somma += int (elemento [4])
        count +=1
    media_totale = round(somma/count,2)
    return media_totale
def media(disegnatore): 
    somma = 0
    count = 0
    for elemento in lista_liste:
        if elemento[2].casefold() == disegnatore.casefold():
            somma += int (elemento [4])
            count +=1
    media_totale = round(somma/count,2)
    return media_totale
def funzione_giochi(scegli, numero :int):
    for x in lista_liste2:
            if x[int(numero)].casefold() == scegli:
                print (Videogame(*x))
def funzione_fumetti(scegli, numero :int):
    for x in lista_liste:
            if x[int(numero)].casefold() == scegli:
                print (Fumetti(*x))
def funzione_massimo_minimo(var):
    lista = sorted(lista_liste2, key= lambda x : x[4], reverse=var)
    massimo_minimo= int(lista[0][4]) 
    for x in lista: 
        if massimo_minimo == int(x[4]): 
            print (Videogame(*x))

negozio = Negozio("Gameshop", lista_liste2, lista_liste)

cmd = ""
while cmd != 0:
    with open ("./res/es02_menu.txt", encoding='utf-8') as file:
        print(file.read())
        print ()
    cmd = int(input("Inserisci un numero: "))
    
    if cmd == 1:
        print ("."*50)
        negozio.mostra_videogiochi()
        print ("."*50)

    if cmd == 2: 
        print ("."*50)
        negozio.mostra_fumetti()
        print ("."*50)
    if cmd == 3:
        funzione_giochi("nintendo",3)
    if cmd == 4: 
        funzione_fumetti("alan moore", 2)
    if cmd == 5: 
        scelta = input("Scegli la console per vedere i videogames disponibili: ").casefold()
        funzione_giochi(scelta,3)
    if cmd ==6 : 
        scelta= input("Scegli una casa editrice per vedere i fumetti disponibili: ").casefold()
        funzione_fumetti(scelta, 1)
    if cmd == 7: 
        scegli = input("Scegli una parola chiave per vedere tutti i videogiochi e i fumetti che presentano nel titolo la parola chiave: ")
        for x in lista_liste:
            if scegli.casefold() in x[0].casefold() :
                print (Fumetti(*x))
        for x in lista_liste2:
            if scegli.casefold() in x[0].casefold() :
                print (Videogame(*x))
    if cmd == 8:
        for x in lista_liste2:
            if int(x[4]) >= 60 and int(x[4])<=90 :
                print (Videogame(*x))
    if cmd== 9:
        for x in lista_liste2:
            if int(x[4]) >90 :
                print (Videogame(*x))
    if cmd == 10:
        print (f"\nLa media delle pagine di tutti i fumetti è {media()}\n")
    if cmd == 11:
        scelta = input("\nScegli un disegnatore per vedere la media delle pagine dei fumetti: ")
        print (f"\nLa media delle pagine di {scelta.title()} è {media(scelta)}\n")
    if cmd == 12: 
        funzione_massimo_minimo(True)
    if cmd == 13:
        funzione_massimo_minimo(False)
    if cmd == 14:
        pagine = sorted (lista_liste, key= lambda x: int (x[4]))
        for x in pagine:    
            print (Fumetti(*x))
    if cmd == 15:
        alto = sorted(lista_liste2, key= lambda x : x[4], reverse=True )
        for x in alto: 
            print (Videogame(*x))
    if cmd == 16:
        print ("Aggiungi un videogioco:\n")
        videogioco = Videogame(titolo=input("Titolo: "),console=input("Console: "),genere=input("Genere: "),studio_sviluppo=input("Studio sviluppo: "),voto_critica=input("Voto critica: "))
        if isinstance(videogioco, Videogame):
            with open('res/videogames.csv', 'a', newline='', encoding='utf-8') as file:
                file.write(videogioco.stampa_file())
                file.seek(0)
    if cmd == 17:
        print ("Aggiungi un nuovo fumetto:\n")
        fumetto = Fumetti(titolo=input("Titolo: "),casa_editrice=input("Casa_editrice: "), scrittore=input("Scrittore: "),disegnatore=input("Disegnatore: "),n_pagine=input("Numero pagine: "))
        if isinstance(fumetto, Fumetti):
            with open('res/fumetti.csv', 'a', newline='', encoding='utf-8') as file:
                file.write(fumetto.stampa_file())
                file.seek(0)

    if cmd == 0:
        exit() 