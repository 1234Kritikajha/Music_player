import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import os

# -----------------------------------
# BASE DIRECTORY FOR SONG FILES
# -----------------------------------
BASE = r"C:\Users\jhakr\OneDrive\Documents\MCA\python work\musicbox"

# -----------------------------------
# SONG DATABASE
# -----------------------------------
songs = {
    "Sahiba": {
        "file": os.path.join(BASE, "Sahiba.mp3"),
        "lyrics": [
     """
        Sahiba, aaye ghar kaahe na
        Aise toh sataye na,
        Dekhu tujhko chain aata hai..

        Sahiba neendein veendein aaye na,
        Raatein kaati jaye na,
        Tera hi khayal din raen aata hai..


        Sahiba samandar,
        meri aankhon mein reh gye,
        Hum aate aate jaana,
        teri yaadon mein reh gye.
        Yeh palkein gawahi hai,
        hum raaton mein reh gye,
        Jo vaade kiye saare,
        bas baaton mein reh gyee..

        Baaton baaton mein hi
        Khaabon khaabon mein hi
        Mere kareeb hai tu.
        Teri talab mujhko teri talab Jaana
        ho tu kabhi rubru…

        Shor sharaba jo seene mein hai
        Mere kaise byaan main karun
        Haal jo mera hai main
        kisko bataun, mere sahiba
        Dil na kiraye ka, thoda toh sambhalo na,
        Naazuk hai yeh toot jata hai..
        Sahiba neendein veendein aaye na
        Raatein kaati jaye na..
        Tera hi khayal din raen aata hai.
        *******************

        *******************
        Kaisi bhala, shab hogi woh,
        Sang jo tere, dhalti hai.
        Dil ko koi, khaahish nahi,
        Teri kami khalti hai..
        Aaram na, abb aakhon ko
        Khaab bhi na badalti hai..
        Dil ko koi, khaahish nahi,
        Teri kami jana khalti hai..


        Sahiba, tu hi mera aayina,
        Hathon mein bhi mere haan,
        Tera hi naseeb aata hai.

        Sahiba neendein veendein aaye na
        Raatein kaati jaye na,
        Tera hi khayal din raen aata hai..
        Sahiba neendein veendein aaye na,
        Raatein kaati jaye na..
        Tera hi khayal din raen aata hai….."""
        ],
        "delays": [2000, 1800, 2100, 2400, 1700, 2000, 2000, 1700, 2300]
    },

    "Meherbaan": {
        "file": os.path.join(BASE, "meherbaan.mp3"),
        "lyrics": [
            """
        Ye aa ya-ya ya-ya…

        (Pre-chorus)
        Dil ki maange thodi thi kam
        Har duaa bhi thodi maddham
        Tune kaandhe pe sar jhukaaya jab
        Jaise dargah pe baandhe dhaage tab
        Bina maange hi mill gaya hai sab

        (Chorus)
        Meherbaan hua hua
        Meherbaan hua hua
        Meherbaan.. hua
        Meherbaan hua Rab  
        Meherbaan.. hua
        Meherbaan hua Rab

        (Post-Chorus)
        Duaa rang rangiya yun malang laal laal rang
        Rooh ki patang baandhi tere sang
        Tab hi toh laga
        Meherban hua Rab
        O din ye sehre sa saja
        Meherbaan huaa Rab
        Ye aa ya-ya ya-ya…


        (Verse)
        Haathon ko tere apne
        Haathon mein le leti hoon
        Ke taqdeerein apni saari padh loon
        Aankhon mein tere chhupte
        Armaan main dhoondhta hoon
        Bas tu soche, aur poore main kar doon
        Abhi abhi toh hum adhoore thhe
        Poore ho gaye tere roobaroo
        Oo.. ye bhi deekhe na
        Kahaan main khatam, kahaan tu shuru

        (Pre-Chorus)
        Aankhein teri (aankhein teri)
        Girti hain jab (girti hain jab)
        Ab to neendein aati hain tab
        Humko lagta hai kuch dino se ab
        Tu ibaadat hai, tu hi hai mazhab
        Bewajah kaise, kyu, kahaan aur kab

        (Chorus)   
        Meherban hua hua
        Meherban hua hua
        Meherban.. hua
        Meherban hua Rab
        Meherban.. hua
        Meherban hua Rab

        (Bridge)
        Rab ne banaaya sabko
        Par kaun bataaye Rab ko
        Mar ke tum pe, hum saans lete hain
        Rab se karun jo duaayein
        Ab ye tujhi tak jaayein
        Tu jo sun le toh sunta ye Rab hai..
        Jaane naa jahaan
        Jaane hai kahaan
        Mili thi meri teri haan me haan
        Sach hai yahi tujh sa kahin
        Nahin hai nahin

        (Pre-Chorus)
        Meri raahein aayein tujh tak
        Iss janam se har janam tak
        Waqt ko rokein aa zara sa ab
        Usko samjha dein ishq ka matlab
        Chhod ke zidd ye maan lega ab

        (Chorus)
        Meherbaan hua hua
        Meherbaan hua hua
        Meherbaan.. hua
        Meherbaan hua Rab
        Meherbaan.. hua
        Meherbaan hua Rab
        Meherbaan.. hua
        Meherbaan hua RaB"""

        ],
        "delays": [2000, 2000, 2000, 2000]
    }
}

