"""
Definire una classe Data per rappresentare una specifica data all'interno di un anno non bisestile.
#STATO:
- mappa_mesi: dizionario con chiave il numero del mese e valore il numero di giorni. Esempio: {1: 31, 2: 28, ...}. Sfruttare questa mappa per controllare la validità di una data e per calcolare la differenza tra due date.
- giorno: intero con valore compreso tra 1 e il numero di giorni del mese. 
- mese: intero con valore compreso tra 1 e 12.
Ogni volta che si modifica una di queste variabili di istanza, devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError se i parametri non sono validi.

#METODI:
- Costruttore che prende in input giorno, mese e anno e inizializza le variabili di istanza. Esempio di utilizzo: d = Data(1, 1) FATTO
- Metodi getter e setter per giorno e mese. FATTO
- Metodo per la rappresentazione in forma di stringa della data, rispettando il formato di esempio: "1/1"
- Metodo per il calcolo della differenza in giorni tra due date. Esempio di utilizzo: d2 - d1 dove d1 = Data(1, 1), d2 = Data(1, 2), risultato -> 31. Nota, d2 - d1 deve essere uguale a d1 - d2.
- Metodo per il confronto di uguaglianza tra due date.
- Metodo per il confronto di maggiore tra due date. Esempio di utilizzo: d1 < d2
- Metodo per il confronto di minore tra due date. Esempio di utilizzo: d1 > d2
- Metodo per il confronto di minore o uguale tra due date. Esempio di utilizzo: d1 <= d2
"""
#chiedere perchè se il costruttore prende in input giorno, mese e anno, ma poi si inizializzano solo giorno e mese e non l'anno
#dire se va bene il controllo del giorno e mese nel costruttore o se va fatto in un metodo setter
class Data:
    mappa_mesi = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} #2025 anno di riferimento non bisestile

    def __init__(self, giorno:int, mese:int, anno:int=2025):
        self._mese = None
        self.anno = anno
        self.set_mese(mese)
        self.set_giorno(giorno)

    #metodi getter e setter per giorno e mese
    def get_giorno(self): 
        return self._giorno
    
    def set_giorno(self, valore):
        #controllo che il giorno è un numero intero
        if not isinstance(valore, int):
            raise TypeError("Il giorno deve restituire un numero intero")
        #controllo che il valore del giorno sia compreso tra 1 e il numero di giorni del mese
        if valore < 1 or valore > self.mappa_mesi.get(self._mese, 31):
            raise ValueError(f"Giorno non valido per il mese {self._mese}")
        self._giorno = valore

    def get_mese(self):
        return self._mese
    
    def set_mese(self, valore):
        #controllo che il mese sia un intero
        if not isinstance(valore, int):
            raise TypeError("Il mese deve restituire un numero intero")
        if valore < 1 or valore > 12:
            raise ValueError("Il mese deve essere compreso tra 1 e 12")
        self._mese = valore

    #metodo per la rappresentazione in forma di stringa della data
    def __str__(self):
        return f"{self._giorno}/{self._mese}/{self.anno}"
    
    #metodo per il calcolo della differenza in giorni tra due date
    def __sub__(self, other):
        if not isinstance(other, Data):
            raise TypeError("Operazione non consentita tra oggetti di tipo diverso")
        # Calcola il numero totale di giorni dall'inizio dell'anno per ciascuna data
        giorni_self = sum(self.mappa_mesi[m] for m in range(1, self._mese)) + self._giorno # generator expression per sommare i giorni di tutti i mesi precedenti riferiti alla data self (d1)
        giorni_other = sum(self.mappa_mesi[m] for m in range(1, other._mese)) + other._giorno # generator expression per sommare i giorni di tutti i mesi precedenti riferiti alla data other (d2)
        # Calcola la differenza in valore assoluto tra i due numeri di giorni
        return abs(giorni_self - giorni_other) # ritorna il valore assoluto della differenza tra i due numeri di giorni
    
    #metodo per il confronto di uguaglianza tra due date
    def __eq__(self, other):
        if not isinstance(other, Data):
            raise TypeError("Operazione non consentita tra oggetti di tipo diverso")
        return self._giorno == other._giorno and self._mese == other._mese # ritorna un valore booleano
    
    #metodo per il confronto di maggiore tra due date
    def __lt__(self, other):
        if not isinstance(other, Data):
            raise TypeError("Operazione non consentita tra oggetti di tipo diverso")
        return (self._mese, self._giorno) < (other._mese, other._giorno) # ritorna un valore booleano
    
    #metodo per il confronto di min
    def __gt__(self, other):
        if not isinstance(other, Data):
            raise TypeError("Operazione non consentita tra oggetti di tipo diverso")
        return (self._mese, self._giorno) > (other._mese, other._giorno) # ritorna un valore booleano
    
    #metodo per il confronto di minore o uguale tra due date
    def __le__(self, other):
        if not isinstance(other, Data):
            raise TypeError("Operazione non consentita tra oggetti di tipo diverso")
        return (self._mese, self._giorno) >= (other._mese, other._giorno) # ritorna un valore booleano
    
