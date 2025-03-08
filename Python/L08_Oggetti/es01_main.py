'''
Crea delle istanze della classe Studente con dati diversi.
- Inserisci gli oggetti Studente in una lista
- Stampare la scheda di ciascun studente, 
           l'etÃ di ogni studente,
           la media dei voti di ogni studente,
           la media di italiano della classe prima
           l'elenco degli studenti di una specifica classe fornita dall'utente
'''
from es01_classi import Studente

with open ("./res/studenti.csv") as file:
    lista = file.readlines()

lista_liste = []
for elemento in lista:
    j= elemento.split(",")
    lista_liste.append(j)


for x in lista_liste:
    print (Studente(*x))

    
classi_var = ["1A","1B","1C","1D","1F","1G"]
count = 0 
somma = 0 
for studenti in lista_liste:
    if studenti[3] in classi_var:
        count +=1
        somma  += (int (studenti[4]))

print (f"La media delle classe prime è: {somma/count}, ci sono {count} alunni")

scelta_classe = input ("Scegli una classe per sapere l'elenco degli studenti: ").casefold()
for studenti in lista_liste:
    if studenti[3].casefold() == scelta_classe:
        print (Studente(*studenti))