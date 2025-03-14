with open ('C:/Users/lordj/Desktop/DAITA24/L06_lettura_file/res/menu_ristorante.txt', encoding='utf-8') as file:
    print ("\nBenvenuto al mio ristorante\n")
    print ("Questo è il menù:\n")
    c = " "
    while c != "0":
       
        print (file.read())   
        c = int(input("inserisci un valore corrispondente a ciò che vuoi visualizzare: "))  
        
        with open ('C:/Users/lordj/Desktop/DAITA24/L06_lettura_file/res/menu_piatti.txt') as file1:
            n_piatti = int (file1.readline())
            elementi_file = file1.read().splitlines()
            
            lista_piatti_secondi =[]
            lista_piatti_primi =[]
            lista_piatti_contorni= []
            lista_piatti_antipasti= []
            lista_c = []
            lista_ultimata = []
            lista_piatti = []
            for elemento in range (0,len(elementi_file),3):
                lista = elementi_file[elemento:elemento+3]
                lista_c = lista[0]+ ", "+ lista[1]
                prova = lista[0]+","+lista[1]+","+lista[2]
                lista_piatti.append (lista_c)
                lista_ultimata.append(prova)

            for i  in lista_ultimata:
                if "Primo" in i:
                    lista_piatti_primi.append(i.replace(",Primo",""))
                if "Secondo" in i:
                    lista_piatti_secondi.append(i.replace(",Secondo",""))
                if "Antipasto" in i:
                    lista_piatti_antipasti.append(i.replace(",Antipasto",""))
                if "Contorno" in i:
                    lista_piatti_contorni.append(i.replace(",Contorno",""))
        if c == 1:
                print("-"*40)
                print (f"\nCi sono {n_piatti} piatti nel mio menù")
                 # Serve solo per visualizzare meglio:
                print ("\nAntipasti:\n") 
                for j in lista_piatti_antipasti:
                    dettaglio = j.split(",")
                    print (*dettaglio, end="€\n")
                print ("\nPrimi:\n")
                for j in lista_piatti_primi:
                    dettaglio = j.split(",")
                    print (*dettaglio, end="€\n")
                print ("\nSecondi:\n")
                for j in lista_piatti_secondi:
                    dettaglio = j.split(",")
                    print (*dettaglio, end="€\n")
                print ("\nContorni:\n")
                for j in lista_piatti_contorni:
                    dettaglio = j.split(",")
                    print (*dettaglio, end="€\n")

                print("-"*40)
        if c == 2:
            lista_prezzi = []
            print("-"*40)
            for elemento in range (0,len(elementi_file),3):
                lista1 = elementi_file[elemento:elemento+3]
                prezzo= int(lista1[1])
                lista_prezzi.append(prezzo)
            costo_medio = sum(lista_prezzi)/(len(lista_prezzi))
            
            print (f"Il costo medio dei piatti è: {round(costo_medio,2)}")
            print("-"*40)
        if c == 3:
            
            print ("\nDimmi che categoria vuoi visualizzare:\n")
            scelta = input("Antipasti, Primi, Secondi o Contorni? ").capitalize()
            print("-"*40)
            if scelta == "Antipasti":
                print ("\nAntipasti:\n")
                for j in lista_piatti_antipasti:
                    dettaglio = j.split(",")
                    print (*dettaglio, end="€\n")
                    
            if scelta == "Primi":
                print("\nPrimi:\n")
                for j in lista_piatti_primi:
                    dettaglio = j.split(",")
                    print (*dettaglio, end="€\n")
            if scelta =="Secondi":        
                print ("\nSecondi:\n")
                for j in lista_piatti_secondi:
                    dettaglio = j.split(",")
                    print (*dettaglio, end="€\n")
            if scelta == "Contorni":
                print ("\nContorni:\n")
                for j in lista_piatti_contorni:
                    dettaglio = j.split(",")
                    print (*dettaglio, end="€\n")
            print("-"*40)
        if c == 4:
            
            prezzo1 =[]
            prezzi =[]
            cost = []
            print ("\nInserisci Antipasto, Primo, Secondo o Contorno per sapere il prezzo medio della categoria scelta: ")
            scelta1 = input("Antipasti, Primi, Secondi o Contorni? ").capitalize()
            print("-"*40)
            if scelta1 == "Primi":
                for i in lista_piatti_primi:
                    cost.append(i.split(","))
                for j in cost:
                    prezzo1 = int(j[1])
                    prezzi.append(prezzo1)
                costo_medio1 = sum(prezzi)/len(prezzi)
                print (f"Il costo medio dei {scelta1} è {costo_medio1}")

            if scelta1 == "Secondi":
                for i in lista_piatti_secondi:
                    cost.append(i.split(","))
                for j in cost:
                    prezzo1 = int(j[1])
                    prezzi.append(prezzo1)
                costo_medio1 = sum(prezzi)/len(prezzi)
                print (f"Il costo medio dei {scelta1} è {costo_medio1}")

            if scelta1 == "Contorni":
                for i in lista_piatti_contorni:
                    cost.append(i.split(","))
                for j in cost:
                    prezzo1 = int(j[1])
                    prezzi.append(prezzo1)
                costo_medio1 = sum(prezzi)/len(prezzi)
                print (f"Il costo medio dei {scelta1} è {costo_medio1}")

            if scelta1 == "Antipasti":
                for i in lista_piatti_antipasti:
                    cost.append(i.split(","))
                for j in cost:
                    prezzo1 = int(j[1])
                    prezzi.append(prezzo1)
                costo_medio1= sum(prezzi)/len(prezzi)
                print (f"Il costo medio degli {scelta1} è {costo_medio1}")
            print("-"*40)

        if c == 5: 
            print("-"*40)
            print("\nIl piatto più costoso è:\n")
            lista_costi = []
            for elemento in range (0,len(elementi_file),3):
                lista = elementi_file[elemento:elemento+3]
                piatto_costoso = int(lista[1])
                lista_costi.append(piatto_costoso)
            massimo = lista_costi[0]
            for n in lista_costi:
                if n > massimo:
                    massimo = n
            indici =[]
            for i in range (len(lista_costi)-1):
                if massimo == lista_costi[i]:
                    indice_cercato = i
                    indici.append(indice_cercato)
            for i in indici:
                    print (f"{lista_piatti[i]}€\n")
            print("-"*40)
                        
        if c == 6:
            print("-"*40)
            print("La categoria più riccorente è:")
            massimo1 = len(lista_piatti_antipasti)
            massimo2 = len (lista_piatti_contorni)
            massimo3 = len (lista_piatti_primi)
            massimo4 = len (lista_piatti_secondi)
            
            if massimo1> massimo2 and massimo1> massimo3 and massimo1> massimo4:
                print (f"\nAntipasti, sono {massimo1}")
            if massimo2> massimo1 and massimo2> massimo3 and massimo2> massimo4:
                print (f"\nI contorni, sono {massimo2}")
            if massimo3> massimo1 and massimo3> massimo2 and massimo3> massimo4:
                print (f"\nI primi, sono {massimo3}")
            if massimo4> massimo2 and massimo4> massimo3 and massimo4> massimo1:
                print (f"\nI Secondi, sono {massimo4}")
            print("-"*40)
            
        if c == 0:
            print("-"*40)
            print ("Grazie di essere venuto al mio ristorante")
            print("-"*40)
            exit()
        
                    
            
            
                

               


