from classi import Data
"""
Definire una classe Stanza che rappresenta una stanza di un hotel.
#STATO:
- numero_stanza: intero positivo.
- posti: intero positivo.
- prezzo_base: numero con virgola maggiore di 1.
Ogni volta che si modifica una di queste variabili di istanza, devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError se i parametri non sono validi.
#METODI:
- Costruttore che prende in input il numero della stanza, il numero di posti e il prezzo base. Esempio di utilizzo: s = Stanza(101, 2, 50.0)
- Metodi getter e setter per il numero della stanza, il numero di posti e il prezzo base.
- Metodo calcola_prezzo che prende in input l'intero numero_notti e restituisce il prezzo della stanza per il periodo indicato. Il prezzo della stanza è dato dal prezzo base moltiplicato per il numero di notti di permanenza.
- Metodo per la rappresentazione in forma di stringa della stanza, rispettando il formato di esempio: "101, 2 posti" dove 101 è il numero della stanza e 2 il numero di posti.
- Metodo per il confronto di uguaglianza profonda tra due stanze.
- Metodo get_tipo_stanza che restituisce il nome della classe. Esempio di utilizzo: s.get_tipo_stanza() restituisce "Stanza"
"""
class Stanza:
    def __init__(self, numero_stanza, posti, prezzo_base):
        self.set_numero_stanza(numero_stanza)
        self.set_posti(posti)
        self.set_prezzo_base(prezzo_base)
#todo usiamo @param magari per tutti i metodi che ci servono?
    def get_numero_stanza(self):
        return self.numero_stanza
    
    def set_numero_stanza(self, numero_stanza):#todo aggiungere logica per il txt
        if type(numero_stanza) != int:
            raise TypeError("Il numero della stanza deve essere un intero")
        if numero_stanza <= 0:
            raise ValueError("Il numero della stanza deve essere un intero positivo")
        self.numero_stanza = numero_stanza

    def get_posti(self):
        return self.posti
    
    def set_posti(self, posti):#todo aggiungere logica per il txt
        if type(posti) != int:
            raise TypeError("Il numero di posti deve essere un intero")
        if posti <= 0:
            raise ValueError("Il numero di posti deve essere un intero positivo")
        self.posti = posti

    def get_prezzo_base(self):
        return self.prezzo_base
    
    def set_prezzo_base(self, prezzo_base): #todo: usiamo una regex per controllare il tipo di prezzo_base? aggiungere logica per il txt
        if type(prezzo_base) != float:
            raise TypeError("Il prezzo base deve essere un numero con virgola")
        if prezzo_base <= 1:
            raise ValueError("Il prezzo base deve essere maggiore di 1")
        self.prezzo_base = prezzo_base

    def calcola_prezzo(self, numero_notti):
        if type(numero_notti) != int:
            raise TypeError("Il numero di notti deve essere un intero")
        if numero_notti < 0:
            raise ValueError("Il numero di notti deve essere un intero positivo")
        return self.prezzo_base * numero_notti
    
    def __str__(self):#todo cambiare nome metodo questo e quello dopo
        return f"{self.numero_stanza}, {self.posti} posti"
    
    def __eq__(self, other):
        return self.numero_stanza == other.numero_stanza and self.posti == other.posti
    
    def get_tipo_stanza(self):#todo da finire
        return "Stanza"
    
"""
Definire una classe Suite che estende Stanza e rappresenta una suite di un hotel. Una suite è una stanza con almeno 4 posti e con una lista di extra.
#STATO:
- extra: lista di stringhe.
Ogni volta che si modifica questa variabile devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError in casi errati.
#METODI:
- Costruttore che prende in input il numero della stanza, il numero di posti, la lista di extra e il prezzo base, e inizializza le variabili ereditate. Esempio di utilizzo: s = Suite(102, 4, ["TV", "WiFi", "Jacuzzi"], 200.0)
- Metodi getter e setter per la lista di extra.
- Metodo calcola_prezzo che prende in input l'intero numero_notti e calcola il prezzo della stanza per il periodo indicato. Il prezzo di una notte per una suite è dato dal prezzo base maggiorato del 50% più 10 euro per ogni extra.
- Metodo per la rappresentazione in forma di stringa della suite. Rispettando il formato di esempio: "Suite 102, 4 posti, con TV, WiFi e Jacuzzi"
- Metodo per il confronto di uguaglianza profonda tra due suite.
- Metodo get_tipo_stanza che restituisce il nome della classe. Esempio di utilizzo: s.get_tipo_stanza() restituisce "Suite"
"""

