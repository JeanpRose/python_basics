
# Programmazione orientata agli oggetti (OOP)(Object oriented Programming)


# classe è il modello

# SINTASSI
# class NomeClasse:
#   attributi -> indicano le caratteristiche comuni a tutti gli oggetti di questo tipo
#
# metodi ->  funzioni specifiche dell'oggetto

# modello è tutto quello che c'è scritto dentro "class"
class Persona:
    # attributi
    nome = "non definito"
    cognome = "non definito"
    eta = 0 


# creo una persona specifica (istanza)
p1 = Persona()
p2 = Persona()

print (type(p1))
print ("1--")
print (p1.nome, p1.cognome, p1.eta)

p1.nome = " Filippo"
print (p1.nome)
print ()
print (Persona.nome)

Persona.nome = "Marco"

p3 = Persona ()

print (p3.nome)