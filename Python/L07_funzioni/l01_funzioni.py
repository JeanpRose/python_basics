import random

# funzioni
# In Python, le funzioni sono blocchi di codice che eseguono un'operazione specifica. 
# Ti permettono di riutilizzare il codice, ridurre la ripetizione e rendere 
# i programmi più modulari.


# Una funzione in Python si definisce con la parola chiave def 
# seguita dal nome della funzione e, opzionalmente,
#  da parametri tra parentesi.


def saluta(nome):
    print(f"Ciao, {nome}!")

# def: parola chiave per definire una funzione.
# saluta: il nome della funzione.
# nome: un parametro della funzione.

# Una volta definita, puoi chiamarla semplicemente usando il suo nome 
# seguito da parentesi:

saluta("Mario")  # Output: Ciao, Mario!



# Le funzioni possono restituire valori usando la parola chiave return.

def somma(a, b):
    return a + b

risultato = somma(3, 5)
print(risultato)  # Output: 8


# Parametri e argomenti
# Parametri: i nomi definiti nella funzione.
# Argomenti: i valori passati alla funzione.


# Parametri predefiniti: puoi assegnare valori di default ai parametri.
def saluta(nome="Anonimo"):
    print(f"Ciao, {nome}!")

saluta()  # Output: Ciao, Anonimo!
saluta("Luca")  # Output: Ciao, Luca!


# Argomenti posizionali e nominati: puoi passare argomenti in base alla
#  posizione o con il nome del parametro.


def dettagli(nome, età):
    print(f"Nome: {nome}, Età: {età}")

dettagli("Anna", 25)  # Posizionali
dettagli(età=25, nome="Anna")  # Nominati



# Funzioni anonime (Lambda)
# Una lambda function è una funzione anonima, 
# usata per operazioni semplici.

somma = lambda a, b: a + b
print(somma(3, 5))  # Output: 8


# Funzioni come oggetti
# Le funzioni possono essere assegnate a variabili 
# passate come argomenti o restituite da altre funzioni.

def saluta():
    return "Ciao!"

f = saluta  # Assegna la funzione a una variabile
print(f())  # Output: Ciao!



# Tipi di argomenti avanzati
# Argomenti arbitrari (*args): permette di passare un numero variabile 
# di argomenti.

def somma(*numeri):
    return sum(numeri)

print(somma(1, 2, 3))  # Output: 6



# Argomenti arbitrari con chiave (**kwargs): 
# permette di passare argomenti nominati variabili.

def dettagli(**info):
    for chiave, valore in info.items():
        print(f"{chiave}: {valore}")

dettagli(nome="Anna", età=25, città="Roma")



# Funzioni annidate
# Puoi definire funzioni dentro altre funzioni.

def esterna():
    def interna():
        print("Funzione interna!")
    interna()

esterna()  # Output: Funzione interna!



# Decoratori
# I decoratori sono funzioni che prendono un'altra funzione come 
# argomento, la modificano o la estendono.

def decoratore(funzione):
    def wrapper():
        print("Prima della funzione")
        funzione()
        print("Dopo la funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")

saluta()

# Documentazione delle funzioni
# Puoi aggiungere una docstring per descrivere cosa fa la funzione.

def saluta(nome):
    """Saluta una persona specifica."""
    print(f"Ciao, {nome}!")

print(saluta.__doc__)



## esempio dado

print ("----------Lancio Dado senza return")
# roba inutile
def lancio_dado_senza_return():
    random.randint(1,6)
lancio_dado_senza_return()



print ("----------Lancio Dado con print")
def lancio_dado_con_print():
    print (random.randint(1,6))

lancio_dado_con_print()

def lancio_dado ():
    return random.randint(1 , 6)

print ("--- lancio dado \n",lancio_dado())

print ("lancio dado 200 volte: ")
for n in range(201):
    print (lancio_dado())








