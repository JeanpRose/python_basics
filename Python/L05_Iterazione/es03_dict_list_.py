'''
Partendo da una lista di nuovi assunti, dove ogni elemento è una tupla 
contenente il nome di una persona, il suo ruolo lavorativo e il salario, 
l'obiettivo è rimuovere dalla lista tutte le persone che ricoprono ruoli 
legati al database (ad esempio, quelli che hanno "SQL" nel loro ruolo).

'''          #  0                  1              2     
new_hires = [('Leslie Burton', 'HR Specialist', 2300),
             ('Mark Adams', 'SQL Analyst', 4000),
             ('Dorothy Castillo', 'SQL Designer', 3100)]


for persona in new_hires.copy(): 
    if 'SQL' in persona[1]:
        new_hires.remove(persona)

print (new_hires)


'''
Partendo da un dizionario che contiene i risultati di un esame, 
dove le chiavi sono i nomi degli studenti e i valori sono i punteggi ottenuti, 
l'obiettivo è calcolare la differenza tra il punteggio più alto e il punteggio più basso.
'''

exam_results = {
    'Dominic Vargas': 67,
    'Marion Riley': 89,
    'Candice White': 45,
    'Doreen Goodwin': 82,
    'Janet Hunter': 98,
    'Jaime Page': 32,
    'Neil Fernandez': 76,
    'Jana Frank': 28,
    'Adrienne Perkins': 98,
    'Rosa Mccarthy': 34
    }

risultati = list (exam_results.values())
massimo = risultati[0]
minimo = risultati [0]

for i in risultati:
    if i > massimo:
        massimo = i
    if i < minimo:
        minimo = i

print ("Il massimo è: ", massimo)
print ("Il minimo è: ", minimo)
print ("La differenza tra massimo e minimo fa: ", (massimo-minimo))


