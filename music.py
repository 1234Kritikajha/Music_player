import time
import pygame
import os

def play_song():
    pygame.mixer.init()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    song_path = os.path.join(base_dir, "sahiba.mp3")
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()   # play once, full song

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
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
    ]

    delays = [2.0, 1.8, 2.1, 2.4, 1.7, 2.0, 2.0, 1.7, 2.3]

    print("\n🎶 Now Playing: Sahiba 🎶\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

if __name__ == "__main__":
    play_song()
    print_lyrics()

    # ✅ keep program alive until song finishes
    while pygame.mixer.music.get_busy():
        time.sleep(1)