"""
Definire una classe Prenotazione per rappresentare una prenotazione di una stanza di un hotel.
Le pronotazioni saranno solo all'interno dello stesso anno solare. Ad esempio, non è possibile avere come data di arrivo il 27/12 e come data di partenza il 5/1.
#STATO:
- id_prenotazione: intero non negativo.
- numero_stanza: intero positivo.
- data_arrivo: oggetto di tipo Data.
- data_partenza: oggetto di tipo Data, non deve essere precedente alla data di arrivo.
- nome_cliente: stringa non vuota.
- numero_persone: intero positivo.
Ogni volta che si modifica una di queste variabili di istanza, devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError se i parametri non sono validi.

#METODI:
- Costruttore che prende in input il numero della stanza, la data di arrivo, la data di partenza, il nome del cliente e il numero di persone. Esempio di utilizzo: p = Prenotazione(101, Data(1, 1), Data(5, 1), "Mario Rossi", 2)
- Metodi getter e setter per il numero della stanza, la data di arrivo, la data di partenza, il nome del cliente e il numero di persone.
- Metodo per la rappresentazione in forma di stringa della prenotazione. Rispettando il formato di esempio: "Prenotazione 1 per stanza 101 da 1/1 a 5/1 a nome Mario Rossi per 1 persone"
- Metodo per il confronto di uguaglianza profonda tra due prenotazioni.
"""
#cercare i metodi per il confronto di uguaglianza profonda o no
class Prenotazione:
    id_counter = 1

    def __init__(self, id_prenotazione=None, numero_stanza=0, data_arrivo=None, data_partenza=None, nome_cliente="", numero_persone=0):
        if id_prenotazione is None:
            self.id_prenotazione = Prenotazione.id_counter
            Prenotazione.id_counter += 1
        else:
            if not isinstance(id_prenotazione, int) or id_prenotazione < 0:
                raise ValueError("L'ID della prenotazione deve essere un intero non negativo.")
            self.id_prenotazione = id_prenotazione

        self.numero_stanza = numero_stanza
        self.data_arrivo = data_arrivo
        self.data_partenza = data_partenza
        self.nome_cliente = nome_cliente
        self.numero_persone = numero_persone

    @property
    def id_prenotazione(self):
        return self._id_prenotazione

    @id_prenotazione.setter
    def id_prenotazione(self, value):
        if not isinstance(value, int):
            raise TypeError("L'ID della prenotazione deve essere un intero.")
        if value < 0:
            raise ValueError("L'ID della prenotazione deve essere un intero non negativo.")
        self._id_prenotazione = value

    @property
    def numero_stanza(self):
        return self._numero_stanza

    @numero_stanza.setter
    def numero_stanza(self, value):
        if not isinstance(value, int):
            raise TypeError("Il numero della stanza deve essere un intero.")
        if value <= 0:
            raise ValueError("Il numero della stanza deve essere un intero positivo.")
        self._numero_stanza = value

    @property
    def data_arrivo(self):
        return self._data_arrivo

    @data_arrivo.setter
    def data_arrivo(self, value):
        if not isinstance(value, Data):
            raise TypeError("La data di arrivo deve essere un oggetto di tipo Data.")
        self._data_arrivo = value

    @property
    def data_partenza(self):
        return self._data_partenza

    @data_partenza.setter
    def data_partenza(self, value):
        if not isinstance(value, Data):
            raise TypeError("La data di partenza deve essere un oggetto di tipo Data.")
        if value < self.data_arrivo:
            raise ValueError("La data di partenza non può essere precedente alla data di arrivo.")
        if value.anno != self.data_arrivo.anno:
            raise ValueError("Le prenotazioni devono essere all'interno dello stesso anno solare.")
        self._data_partenza = value

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, value):
        if not isinstance(value, str):
            raise TypeError("Il nome del cliente deve essere una stringa.")
        if not value.strip():
            raise ValueError("Il nome del cliente deve essere una stringa non vuota.")
        self._nome_cliente = value

    @property
    def numero_persone(self):
        return self._numero_persone

    @numero_persone.setter
    def numero_persone(self, value):
        if not isinstance(value, int):
            raise TypeError("Il numero di persone deve essere un intero.")
        if value <= 0:
            raise ValueError("Il numero di persone deve essere un intero positivo.")
        self._numero_persone = value

    def __str__(self):
        persone_str = "persona" if self.numero_persone == 1 else "persone"
        return f"Prenotazione {self.id_prenotazione} per stanza {self.numero_stanza} da {self.data_arrivo.get_giorno()}/{self.data_arrivo.get_mese()} a {self.data_partenza.get_giorno()}/{self.data_partenza.get_mese()} a nome {self.nome_cliente} per {self.numero_persone} {persone_str}"

    def __eq__(self, other):
        if not isinstance(other, Prenotazione):
            return False
        return (
            self.numero_stanza == other.numero_stanza and
            self.data_arrivo == other.data_arrivo and
            self.data_partenza == other.data_partenza and
            self.nome_cliente == other.nome_cliente and
            self.numero_persone == other.numero_persone
        )

