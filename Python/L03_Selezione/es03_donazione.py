'''
    Scrivi un programma che determina chi è idoneo a donare il sangue. 
    Per poter donare, è necessario soddisfare i seguenti requisiti: 
    essere maggiorenni, non fare uso di sostanze stupefacenti e 
    non aver fatto un tatuaggio nei sei mesi precedenti alla donazione. 
    Alla fine del programma, comunica all'utente se può o non può donare il sangue.
'''
# idoneo
# >18
# no stupefacenti
# no tatuaggio nei sei mesi

anni = int(input("Quanti anni hai? "))
droghe = input("Fai uso di stupefacenti? (Rispondere SI o  NO) ")
droghe = droghe.casefold()
tatuaggi = input("Hai fatto un tatuaggio negli ultimi sei mesi? (Rispondere SI o  NO) ")
tatuaggi = tatuaggi.casefold()
if anni >= 18 and droghe == "no" and tatuaggi == "no":
    print ("Puoi donare il sangue")
else:
    print ("Non puoi donare il sangue")