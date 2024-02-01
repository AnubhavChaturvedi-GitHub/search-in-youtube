import time
import pywhatkit as kt
from Head.Mouth import speak
import random
import pyautogui as ui
import webbrowser
from Data.dlg_data.dlg import *


def youtube_search(text):
    dlg = random.choice(yt_search)
    speak(dlg)
    webbrowser.open("https://www.youtube.com/")
    time.sleep(2)
    ui.press("/")
    ui.write(text)
    s12 = random.choice(s1)
    speak( s12 )
    time.sleep(0.5)
    ui.press("enter")
    s12 = random.choice(s2)
    speak(s12)


def play_music_on_youtube(text):
    playdlg = random.choice(playsong)
    speak(playdlg)
    kt.playonyt(text)
    time.sleep(3)
    speak("playing.."+text)
    ui.press("space")

