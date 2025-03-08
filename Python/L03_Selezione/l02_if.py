# if statment 

# SINTASSI

# if condizione:
# indentazione (4 spazi a destra)
#     blocco di codice
#
# istruzione successiva dal programma 

numero = int(input("Indovina il numero da 1 a 10: "))

if numero == 4:
    print ("Hai indovinato")
else: print("Non hai indovinato")

print ("." * 50)

# altro esempio

risposta = input ("Fuori piove? ")
risposta= risposta.casefold() # cosi se l'utente risponde con maiuscole

if risposta == "si":
    print ("Ok prendo l'ombrello")
else: 
    risposta2 = input ("Menomale, c'è il sole? ")
    if risposta2 == "si":
        print ("Daje")

print ("." * 50)

# altro esempio

cinema = input ("Vuoi andare al cinema: ")

if cinema == "si":  
    popcorn = input("Vuoi i popcorn? ")
    if popcorn == "si":
        tempo = input ("Vuoi andare prima di pranzo? ")
        if tempo == "si":
            print ("Allora andiamo!")  

print ("." * 50)


# IF- ELSE
# con if-else definiamo l'esecuzione di due blocchi di codice
# uno nel caso in cui la condizione sia vera (TRUE)
# uno nel caso in cui la condizione sia (FALSE)

# SINTASSI

# if condizione :
#     blocco di codice
# else: 
#     blocco di codice

if numero > 0: 
    print ("il numero è positivo")
else : 
    if numero == 0: 
        print ("Il numero è nullo")
    else:
        print ("Il numero è negativo ")
        

print ("." * 50)

# OPERATORI LOGICI
# and --> tutte le condizioni devono essere verificate
# or --> almeno una condizione deve essere verificata
# not --> negazione 


# in questo caso affinché le condizioni risultino TRUE entrambe 
# le condizioni devono essere TRUE

if numero > 10 and numero < 20: 
    print ("il numero è compreso tra 10 e 20") 
else:
    print ("il numero non è compreso tra 10 e 20") 

print ("." * 50)

if numero < 0 or numero > 100:
    print ("Il numero è minore di 0 o maggiore di 100")

print ("." * 50)

if not numero == 10: 
    print("il numero non è 10")


print ("." * 50)

# IF-ELIF-ELSE
# 
# SINTASSI

# if condizione:
#      blocco di codice
# elif Ccondizione:
#      blocco di codice
# else: 
#      blocco di codice
#
# se una condizione viene verificata l'if-elif-else 
# si ferma e non esegue tutto



if numero == 0:
    print ("numero è nullo")
elif numero > 0:
    print ("numero positivo") 
else: 
    print ("il numero è negativo")


# altro esempio 

nome = input("inserisci il tuo nome: ")

if nome == "Samantha": 
    print ("Ciao Samantha")
elif nome == "Diana":
     print ("Ciao Diana")
elif nome == "Diana":
     print ("Ciao Diana")
elif nome == "Dario":
     print ("Ciao Dario")
elif nome == "Filippo":
     print ("Ciao Filippo")
else: 
    print ("Non ti conosco")


# IF piatti
# si potrebbero verificare entrambe le condizioni
# sono due IF separati

if numero > 0:
    print ("Positivo")
if numero == "pari":
    print ("pari")


# IF ANNIDATI
# if contenuti all'interno di un costrutto 
# if (if, if-else, if-elif-else)

eta = int(input("Inserisci la tua età: "))

if eta >= 0 and eta <=125:
    if eta >= 18:
        print (f"{nome.capitalize()} hai {eta} anni, sei maggiorene")
    else:
        print (f"{nome.capitalize()} hai {eta} anni, sei minorenne")
else:
    print ("Dati inseriti non conformi")
    if eta < 0:
        print ("non sei ancora nato")
    else:
        print ("sei un vampiro")