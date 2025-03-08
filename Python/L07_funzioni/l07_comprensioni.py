# le comprehension ci permettono di definire
# velocemente una collezione

# LIST COMPREHENESION

# SINTASSI

# [espressione for elemento in collezione if condizione]


nums = [1,2,3,4,5,6, 8, 10, 9, 22, 12,11, 13, 15]

# creo una lista che contenrrà i numeri pari

lista = []

for num in nums: 
    if num % 2 == 0:
        lista.append(num)
print (lista) 

# ora con le comprhension

nums_pari = [num for num in nums if num % 2 == 0]
print (nums_pari)


# creo una nuova lista che conterrà i numeri pari
# aumentati di 10

nums_pari_10 = [num +10 for num in nums if num%2 == 0]
print(nums_pari_10)
#creo una lista con i numeri maggiori 4
nums_over_4 = [num for num in nums if num > 4]
print (nums_over_4)


parole = ["cane","gatto", "ghepardo","falco", "radar", "lupo", "coccodrillo", "oca", "anna"]

parole_pali  = [parola for parola in parole if parola == parola [::-1] ]
print (parole_pali)


# creo una lista dove voglio vedere se i numeri maggiori di 4 sono pari o dispari

nums_pari_dispari = [f"Pari: {num}" if num % 2 == 0 else f"Dispari: {num}" for num in nums if num > 4]
print (nums_pari_dispari)

# dict comprehension

# sintassi 
# {espressione_key : espressione_value for elemento in collezione if condizioni}

frutti =["mela","pera","arancia"]

frutti_dic1 = {frutto: len(frutto) for frutto in frutti}

print (frutti_dic1)

# set comprehension
set1 = {s*5 for s  in [1,2,1,0,15] if s <10}
print (set1)


# tuple generator 
# se usiamo la sintasssi delle comprehension 
# per definire una tupla andiamo a ottenere un generatore

tupla1 = (1,2,3,4,5,6,7,8)
generatore = (elemento *2 for elemento in tupla1 if elemento % 2 ==0)

# generatore -> calcola i valori al momento del bisogno
for num in generatore:
    print (num)

# un generatore crea gli elementi solo nel momento in cui sono richiesit

# list e dict comprehension allocano subuto tutti gli elementi in memoria