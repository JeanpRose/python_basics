# possiamo avere funzioni all'interno di altre funzioni

contatti = []
def gestore_contatti (nome = None, numero = None, lista_contatti = contatti):

    def aggiungi_contatto (nome_agg, numero_agg):

        contatto = {
            "nome" : nome_agg,
            "numero" : numero_agg
        }
        lista_contatti.append(contatto)
    def mostra_contatti():
        for contatto in lista_contatti:
            print (f"Nome: {contatto["nome"] } - Numero: {contatto["numero"]} ")
    
    if nome != None and numero != None:
        aggiungi_contatto(nome, numero)

    print (f"Elenco dei contatti in lista: ")
    mostra_contatti()


gestore_contatti ("Carlo", "3332342283")