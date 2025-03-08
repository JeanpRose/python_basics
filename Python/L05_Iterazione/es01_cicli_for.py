lista_numeri = [5, 9, 25, 33, 114]

# calcolare e stampare la somma dei numeri contenuti nella lista
somma = 0
for i in lista_numeri:
    somma += i

print ("La somma dei numeri è: ", somma)

# creare una nuova lista che contiene i quadrati dei numeri della lista di partenza
quadrati = []

for numero in lista_numeri:
    ris_quadrati = numero * numero 
    quadrati += [ris_quadrati]
  
print ("la lista dei quadrati è: ", quadrati)

lista_parole = ["cane", "Gatto", "gnu", "ghepardo", "alce", "scimmia", "lupo"]

# creare una nuova lista che contiene solo i nomi che iniziano con la lettera g

lista = []
for elemento in lista_parole:
    if elemento[0].casefold() == "g":
        lista += [elemento]  

print ("Gli animali che iniziano con la g sono: ",lista)


# creare una nuova lista che contiene solo i nomi che come seconda lettera hanno una vocale 
vocali = "aeiou"
lista2 = []
for elemento in lista_parole:
    if elemento[1].casefold() in vocali:
        lista2 += [elemento]  

print ("Gli animali che come seconda lettera hanno una vocale sono: ", lista2)




