# Type Casting 

# se ho un numero scritto con stringa posso trasformarlo
# con un numero grazie a int()

stringa = "12"

print (type(stringa)) # stampera la classe str

print (type(int(stringa))) # usando int() ci dara classe int

numero_decimale = 10.526
print (int(numero_decimale)) # scriverà 10

print ("True in int", int(True)) # stampa 1
print ("True in int", int(False)) # stampa 0


print ("."*50)
# qualsiasi numero dicerso da 0 è Vero|True
# solo 0 ci darà false

print(bool(15.23)) # True
print(bool(63)) # True
print(bool(0)) # False

# anche con le stringhe funziona allo stesso modo
# è False se non c'è niente

print (bool("")) # FALSE

# anche lo spazio vale come True
print (bool(" ")) # TRUE


# str()
# str() serve per trasformare le cose dentro la parentesi 
# in stringa
# possiamo trasformare un booleano in stringa


print (str(True))
print (str(False))

# float () trasforma in un numero anche decimale 
# una stringa 

num = "115"
print (float(num))