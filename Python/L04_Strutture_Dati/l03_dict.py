# dizionario: struttura dati *ordinata che contiene delle coppie (chiave, valore)
# la chiave è univoca e ad essa sono associati valori
# ( key : value)
# i valori sono raggiungibili tramite la chiave corrispondente

# *dalla versione 3.7 dizionari sono ordinati, prima non è ordinata

# dizionari vuoti
my_dict = {}
my_dict = dict()

print (my_dict)
print (type (my_dict))

# creiamo un dizionario 
punteggi = {
    # key (valore univoco) : value (valore associato)
    "primo" : "25",
    "secondo": 20,
    "terzo": 16
}

print (punteggi)

# se voglio stampare solo uno dei valori del dizionario uso la chiave
# nome_dizionario [key]
print ("punteggio [\"primo\"]", punteggi ["primo"])

# modifica o inserimento 
# se la chiave esiste modifico, se no inserisco nuova coppia

punteggi["terzo"] = 15
print (punteggi)

punteggi["quarto"] = 10
print (punteggi)


print ()

# con .keys() ottengo tutte le chiavi di un dizionario
# in un oggetto dict.keys

print (punteggi.keys())

# if "terzo" in list (punteggi.keys())


# con .values() ottengo i valori associati alla chiave
# oggetto dict_values
print (punteggi.values())

# .items() ottengo chiavi e valori del dizionario
# dict_items
print (punteggi.items())

# avrò una lista di tuple. Ogni tupla avrà (chiave,valore)
print (list(punteggi.items()))


prova = {
    "id" : 0,
    "dati_anagrafici": {
        "nome":"filippo",
        "linguaggi" : ["python", "scala"]
    }
}

prova["dati_anagrafici"]["nome"]

print (prova["dati_anagrafici"]["nome"])
print (prova ["dati_anagrafici"]["linguaggi"][1])


print ()

# accesso al valore assocciato ad una chiave tramite il metodo .get()
# nell'esempio andiamo a prendere il valore della chiave "primo"
# se non trova la chiave restituisce "None" oppure possiamo dirgli noi 
# che valore ci deve dare se non trova una chiave
# .get("chiave", -1) se non trova la chiave mi darà -1
print (punteggi.get("primo"))

# per creare una chiave con il valore di un'altra chiave 

punteggi["vincitore"] = punteggi["primo"]
print (punteggi)

# posso cancellare una chiave con del 

del punteggi["primo"]
print (punteggi)


# .update() modifica e aggiunge ad un dizionario

nuovi_punteggi = {
    "primo":125, 
    "secondo": 121
}

print (nuovi_punteggi)

print (punteggi)
punteggi.update(nuovi_punteggi)
print (punteggi)

# .clear() svuota il dizionario

punteggi.clear()
print (punteggi)


# .popitem() elimina l'ultima coppia chiave/valore e restituisce
# una tupla composta da (chiave, valore)
# quindi elimina dal dizionario, ma lo restituisce da qualche parte
# che sia un print o una variabile. 
# Sarà una tupla quello che restituisce


d1 = {
    "a":1,
    "b": 2, 
    "c" : 3
}

print (d1)

print(d1.popitem())


# .pop(chiave) elimina la coppia chiave/valore in base alla chiave indiciata
# restituisce il valore della chiave 
# se non c'è la chiave possiamo aggiungere un parametro di restituzione 
# print (d1.pop("f", "La chiave non è presente"))

print (d1.pop("a"))
print (d1)
print (d1.pop("f", "La chiave non è presente"))

eroi = "batman", "superman"

# .fromkeys(elemento iterabile, valore della chiave)
# creo un dizionario con le chiavi prese dall'iterabile e i valori 
# vengono settati uguali al valore specificato
# se non specifico nessun valore sarà "None"
 
d_eroi = dict.fromkeys(eroi, "sconosciuto")

print(d_eroi)

identita ={"batman": "Bruce Wayne"}
d_eroi.update(identita)
print (d_eroi)

d_eroi["superman"] = "Nuovo update" 
print (d_eroi)

# creo un dizionario a partire da piu input

chiave = input ("Nome: ")
chiave2 = input ("Nome2: ")

dict_input = { 
    chiave : int(input("Età : ")),
    chiave2 : int(input("Età : "))
}

print (dict_input)

# .copy() per creare una copia di un dizionario
