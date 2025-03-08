 # Argomenti della funzione print 

# nome_funzione (argomenti)

print("ciao")

# possiamo manipolare le funzione dentro print 
# come "sep" o "end"
# con la modifica a "end" si modifica quello che 
# viene aggiunto alla fine 
# di default c'è NEWLINE "\n"

print ("ciao", end= "") # tolgo qualsiasi spazio
print ("come") # stampera "ciaocome"


print (" buona serata ", end = "-- VALORE CHE VIENE AGGIUNTA ALLA FINE--")
print ("a tutti")

# sep 
# cambiamo il separatore tra i valori del print
print("ciao","ciao", "ciao", sep=",")