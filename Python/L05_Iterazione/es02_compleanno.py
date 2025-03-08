'''
Scrivi un programma per organizzare una festa di compleanno che permetta di gestire 
la raccolta fondi per un regalo. Il programma deve:

Chiedere all'utente quanti saranno gli invitati alla festa.
Per ogni invitato:
 
Chiedere il nome.
Chiedere quanto vuole contribuire al regalo.
Calcolare il totale del budget raccolto.
Mostrare un riepilogo con:
 
La lista degli invitati.
I contributi individuali.
Il budget totale disponibile per il regalo.
'''
invitati = int(input("Quanti invitati ci saranno alla festa?: " ))
nome= []
contributo = []
totale_budget = 0
num = 0 

for invitato in range (invitati):
    nome.append(input (f"Inserisci il nome dell'invitato n° {(invitato+1)}: ").capitalize())

for nome_invitato in nome: 
    contributo.append(int (input (f"Quanto vuole contribuire {nome_invitato}: ")))

for numero in contributo:
    totale_budget += numero

print ("-" * 50)

print (f"La lista degli invitati è: ")


for lista in nome:
        print( f" {num+1}) {lista}")
        num +=1


print ("Ogni invitato ha contribuito così: ")

for num in range (len(nome)):
    print (f"{nome[num]} ha contribuito con {contributo[num]}€" )

print (f"Il totale dei soldi raccolti è: {totale_budget}€")