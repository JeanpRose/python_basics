
# Come si scrivolo le date su python? 
#  importiamo la libreria datetime
import datetime

# oppure ci importiamo solo delle cose o
# cose che ci servono
from datetime import datetime, timedelta 

data_ora_corrente = datetime.now()

print (data_ora_corrente)


data_specifica = datetime(2024, 7,14)

print (data_specifica)



data_ora_specifica = datetime (2003,7,15,7,45,30)

print (data_ora_specifica)

# per prendere solo la data precisa di adesso
data_corrente = datetime.now().date() 

print (data_corrente)

# per prendere l'ora corrente 
# diventa di tipo _TIME e non più DATE
ora_corrente = datetime.now().time()

print(ora_corrente) 

# prendiamo solo le ore
print (ora_corrente.hour)


# con il timedelta facciamo operazioni
# operazioni solo con oggetti datetime


data_futura = data_corrente + timedelta(weeks=14)

print(data_futura)

# darà errore perché non è del tipo datetime o date
# ora_futura= ora_corrente + timedelta(minutes=30)
# print (ora_futura)
ora_futura = datetime.now() + timedelta(minutes=30) 

print (ora_futura.time())


data_inizio_corso = datetime(2024, 11, 5)
fine_corso = data_inizio_corso + timedelta(days= 17, weeks = 14)
print(fine_corso)



# come calcoliamo l'età precisa
# strtime (data, formato_data) mi permette di convertire
# una stringa (con un formato specificato) in un oggetto datetime

# chiediamo la data di nascità all'utente
data_nascita_input = input ("Inserisci la data di nascità (dd-mm-yyyy): ")

data_nascita = datetime.strptime(data_nascita_input, "%d-%m-%Y")
print (data_nascita_input)
print (data_nascita.date())

data_ora_corrente = datetime.now()

eta = data_ora_corrente.year - (data_nascita.year)

eta1 = data_ora_corrente.year - data_nascita.year - ((data_ora_corrente.month, data_ora_corrente.day) < (data_nascita.month, data_nascita.day))

print ((data_ora_corrente.month, data_ora_corrente.day) < (data_nascita.month, data_nascita.day))
# il print sopra mi restituisce True se la data di nascita (mese, giorno)
# è successiva alla data corrente (mese, giorno)

# true se non ha compiuto gli anni | 1
# false se l'ha già compiuti | 0

# true = 1
# false = 0 

# if eta1 == True:
#     eta = eta - 1

# print (eta)
print(eta1)