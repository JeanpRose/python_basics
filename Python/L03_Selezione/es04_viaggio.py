# Scrivi un programma che calcoli diverse informazioni relative al prezzo del biglietto aereo.

# Chiediamo le seguenti informazioni all'utente:

# Il numero totale di persone per il viaggio.
# Quanti tra queste persone hanno un'età inferiore a 14 anni e quante hanno un'età superiore ai 65 anni.
# Quanti bagagli da stiva devono essere registrati.
# La destinazione del viaggio (il continente).
# Il mese di partenza.


# Il prezzo del biglietto si calcola nel seguente modo:
# A seconda della destinazione, il prezzo di partenza per persona varia:
# Europa: 100 euro.
# Africa: 150 euro.
# Asia: 250 euro.
# America: 400 euro.
# Altri continenti: 600 euro.

# A seconda dell'età, si applica uno sconto al prezzo del biglietto:
# Le persone sotto i 14 anni ricevono uno sconto del 15%.
# Le persone sopra i 65 anni ricevono uno sconto del 10%.

# A seconda del mese di partenza, si applica un sovrapprezzo al prezzo del gruppo:
# Febbraio e Novembre: 20% in più.
# Gennaio e Dicembre: 30% in più.
# Giugno, Luglio e Agosto: 50% in più.

# Per ogni bagaglio da stiva registrato, viene aggiunto un sovrapprezzo di 20 euro al prezzo del gruppo.

# In output, desideriamo ottenere le seguenti informazioni:
# Il costo totale del gruppo.
# Il costo del biglietto per un adulto.
# Il costo del biglietto per una persona sotto i 14 anni.
# Il costo del biglietto per una persona sopra i 65 anni.
# Il numero di bagagli da stiva registrati e il costo.
# 

print ("Benvenuto")

numero_persone = int (input("Quante persone siete? "))
if numero_persone < 0: 
    print ("Numero di persone non valido, inserisci un numero positivo")
    exit()

anni_14 = int (input("Quanti hanno meno di 14 anni? ")) if numero_persone > 1 else int (input("Hai meno di 14 anni? "))
if anni_14 > numero_persone:
    print ("Numero di minorenni maggiore del numero di persone totale")
    exit()

anni_65 = int (input("Quanti hanno più di 65 anni? ")) if numero_persone > 1 else int (input("Hai più di 65 anni? "))
if anni_65 > numero_persone:
    print ("Numero di persone maggiori di 65 anni maggiore del numero di persone totale")
    exit()

destinazione = input("Dove viaggiate? [Continente] ").capitalize() if numero_persone > 1 else input("Dove viaggi? [Continente] ").capitalize()
if destinazione == int or destinazione == float:
    print ("Inserire una destinazione valida, non un numero")
    exit()

mese = input("In che mese partite? ").casefold() if numero_persone > 1 else input("In che mese parti? ").casefold()
if mese == int or mese == float:
    print ("Inserire un mese valido, non un numero")
    exit()

bagaglio = int(input("Quanti bagagli avete? ")) if numero_persone > 1 else int(input("Quanti bagagli da stiva hai? "))
if bagaglio == str or bagaglio < 0 :
    print ("Inserire un NUMERO di bagagli valido")
    exit()

# prezzo in base alla destinazione

if destinazione == "Europa": 
    prezzo = 100
elif destinazione == "Africa":
    prezzo = 150
elif destinazione == "Asia":
    prezzo = 250
elif destinazione == "America": 
    prezzo =  400
else: 
    prezzo = 600

# prezzo in base al mese

if mese == "febbraio" or mese == "novembre":
    prezzo += (prezzo*20/100)
elif mese == "gennaio" or mese == "dicembre":
    prezzo += (prezzo*30/100)
elif mese == "giugno" or mese == "luglio" or mese == "agosto":
    prezzo += (prezzo*50/100)

# prezzo

prezzo = prezzo * numero_persone
prezzo_persona = prezzo/numero_persone 
prezzo_persona_14 = 0
prezzo_persona_65 = 0
if anni_14 >= 1:
    prezzo_persona_14 = (prezzo_persona - (prezzo_persona*15/100))*anni_14
    prezzo_14 = prezzo_persona_14 / anni_14
    
if anni_65 >= 1:
    prezzo_persona_65 = (prezzo_persona -(prezzo_persona*10/100))*anni_65
    prezzo_65 = prezzo_persona_65 / anni_65 


adulti = numero_persone - anni_14 - anni_65
prezzo = (prezzo_persona*adulti) + prezzo_persona_14 + prezzo_persona_65

# bagagli

if bagaglio > 1:
    prezzo += (bagaglio * 20)

prezzo_bagaglio = bagaglio *20

# output

print ("."*50)

print (f"""Il prezzo totale è {prezzo}€
il prezzo a persona per un adulto è {prezzo_persona}€""")
print (f"Il costo del biglietto per una persona sotto i 14 anni è {prezzo_14}€\n" if anni_14 >= 1 else "", end = "" )
print (f"Il costo del biglietto per una persona sopra i 65 anni è {prezzo_65}€\n" if anni_65 >= 1 else "", end = "" )
print (f"Il numero di bagagli da stiva registrati è {bagaglio} e il costo è {prezzo_bagaglio}"if bagaglio >= 1 else "")





