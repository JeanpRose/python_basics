# Le eccezioni sono degli errori che si verificano a runtime
# e bloccano l'esecuzione del programma 


# esempio
# num = input("Inserisci un numero: ")

# print (num/2)

# TypeError : si verifica quando un operazione viene eseguita su un tipo di 
# dato non supportato


## try - except

"""
    try: 
        blocco di codice
    except ClasseEccezione as error:
        print (error)
        print ("Sei nel except")
"""




# esempio
num1 = 5
num2 = 1 #0

try: 
    d = num1/num2
except ZeroDivisionError as error:
    print ("Non puoi dividere per zero")
    print (f"ERROR:  {error}")
except TypeError as e : 
    print ("Non puoi dividere TIPI diversi")
    print (f"Errore: {e}")
else:
    print (f"Bravo la div da come risultato {d}")

# il finally viene sempre eseguito, sia se si solleva un 
# eccezzione sia se funziona tutto correttamente
finally:
    print ("STAMPO SEMPRE")


# TypeError 
# ZeroDivisionError
# SyntaxError

# ImportError: Questa eccezione viene sollevata quando un'istruzione 
# di importazione fallisce 

# ModuleNotFoundError: questa eccezzione viene sollevata quando non viene
# trovato il modulo es: from es03_vlass import qualcosa. Il problema sta nell'
# aver chiamato in modo errato es03_class


