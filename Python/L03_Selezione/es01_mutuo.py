'''
Calcolare il valore della rata di una casa sapendo che
la casa ha 3 stanze:
    salotto: quadrato
    camera da letto: rettangolare
    bagno: quadrato
Il valore totale del mutuo è dato dal valore al metro quadro per il numero di metri quadrati.
Una volta trovato il mutuo totale, dividerlo per il numero delle rate in cui si vuole 
suddividere il costo.
Il programma richiede all'utente nome, cognome, anno di nascita e in quante rate vuole dividere
il mutuo, dimensioni stanze

Stampare una scheda che riporti
Nomitativo: [nome] [cognome] - [eta]
Metri casa: [metriquadrati] m - Costo metro quadro: [costometroquadro] €
Valore Mutuo: [valore mutuo] € - Numero rate: [numerorate] - Importo singola rata: [rata] €
'''

# Svolgimento

# salotto:

lato = int (input("Quanto misura il lato del salotto: "))
area_salotto = lato**2

# camera da letto 

base = int(input("Quanto misura la base della stanza: "))
altezza =  int(input("Quanto misura l'altezza della stanza: "))
area_camera = base * altezza

#bagno 
lato_b = int (input("Quanto misura il lato del bagno: "))
area_b = lato_b**2

# valore metro quadrato 
valore_metroq = 8051

# metro quadrato intera casa

casa = area_salotto + area_b + area_camera

# valore mutuo

mutuo = casa * valore_metroq

# rate

anni = int (input("In quanti anni vuoi pagare il mutuo? "))

# rata mutuo
numero_rate = anni * 12
rata_mutuo = mutuo / numero_rate
rata_mutuo = round (rata_mutuo,2)

# dati sensibili
nome = input("Qual è il tuo nome?: ")
cognome = input("Qual è il tuo cognome?: ")
anno_di_nascita = int(input("Quando sei nato? (inserire l'anno): "))
eta = 2024 - anno_di_nascita

# scheda

print ("." * 50)

print (f"Nomitativo: {nome} {cognome} - {eta} anni")
print (f"Metri casa: {casa} m2 - Costo metro quadro: {valore_metroq} €")
print (f"Valore Mutuo: {mutuo} € - Numero rate: {numero_rate} - Importo singola rata: {rata_mutuo} €")

print ("." * 50)