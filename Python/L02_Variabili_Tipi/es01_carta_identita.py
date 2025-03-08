nome = 'Jean Pierre'
cognome = 'Rosero'
anno_di_nascita = 1999
citta = 'Roma (RM)'
eta = 2024 - anno_di_nascita
print ('Nominativo: ', nome, cognome)
print ('Età: ', eta)
print ('Città: ', citta)

#possiamo trasformare un numero in stringa:
eta = str(eta)
print (eta)

print(f"Nominativo: {nome+" "+ cognome}\nEtà: {eta} \nCittà: {citta}")