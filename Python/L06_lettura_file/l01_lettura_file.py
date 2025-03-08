# C:\Users\lordj\Desktop\DAITA24\L06_lettura_file\res\nintendo.txt
# L06_lettura_file\res\nintendo.txt

# nome_file = 'C:/Users/lordj/Desktop/DAITA24/L06_lettura_file/res/nintendo.txt'
# file_nintendo = open (nome_file)

# altra opzione 
nome_file = './res/nintendo.txt'
file_nintendo = open(nome_file)

# print (type (file_nintendo))

print (file_nintendo.read())


# per chiudere un file
# file_nintendo.close()

# .closed stiamo chiedendo se il file è ancora chiusa
# risponderà con True|False 
print ("La lettura da file è chiusa? ",file_nintendo.closed)
print ("."*50)
# seek
file_nintendo.seek(11)

print(file_nintendo.read())

file_nintendo.close()

print ()

with open ('./res/nintendo.txt') as file:
    # print (file.read()) # legge tutto il file
    # readline legge la prima riga
    print ("readline: ", file.readline())
    print (file.readline())
    # .seek(n) posiziono il puntatore in una posizione specifica
    #file.seek(0)
    # .readlines() ci restituisce gli elementi di un file in una lista
    # leggerà tutte le righe
    print (file.readlines())

# fuori dal with il file sarà sempre chiuso
# print (file.closed)

with open ('./res/nintendo.txt') as file:
    print (file.readlines())

with open ('./res/nintendo.txt') as file:
    testo = file.read()
    print(testo)

print (type(testo))

# splitlines() divido la stringa in
lista = testo.splitlines()

print(lista)

# .split(n) crea una lista e divide/ separa la lista in base alla n 

lista2 = testo.split ("i")
print(lista2)