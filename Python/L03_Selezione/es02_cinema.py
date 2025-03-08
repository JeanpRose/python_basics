# Scriviamo un programma che calcoli il prezzo di un biglietto per il cinema
# Chiediamo all'utente la sua età, il comune di residenza e il lavoro svolto
# Se l'utente è residente a Como, il prezzo del biglietto è 0
# Se l'utente è minorenne il prezzo del biglietto viene scontato di 3€
# Se l'utente ha più di 70 anni, il prezzo del biglietto viene scontato di 5€
# Se l'utente è uno studente o un docente, il biglietto viene scontato di altri 2€
# Di base, il biglietto costa 10€
 
anni = int(input("Quanti anni hai?: "))
citta = input("Dove sei residente attualmente: ")
citta = citta.casefold()
lavoro = input ("Che lavoro fai?: ")
lavoro = lavoro.casefold()

# costo biglietto
biglietto = 10 

if citta == "como": 
    biglietto = 10-biglietto 
    print (f"il costo del biglietto è {biglietto}")
if anni < 18:
    if lavoro == "studente" or lavoro== "docente":
        biglietto = biglietto - 5 
        print (f"Sei minorenne e anche {lavoro} allora il costo del biglieto è scontato di 5€, il totale è {biglietto}€")
    else: 
        biglietto = 10-3 
        print (f"Il costo del biglieto è scontato di 3€, il totale è {biglietto}€")
if anni > 70:
    if lavoro == "studente" or lavoro== "docente":
        biglietto = biglietto - 7 
        print (f"Hai più di 70 anni e sei {lavoro} allora Il costo del biglieto è scontato di 7€, il totale è {biglietto}€")
    else: 
        biglietto = 10-5 
    print (f"Il costo del biglieto è scontato di 5€, il totale è {biglietto}€")
if anni > 18 :
    if lavoro == "studente" or lavoro== "docente":
        biglietto = biglietto - 2  
        print (f"Il costo del biglieto è scontato di 2€ perché sei {lavoro}, il totale è {biglietto}€")
else: 
    print (f"il costo del biglietto è {biglietto}")