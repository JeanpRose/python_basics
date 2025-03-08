nintendo  = ["Mario",2, "Luigi",3, "Peach", 4, "Zelda", 5, "Yoshi"]

# itero tramite una sequenza di numeri interi
# generata dalla funzione range ()

# range (vlore_finale) parte da 0 e arriva fino al valore indicato (ESCLUSO)

# range (valore_iniziale, valore_finale) genera una sequenza di numeri
# dal valore iniziale al valore finale (ESCLUSO)

for i in range (5):
    print (i)

print ()

for i in range (2,9):
    print (i)

print ()

# range (start, stop, passo)

for i in range (10, 101,10):
    print (i)

for i in range (0,len(nintendo)+1, 2):
    print(nintendo[i])

for i in range (10,0,-1):
    print (i)

print ()

lista_num = list (range(20))

print (lista_num)

