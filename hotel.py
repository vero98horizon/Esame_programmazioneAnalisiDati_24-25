from stanze import *
from classi import *
"""
Definire una classe Hotel che rappresenta un hotel.
#STATO:
- stanze: dizionario con chiave il numero della stanza e valore l'oggetto stanza.
- prenotazioni: dizionario con chiave un intero e valore l'oggetto prenotazione.
- id_prenotazioni: intero progressivo inizializzato a 1 e incrementato ogni volta che una prenotazione viene aggiunta, da usare come chiave per le prenotazioni.
#METODI:
- Costruttore che inizializza le variabili di istanza. Esempio di utilizzo: h = Hotel()
- Metodo per il confronto di uguaglianza profonda tra due hotel.
- Metodo per la rappresentazione in forma di stringa dell'hotel. Rispettando il formato di esempio: "Hotel: 3 stanze (101,102,103), 2 prenotazioni." (Nota: non è necessario stampare i dettagli delle stanze e delle prenotazioni).
- Metodi specificati in seguito.
"""

"""
Inserisce una nuova stanza nell'hotel.
:param stanza oggetto di tipo Stanza da aggiungere all'hotel
:raise TypeError: se i parametri non hanno il tipo corretto
:raise ValueError: se i parametri non sono nel range di valori ammessi
"""      
class Hotel:
    def __init__(self):
       self.stanze = {}
       self.prenotazioni = {}
       self.id_prenotazioni = 1

    def __eq__(self, other):
        return self.stanze == other.stanze and self.prenotazioni == other.prenotazioni and self.id_prenotazioni == other.id_prenotazioni 
   
    def __str__(self):
        stanze_str = ",".join(str(num) for num in sorted(self.stanze.keys()))
        return f"Hotel: {len(self.stanze)} stanze ({stanze_str}), {len(self.prenotazioni)} prenotazioni."
            
    def aggiungi_stanza(self, stanza):  
        gestione_errori(stanza,Stanza)
        if stanza.get_numero_stanza() in self.stanze:
            raise ValueError("La stanza è già presente nell'hotel")
        self.stanze[stanza.get_numero_stanza()] = stanza 


