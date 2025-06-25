import os.path
from asyncio.windows_events import INFINITE
from playwright.sync_api import sync_playwright as play


def Staffeln_Suchen():
    with play() as p:
        Browser = p.firefox.launch(headless=False)
        Seite = Browser.new_page()
        Seite.goto("https://aniworld.to/animes")
        Staffeln = []

        for i in range(1, INFINITE):
            try:
                Seite.locator(f"xpath=/html/body/div/div[2]/div[4]/div[{i}]/div/h3").text_content(timeout=1000)
            except:
                break

            for a in range(1, INFINITE):
                print(str(i) + "-" + str(a))
                try:
                    Link = Seite.locator(f"xpath=/html/body/div/div[2]/div[4]/div[{i}]/ul/li[{a}]/a").get_attribute("href", timeout=500)
                    Staffeln.append(Link)
                except:
                    break

        print(len(Staffeln))
        with open("X:/Staffeln_gefunden", "w") as file:
            for i in Staffeln:
                file.write(i + "\n")

def Staffeln_Prüfen(Staffeln):
    Fehlende_Staffeln = []

    for i in Staffeln:
        if not os.path.exists(f"X:/Aniworld_Datenbank-update/Aniworld/aniworld.to{i}"):
            Fehlende_Staffeln.append(i)

    with open("X:/Staffeln_Fehlend", "w") as file:
        for i in Fehlende_Staffeln:
            file.write(i + "\n")
#Staffeln_Suchen()
Staffeln = open("X:/Staffeln_gefunden", "r").read().split("\n")
Staffeln_Prüfen(Staffeln)