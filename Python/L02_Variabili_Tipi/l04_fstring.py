
titolo = "Dune"
autore = "Frank Herbert"
anno = 1965

print ()

# modo 1 
# concateno le stringhe prima di stamparle usando (+)
print("1- Titolo: " + titolo + "\nAutore: "+ autore + "\nAnno: "+ str(anno))
# notare che va lasciato lo spazio dopo i due punti 
# "1- Titolo: "


# modo 2 
# passo alla funzione print tutte le stringhe che 
print ("2- Titolo:" , titolo, "\nAutore:", autore, "\nAnno:", str(anno))
#non ha bisogno di spazi come in precedenza

# modo 3
# creo una stringa con i segnaposti (placeholder) per le variabili
# con .format (var1, var2, ecc) specifico l'ordine di inserimento delle variabili
# le variabili verrano quindi inserite al posto dei placeholder

print("3-Titolo: {0}\nAutore: {1} \nAnno: {2}".format(titolo, autore, anno))
#                                                       0        1      2   
# se voglio inserire le variabili secondo un ordine definito manualmente
# posso inserire gli indici dentro i placeholder per specificare quale
# variabile verrà inserita in quel placeholder

print ()

# modo 4 
# usando f"" definisco una stringa che può contenere direttamente le variabili
# F-String
print(f"4-Titolo: {titolo}\nAutore: {autore} \nAnno: {anno}")

# f-string si può usare anche con stringhe multiriga
print (f""" 4b-Titolo: {titolo}
Autore: {autore}
Anno: {anno}""")    

print()

# METODI STRINGHE 
# con .upper() applicato ad una stringa transformo il contenuto in lettere maiuscole
# con .lower() applicato ad una stringa transformo il contenuto in lettere minuscole
# con .title() applicato ad una stringa transformo la prima lettera di ogni parola in maiuscolo
# con . capitalize() applicato ad una stringa transformo la prima lettera in maiuscolo e tutto il resto in minuscolo
# con .casefold () applicato ad una stringa transformo il contenuto in lettere minuscolo però piu aggressivo rispetto a .lower


stringa_esempio1 = "filippo"

print (stringa_esempio1.upper())

print()

stringa_esempio2 = "CIAOOOO"
print (stringa_esempio2.lower())

print()

stringa_esempio3 = "vi sTO spIEganDo i MEtodI"
print(stringa_esempio3.title()) # output : Vi Sto Spiegando I Metodi
print(stringa_esempio3.capitalize()) # output: Vi sto spiegando i metodi
print(stringa_esempio3.casefold()) # output: vi sto spiegando i metodi

# il metodo .lower() non riesce a convertire alcuni caratteri
# alcuni caratteri speciali che non sono specificati nella tabella ASCII 
# es: ß

print("ß".lower())
print("ß".casefold())
