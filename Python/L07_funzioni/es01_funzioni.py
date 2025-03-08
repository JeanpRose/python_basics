
# Funzione per convertire la temperatura da celsius a fahrenheit e viceversa

def convertitore_f (temperatura_C: int):
    t_f = (temperatura_C * 9/5) + 32 
    return t_f

print ("Inserisci il valore da convertire in Celsius da Fahrenheit: ")

valore = int(input())

print(convertitore_f(valore))

def convertitore_c (temperatura_F: int):
    t_c = (temperatura_F -32) * 5/9 
    return t_c

print ("Inserisci il valore da convertire in Fahrenheit da Celsius: ")
valore = int(input())
print (round(convertitore_c(valore)))

# altro modo più compatto

def celsius_fahrenheit(grado, tipo : "f" "c"):
    if tipo == "f":
        return (grado-32) *5/9
    if tipo == "c":
        return (grado*9/5) + 32
    else: 
        return f"{tipo} non valido"

print (celsius_fahrenheit(tipo ="c",grado= 23))
print (celsius_fahrenheit(tipo = "f", grado = 32))



# Funzione per analizzare un testo - numero di parole, numero di caratteri e numero frasi
 
def analisi (testo):
    parole = len(testo.split())
    caratteri = len(testo.replace(" ",""))
    separatori = [ ".", "!", "?"]
    frasi = 0
    for carattere in testo:
        if carattere in separatori:
            frasi += 1
    
    

    return f"""
Numero di parole: {parole}
Numero di caratteri (senza spazi):{caratteri}
Numero di frasi: {frasi}
    """
testo_prova = input ("Inserisci un testo: ")

print(analisi(testo_prova))


#  funzione per calcolare somma e differenza
def somma (num1 : int, num2 : int) -> int:
    return num1 + num2
print (somma(2,3))

def differenza (num1 : int, num2 : int) -> int:
    return num1 - num2
print (differenza(23,2))




# funzione per validare l'età, dire se maggiorenne o minorenne

def eta (eta1 = "Sei Maggiorenne", eta2 = "Sei Minorenne") :
    inserisci = int(input("Inserisci la tua età: "))
    return eta1 if inserisci >= 18 else eta2

print (eta())

# funzione per convertire una valuta - importo * tasso cambio

def cambio (importo, tasso_cambio):
    ris = importo * tasso_cambio
    return ris

print (cambio(200, 0.95))


