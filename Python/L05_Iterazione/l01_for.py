
# l'iterazione in python si riferisce alla ripetizione dell'
# esecuzione di un blocco di codice 

# Python supporta diversi forme di iterazione(principalmente cicli for e while):


# Il ciclo for in Pyhton viene utilizzato per iterare su una sequenza
# (una lista, una tupla, un dizionario, un set o una stringa)
# tutto ciò che ha piu di un elemento è un oggetto iterabile
# 

personaggi = ["Satoru", "Yuji", "Megumi", "Nobara", "Kento"]

# SINTASSI

# for elemento in collezione:
#       blocco codice

# 

# a ogni giro del "for" a nome viene assegnato il valore
# di un elemento della lista, finché non finisce tutti gli elemeni di una lista

for nome in personaggi:
    # dentro il blocco di codice posso usare "nome" e a ogni giro avrà un valore diverso
    print (nome)


for nome in personaggi:
    if nome[0] in ["S", "K"]:
        print (nome)


risposta = ""

for elemento in personaggi:
    risposta += elemento + "-"

risposta = risposta[0:-1]


risposta = ""
for elemento1 in personaggi:
    if elemento1 != personaggi[-1]:
        risposta += elemento1 + "-"
    else: 
        risposta += elemento1

print (risposta)


counter = 0 
risposta = ""

for el in personaggi:
    if counter == 0:
        risposta += el
    else:
        risposta += "-"+ el
    counter += 1

print (risposta)

print("."*50)

personaggi_6_lettere = []

for el in personaggi:
    if len(el) == 6:
        personaggi_6_lettere += [el] 
        # personaggi_6_lettere.append(el)

print (personaggi)
print (personaggi_6_lettere)

# usando pop 
# dobbiamo avere la lista di 6 personaggi
# problema che ci serve l'indice e non la lunghezza

personaggi_6_lettere =[]

for elemento in personaggi.copy():
    if len(elemento) == 6: 
        indice = personaggi.index(elemento)
        personaggi_6_lettere.append(personaggi.pop(indice))

print (personaggi_6_lettere)
print (personaggi)


print ("-" * 50)

# vogliamo stampare delle parole con 6 lettere tutte le lettere tranne la i
personaggi = ["Satoru", "Yuji", "Megumi", "Nobara", "Kento"]

for nome1 in personaggi: 
    if len(nome1) == 6:
        for lettera in nome1:
            if lettera != "i":
                print (lettera)
        print (f"Fine per {nome1}")


print ("-" * 50)

# di ogni personaggi stampo prima il nome e poi solamente 
# le vocali che lo pongono 
vocali = "aeiou"

for nome in personaggi:
    print (nome)
    for lettera in nome:
        if lettera in vocali:
            print (lettera)



print ("-" * 50)





