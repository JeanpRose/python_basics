# Calcolare perimetro e area di un rettangolo
# base e altezza saranno due variabili
# il valore delle variabili potete sceglierlo voi
# Stampare alla fine la dicituara
# Base: [base] cm Altezza: [altezza] cm Area: [area] cm2 Perimetro: [perimetro] cm

# ripetere per quadrato e cerchio

# per pi greco importare math

import math


# rettangolo

base = 3
altezza = 6 
perimetro_r = (base + altezza)*2
area_r =  base * altezza 

# cerchio
#per utilizzare la libreria math 
# scriviamo 

PI= math.pi

raggio = 12 
area_c = (raggio**2) * PI
perimetro_c = 2*PI*raggio



# quadrato
lato = 6
perimetro_q = lato * 4 
area_q = lato**2

print( f"Rettangolo:\n\nBase: {base} cm \nAltezza: {altezza} cm \nArea: {area_r} cm2 \nPerimetro: {perimetro_r}  cm\n")
print( f"Cerchio:\n\nRaggio: {raggio} cm \nArea: {round(area_c,3)} cm2 \nPerimetro: {round(perimetro_c,3)}  cm\n")
print( f"Quadrato:\n\nLato: {lato} cm\nArea: {area_q} cm2 \nPerimetro: {perimetro_q}  cm\n")
