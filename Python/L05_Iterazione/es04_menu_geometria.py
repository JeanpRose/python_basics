# Calcolare perimetro e area di un rettangolo
# base e altezza saranno due variabili
# il valore delle variabili potete sceglierlo voi
# Stampare alla fine la dicituara
# Base: [base] cm Altezza: [altezza] cm Area: [area] cm2 Perimetro: [perimetro] cm

# ripetere per quadrato e cerchio

# per pi greco importare math
import math
menu = """
Scegli la figura: 
1. Quadrato
2. Rettangolo
3. Cerchio
0. Esci
"""
cmd = " "

while cmd != "0": 
    print (menu)
    cmd = input ("Inserisci quale figura vuoi: (numero) ")

    if cmd == "1": 
        print("Inserisci le misure del quadrato")
        lato = int (input("Inserisci lato: "))
        area = lato * lato
        perimetro = lato * 4
        output= f"Quadrato:\nLato: {lato}\nArea: {area}\nPerimetro: {perimetro}"
        break
    elif cmd == "2":
        print("Inserisci le misure del rettangolo")
        base = int (input("Inserisci base: "))
        altezza = int (input("Inserisci altezza: ")) 
        perimetro_r = (base + altezza)*2
        area_r =  base * altezza
        output= f"Rettangolo:\nBase: {base}\nAltezza: {altezza}\nArea: {area_r}\nPerimetro: {perimetro_r}"
        break
    elif cmd == "3":
        PI= math.pi
        raggio = int (input("Inserisci raggio: "))
        area_c = (raggio**2) * PI
        perimetro_c = 2*PI*raggio
        output= f"Cerchio:\nRaggio: {raggio}\nArea: {round(area_c,2)}\nPerimetro: {round(perimetro_c,2)}"
    elif cmd == "0":
        output = "Arrivederci"
        break
    else:
        print("Comando errato: inserisci un valore tra questi: 1 - 2 - 3 - 0")
 

   
print ("."*50)
print(output)