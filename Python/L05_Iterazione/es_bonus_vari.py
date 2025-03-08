# 1 - Write a Python script to concatenate the following list of dictionaries 
# to create a new dictionary.


lista_diz = [{1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60},
             {7:10, 8:20}, {9:30, 10:40}, {11:50, 12:60},
             {13:10, 14:20}]

dizionario ={}

for lista in lista_diz:
    dizionario.update(lista)

print (dizionario)

# 2 - Write a Python script to generate and print a dictionary that contains 
# a number (between 1 and n) in the form (x, x*x).

# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



utente = int(input("Inserisci un numero: "))
diz = {}

for i in range(1,utente+1):
    diz[i]= i*i


print (diz)

# altra prova

# diz1 = {}

# for i in range(1,utente+1):
#     diz1= dict.fromkeys(i, (i*i))


# print (diz1)



# in una lista trovare 2 numeri che sommati
# danno un target

nums = [3,2,4,3,5,4,1,0,3,2,6]

target = 10

for i in range(len(nums)+1):
    for j in range(i+1, len (nums)):
        if nums[i] + nums[j] == target:
            print (f"{nums[i]} + {nums[j]} fa {target}")


    