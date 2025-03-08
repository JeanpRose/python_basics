# operatore di assegnaione= 
num = 5 # assegno il valore intero 5 alla variabile num

# operatori di confronto (comparison operators) = boolean 
# il risultato di un confronto può essere vero o falso

print ("num == 4  ", num == 4 )  # == |uguaglianza| confronto se sono uguali
# num == 4 in questo caso restituisce False (num vale 5)

print ("num == 5  ", num == 5 )  # == |uguaglianza| confronto se sono uguali
# num == 5 in questo caso restituisce True (num vale 5)

print()

# come si fa il diverso? (l'interrogazione)

print("num è diverso da 4? ", num != 4) # != | Disuguaglianza| confronto se sono diversi 

# è maggiore? 

print ("num è maggiore di 4?", num > 4 ) # > |maggiore| confronto se maggiore

# è minore ? 

print ("num è minore di 4?", num < 4 ) # < |minore| confronto se minore

# è maggiore uguale? 

print ("num è maggiore o uguale di 4?", num >= 4 ) # >= |maggiore uguale| confronto se maggiore uguale

# è minore uguale ? 

print ("num è minore o uguale di 4?", num <= 4 ) # <= |minore uguale| confronto se minore uguale

print()

# si può usare anche sulle stringhe 

print("ciao è uguale a: ", "ciao"=="ciao")


print()

# OPERATORI ARITMETICI

print("num + 4 = ", num + 4) # + |somma|
print("num - 4 = ", num - 4) # - |differenza|
print("num * 4 = ", num * 4) # * |moltiplicazione|
print("num / 4 = ", num / 4) # / |divisione|
print("num // 4 = ", num // 4) # + |divisione senza parte decimale| ci darà solo la parte intera
print("num % 4 = ", num % 4) # % |resto della divisione| ci darà il resto della divisione
print("num ** 4 = ", num ** 4) # ** |elevamento a potenza| ci darà l'elelevamento a potenza

# precedenza operatori
# () parentesi
# ** elevamento a potenza
#  * / // % moltiplicazione, divisione, floor division, modulus
# + - addizione, sottrazione

print (5 + 4 * 3) # prima fa la moltiplicazione
print ((5 + 4 )* 3) # prima addizione nelle parentesi

print ("-" * 50 )

n1 = 3.214
n2 = 3.4455
totale = n1 * n2

print(totale)

# round () 
# con round() posso definire il numero di cifre decimale che voglio vedere
# round (numero, numero di cifre decimali )

print(round(totale, 5))
print(round(totale)) # se non metto il numero di cifre decimali mettera un intero
