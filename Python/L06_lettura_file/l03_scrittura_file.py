# r -> apre il file in modalità lettura (read) (di default)
# w -> apre il file in modalità di scrittura. Se il file non esiste lo crea,
#       altrimenti sovrascrive il contenuto

with open('res/scrivi.txt', 'w') as file:
    
    for n in range(5):
        file.write(str(n))
        
with open('res/scrivi.txt', 'w') as file:
    
    for n in range(5):
        if n < len(range(5)) - 1:
            file.write(str(n) + '\n')
        else:
            file.write(str(n))
        

with open('res/scrivi.txt', 'w') as file:
    
    for n in range(5):
        if n < len(range(5)) - 1:
            file.writelines(str(n) + '\n')
        else:
            file.writelines(str(n))

lista = ['Brasato al barolo', '20', 'Secondo', 'Spaghetti allo scoglio', '15', 'Primo']
with open('res/scrivi.txt', 'w') as file:
    file.writelines(lista)            
            
lista = ['Brasato al barolo\n', '20\n', 'Secondo\n', 'Spaghetti allo scoglio\n', '15\n', 'Primo']
with open('res/scrivi.txt', 'w') as file:
    file.writelines(lista)
    
# La modalità 'a' (append) consente di aggiungere nuovi contenuti al file 
# senza sovrascrivere il contenuto esistente
with open('res/scrivi.txt', 'a') as file:
    for n in range(2, 7):
        file.write('\n' + str(n))

# r - a 
# r+ -> apre il file in modalità modifica. Permette di leggere e scrivere contemporaneamente
# lettura e append
with open('res/numeri.txt', 'r+') as file:
    print(file.read())
    for n in range(4, 20, 3):
        file.write('\n' + str(n))
    file.seek(0)
    print(file.read())

# w - r  
# w+ -> apre il file in modalità modifica. Permette di leggere e scrivere contemporanemente. 
#       sovrascrive il contenuto del file.

with open('res/numeri2.txt', 'w+') as file:
    # 4 - 7 - 10 - 13 - 16 - 19
    for n in range(4, 20, 3):
        file.write("\n" + str(n)) if n != 4 else file.write(str(n))
        
        # if n < len(range(4, 20, 3)):
        #     file.write(str(n))
        # else:
        #     file.write('\n' + str(n))
    file.seek(0)
    print(file.read())

# https://www.geeksforgeeks.org/file-mode-in-python/

    
        
        
    
    
        



