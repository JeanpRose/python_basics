

def somma(num1: int, num2: int) -> int:
    risultato = num1 + num2
    return risultato

print (somma(2 , 4))



print ("."*30)

def calcolo_prezzo(prezzo, sconto = 0,  unita = 1):
    if sconto > 100 :
        sconto = 0
    prezzo_totale = prezzo * unita *(1-sconto /100)
    return prezzo_totale

print (calcolo_prezzo(14, 2))


# creare una funzione indefinita, cioè che accetta
# valori indefiniti (come print()) 

def somma_numeri (*nums):
    somma = 0
    for num in nums:
        somma += num
    return somma

print (somma_numeri(3,5,4 ,2,1,5))

lista =[2, 4, 5, 7, 9, 12]
print(somma_numeri(*lista))




def somma_differenza (scelta, n, *numeri):
    if scelta == "somma":
        for numero in numeri: 
         n += numero
    elif scelta == "differenza" :
        for numero in numeri:
            n -= numero
    return n 

print (somma_differenza("differenza", 100,2,4,5,6,4))



# Argomenti arbitrari con chiave (**kwargs): 
# permette di passare argomenti nominati variabili.

def dettagli(**info):
    for chiave, valore in info.items():
        print(f"{chiave}: {valore}")

dettagli(nome = input("inserisci nome: "), età = int(input("Inserisci età: ")), città = input ("Inserisci città: "))


