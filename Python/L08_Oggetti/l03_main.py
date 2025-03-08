from l03_classi import Persona, Automobile

p1 = Persona("Asuna",17)
p2 = Persona("Kirito",16)
p3 = Persona("Yu",12)
p4 = Persona("Mika",18)
p5 = Persona("Geto",32)


persone = []
persone.append(p1)
persone.append(p2)
persone.append(p3)
persone.append(p4)
persone.append(p5)

nom_input = input ("Inserisci un nominativo: ")
eta_input = int(input ("Inserisci l'età: "))
p6 = Persona (nom_input, eta_input)

persone.append (p6)

for persona in persone:
    if isinstance(persona, Persona):
        print (persona)


print("."*50)

a1 = Automobile("Fiat", "500", 7500, 2015)

print (a1)

a2 = Automobile ("Ferrari", "Enzo", 80000, 2018)
persone.append (a1)
persone.append (a2)

for x in persone:
    if isinstance(x, Automobile):
        print(x)
        print()
