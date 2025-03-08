
# Dottore,nominativo,anno_nascita,residenza,reparto,anni_lavoro,tirocinante,numero_interventi,interventi_riusciti
# Paziente,nominativo,anno_nascita,residenza,Patologia,ricovero,giorni_ricovero,ticket

from es04_classi import Ospedale

PATH = "./res/persone.txt"

ospedale = Ospedale("Gemelli", [])


ospedale.lettura_file(PATH)

while True:
    stampa_menu = input("Vuoi stampare il menù: [y | n] ")
    if stampa_menu.casefold() not in ["n","no"]:
        with open ("./res/menu_ospedale.txt", "r", encoding= "utf-8" ) as file:
            print (file.read())

    cmd = input("Inserisci funzione richiesta: ")

    match cmd:
        case "0":
            print("Termino programma")
            break
        case "1":
            ospedale.mostra_persone("Persona")
        case "2":
            ospedale.mostra_persone("Dottore")
        case "3":
            ospedale.mostra_persone("Paziente")
        case "4":
            ospedale.dottori_varie(1)
        case "5":
            ospedale.dottori_varie(2)
        case "6":
            ospedale.dottori_varie(3)
        case "7":
            ospedale.dottori_varie(4)
        case "8":
            ospedale.dottori_varie(5)
        case "9":
            ospedale.pazienti_vari(1)
        case "10":
            ospedale.dottori_varie(7)
        case "11":
            ospedale.dottori_varie(8)
        case "12":
            ospedale.dottori_varie(9)
        case "13":
            ospedale.dottori_varie(10)
        case "14":
            ospedale.dottori_varie(11)
        case "15":
            ospedale.pazienti_vari(2)
        case _:
            print ("Inserisci un numero valido")