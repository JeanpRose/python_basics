# SINTASSI

# while condizione:
#       blocco codice

# finché la condizione è vera entrerà nel while

# esempio
n = 0 

# si crea un loop infinito finché la condizione è vera

while n <= 100:
    print(n)
    n += 1

# altro esempio 
n1 = 99

while n1 > 0 :
    print(n1)
    n1 -=1

# altro esempio
print ("."*50)
lista = [1,2,4,6,9]

for n in lista:
    print (n)

n = 0
print ("."*50)
while n < (len(lista)):
    print (lista[n])
    n += 1

voto = -1

while voto < 0 or voto > 10:
    voto = int (input("Inserisci un voto da 0 a 10: "))
    if 6 < voto >= 10:
        print (f"Bravo/a hai preso {voto}")
    else: 
        print (f"Sei un coglione hai preso {voto}")




# print (f"Bravo/a hai preso {voto}")

print ("."*50)

# se uso while True l'unico modo per interrompere il ciclo è usare break

n = 0
while True :
    print (n)
    n += 1 
    if n == 100:
        break # interrompe il ciclo while

print ("."*50)

n = 20

b = True 

while b:
    print (n)
    n  -= 1
    if n == 0: 
        b = False

print ("."*50)
n = 0
while True: 
   
    if n == 5:
        n +=1
        continue # passa al prossimo giro del ciclo saltando tutte le istruzioni scritte sotto

    if n == 10: 
        break
    print (n)
    
    n += 1


