# Classe Dipendente
class Dipendente:
    def __init__(self, id, nominativo, base_salary, department, hours_worked_per_week):
        self.id = id
        self.nominativo = nominativo
        self.base_salary = base_salary
        self.department = department
        self.hours_worked_per_week = hours_worked_per_week

    def calculate_salary(self):
        if self.hours_worked_per_week > 50:
            overtime_hours = self.hours_worked_per_week - 50
            overtime_amount = overtime_hours * (self.base_salary / 50)
            return self.base_salary + overtime_amount
        return self.base_salary
    def __str__(self):
      return f"\nID: {self.id} | Nome: {self.nominativo} | Salario: {self.calculate_salary():.2f} | Dipartimento: {self.department} | Ore settimanali: {self.hours_worked_per_week}\n"
    def __repr__(self):
        return self.__str__()

# Classe Ufficio
class Ufficio:
    def __init__(self, nome, indirizzo):
        self.nome = nome
        self.indirizzo = indirizzo
        self.lista_impiegati = []

    def aggiungi_dipendente(self, dipendente):
        self.lista_impiegati.append(dipendente)

    def elimina_dipendente(self, id_dipendente):
        self.lista_impiegati = [d for d in self.lista_impiegati if d.id != id_dipendente]

# MAIN
    @staticmethod
    def carica_ufficio_da_file(file_path):
        ufficio = Ufficio("DAITA24", "300 E St SW, Suite 5R30, Washington DC 20546 ")
        with open(file_path, "r") as file:
            for line in file:
                id, nominativo, base_salary, department, hours_worked_per_week = line.strip().split(",")
                dipendente = Dipendente(
                    id,
                    nominativo,
                    float(base_salary),
                    department,
                    int(hours_worked_per_week)
                )
                ufficio.aggiungi_dipendente(dipendente)
        return ufficio


    
    @staticmethod
    # 1. Dipendenti con salario definitivo > [valore]
    def dipendenti_con_salario_superiore(ufficio, valore):
        for d in ufficio.lista_impiegati:
            if d.calculate_salary()  > valore:
                print (d)


    @staticmethod
    # 2. Dipendenti di un dipartimento a scelta dell'utente
    def dipendenti_per_dipartimento(ufficio, dipartimento):
        for d in ufficio.lista_impiegati:
            if d.department.lower() == dipartimento.lower():
                print (d)

    @staticmethod
    # 3. Dipendenti il cui cognome inizia con una vocale
    def dipendenti_con_cognome_vocale(ufficio):
        vocali = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for d in ufficio.lista_impiegati:
            if d.nominativo.split()[-1][0] in vocali:
                print (d)

