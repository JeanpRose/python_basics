
with open('res/menu_ristorante.txt', encoding='utf-8') as file:
    menu = file.read()


# liste parallele
list_nomi = []
list_prezzi = []
list_tipi = []
lista_piatti = []
with open('res/menu_piatti.txt', encoding='utf-8') as file:
    num = int(file.readline())
    for i in range(num):
        list_nomi.append(file.readline().strip())
        list_prezzi.append(int(file.readline()))
        list_tipi.append(file.readline().strip())
        # nome = file.readline().strip()
        # prezzo = int(file.readline())
        # tipo = file.readline().strip()
        # lista_piatti.append([nome, prezzo, tipo])
        

comando = ''

while comando != '0':
    
    comando = input(menu + '\n**')
    
    if comando == '1':
        for i in range(len(list_nomi)):
            print(f'Nome: {list_nomi[i]} - Prezzo: {list_prezzi[i]}€ - Tipo: {list_tipi[i]}')
        print('-' * 40)
        
    elif comando == '2':
        print('-' * 40)
        somma = 0
        for prezzo in list_prezzi:
            somma += prezzo
        media = somma / len(list_prezzi)
        print(f'Il costo medio di un piatto è {media}€')
        print(f'Il costo medio di un piatto è {sum(list_prezzi) / len(list_prezzi)}€')
        print('-' * 40)
    
    elif comando == '3':
        tipo_input = input('Inserisci la categoria richiesta: ').capitalize()
        print('-' * 40)
        print(f'Elenco dei piatti della categoria: {tipo_input}')
        for i in range(len(list_tipi)):
            if list_tipi[i] == tipo_input:
                print(f'Nome: {list_nomi[i]} - Prezzo: {list_prezzi[i]}€')
        print('-' * 40)  
    
    elif comando == '4':
        print('-' * 40)  
        tipo_input = input('Inserisci la categoria richiesta: ').capitalize()
        somma = 0
        count = 0
        
        for i in range(len(list_tipi)):
            if list_tipi[i] == tipo_input:
                somma += list_prezzi[i]
                count += 1
        
        if count > 0:
            print(f'Il costo medio di un piatto della categoria {tipo_input} è {round(somma/count, 2)}€')
        else:
            print(f'Non ci sono piatti della categoria {tipo_input}')
            
        print('-' * 40)  
        
    elif comando == '5':
        print('-' * 40)
        prezzo_max = max(list_prezzi)
        for i in range(len(list_prezzi)):
            if list_prezzi[i] == prezzo_max:
                print(f'Nome: {list_nomi[i]} - Prezzo: {list_prezzi[i]}€')
        # prezzo_max = 0
        # ris = ''
        # for i in range(len(list_prezzi)):
        #     if list_prezzi[i] > prezzo_max:
        #         prezzo_max = list_prezzi[i]
        #         ris = f'Nome: {list_nomi[i]} - Prezzo: {list_prezzi[i]}' 
        #     elif list_prezzi[i] == prezzo_max:
        #         ris += f'\nNome: {list_nomi[i]} - Prezzo: {list_prezzi[i]}' 
        # print(ris)
    
    elif comando == '6':
        set_tipi = set(list_tipi)
        # V1
        # max_tipo = 0
        # ris = ''
        # for tipo in set_tipi:
        #     conteggio_tipo = list_tipi.count(tipo)
        #     if conteggio_tipo > max_tipo:
        #         max_tipo = conteggio_tipo
        #         ris = f'La categoria più ricorrente è {tipo} con {max_tipo}'
        #     elif conteggio_tipo == max_tipo:
        #         ris += f'\nLa categoria più ricorrente è {tipo} con {max_tipo}'
        # print(ris)
        
        # V2
        # count_a = 0
        # count_p = 0
        # count_s = 0
        # count_c = 0
        # for i in range(len(list_tipi)):
        #     if list_tipi[i] == 'Antipasto':
        #         count_a += 1
        #     elif list_tipi[i] == 'Primo':
        #         count_p += 1
        #     elif list_tipi[i] == 'Secondo':
        #         count_s += 1
        #     else:
        #         count_c += 1
        # if count_a > count_p :
        #         if count_a > count_s:
        #             if count_a > count_c :
        #                 print('Il piatto più ricorrente è antipasto con: ', count_a)
        # if count_p > count_a :
        #     if count_p > count_s:
        #         if count_p > count_c : 
        #             print('Il piatto più ricorrente è primo con: ', count_p)
        # if count_s > count_p:
        #     if count_s > count_a:
        #         if count_s > count_c:
        #             print('Il piatto più ricorrente è secondo con: ', count_s)
        # if count_c > count_p:
        #     if count_c > count_a:
        #         if count_c > count_s :
        #             print('Il piatto più ricorrente è contorno con: ', count_c)
        
        # V3
        a = 0
        max = 0   
        k = ''        
        for tipo in set_tipi:
            a = 0
            for t in list_tipi:
                if tipo == t:
                    a += 1
            if a > max:
                k = tipo
                max = a
            
        print(k, max)
        
    elif comando == '0':
        print('-' * 40)
        print('Buona serata!')
        print('-' * 40)
    else:
        print('-' * 40)
        print("Valore sconosciuto, riprova!")
        print('-' * 40)
        

            
                
            