"""
Definire una classe Singola che estende Stanza e rappresenta una stanza singola di un hotel. Una stanza singola è una stanza con un solo posto.
#METODI:
- Costruttore che prende in input il numero della stanza e il prezzo base, e inizializza opportunamente le variabili ereditate. Esempio di utilizzo: s = Singola(103, 40.0)
- Metodo per la rappresentazione in forma di stringa della stanza. Rispettando il formato di esempio: "Singola 103, 1 posto"
- Metodo per il confronto di uguaglianza profonda tra due stanze singole.
- Metodo get_tipo_stanza che restituisce il nome della classe. 
"""

"""
Definire una classe Doppia che estende Stanza e rappresenta una stanza doppia di un hotel. Una stanza doppia è una stanza con due posti.
#METODI:
- Costruttore che prende in input il numero della stanza e il prezzo base, e inizializza opportunamente le variabili ereditate. Esempio di utilizzo: s = Doppia(104, 60.0)
- Metodo per la rappresentazione in forma di stringa della stanza. Rispettando il formato di esempio: "Doppia 104, 2 posti"
- Metodo calcola_prezzo che prende in input l'intero  numero_notti e calcola il prezzo della stanza per il periodo indicato. Il prezzo di una notte per una doppia è dato dal prezzo base maggiorato del 20%.
- Metodo per il confronto di uguaglianza profonda tra due stanze doppie.
- Metodo get_tipo_stanza che restituisce il nome della classe. 
"""
class Suite(Stanza):
    def __init__(self, numero_stanza, posti, extra, prezzo_base):
        if posti < 4:       #todo manca controllo  se è 0, e servono dei valori di default per extra che deve essere una lista di stringhe
            raise ValueError("Una suite deve avere almeno 4 posti")
        super().__init__(numero_stanza, posti, prezzo_base)
        self.set_extra(extra)

    def get_extra(self):
        return self.extra
    
    def set_extra(self, extra):
        if type(extra) != list:
            raise TypeError("Gli extra devono essere una lista")
        for e in extra:
            if type(e) != str:
                raise TypeError("Gli extra devono essere delle stringhe")
        self.extra = extra

    def calcola_prezzo(self, numero_notti):
        if type(numero_notti) != int:
            raise TypeError("Il numero di notti deve essere un intero")
        if numero_notti < 0:
            raise ValueError("Il numero di notti deve essere un intero positivo")
        return self.prezzo_base * numero_notti * 1.5 + 10 * len(self.extra)
    
    def __str__(self):
        return f"Suite {self.numero_stanza}, {self.posti} posti, con {', '.join(self.extra)}"
    
    def __eq__(self, other):
        return super().__eq__(other) and self.extra == other.extra
    def get_tipo_stanza(self):
        return "Suite"
    
class Singola(Stanza):
    def __init__(self, numero_stanza, prezzo_base):
        super().__init__(numero_stanza, 1, prezzo_base)

    def __str__(self):
        return f"Singola {self.numero_stanza}, 1 posto"
    
    def __eq__(self, other):
        super().__eq__(other)
    
    def get_tipo_stanza(self):
        return "Singola"
    
class Doppia(Stanza):
    def __init__(self, numero_stanza, prezzo_base):
        super().__init__(numero_stanza, 2, prezzo_base)

    def calcola_prezzo(self, numero_notti):
        return self.prezzo_base * 1.2 * numero_notti
    
    def __str__(self):
        return f"Doppia {self.numero_stanza}, 2 posti"
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def get_tipo_stanza(self):
        return "Doppia"
    

