'''
es35: organizza  con un dizionario i dati sui conti bancari con numero del conto e saldo. 
Fornito poi il numero di conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa.
'''
conti_bancari = {"1": 100,
                 "2": 1000,
                 "3": 10000,
                 "4": 100000,
                 "5": 1000000,
}

numero_conto = input("Immetetre il numero del conto corrente per visualizzare il proprio saldo: ")

if numero_conto not in conti_bancari:
    print("Spiacenti, il conto: ", numero_conto, " non si trova nella mappa")
else:
    print("Il saldo del conto ", numero_conto, " è di ", conti_bancari[numero_conto], " euro.")