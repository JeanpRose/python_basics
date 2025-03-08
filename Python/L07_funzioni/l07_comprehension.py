#                              List Comprehension

# Usata per creare una nuova lista trasformando o filtrando elementi di un iterabile.

# SINTASSI:
# [espressione for elemento in iterabile if condizione]

# espressione: cosa includere nella nuova lista (può essere una trasformazione).
# elemento: ogni elemento dell'iterabile originale.
# iterabile: la struttura dati su cui iterare.
# condizione (opzionale): un filtro per includere solo certi elementi.

# ESEMPIO:
numeri = [1, 2, 3, 4, 5]
quadrati = [x ** 2 for x in numeri]
print(quadrati)  # Output: [1, 4, 9, 16, 25]


numeri = [1, 2, 3, 4, 5, 6]
pari = [x for x in numeri if x % 2 == 0] # La prima x sarà ciò che ci restituira nella lista
print(pari)  # Output: [2, 4, 6]

numeri = [1, 2, 3, 4, 5, 6]
dispari_triplicati = [x * 3 for x in numeri if x % 2 != 0]
print(dispari_triplicati)  # Output: [3, 9, 15]



#                           Dictionary Comprehension

# Usata per creare un nuovo dizionario trasformando o filtrando coppie chiave-valore.

# SINTASSI: 

# {chiave: valore for elemento in iterabile if condizione}

# chiave: l'espressione che determina le chiavi del dizionario.
# valore: l'espressione che determina i valori corrispondenti alle chiavi.
# iterabile: un oggetto iterabile (ad esempio una lista, una tupla o un dizionario).
# condizione (opzionale): un'espressione booleana che filtra gli elementi da includere.


# ESEMPIO (Invertire chiave e valore):
dizionario = {'a': 1, 'b': 2, 'c': 3}
inverso = {v: k for k, v in dizionario.items()}
print(inverso)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# Filtrare coppie con valori maggiori di 1:
dizionario = {'a': 144, 'b': 2, 'c': 3, "d" : 1}
filtrato = {k: v for k, v in dizionario.items() if v > 1}
print(filtrato)  # Output: {'b': 2, 'c': 3}

#                             Set Comprehension
# Usata per creare un nuovo insieme (set) trasformando o filtrando elementi.ù

# SINTASSI:
# {espressione for elemento in iterabile if condizione}

# Esempio:
# Creare un set di numeri univoci e dispari:

numeri = [1, 2, 2, 3, 4, 5, 5]
dispari = {x for x in numeri if x % 2 != 0}
print(dispari)  # Output: {1, 3, 5}


#                             Generator Comprehension
# Simile alle list comprehension, ma restituisce un oggetto generatore invece di una lista. 
# Questo è utile per risparmiare memoria quando si lavora con grandi quantità di dati.

# SINTASSI:
#  (espressione for elemento in iterabile if condizione)

# Esempio:
# Calcolare il quadrato dei numeri senza creare una lista intermedia:

numeri = [1, 2, 3, 4, 5]
quadrati = (x ** 2 for x in numeri)
print(list(quadrati))  # Output: [1, 4, 9, 16, 25]