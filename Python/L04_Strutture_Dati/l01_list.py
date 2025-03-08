
# la lista (list) è  una struttura ordinata che 
# può contenere elementi 

# lista viene definita da []
print ([1,2,3])
print (type([1,2,3]))

# creo una lista vuota tramite literal []
my_list1 = []
# oppure un altro metodo è 
my_list2 = list()

print (my_list1, my_list2) # stampera solo le parentesi vuote


# esempi
# Anche nelle liste gli indice partono da 0
my_list_num = [63, 25, 89, 5, 17, 99]
#              0    1   2  3   4   5   

print (my_list_num)

# in: mi dice se un valore è contenuto nella lista

print (25 in my_list_num) # darà true


# un altro esempio di in: 
stringa = "ciao"
print ("ci" in stringa) # darà true

print (my_list_num[0]) # per stampare un elemento della lista
 
print ()

# insert (n, elemento) --> inserisce l'elemento nella posizione n della lista
# se andiamo oltre l'indice lo metterà alla fine 
# in questo abbiamo messo 12 ma ce lo mette alla posizione 6
my_list_num.insert(12, 444)
print (len(my_list_num))

# append (elemento) --> aggiunge un elemento alla fine della lista
my_list_num.append(-12)
print (my_list_num)

# remove(elemento) --> rimuove la prima apparizione dell'elemento

my_list_num.remove(89) 
print (my_list_num)

print()

# esempio

my_lista_nintendo = ["Mario", "Luigi", "Peach"]
print (my_lista_nintendo)
print ("Mario" in my_lista_nintendo) # True or False
print ("my_list_nintendo [0]: ", my_lista_nintendo[0])
print ("my_list_nintendo [1]: ", my_lista_nintendo[1])
print ("my_list_nintendo [2]: ", my_lista_nintendo[2])
# aggiungere lista all'iterno di se stessa
# [...] indica che la lista contiene un riferimento a se stessa
lista_prova_folla = [1, 2, 3]
lista_prova_folla.append(lista_prova_folla)

print (lista_prova_folla)

print("Lunghezza my_lista_nintendo: ", len(my_lista_nintendo))

my_lista_nintendo.insert(1, "Link")
print (my_lista_nintendo)


print ("my_list_nintendo [0]: ", my_lista_nintendo[0])
print ("my_list_nintendo [1]: ", my_lista_nintendo[1])
print ("my_list_nintendo [2]: ", my_lista_nintendo[2])
print ("my_list_nintendo [3]: ", my_lista_nintendo[3])

print ("Yoshi" not in my_lista_nintendo) # true or false

# inizio incluso fine escluso
print (my_lista_nintendo[1:3])

# dal -2 fino alla fine 
print (my_lista_nintendo[-2:])

# prendi elemento in posizione -5, conto da destra a partire da -1

# cancello elemento lista
# "del" cancello qualcosa dalla lista
print (my_lista_nintendo)
del my_lista_nintendo[0]
print (my_lista_nintendo)

# per non confonderci 
# [0][0] concatenazioni di "prendere"
# il primo [0] significa da una lista prendi il primo elemento
# il secondo [0] dal primo elemento della lista prendi il primo indice
# quindi se il primo elemento di una lista [0]:["Zelda", "Link"]
# sarà "Zelda"
# il primo indice [0] è di Zelda è Z

print (my_lista_nintendo [0][0])

# rimuovi e restituisce
# pop() elimina l'ultimo elemento della lista 
# inoltre mi restituisce l'elemento cancellato
# se nelle parentesi non scrivo nulla mi cancella e prende l'ultimo elemento
# 
# a = my_lista_nintendo.pop()

# print (a)
print (my_lista_nintendo)
my_lis_pop = []
my_lis_pop.append(my_lista_nintendo.pop())
print (my_lis_pop)
print (my_lista_nintendo)

print ("." * 50)

# se diciamo nuova lista = lista 
# stiamo indicando che entrambre le liste puntano alla stessa struttura
# quindi le modifiche apportate si riflettono su entrambre le variabili

nintendo = my_lista_nintendo

print (nintendo, my_lista_nintendo, sep = "-"*10)
# avranno lo stesso id
print (id(nintendo), id(my_lista_nintendo), sep = "-"*10 )

