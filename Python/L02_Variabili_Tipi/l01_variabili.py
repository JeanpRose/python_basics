# CONVENZIONI PER I NOMI DELLE VARIABILI

# Il nome di una variabile, per convenzione, deve iniziare con una lettera minuscola.
# È possibile usare lettere e numeri, ma il nome della variabile NON può iniziare con un numero.

# Non è possibile usare spazi nei nomi delle variabili.
# Per separare le parole si utilizza l'underscore '_', una pratica nota come "snake case".
# Esempio: nome_variabile

# È sconsigliato iniziare il nome di una variabile con un underscore '_', 
# poiché in Python questo è spesso utilizzato per variabili speciali o private.

# Esempio corretto di "snake case":
nome_studente = "Mario"

# Esempio errato:
# 1nome = "Errore"   ❌  (Non può iniziare con un numero)
# nome studente = "Errore"  ❌  (Non può contenere spazi)

# PRINCIPI DELLA PROGRAMMAZIONE CLASSICA (SONO 3):
# SEQUENZA: il codice viene eseguito nell'ordine in cui è scritto.
#    Questo significa che le istruzioni vengono eseguite riga per riga, dall'alto verso il basso.

# SINTASSI PER CREARE UNA VARIABILE:
# nome_variabile = valore

# Creiamo una variabile di nome 'parola' e le assegniamo il valore 'Ciao'
parola = 'Ciao'

# Usiamo la variabile in una stampa
print('Benvenuto', parola)  # Output: Benvenuto Ciao

# Creiamo un'altra variabile con un nuovo valore
parola2 = 'Come va?'
print(parola2)  # Output: Come va?

# Creiamo una variabile numerica
numero = 32  
print(numero)  # Output: 32

# SCORCIATOIE DA TASTIERA UTILI IN VISUAL STUDIO CODE:
# Ctrl + Shift + P  → Apre il menu dei comandi di VS Code
# Ctrl + C         → Copia
# Ctrl + V         → Incolla
# Ctrl + X         → Taglia
# Ctrl + Z         → Annulla l'ultima azione
# Ctrl + Y         → Ripristina l'ultima azione annullata
# Ctrl + +         → Zoom avanti
# Ctrl + -         → Zoom indietro

# Chiediamo all'utente di inserire il proprio nome
nome = input('Scrivi il tuo nome: ')

# Stampiamo un messaggio di benvenuto personalizzato
print('Benvenuto ' + nome)  # Output: Benvenuto [Nome inserito dall'utente]
