'''
creare un file e inserire 15 animali
animale1
animale2
.
.
.
stampare gli animali incolonnati nell'ordine in cui sono scritti
output:
    animale1
    animale2
stampare gli animali incolonnati nell'ordine dall'ultimo al primo
output: 
    animale2
    animale1
stampare gli animali sulla stessa riga separati da virgole
output:
    animale1, animale2, ecc
'''

lista_animali = ["Leone", "Elefante","Giraffa", "Tigre", "Orso polare","Delfino","Aquila","Canguro","Pinguino","Cavallo","Tartaruga","Panda","Rinoceronte","Scimmia","Lupo"]
lista_animali_invertita =[]
for n in lista_animali:
    lista_animali_invertita.insert(0,n)

lista = []
with open ("res/animali.txt", "w+") as file:
    print ("."*40)
    for i in range (len(lista_animali)):
        if  i < range(len(lista_animali))[-1]:
            lista.append(lista_animali [i] +"\n")
        else:
            lista.append(lista_animali [i])
    
    file.writelines(lista)
    file.seek(0)
    print (file.read())
    print ("."*40)

lista2 = []
with open ("res/animali.txt", "w+") as file:
    print ("."*40)
    for i in range (len(lista_animali_invertita)):
        if  i < range(len(lista_animali_invertita))[-1]:
            lista2.append(lista_animali_invertita[i] +"\n")
        else:
            lista2.append(lista_animali_invertita[i])
    file.writelines(lista2)
    file.seek(0)
    print (file.read())
    print ("."*40)


with open ("res/animali.txt", "w+") as file:
    print ("."*40)
    lista3 = []
    for i in range (len(lista_animali)):
        if  i < range(len(lista_animali))[-1]:
            lista3.append(lista_animali [i] +", ")
        else:
            lista3.append(lista_animali [i])
    file.writelines(lista3)
    file.seek(0)
    print (file.read())
    print ("."*40)



