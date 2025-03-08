
# 
# if condizione : 
#    istruzione 
# else: 
#    istruzione

# variabile = valore_se_true if condizione else valore_se falsa
#  il ternario si usa quando si hanno SOLO due opzioni
# verifichiamo se è pari o dispari

numero = 5

if numero % 2 == 0: 
    print ("pari")
else:
    print ("dispari")


# esempio ternario

risultato = "pari" if numero % 2 == 0  else "dispari"

print (risultato)

# altro esempio

studenti = 2
saluto = "Ciao Filippo!" if studenti == 1 else "Ciao ragazzi!"

print (saluto)

# altro esempio

n_cani = int(input("Quanti cani vuoi adottare? "))
print(f"Hai adottato {n_cani} " + ("cane" if n_cani == 1 else "cani"))

# altro esempio  

risultato = "negativo" if numero < 0 else "zero" if numero == 0  else "positivo"
print (risultato)


# è come scrivere

if numero <0 : 
    risultato = "negativo"
else: 
    if numero == 0 :
        risultato = "zero"
    else: 
        risultato = "positivo"

print (risultato)