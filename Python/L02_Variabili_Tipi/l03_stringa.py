nome = 'Jean Pierre'
cognome= 'Rosero'

print(nome, cognome) # stampo piu cose (le separo con la ','  viene inresito da solo lo spazio)

print(nome + cognome) # concatenazione tra stringhe (stringhe vengono unite, non ci saranno spazi)

stringa_monoriga = 'Ciao a tutti! Come va?'# stringa in unica riga
print(stringa_monoriga)
stringa_multiriga = """Ciao
come va?
tutto bene
"""
print (stringa_multiriga)

# posso andare a capo anche nelle stringhe monoriga
# si usa un carattere speciale
# \n (newline) indica di andare a capo
print()
print ('Filippo \nPvanello')

#posso unire le due variabili 
nominativo= nome + '\n' + cognome

print(nominativo)