"""
Prenota una stanza nell'hotel e incrementa id_prenotazioni se la prenotazione va a buon fine.
Crea un oggetto Prenotazione con id_prenotazioni e i parametri in ingresso, e lo aggiunge al dizionario delle prenotazioni.
:param numero_stanza: numero della stanza da prenotare
:param data_arrivo: oggetto di tipo Data rappresentante la data di arrivo
:param data_partenza: oggetto di tipo Data rappresentante la data di partenza
:param nome_cliente: stringa rappresentante il nome del cliente
:param numero_persone: intero rappresentante il numero di persone
:return indice della prenotazione
:raise TypeError: se i parametri non hanno il tipo corretto
:raise ValueError: se la stanza è già occupata nelle date indicate
:raise KeyError: se la stanza non è presente nell'hotel
"""
    def prenota(self, numero_stanza, data_arrivo, data_partenza, nome_cliente, numero_persone):
        gestione_errori(data_arrivo,Data)
        gestione_errori(data_partenza,Data)
        gestione_errori(nome_cliente,str)
        gestione_errori(numero_persone,int,0)
        
        if numero_stanza not in self.stanze:
            raise KeyError("La stanza non è presente nell'hotel")
        stanza = self.stanze[numero_stanza]
        if numero_persone > stanza.get_posti():     #Controllo numero persone rispetto ai posti della stanza
            raise ValueError(f"La stanza {numero_stanza} non può ospitare più di {stanza.get_posti()} persone")
    
       for prenotazione in self.prenotazioni.values():# Controllo sovrapposizione date
                if prenotazione.get_numero_stanza() == numero_stanza:
                    if data_arrivo < prenotazione.get_data_partenza() and data_partenza > prenotazione.get_data_arrivo():
                        raise ValueError("La stanza è già occupata nelle date indicate")

       prenotazione = Prenotazione(self.id_prenotazioni, numero_stanza, data_arrivo, data_partenza, nome_cliente, numero_persone)
       self.prenotazioni[self.id_prenotazioni] = prenotazione
       self.id_prenotazioni += 1
       return self.id_prenotazioni - 1

    """
    Disdice una prenotazione dell'hotel.
    :param indice della prenotazione da disdire
    :raise KeyError: se la prenotazione non è presente nell'hotel
    """    
    def disdici(self, indice):  
        if indice not in self.prenotazioni:
            raise KeyError("La prenotazione non è presente nell'hotel")
        del self.prenotazioni[indice]

    """
    Rimuove una stanza dall'hotel e tutte le prenotazioni relative a quella stanza.
    :param numero_stanza: numero della stanza da rimuovere
    :raise KeyError: se la stanza non è presente nell'hotel
    """
    def rimuovi_stanza(self, numero_stanza):    
        if numero_stanza not in self.stanze:
            raise KeyError("La stanza non è presente nell'hotel")
        for prenotazione in list(self.prenotazioni.values()):
            if prenotazione.get_numero_stanza() == numero_stanza:
                del self.prenotazioni[prenotazione.get_id()]

        del self.stanze[numero_stanza]

    """
    Restituisce una stanza specifica dell'hotel.
    :param numero_stanza: numero della stanza da restituire
    :return: la stanza con numero_stanza
    :raise KeyError: se la stanza non è presente nell'hotel
    """
    def get_stanza(self, numero_stanza):
        if numero_stanza not in self.stanze:
            raise KeyError("La stanza non è presente nell'hotel")
        return self.stanze[numero_stanza]

    """
    Restituisce la lista delle stanze presenti nell'hotel.
    :return: la lista delle stanze presenti nell'hotel
    """
    def get_stanze(self):
        return list(self.stanze.values())

    """
    Restituisce la lista delle stanze per tipo passato presenti nell'hotel.
    :param tipo: stringa rappresentante il tipo di stanza da cercare
    :return: la lista delle stanze per tipo passato presenti nell'hotel
    """
    def get_stanze_tipo(self, tipo):
        return [stanza for stanza in self.stanze.values() if stanza.get_tipo_stanza() == tipo]

    """
    Restituisce la lista delle prenotazioni presenti nell'hotel.
    :return: la lista delle prenotazioni presenti nell'hotel
    """
    def get_prenotazioni(self):
        return list(self.prenotazioni.values())

    """
    Restituisce una prenotazione specifica dell'hotel.
    :param indice: indice della prenotazione da restituire
    :return: la prenotazione con indice
    :raise KeyError: se la prenotazione non è presente nell'hotel
    """
    def get_prenotazione(self, indice):
        return self.prenotazioni[indice]

    """
    Restituisce la lista delle prenotazioni presenti nell'hotel in una data specifica.
    :param data: data da cercare
    :return: la lista delle prenotazioni presenti nell'hotel in una data specifica
    :raise TypeError: se data non è un oggetto di tipo Data
    """
    def get_prenotazioni_data(self, data):
        return [prenotazione for prenotazione in self.prenotazioni.values() if prenotazione.get_data_arrivo() <= data and prenotazione.get_data_partenza() >= data]

    """
    Restituisce il prezzo di una prenotazione specifica ottenuto dal prezzo della stanza per il numero di persone.
    :param indice: indice della prenotazione da cercare
    :return: il prezzo della prenotazione con indice
    :raise KeyError: se la prenotazione non è presente nell'hotel
    """
    def prezzo_prenotazione(self, indice):  #TODO controllare 
        pren = self.prenotazioni[indice]
        notti = pren.get_data_partenza() - pren.get_data_arrivo()
        # calcolo prezzo della stanza per 'notti'
        prezzo_stanza = pren.get_stanza().calcola_prezzo(notti)
        # moltiplico per il numero di persone
        return prezzo_stanza * pren.get_numero_persone()


    """
    Restituisce la lista delle prenotazioni presenti nell'hotel per un cliente specifico.
    :param cliente: nome del cliente da cercare
    :return: la lista delle prenotazioni presenti nell'hotel per un cliente specifico
    """
    def get_prenotazioni_cliente(self, cliente):
        return [prenotazione for prenotazione in self.prenotazioni.values() if prenotazione.get_nome_cliente() == cliente]


    """
    Restituisce la lista delle stanze libere nell'hotel in una data specifica.
    :param data: data da cercare
    :return: la lista delle stanze libere nell'hotel in una data specifica
    :raise TypeError: se data non è un oggetto di tipo Data
    """
    def get_stanze_libere(self, data):
        data = Data(data.get_giorno(), data.get_mese(), data.get_anno())
        if type(data) != Data:
            raise TypeError("La data deve essere un oggetto di tipo Data")
        stanze_libere = []
        for stanza in self.stanze.values():
            occupata = False
            for prenotazione in self.prenotazioni.values():
                if prenotazione.get_numero_stanza() == stanza.get_numero_stanza():
                    if prenotazione.get_data_arrivo() <= data and prenotazione.get_data_partenza() >= data:
                        occupata = True
            if not occupata:
                stanze_libere.append(stanza)
        return stanze_libere

        

    """
    Restituisce la lista delle prenotazioni presenti nell'hotel per un tipo di stanza specifico.
    :param tipo_stanza: stringa rappresentante il tipo di stanza da cercare
    :return: la lista delle prenotazioni presenti nell'hotel per un tipo di stanza specifico
    """
    def get_prenotazioni_tipo_stanza(self, tipo_stanza):
        tipo_stanza = tipo_stanza.capitalize()
        return [prenotazione for prenotazione in self.prenotazioni.values() if prenotazione.get_stanza().get_tipo_stanza() == tipo_stanza]

    """
    Restituisce la lista delle stanze dell'hotel sopra un prezzo specifico fra due date.
    :param numero_notti: numero di notti da considerare
    :param prezzo: prezzo da confrontare
    :return: la lista delle stanze dell'hotel sopra un prezzo specifico
    """    
    def get_stanze_sopra_prezzo(self, numero_notti, prezzo):
        numero_notti = int(numero_notti)
        prezzo = float(prezzo)

        if prezzo <= 1:
            raise ValueError("Il prezzo deve essere maggiore di 1")
        stanze_sopra_prezzo = []
        for stanza in self.stanze.values():
            if stanza.calcola_prezzo(numero_notti) > prezzo:
                stanze_sopra_prezzo.append(stanza)
        return stanze_sopra_prezzo

    """
    Restituisce il numero totale di persone presenti nell'hotel in una data specifica.
    :param data: data da cercare
    :return: il numero totale di persone presenti nell'hotel in una data specifica
    :raise TypeError: se data non è un oggetto di tipo Data
    """    
    def get_numero_persone_data(self, data):
        gestione_errori(data,Data)
        data = Data(data.get_giorno(), data.get_mese(), data.get_anno())
        persone_presenti = 0
        for prenotazione in self.prenotazioni.values():
            if prenotazione.get_data_arrivo() <= data and prenotazione.get_data_partenza() >= data:
                persone_presenti += prenotazione.get_numero_persone()
        return persone_presenti

    """
    Salva lo stato dell'hotel su un file. Le eccezioni non devono essere gestite in questo metodo.
    :param nomefile: nome del file su cui salvare lo stato dell'hotel
        """
    def salva(self, nomefile):
    
        with open(nomefile, 'w', encoding='utf-8') as file:
            file.write("Hotel\n")
            # Salvataggio delle stanze
            for stanza in self.stanze.values():
                  tipo = stanza.get_tipo_stanza()
                  file.write(f"{tipo},{stanza.get_numero_stanza()},{stanza.get_posti()},{stanza.get_prezzo_base()}\n")
            # Salvataggio delle prenotazioni
          

            for prenotazione in self.prenotazioni.values():
                file.write(
                    f"{prenotazione.get_id()},{prenotazione.get_numero_stanza()},{prenotazione.get_data_arrivo()},"
                    f"{prenotazione.get_data_partenza()},{prenotazione.get_nome_cliente()},{prenotazione.get_numero_persone()}\n"
                )

    """
    Carica lo stato dell'hotel da un file e sostituisce lo stato corrente se il caricamento va a buon fine. Le eccezioni non devono essere gestite in questo metodo.
    :param nomefile: nome del file da cui caricare lo stato dell'hotel
    :raise ValueError: se il file non è nel formato corretto (es. se non è presente il nome dell'hotel)
    """
    def carica(self, nomefile):
        """
        Carica lo stato dell'hotel da un file e sostituisce lo stato corrente se il caricamento va a buon fine.
        Le eccezioni non vengono gestite in questo metodo.
        
        :param nomefile: nome del file da cui caricare lo stato dell'hotel
        :raise ValueError: se il file non è nel formato corretto (es. se non è presente "Hotel" come prima riga)
        """
        with open(nomefile, 'r', encoding='utf-8') as file:
            righe = file.readlines()
            
            if not righe or righe[0].strip() != "Hotel":
                raise ValueError("Il file non è nel formato corretto")
            # Reset dello stato corrente
            self.stanze = {}
            self.prenotazioni = {}
            self.id_prenotazioni = 1
            # Elaborazione delle righe successive
            for riga in righe[1:]:
                # Se la riga è vuota la saltiamo 
                if not riga.strip():
                    continue
                dati = riga.strip().split(",")
                if len(dati) == 3:
                    # Dati della stanza: numero_stanza, posti, prezzo_base
                    stanza = Stanza(int(dati[0]), int(dati[1]), float(dati[2]))
                    self.stanze[int(dati[0])] = stanza
                elif len(dati) == 6:
                    # Dati della prenotazione: id, numero_stanza, data_arrivo, data_partenza, nome_cliente, numero_persone
                    prenotazione = Prenotazione(
                        int(dati[0]),
                        int(dati[1]),
                        Data.from_string(dati[2]),
                        Data.from_string(dati[3]),
                        dati[4],
                        int(dati[5])
                    )
                    self.prenotazioni[int(dati[0])] = prenotazione
                    # Aggiorna l'id progressivo se necessario
                    if int(dati[0]) >= self.id_prenotazioni:
                        self.id_prenotazioni = int(dati[0]) + 1
                else:
                    raise ValueError("Il file contiene una riga con formato non riconosciuto")

        