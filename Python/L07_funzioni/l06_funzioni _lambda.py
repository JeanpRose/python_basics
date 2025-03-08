

# funzione lambda, funzione anonima

# vecchio modo di scrivere una funzione: 
        # def somma(x,y):
        #     return x+y


# possiamo definire una funzione anonima che fa la stessa cosa 
# di quella prima

somma = lambda x,y : x+y

print (somma(2,5))


# esempio
numeri = [1,4 ,2, 7, 5, 6]

print (f"Numeri : {numeri}")

# map (funzione, collezione) collezione è un iterabile 
# quindi map è una funzione che si occupa di applicare
#  a tutti gli elementi di un iterabile una funzione

quadrati = list(map (lambda x : x**2, numeri))
print (quadrati)


# esempio
parole = ["cane", "gatto"]

parole_capitalized = list(map(lambda parola: parola.title(),parole))

print (parole_capitalized)

# altro esempio

pari_in_lista_numeri = list(map(lambda numero: numero % 2 == 0, numeri))
print (pari_in_lista_numeri)

# filter (funzione, collezione) --> applica un filtro alla collezione che 
# gli andiamo a passare

pari = list(filter(lambda num: num % 2 == 0, numeri))
print (pari)

# sorted() 
parole = ["cane","gatto", "ghepardo","falco", "radar", "lupo", "coccodrillo", "oca", "anna"]

parole_ordinate  = sorted(parole, reverse = True)

print(parole_ordinate)


parole_ord_per_lunghezza = sorted (parole, key = lambda parola : len(parola), reverse = True)
print (parole_ord_per_lunghezza)


# voglio una lista che mi dia la lunghezza di ogni parola della lista

lunghezza_parole = list(map(lambda p : len(p), parole))

print (lunghezza_parole)


parole_magg_4 = list(filter(lambda x: len(x) > 4, parole))
print (parole_magg_4)


# voglio vedere una lista con solo le parole palindrome

parole_palindrome = list(filter(lambda parola: parola==parola[::-1], parole))
print (parole_palindrome) 