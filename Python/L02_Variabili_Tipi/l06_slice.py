# Ogni carattere ha un indice a cui appartiene in base alla posizione

titolo = "La ricerca della felicità"
#         0123456789


titolo2 = "Una vera soddisfazione quando funziona tutto"
#          01234567
# Possiamo estrarre un carattere da una stringa 
# Sintassi:
# stringa[indice]

print (titolo[0])
print (titolo [1])
print (titolo[2])
print (titolo[3])
print (titolo[4])
print (titolo [-1]) #possiamo usare il - per prendere l'ultimo carattere

print()
# SLICING stringhe
# inizio incluso | fine escluso

# stringa [inizio:fine]
print (titolo2[4:8])
print (titolo2[2:4])
print (titolo2 [0:3])
print (titolo2 [:10]) # se non specifico indice di partenza allora è l'inizio
print (titolo2 [10:]) # se non specifico indice di fine allora è fino alla fine 
print (titolo2 [-2:]) # dal carattere in posizione -2 (conto dalla fine)fino alla fine

# stringa[inizio:fine:passo]
print (titolo2[0:11:2]) # va da inizio a fine prendendo un carattere ogni tot
# bisogna specificare il passo


# si puo girare la parola al contrario
#
print (titolo [::-1])

print("-"*50)

# len() resitituisce il numero di elementi dell'oggetto
# conta anche gli spazi 

print ("la lunghezza del titolo è: ",len(titolo)) # stampo la lunghezza della stringa titolo


print(titolo[len(titolo):len(titolo)-2:-1])


print("-"*50)

stringa = "ciao"
print(stringa[0]+stringa[-1]) # stampa lettera iniziale e finale
print(stringa[0]+stringa[len(stringa)-1]) # se vogliamo usare len()
# dobbiamo stare attenti che len conta la lunghezza della parola
# l'indice visto che inizia da 0 è 3 per l'ultima lettera
# quindi dobbiamo fare la sottrazione dalla lunghezza totale di 1
# "ciao" avrà lunghezza 4 se contiamo le lettere (usando len())
#  0123 l'indice sarà 3 per l'ultima lettera
# Da questo ne consegue che per indicare l'indice 3 con len()
# dobbiamo sotrarre 1 a len(ciao)=4 

print("-"*50)

parola = "Za"
print (max(parola)) # trova il massimo | segue la tabella ASCII
# nella tabella ASCII "a" è maggiore di "z"
# ASCII ha prima lettere maiuscolo e poi minuscole
print (min(parola)) # trova il minimo | segue la tabella ASCII
# nella tabella ASCII "a" è maggiore di "z"
# ASCII ha prima lettere maiuscolo e poi minuscole






print("-"*50)

saluto = "Buongiorn?"
#         0123456789

#.find() per cercare un carattere (o stringa) all'interno di una stringa 

print(saluto.find("?"))# questo mi restituisce l'indice del carattere cercato

print(saluto.find("ngi")) # mi dice da dove parte (dal terzo indice (=3))

print(saluto.find("ciao")) # se non trova niente restituisce -1

# utilizzo un metodo sul risultato di un altro metodo

print(saluto.find("buon")) # non lo trova perché ha la B minuscola

#utilizzo il.lower() per fare in modo di trovarla
print(saluto.lower().find("buon")) # lo trova e mi dice che sta all'indice 0


print("-"*50)

# Replace

print(saluto.replace("n","$")) # sostituisce la n con $

# funziona anche con parole e non solo un carattere

print(saluto.replace("ngi", "$")) # Buo$orn? restituisce questo

print("-"*50)
# .rstrip() rimuove gli spazi a destra di una parola 
# .lstrip() rimuove spazi a sinistra 
# .strip() rimuove gli spazi a destra e a sinistra


esempio = "         ciao a tutti     "
print (esempio)
print(len(esempio))


print(esempio.rstrip()) 
print(len(esempio.rstrip())) 

print(esempio.lstrip()) 
print(len(esempio.lstrip())) 


print(esempio.strip())  
print(len(esempio.strip())) 

# serve perché bisogna stare attenti agli spazi
citta = " pavia "

print("Abiti a pavia?", citta == "pavia") # ci dirà false perche in partenza la variabile citta ha degli spazi

citta = " pavia "

print("Abiti a pavia?", citta.strip() == "pavia") # dirà true



# .startwith(str) permette di stabilire se la stringa inizia
# con una particolare sequenza di caratteri 
# restituisce un boolean TRUE|FALSE
# è case sensitive cioè tocca stare attenti a maiuscola o minuscola

saluto = "Buongiorno"
print (saluto.startswith("bu")) # False perche inizia per Bu
print (saluto.startswith("Bu")) # True


#cursore multiplo 
# alt + click posiziona un cursore dove ho cliccato
# ctrl + alt + freccia su/giu: aggiunge un cursore sopra/sotto