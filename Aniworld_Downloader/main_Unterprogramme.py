import os
from tkinter import filedialog


def Staffelauswahl (Staffeln):
    global Staffeln_zum_Downloaden
    Filme = False
    print("Es wurden die Staffeln: ")
    Staffeln_Auswahl = []
    for i in range(len(Staffeln)):
        if Staffeln[0] == "Filme":
            Filme = True
        Staffeln_Auswahl.append(str(i) + ". " + Staffeln[i])
        print(str(i) + ". " + Staffeln[i])

    Eingabe_Staffel = int(input("gefunden (links Staffelnummer, rechts Staffel), tippe die Nummer der Staffel ein, um sie zu downloaden (Nur die Nummer und Enter!!!): "))

    if Filme:
        Staffeln_zum_Downloaden = Eingabe_Staffel
    else:
        Staffeln_zum_Downloaden = Eingabe_Staffel + 1
    return Staffeln_zum_Downloaden, Filme

def Index_Check():
    Cache = os.getenv("LOCALAPPDATA") + "\\Aniworld-Downloader\\"
    Index = os.listdir(Cache)
    Index_split = []

    for i in Index:
        Index_split.append(i.split("_"))

def Download_Ordner_Auswahl() -> str:
    return filedialog.askdirectory(title="Ordner zum Downloaden auswählen")

def Selenium_vorbereiten(play):
    from playwright.sync_api import sync_playwright

    Browser = play.firefox.launch(headless=False)
    Seite = Browser.new_page()
    return Seite