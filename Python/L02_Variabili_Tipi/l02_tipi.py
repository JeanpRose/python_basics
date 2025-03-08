# le varaiabili possono contenere dati di vario tipo
# ogni tipo ha le sue caratteristiche

# Tipi: 

# Testo = str (strings)
# Numeri interi = int (intero positivo o negativo)
# Numeri decimali = float (floating point number) ad esempio 3.5, ricordarsi che la parte decimale è con il punto e non con la virgola
# Boolean = due valori possibili (True|False)
print() #se si vuole uno spazio vuoto prima
#str 
stringa = 'qualcosa'
print('---string---')
print(stringa)
print(type(stringa))

print('.'* 40) #aggiunge punti per 40 volte

# int
numero_intero= 11 
print('---numero intero---')
print(numero_intero)
print(type(numero_intero))


print('.'* 40) #aggiunge punti per 40 volte

# float
numero_decimale= 3.5
print('---numero decimale---')
print(numero_decimale)
print(type(numero_decimale))

print('.'* 40) #aggiunge punti per 40 volte

# bool
booleano= True # sempre iniziale maiuscola sennò non funziona
print('-Booleano:')
print(booleano)
print (type(booleano))


# eliminare una variabile
del numero_decimale
print(numero_decimale) # errore perche ho gia cancellato