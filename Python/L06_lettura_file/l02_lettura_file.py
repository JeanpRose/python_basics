with open ('C://Users//lordj//Desktop//DAITA24//L06_lettura_file//res//nintendo.csv') as file: 
    # cosi facendo prendiamo ogni riga di nintendo.csv
    elementi_file = file.read().splitlines()

print (elementi_file)
# andiamo a prendere ogni elemento 
for elemento in elementi_file:
    # elemento = "Mario, 12"
    dettagli = elemento.split(",")
    nome = dettagli [0]
    num_giochi = int(dettagli[1])

    print (f"Nome del personaggio Nintendo: {nome}\nNumero di giochi in cui è apparso: {num_giochi}")

# se vogliamo usare il dizionario

diz = {}
lista = []
for elemento in elementi_file:
    dettagli = elemento.split(",")
    diz = {dettagli[0]:int(dettagli[1])}
    lista.append(diz)
    diz = lista

print (diz)