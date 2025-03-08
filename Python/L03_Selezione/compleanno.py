
from datetime import datetime, timedelta

data_nascita_input = input ("Inserisci la data di nascità (dd-mm-yyyy): ")

data_nascita = datetime.strptime(data_nascita_input, "%d-%m-%Y")

data_ora_corrente = datetime.now()

eta1 = data_ora_corrente.year - (data_nascita.year)

eta = eta1 - ((data_ora_corrente.month, data_ora_corrente.day) < (data_nascita.month, data_nascita.day))
