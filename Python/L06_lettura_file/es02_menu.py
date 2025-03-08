# leggere file gruppi
# poi creare menu interattivo
with open("C:/Users/lordj/Desktop/DAITA24/L06_lettura_file/res/menu_gruppi.txt", encoding="utf-8") as file:
    menu = file.read()

list_band = []
list_dischi = []
list_provenienza = []


cmd = " "

while cmd != 0:
    with open("C:/Users/lordj/Desktop/DAITA24/L06_lettura_file/res/gruppi.csv", "r+",encoding="utf-8") as file:
        elementi_file = file.read().splitlines()
        for elemento in elementi_file:
            dettagli = elemento.split(",")
            list_band.append(dettagli [0])
            list_dischi.append(int(dettagli[1]))
            list_provenienza.append(dettagli[2])

    cmd = int(input(menu + "\nInserisci un numero: "))
    cresc =[]
    for i in range(len(list_dischi)):
        
        band = {}
        band[list_band[i]] = list_dischi[i]
        cresc.append(band)
    diz = {}
    for lista in cresc:
        diz.update(lista)
        
    dizionario_ordinato = dict(sorted(diz.items(), key=lambda item: item[1]))
        
    band1 = list (dizionario_ordinato.keys())
    dischi1 = list (dizionario_ordinato.values())

    if cmd == 1:
        print("-" * 40)
        print ("La lista delle band è:")
        for i in list_band:
            print (i)
        print("-" * 40)
    if cmd == 2:
        print("-" * 40)
        media = sum(list_dischi)/len(list_dischi)
        print(f"La media complessiva dei dischi è {round (media)}")
        print("-" * 40)
    if cmd == 3:
        print("-" * 40)
        
        print(f"Elenco dei gruppi britannici:")
        for i in range(len(list_provenienza)):
            if list_provenienza[i] ==  "Regno Unito":
                print ("."*20)
                print(f"Band:{list_band[i]} \nDischi:{list_dischi[i]}\nPaese:{list_provenienza[i]}")
                print ("."*20)
        print("-" * 40)  
    if cmd == 4:
        print("-" * 40)
        lista_eng = []
        somma = 0
        print(f"Media dischi dei gruppi britannici:")
        for i in range(len(list_provenienza)):
            if list_provenienza[i] ==  "Regno Unito":
                lista_eng.append(list_provenienza[i])
                somma += list_dischi[i]
        
        print(f"La media è: {round (somma / len(lista_eng))}")
                
        print("-" * 40) 
    if cmd == 5: 
        print("-" * 40)
        lista_ame = []
        somma = 0
        print(f"Media dischi dei gruppi americani:")
        for i in range(len(list_provenienza)):
            if list_provenienza[i] ==  "Stati Uniti":
                lista_ame.append(list_provenienza[i])
                somma += list_dischi[i]
        
        print(f"La media è: {round (somma / len(lista_ame))}")
                
        print("-" * 40)
    if cmd == 6: 
        print("-" * 40)
        print ("Elenco dei gruppi che hanno più di 10 dischi:")
        
        for i in range(len(list_dischi)):
            if list_dischi[i] > 10:
                print ("."*20)
                print(f"Band:{list_band[i]} \nDischi:{list_dischi[i]}")
                print ("."*20)
    if cmd == 7: 
        print('-' * 40)
        print("Elenco dei gruppi in base al numero di dischi in ordine crescente")
        print ("."*20)

        for i in range (len(band1)):
            print (band1[i], dischi1[i])
        print ("."*20)

    if cmd == 8:
        print ("\nGruppo con meno dischi:\n")
        
        minimo = dischi1[1]
        for n in dischi1:
            if n < minimo:
                minimo = n
        indici =[]
        for i in range (len(dischi1)):
            if minimo == dischi1[i]:
                indice_cercato = i
                indici.append(indice_cercato)
        for i in indici:
            print (f"{band1[i]} e hanno {dischi1[i]} dischi\n" if band1[i] != "Jimi Hendrix" else f"{band1[i]} e ha {dischi1[i]} dischi\n" )
        print("-"*40)
    if cmd == 9:
        print("-" * 40)
        print ("."*20)
        band_eng=[]
        for i in range(len(list_provenienza)):
            if list_provenienza[i] ==  "Regno Unito":        
                band_eng.append(list_band[i])
        print(f"Gli inglesi sono: {len(band_eng)}")
        print ("."*20)

        print ("."*20)
        band_ame=[]
        for i in range(len(list_provenienza)):
            if list_provenienza[i] == "Stati Uniti":        
                band_ame.append(list_band[i])

        print(f"Gli americani sono: {len(band_ame)}")
        print ("."*20)
        print ("."*20)
        band_aus=[]
        for i in range(len(list_provenienza)):
            if list_provenienza[i] == "Australia":        
                band_aus.append(list_band[i])

        print(f"Gli australiani sono: {len(band_aus)}")
        print ("."*20)
        print("-" * 40)
    if cmd == 10:
        decisione = input("Inserisci un nome e verificherò se il gruppo è presente: ").title()
        if decisione in list_band:
            print ("."*20)
            print("Il gruppo è presente")
            print ("."*20)
        else: 
            print ("."*20)
            print ("Il gruppo non è presente")
            print ("."*20)
            

    if cmd == 11:
        decisione1 = input("Inserisci una parola o carattere e verificherò se è presente nel gruppo: ").casefold()
        print ("."*20)
        for i in list_band:
            if decisione1 in i.casefold():
                print(f"{decisione1} è presente in {i}")
        print ("."*20)

    if cmd == 12: 
        with open('res/gruppi.csv', 'a') as file:
            band2 = input("Insersci il nome di una band: ").capitalize()
            dischi2 = input("Inserisci il numero di dischi: ")
            provenienza2 = input("Inserisci la provenienza: ").capitalize()
            file.write(f"\n{band2}, {dischi2}, {provenienza2}")
            file.seek(0)

    if cmd == 13:
        print("-" * 40)
        set_prov =set(list_provenienza)
        output = ""
        for i in set_prov:
            if output:  # Se la stringa non è vuota, aggiungi una virgola
                output += ", "
            output += i

        
        print()

        print ("Elimino i gruppi in base al paese che mi indichi: ")
        print()
        print  ("Scegli tra: ", output)
        eliminazione = input().title()
        print ("."*20)
        for i in range(len(list_provenienza)):
            if eliminazione in list_provenienza[i]:
                continue
            else:
                print(list_band[i],",", list_dischi[i], ",",list_provenienza[i])
        print ("."*20)
        print("-" * 40)
    if cmd == 0:
        exit()


    