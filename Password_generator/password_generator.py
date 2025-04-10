import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip
from PIL import Image, ImageTk
import os

def passwort_generieren():
    # Zeichen basierend auf der ausgewählten Schwierigkeit
    if schwierigkeit_var.get() == "Einfach":
        zeichen = string.ascii_letters + string.digits
    elif schwierigkeit_var.get() == "Mittel":
        zeichen = string.ascii_letters + string.digits + string.punctuation.replace("'", "").replace('"', '')
    else:  # Schwer
        zeichen = string.ascii_letters + string.digits + string.punctuation
    
    # Länge des Passworts aus der Combobox
    laenge = int(laenge_var.get())
    
    # Passwort generieren
    passwort = ''.join(random.choice(zeichen) for _ in range(laenge))
    passwort_var.set(passwort)

def passwort_kopieren():
    pyperclip.copy(passwort_var.get())

# Hauptfenster erstellen
root = tk.Tk()
root.title("Passwort Generator")
root.geometry("500x300")

# Icon laden und setzen
try:
    # Icon aus PNG-Datei laden
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
    icon = Image.open(icon_path)
    photo = ImageTk.PhotoImage(icon)
    root.iconphoto(True, photo)
    # Tkinter-Standard-Icon entfernen
    root.iconbitmap('@NONE')
except Exception as e:
    print(f"Fehler beim Laden des Icons: {e}")

# Variablen
passwort_var = tk.StringVar()
schwierigkeit_var = tk.StringVar(value="Mittel")
laenge_var = tk.StringVar(value="12")

# Hauptframe
haupt_frame = ttk.Frame(root, padding="10")
haupt_frame.pack(fill=tk.BOTH, expand=True)

# Schwierigkeitsauswahl
ttk.Label(haupt_frame, text="Schwierigkeit:").pack(pady=5)
schwierigkeit_combo = ttk.Combobox(haupt_frame, textvariable=schwierigkeit_var, 
                                 values=["Einfach", "Mittel", "Schwer"], state="readonly")
schwierigkeit_combo.pack(pady=5)

# Längenauswahl
ttk.Label(haupt_frame, text="Passwortlänge:").pack(pady=5)
laenge_combo = ttk.Combobox(haupt_frame, textvariable=laenge_var, 
                          values=["8", "10", "12", "16", "20"], state="readonly")
laenge_combo.pack(pady=5)

# Passwort anzeigen
ttk.Label(haupt_frame, text="Generiertes Passwort:").pack(pady=10)
passwort_entry = ttk.Entry(haupt_frame, textvariable=passwort_var, width=40, justify='center')
passwort_entry.pack(pady=5)

# Button-Frame
button_frame = ttk.Frame(haupt_frame)
button_frame.pack(pady=20)

# Buttons
generieren_button = ttk.Button(button_frame, text="Passwort generieren", command=passwort_generieren)
generieren_button.pack(side=tk.LEFT, padx=5)

kopieren_button = ttk.Button(button_frame, text="Passwort kopieren", command=passwort_kopieren)
kopieren_button.pack(side=tk.LEFT, padx=5)

# Starte die Hauptschleife
root.mainloop()