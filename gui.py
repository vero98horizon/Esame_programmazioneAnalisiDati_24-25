"""
 Deve essere realizzata un'interfaccia grafica usando il modulo tkinter che carichi automaticamente il file
 hotel_base.txt, permetta di mostrare sin da subito le stanze dell'hotel indicando tipo e numero della stanza
 (con extra in caso di suite) e le seguenti funzionalità:
 - mostrare la lista di prenotazioni dell'hotel;
 - prenotazione di una stanza; cliente
 - disdire la prenotazione di una stanza; cliente
 - ottenere il prezzo di una prenotazione dato l'indice: cliente
 - mostrare l'hotel ad una certa data inserendo i nomi dei clienti nelle stanze a quella data;
 - ottenere le stanze libere ad una certa data;     cliente
 - ottenere le prenotazioni di uno specifico cliente inserendo il nome;
 - ottenere il numero di persone nell'albergo ad una certa data;
 - salvare o caricare da file lo stato dell'hotel permettendo di inserire il nome del file.
 - uscire dall'applicazione
 Per uscire dall'applicazione deve essere possibile usare sia mouse che tastiera.
 L'aspetto dell'interfaccia viene deciso dallo studente.
"""
import tkinter as tk
from tkinter import messagebox

import hotel
from classi import Data
from hotel import Hotel

class myApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")

        # Creazione del frame principale che conterrà canvas e bottoni
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Creazione del frame per il canvas
        self.canvas_frame = tk.Frame(self.main_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        # Inizializzo l'hotel e carico i dati
        self.hotel = Hotel()
        self.hotel.carica("hotel_base.txt")

        # Creazione del canvas nel canvas_frame
        self.canvas = tk.Canvas(self.canvas_frame, bg="white", height=500, width=580)
        self.canvas.pack(pady=10)

        y_position = 20
        self.canvas.create_text(290, y_position,
                                text="Benvenuti nell'albergo!\nLista delle stanze offerte:",
                                fill="black", font=("Arial", 14, "bold"))
        y_position += 40

        # Mostra le informazioni delle stanze
        for stanza in self.hotel.stanze.values():
            tipo = stanza.get_tipo_stanza()
            numero = stanza.get_numero_stanza()
            extra = ", ".join(stanza.get_extra()) if hasattr(stanza, 'get_extra') else ""
            room_text = f"tipo stanza: {tipo} con numero stanza: {numero} {'elementi extra:' + extra if extra else ''}"
            self.canvas.create_text(20, y_position, anchor="w",
                                    text=room_text, fill="black", font=("Arial", 12))
            y_position += 20

        # Frame per i bottoni in basso nel main_frame
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(side=tk.BOTTOM, pady=10)

        btn_frame1 = tk.Button(self.button_frame, text="Area clienti", command=self.go_to_frame1, width=15)
        btn_frame1.pack(side=tk.LEFT, padx=5)
        btn_frame2 = tk.Button(self.button_frame, text="Gestione albergo", command=self.go_to_frame2, width=15)
        btn_frame2.pack(side=tk.LEFT, padx=5)

        # Creo i due nuovi frame (non visibili all'inizio)
        self.frame1 = tk.Frame(self.root, bg="lightblue")
        tk.Label(self.frame1, text="Selezionare il servizio desiderato", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.frame1, text="Prenota una stanza", command=self.open_prenota_stanza_popup).pack(pady=10)
        tk.Button(self.frame1, text="Disdici una prenotazione", command=self.back_to_main).pack(pady=10)
        tk.Button(self.frame1, text="Visualizza prezzo prenotazione", command=self.back_to_main).pack(pady=10)
        tk.Button(self.frame1, text="Visualizza stanze libere", command=self.back_to_main).pack(pady=10)
        tk.Button(self.frame1, text="Torna Indietro", command=self.back_to_main).pack(pady=70)

        self.frame2 = tk.Frame(self.root, bg="lightgreen")
        tk.Label(self.frame2, text="Questo è Frame 2", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.frame2, text="Torna Indietro", command=self.back_to_main).pack(pady=10)
        tk.Button(self.frame2, text="Carica hotel", command=self.back_to_main).pack(pady=10)
        tk.Button(self.frame2, text="Salva hotel", command=self.back_to_main).pack(pady=10)
        tk.Button(self.frame2, text="Mostra tutte le prenotazioni", command=self.back_to_main).pack(pady=10)
        tk.Button(self.frame2, text="Mostra prenotazione di un cliente", command=self.back_to_main).pack(pady=10)
        tk.Button(self.frame2, text="Mostra stato stanze per data", command=self.back_to_main).pack(pady=10)

    def open_prenota_stanza_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Prenotazione Stanza")
        popup.geometry("400x400")

        # Etichette e campi di input
        tk.Label(popup, text="Numero Stanza:").pack(pady=5)
        numero_stanza_entry = tk.Entry(popup)
        numero_stanza_entry.pack(pady=5)

        tk.Label(popup, text="Data Inizio (gg/mm):").pack(pady=5)
        data_inizio_entry = tk.Entry(popup)
        data_inizio_entry.pack(pady=5)

        tk.Label(popup, text="Data Fine (gg/mm):").pack(pady=5)
        data_fine_entry = tk.Entry(popup)
        data_fine_entry.pack(pady=5)

        tk.Label(popup, text="Nome Cliente:").pack(pady=5)
        nome_cliente_entry = tk.Entry(popup)
        nome_cliente_entry.pack(pady=5)

        tk.Label(popup, text="Numero Persone:").pack(pady=5)
        numero_persone_entry = tk.Entry(popup)
        numero_persone_entry.pack(pady=5)

        # Pulsante per confermare la prenotazione
        tk.Button(popup, text="Prenota", command=lambda: self.conferma_prenotazione(
            numero_stanza_entry.get(),
            data_inizio_entry.get(),
            data_fine_entry.get(),
            nome_cliente_entry.get(),
            numero_persone_entry.get(),
            popup
        )).pack(pady=20)

        # Pulsante per annullare
        tk.Button(popup, text="Annulla", command=popup.destroy).pack(pady=5)

    def conferma_prenotazione(self, numero_stanza, data_inizio, data_fine, nome_cliente, numero_persone, popup):
        try:
            # Conversione dei dati
            numero_stanza = int(numero_stanza)
            numero_persone = int(numero_persone)
            data_arrivo,data_partenza= Hotel.parsing_date(data_inizio, data_fine)
            # Effettua la prenotazione
            id_prenotazione = self.hotel.prenota(
                numero_stanza,
                data_arrivo,
                data_partenza,
                nome_cliente,
                numero_persone
            )

            messagebox.showinfo("Successo", f"Prenotazione effettuata con ID: {id_prenotazione}")
            popup.destroy()

        except ValueError as e:
            messagebox.showerror("Errore", f"Dati non validi: {e}")
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {e}")



    def disdici_prenotazione(self, prenotazione_id):
        # Funzione per disdire una prenotazione
        pass
    def visualizza_prezzo_prenotazione(self, prenotazione_id):
        # Funzione per visualizzare il prezzo di una prenotazione
        pass
    def visualizza_stanze_libere(self, data):
        # Funzione per visualizzare le stanze libere
        pass


    def carica_hotel(self, nome_file):
        # Funzione per caricare l'hotel da un file
        pass
    def salva_hotel(self):
        # Funzione per salvare l'hotel su un file
        pass
    def mostra_prenotazioni(self):
        # Funzione per mostrare tutte le prenotazioni
        pass
    def mostra_prenotazione_cliente(self, nome_cliente):
        # Funzione per mostrare la prenotazione di un cliente
        pass
    def mostra_stato_stanze_data(self, data):
        # Funzione per mostrare lo stato delle stanze in una certa data
        pass



    def go_to_frame1(self):
        # Nascondo il main_frame e mostro frame1
        self.main_frame.pack_forget()
        self.frame1.pack(fill=tk.BOTH, expand=True)

    def go_to_frame2(self):
        # Nascondo il main_frame e mostro frame2
        self.main_frame.pack_forget()
        self.frame2.pack(fill=tk.BOTH, expand=True)

    def back_to_main(self):
        # Nascondo i frame secondari e ripristino il main_frame
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.main_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = myApp(root)
    root.mainloop()
