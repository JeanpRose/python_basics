from es_bonus_main import Ufficio


PATH = ("C:/Users/lordj/Desktop/DAITA24/L08_Oggetti/res/impiegati.csv")
ufficio = Ufficio.carica_ufficio_da_file(PATH)
Ufficio.dipendenti_con_salario_superiore(ufficio, 4500)

Ufficio.dipendenti_per_dipartimento(ufficio, "Services")

Ufficio.dipendenti_con_cognome_vocale(ufficio)