# -----------------------------------
# GLOBAL STATE FOR LYRICS TYPING
# -----------------------------------
current_lyrics = []
current_delays = []
line_index = 0
char_index = 0
typing_active = False

# -----------------------------------
# AUDIO CONTROL
# -----------------------------------
def init_pygame():
    pygame.mixer.init()

def play_song(path):
    if not os.path.exists(path):
        messagebox.showerror("File Not Found", f"Could not find audio file:\n{path}")
        return False

    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)
    return True

def stop_song():
    pygame.mixer.music.stop()

# -----------------------------------
# LYRICS TYPING USING after()
# -----------------------------------
def start_lyrics(lyrics, delays, text_widget, char_delay=65):
    global current_lyrics, current_delays, line_index, char_index, typing_active

    current_lyrics = lyrics
    current_delays = delays
    line_index = 0
    char_index = 0
    typing_active = True

    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, "Lyrics:\n\n")
    text_widget.config(state="disabled")

    type_next_char(text_widget, char_delay)

def type_next_char(text_widget, char_delay):
    global line_index, char_index, typing_active

    if not typing_active:
        return

    if line_index >= len(current_lyrics):
        typing_active = False
        return

    line = current_lyrics[line_index]

    text_widget.config(state="normal")

    if char_index < len(line):
        text_widget.insert(tk.END, line[char_index])
        text_widget.see(tk.END)
        text_widget.config(state="disabled")
        char_index += 1
        text_widget.after(char_delay, lambda: type_next_char(text_widget, char_delay))
    else:
        text_widget.insert(tk.END, "\n")
        text_widget.config(state="disabled")
        delay = current_delays[line_index]
        line_index += 1
        char_index = 0
        text_widget.after(delay, lambda: type_next_char(text_widget, char_delay))

def stop_lyrics():
    global typing_active
    typing_active = False

# -----------------------------------
# GUI APPLICATION
# -----------------------------------
def create_gui():
    init_pygame()

    root = tk.Tk()
    root.title("Python Music Player")
    root.geometry("650x450")
    root.resizable(False, False)

    main_frame = ttk.Frame(root, padding=10)
    main_frame.pack(fill="both", expand=True)

    # Song selection
    ttk.Label(main_frame, text="Select Song:", font=("Arial", 11)).grid(row=0, column=0, sticky="w")

    song_names = list(songs.keys())
    selected_song = tk.StringVar(value=song_names[0])

    song_combo = ttk.Combobox(main_frame, textvariable=selected_song, values=song_names, state="readonly", width=30)
    song_combo.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    # Control buttons
    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")

    def on_play():
        stop_song()
        stop_lyrics()

        name = selected_song.get()
        data = songs[name]

        if play_song(data["file"]):
            start_lyrics(data["lyrics"], data["delays"], lyrics_text)

    def on_stop():
        stop_song()
        stop_lyrics()

    play_button = ttk.Button(button_frame, text="Play", command=on_play)
    play_button.grid(row=0, column=0, padx=5)

    stop_button = ttk.Button(button_frame, text="Stop", command=on_stop)
    stop_button.grid(row=0, column=1, padx=5)

    # Lyrics display
    ttk.Label(main_frame, text="Lyrics:", font=("Arial", 11)).grid(row=2, column=0, columnspan=2, sticky="w")

    lyrics_text = tk.Text(main_frame, width=70, height=18, wrap="word")
    lyrics_text.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")
    lyrics_text.config(state="disabled")

    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=lyrics_text.yview)
    scrollbar.grid(row=3, column=2, sticky="ns")
    lyrics_text["yscrollcommand"] = scrollbar.set

    main_frame.rowconfigure(3, weight=1)
    main_frame.columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()