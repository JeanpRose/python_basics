# un set è una collezione di dati non ordinata non modificabile*
# e senza indice

# *Gli elementi del set non sono modificabili, ma è possibile aggiungere
# o rimuovere elementi

# ha le stesse parentesi del dizionario, ma cambia la sintassi. 
# non ci sono i due punti ":"

my_set = {3,4,5,6}
altro_set = set ()

print (my_set, type(my_set))

altro_set.add("a")

print (altro_set)
# se un elemento è già presente non lo aggiunge
# i set non ammettono duplicati
altro_set.add("a")
print (altro_set)



my_set.add(1)
my_set.add(30)
my_set.add(7)
my_set.add(41)
my_set.add(0)
my_set.add(1000)
my_set.add(88)
print(my_set)



yamaha2021 = {20, 21, 25, 46, 4}
yamaha2022 = {20, 21, 4, 40, 35}

print ("yamaha2021 = ", yamaha2021)
print ("yamaha2022 = ", yamaha2022)

# elementi comuni tra due set (insiemi)
# & è l'intersezione tra i due set
# oppure .intersection()

print("Intersezione => ", yamaha2021 & yamaha2022 )
# altro metodo: 
print("Intersezione => ", yamaha2021.intersection(yamaha2022))

# intersection.update mi aggiornerà il set con le intersezioni 
print ("yamaha2021 = ", yamaha2021)

# print("Intersezione => ", yamaha2021.intersection_update(yamaha2022))
print ("yamaha2021 = ", yamaha2021)

# unione tra due set, prendo tutti gli elementi senza ripetizioni
# | => unione tra due set

print ("Unione => ", yamaha2021|yamaha2022)

# si puo fare la differenza tra due set
# bisogna stare attenti che sonon due cose differenti
print ("."*100)
print ("yamaha2021 = ", yamaha2021)
print ("yamaha2022 = ", yamaha2022)

print ("Differenza tra Yamaha2021-Yamaha2022", yamaha2021-yamaha2022)
print ("Differenza tra Yamaha2022-Yamaha2021", yamaha2022-yamaha2021)

# differenza simmetrica tra due set 
# considera solo gli elementi non condivisi tra i set

print ("Differenza simmetrica tra Yamaha2021-Yamaha2022", yamaha2021^yamaha2022)
print ("Differenza simmetrica tra Yamaha2022-Yamaha2021", yamaha2022.symmetric_difference(yamaha2021))


# .remove(elemento) rimuove un elemento, se non è presento genera un'eccezione 
print (yamaha2021)

yamaha2021.remove (20)

print (yamaha2021)

# .discard rimuove un elemento da un set, ma non genera un eccezione se l'
# elemento non è presente (con .remove da errore)

yamaha2021.discard(232)


# .pop() rimuove un elemento a caso e ce lo restituisce

print (yamaha2021.pop()) # random


# .update aggiunge ad un set gli elementi di un altro set se non sono duplicati
print(my_set)
inserisci = ('ciao', 'come', 'va')
my_set.update(inserisci)
print(my_set)

# costruisco un set da iterabili (tupla)
print (altro_set)
altro_set = set(inserisci)
print(altro_set)


# .join si può usare anche sui set

animali = {"Cane", "Gatto", "Pesce"}
risultato = ", ".join(animali)
print(risultato)  
# Output: "Pesce, Cane, Gatto" (l'ordine può variare perché i set non sono ordinati)