# proviamo ad aggiungere qualcosa
nintendo.append ("Wario")
print (nintendo, my_lista_nintendo, sep = "-"*10)

# quindi per duplicare una lista l'unico modo è usare: 
# .copy() 

print ("." * 50)


switch = my_lista_nintendo.copy()
# ora avremo due "id" e quindi due oggetti diversi per python
print (id(switch), id(my_lista_nintendo), sep = "-"*10 )

# per cancellare una lista invece basterrà utilizzare
# .clear ()
# a differenza di "del()" .clear() ci lascia la variabile
# avremo con .clear () una lista vuota
# con del() non avremo più nessuna lista

switch.clear()
print (switch)

print ("." * 50)

l1 = [1, 2, 3]
l2 = [2, 5, 6]
# se facciamo la somma avremo una lista dopo l'altra
# [1, 2, 3, 2, 5, 6]
l3 = l1 + l2 # attenzione l3 = l2 + l1 != l1 + l2
print (l3)

# .count (elemento) conta quante volte l'elemento è presente nella lista
print (f"conta 1 in {l3} : ", l3.count(3))

cerca = int (input ("Indica un numero:  "))

print (f"Conta {cerca} in {l3}: ", l3.count(cerca))

print ("." * 50)
batman = ["Bruce", "Wayne"]
superman = ["Clark","Kent"]
flash = ["Barry","Allen"]
lanterna_verde = []
lanterna_verde.append(input("Inserisci un nome: "))
lanterna_verde.append(input("Inserisci un cognome: "))
print (lanterna_verde)

lista_liste = []

lista_liste.append(superman)
print (lista_liste)

lista_liste.insert (0 , batman)
print (lista_liste)

# ovviamente: 
# se uso gli indici su una stringa, mi sto riferendo ai carattere che compongono la stringa
# se uso gli indici su una lista, mi sto riferendo agli elementi che compongono una lista
# questi elementi possono essere numeri, parole, booleani, liste ecc...
# es: se ho una lista di liste allora con gli indici mi riferisco alle liste che compongono la lista di liste

# posso direttamente creare una lista di liste

lista_liste = [[],[],[]]# creo una lista con al suo interno delle liste

lista_liste = [["Bruce", "Wayne"],["Clark","Kent"], ["Barry","Allen"]]# creo una lista con al suo interno delle liste
print(type(lista_liste[0])) #ottengo una lista ["Bruce", "Wayne"]
print(type(lista_liste[0][0])) # ottengo "Bruce" che è una stringa

print (lista_liste[0][0][0:2]) # ottengo le prime due lettere di "Bruce", "Br"  

# .index(elemento) restituisce l'index\indice\posizione dell'elemento
print (my_lista_nintendo)
print ("Indice di Luigi: ", my_lista_nintendo.index("Luigi"))

print (lista_liste[0].index("Wayne"))

cerca = input ("Cosa vuoi cercare? ")

if cerca in my_lista_nintendo:
    indice_cercato = (my_lista_nintendo.index(cerca))
    print (f"L'elemento è presente alla posizione: {indice_cercato}")
else: 
    print ("elemento non presente")

elemento_ricercato = input("Cosa vuoi cercare : ")
posizione = int(input ("Posizione elemento: "))

if elemento_ricercato in my_lista_nintendo:
    if my_lista_nintendo.index(elemento_ricercato) == posizione:
        print ("vero")
    else: 
        print ("false")
# reversed() 
# con la funzione reversed () andiamo a prendere i valori di un iterabile 
# o lista dall'ultimo al primo
lista10 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
lista2 = []
for p in reversed(lista10):
    lista2.append(p)
    #print (p)
print (lista2)

# Il metodo .join() in Python è usato per unire gli elementi di un iterable 
# (come una lista o una tupla) in una singola stringa, separando gli elementi 
# con una stringa specificata.

# Sintassi:
# "separatore".join(iterable)

# separatore: Una stringa che sarà inserita tra gli elementi dell'iterable.
# iterable: Una sequenza (lista, tupla, set, ecc.) o un oggetto che produce stringhe.

parole = ["Ciao", "mondo", "Python"]
risultato = " ".join(parole)
print(risultato)  # Output: "Ciao mondo Python"

caratteri = ["P", "y", "t", "h", "o", "n"]
risultato = "".join(caratteri)
print(risultato)  # Output: "Python"