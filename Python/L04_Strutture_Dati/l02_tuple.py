# la tupla è una struttura dat immutabile e ordinata che può 
# contenere elementi di tipo eterogeneo (di tipi diversi)

# non è possibilie modificarla

trofei = ()
trofei = tuple()

trofei = ("platino", "oro", "argento", "bronzo")
# posso omettere le parentesi 
trofei = "platino", "oro", "argento", "bronzo"

# come le liste possiamo interaggire 
print ("trofei [0]: ", trofei[0])

# non è possibile modificare una tupla
# trofei [3] = "legno"  #errore

# possiamo contare le cose dentro la tupla

print (trofei.count("oro"))



# possiamo spacchettare i dati contenuti in una tupla

p, o, a, b = trofei
print (p)
print (o)
print (a)
print (b)
# se vogliamo una tupla con un solo elemento dobbiamo scrivere così:
# (elemento,) # metto la virgola
trofei1 = ("bronzo", )
print(type(trofei1))

t= trofei + trofei1
print(t)

print (id(trofei), id(trofei1), id (t))


# ho creato una lista a partire da una tupla


lista_trofeo = list(trofei)
print (type(lista_trofeo), lista_trofeo)

lista_trofeo.append("legno")
print (lista_trofeo)
# da lista a tuple 

trofei_da_lista = tuple (lista_trofeo)
print (type(trofei_da_lista))

spesa = "mela", 3, True, 1.2, lista_trofeo

print (spesa)

# possiamo interagire con le tuple come con le liste
# se vogliamo prendere dalla tupla spesa la lettera "R" 
# della lista trofeo scriveremo: 

print (spesa[4][1][1])