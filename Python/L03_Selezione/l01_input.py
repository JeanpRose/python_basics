
# Possiamo chiedere un input all'utente 
# fare attenzione che la variabile sarà 
# una stringa, quindi se voglia un numero usare 
# una conversione (v. l07_conversione_tipo) 
# input()

# Da input() ottengo sempre una stringa

# esempio

nome = input("Inserisce il tuo nome: ") #\n se vogliamo l'input sotto

# print (f"ciao {nome}")

# print (f"Tipo variabile nome: {type(nome)}") # str

anno_nascita = input("Inserisci il tuo anno di nascità: ")

eta =  2024-int(anno_nascita)
# print (anno_nascita)
#print (eta)

citta = input ("Inserisci la tua città : ")

print (f"Ciao {nome}, hai {eta} anni e vivi a {citta}")