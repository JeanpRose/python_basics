
def gestisci_task():
    elenco_task = []
    elenco_task : list [dict]
    
    def crea_task ( descrizione: str, scadenza: str ): 
        task = {"Descrizione" : descrizione,
            "Scadenza" : scadenza,
            "Completato" : False}
        elenco_task.append(task)
    
    def completa_task (descrizione: str):
        for task in elenco_task: 
            if task["Descrizione"] == descrizione:
                task["Completato"] = True
    
    def visualizza_task():
        for task in elenco_task:
            print (f"{task["Descrizione"]} - {task["Scadenza"]} - {"Completata" if task["Completato"]==True else "In corso"}")
    
    return crea_task, completa_task, visualizza_task 

aggiungi_t, completa_t, visualizza_t = gestisci_task()

aggiungi_t("Fare spesa", "27/11/2024")
visualizza_t()

completa_t("Fare spesa")
visualizza_t()




