# 1- Scrivere un programma che, richiesti in ingresso due valori interi distinti, ne
# determini il maggiore.

num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un numero: "))

if num1 > num2:
    print (f"Il numero maggiore è: {num1}")
else: 
    print (f"Il numero maggiore è: {num2} ")

# 2-  Scrivere un programma che, richiesti due numeri interi qualsiasi, segnali se i due
# numeri sono uguali; in caso contrario indichi il minore e il maggiore.



num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un numero: "))

if num1 == num2:
    print (f"I numeri sono uguali")
else: 
    if num1 > num2:
        print (f"Il numero maggiore è: {num1} mentre il minore è {num2}")
    else: 
        print (f"Il numero maggiore è: {num2} mentre il minore è {num1} ")




# 3- Un negoziante per ogni spesa di importo superiore a 100 € effettua uno sconto del 5%, del
# 10% per ogni spesa superiore a 300 €. Scrivere un programma che richieda all'utente l'ammontare
# della spesa e visualizzi quindi l'importo effettivo da pagare


importo = int(input("Inserisci l'importo da pagare: "))

if importo >= 100 and importo< 300:
    importo -= (importo*5/100)
elif importo >= 300:
    importo -= (importo*10/100)


print (f"l'importo effettivo da pagare è: {importo} ")






# 4- - Scrivere un programma che, richiesti in input tre numeri interi, visualizzi a seconda dei
# casi una delle seguenti risposte:
#         Tutti uguali
#         Due uguali e uno diverso
#         Tutti diversi


num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un numero: "))
num3 = int(input("Inserisci un numero: "))


if num1 == num2 == num3:
    print ("I numeri sono uguali")
else: 
    if num1==num2 and num1 != num3 :
        print (f"Due numeri sono uguali ({num1}) mentre ({num3}) è diverso")
    else: 
        if num1==num3 and num1 != num2 :
            print (f"Due numeri sono uguali ({num1}) mentre ({num2}) è diverso")
        else: 
            if num3==num2 and num1 != num2:
                print  (f"Due numeri sono uguali e sono ({num3}) mentre ({num1}) è diverso")
if num1!=num2 and num1!=num3 and num2!=num3: 
    print ("Sono tutti diversi")

# 5- In una certa scuola le visite d’istruzione sono organizzate secondo il seguente schema:

# - Classi prime: tutte le prime visiteranno Il museo egizio di Torino
# - Classi seconde: la 2^A visiterà il Duomo di Milano, tutte le altre seconde visiteranno il
#   Castello Sforzesco di Milano
# - Classi terze: tutte le terze visiteranno le Gallerie degli Uffizi di Firenze
# - Classi quarte: la 4^B visiterà il Colosseo a Roma, la 4^C il Pantheon a Roma, tutte le altre
#   quarte i Musei Vaticani.
# - Classi quinte: tutte le quinte visiteranno il Cern di Ginevra.

# Scrivere un programma che richieda la classe (un numero intero tra 1 e 5), la sezione (una lettera
# maiuscola) e indichi la meta prevista sulla base dello schema precedente. 

classi = int(input("In che classe va l'alunno? (da 1 a 5) "))
sezione = input ("In che sezione va l'alunno? ").casefold()

alfabeto = "abcdefghilmnopqrstuvwz"


if classi == 1 and sezione in alfabeto: 
    print ("L'alunno visiterà Il museo egizio di Torino")
elif classi == 2 and sezione in (alfabeto[1:]): 
    print ("La classe visiterà il Castello Sforzesco di Milano")
elif classi == 2 and sezione in (alfabeto[0:1]): 
    print ("La 2^A visiterà il Duomo di Milano")
elif classi ==3 and sezione in alfabeto: 
    print ("La classe visiterà la Gallerie degli Uffizi di Firenze")
elif classi == 4 and sezione in (alfabeto[0:1]) and sezione in (alfabeto[3:]): 
    print ("La classe visiterà i Musei Vaticani")
elif classi == 4 and sezione in (alfabeto[1:2]) : 
    print ("La 4^B visiterà il Colosseo a Roma")
elif classi == 4 and sezione in (alfabeto[2:3]):
        print ("La 4^C il Pantheon a Roma")
elif classi == 5 and sezione in alfabeto: 
    print ("L'alunno visiterà il Cern di Ginevra")




