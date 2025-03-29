"""
 Deve essere realizzata un'interfaccia grafica usando il modulo tkinter che carichi automaticamente il file 
 hotel_base.txt, permetta di mostrare sin da subito le stanze dell'hotel indicando tipo e numero della stanza 
 (con extra in caso di suite) e le seguenti funzionalità:
 - mostrare la lista di prenotazioni dell'hotel;
 - prenotazione di una stanza;
 - disdire la prenotazione di una stanza;
 - ottenere il prezzo di una prenotazione dato l'indice:
 - mostrare l'hotel ad una certa data inserendo i nomi dei clienti nelle stanze a quella data;
 - ottenere le stanze libere ad una certa data;
 - ottenere le prenotazioni di uno specifico cliente inserendo il nome;
 - ottenere il numero di persone nell'albergo ad una certa data;
 - salvare o caricare da file lo stato dell'hotel permettendo di inserire il nome del file.
 - uscire dall'applicazione 
 Per uscire dall'applicazione deve essere possibile usare sia mouse che tastiera.
 L'aspetto dell'interfaccia viene deciso dallo studente.
"""


import tkinter as tk
# creazione di una finestra (task1) -- file: 001finestra.py
window = tk.Tk()
# creiamo un widget della classe Label
greeting = tk.Label(text="Hello, Tkinter")
foreground="black"  

# inseriamo il widget nella finestra
# pack() fa il resize della finestra fino a includere esattamente i widget in ordine
greeting.pack()

# aspettiamo un evento (task 4) e attiviamo la finestra (a questo punto viene visualizzata)
window.mainloop()
