# Q1. Write a program to check whether the given input number is divisible by 3 or else
# show a message "Number is not divisible by 3".


numero1 = int(input("Scrivi un numero per scoprire se è divisibile per 3: "))
if numero1 % 3 == 0 :
    numero1 = round(numero1 / 3)
    print (f"E divisibile per 3, fa {numero1}")
else:
    print ("non è divisibile per 3")

print ("." * 50)
# Q2. Write a program that checks whether the given input is an even number or an
# odd number.

numero2 =  int(input("Scrivi un numero per scoprire se è pari o dispari: "))
if numero2 % 2 == 0 : 
    print ("Il numero è pari ")
else:
    print("Il numero è dispari")

print ("." * 50)
# Q3. Write an if/else statement with the following condition:
# If the variable age is greater than 18, output "Old enough", otherwise output "Too young".
age = int(input("Inserisci la tua età: "))

if age > 18 :
    print ("Sei abbastanza vecchio")
else:
    print ("Sei troppo giovane")
print ("." * 50)

# Q4. Write a program that prompts the user for their name, and then displays a special greeting to that person if their name is the same as yours. If the name entered by the user is anything other than your name, your code should not produce any output.

name = input ("Qual è il tuo nome? ")
name = name.casefold()

if name == "jean pierre":
    print ("Abbiamo lo stesso nome, congratualazioni ecco a te un buono amazon")

print ("." * 50)
# Q5. Write a program that takes a calendar year in YYYY format in a variable. Check &
# notify the user whether it is a leap year or not.
# L’utente inserisce un anno ed il calcolatore verifica se l’anno inserito è bisestile.
# Un anno è bisestile se è divisibile per 4 ma non per 100, oppure se è divisibile per 400
# (ad esempio il 1900 non è stato bisestile, mentre il 2000 lo è stato).


anno_bisestile =  int(input ("Scrivi l'anno per scoprire se è bisestile (Nel formato YYYY): "))

if anno_bisestile % 4 == 0 or anno_bisestile % 4 != 0 and anno_bisestile % 400 == 0 : 
    print ("E' un anno bisestile")
else: 
    print ("Non è un anno bisestile")

print ("." * 50)
# Q6. Write a JavaScript program that accept two integers and display the larger. Also
# show if the two integers are equal.




print ("." * 50)
# Q7. Write a program that takes input a number from user & state whether the
# number is positive, negative or zero.

numero_3 = int(input("Inserisci un numero per scoprire se è positivo, negativo o  nullo: "))

if numero_3 > 0: 
    print ("Il numero è positivo")
elif numero_3 == 0:
    print ("Il numero è nullo")
else:
    print ("Il numero è negativo")

print ("." * 50)
# Q8. Write a program that takes a character (i.e. string of length 1) and returns true if
# it is a vowel, false otherwise.

carattere = input ("Digita un carattere: ")

carattere = carattere [0]

if carattere == "a" or carattere =="e" or carattere == "i" or carattere == "o" or carattere == "u" :
    print ("True")
else: 
    print ("False")



#Scrivere un programma che prenda una parola in ingresso dall'utente e la converta
# nel suo equivalente in Pig Latin. Il programma deve seguire le regole del Pig Latin, che variano in base alla prima lettera della parola.
# Regole di converisione:
# Se la parola inizia con una vocale, il programma aggiunge "way" alla fine della parola.
# Esempio: "apple" diventa "appleway".
# Se la parola inizia con una consonante, il programma sposta la prima lettera alla fine della parola e aggiunge "ay".
# Esempio: "python" diventa "ythonpay" 

parola = input ("Inserisci una parola: ")

if parola [0] == "a" or parola [0] =="e" or parola [0] == "i" or parola [0]== "o" or parola [0] == "u" :
    parola = parola + "way"
    print (parola)
else: 
    parola = parola [1:] + parola [0] + "ay"
    print (parola)
