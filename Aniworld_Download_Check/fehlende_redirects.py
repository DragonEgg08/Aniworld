import os
from asyncio.windows_events import INFINITE

from selenium.webdriver.support.color import RGB_PATTERN


def Ordner_prüfen():
    Folgen_Dateien = []
    Pfad = "X:/Aniworld/Aniworld/aniworld.to/anime/stream/"
    Ordner = os.listdir(Pfad)
    for i in Ordner:
        if not os.path.isdir(Pfad + i):
            Ordner.remove(i)
    while True:
        print("Ord: " + str(len(Ordner)))
        print("Re: " + str(len(Folgen_Dateien)))
        for i in Ordner:
            if os.path.isdir(Pfad + i):
                for a in os.listdir(Pfad + i): Ordner.append(i + "/" + a)
                Ordner.remove(i)
            else:
                Ordner.remove(i)
                Folgen_Dateien.append(i)
        if len(Ordner) == 0:
            break
    redirect_speichern(Folgen_Dateien)

def redirect_speichern(Dateien):
    Pfad = "X:/Aniworld/Aniworld/aniworld.to/anime/stream/"
    Redirects = []
    Redirects_Temp = []
    Zähler_Fehler = 0
    Zähler = 0
    for i in range(Zähler, len(Dateien)):
        i = Dateien[i]
        Zähler += 1
        print("Redirects extrahieren: " + str(int(Zähler / len(Dateien) * 100)) + "%")
        try:
            for a in open(Pfad + i, "r", encoding="UTF-8").read().split('"'):
                if "redirect" in a:
                    if a not in Redirects_Temp:
                        Redirects_Temp.append(a)
            for s in Redirects_Temp:
                Redirects_Temp.remove(s)
                s = s.split("/")[-1]
                Redirects.append(s)
        except:
            Zähler_Fehler += 1
    with open("X:/redirects_fehlend.txt", "w") as file:
        for i in Redirects:
            file.write(i + "\n")

def redirects_zu_echten_Links():
    from selenium import webdriver
    Redirects = []
    with open("X:/redirects_fehlend.txt", "r") as file:
        Redirects = file.read().split("\n")

    Redirect_Temp = []

    for i in Redirects:
        try:
            if i.split(".")[1] != "html":
                Redirect_Temp.append(i)
        except IndexError:
            Redirect_Temp.append(i)
    Redirects = Redirect_Temp
    print(len(Redirects))
    Links_Echt = []


    driver = webdriver.Chrome()

    Speichern = 10

    Segmente_Downloaded = 0

    for i in os.listdir("X:/links_echt"):
        Temp = int(i.split("_")[-1])
        if Temp > Segmente_Downloaded:
            Segmente_Downloaded = Temp

    if not os.path.exists("X:/links_echt"):
        os.makedirs("X:/links_echt")

    for i in range(len(Redirects)):
        if Segmente_Downloaded != 0 and int(i/Speichern) > Segmente_Downloaded:
            driver.get(f"https://aniworld.to/redirect/{Redirects[i]}")
            Links_Echt.append(Redirects[i] + "=" + driver.current_url)
            if len(Links_Echt) == Speichern:
                print(str(round(i / len(Redirects) * 100, 3)) + f"% | {int(i/Speichern)} Dateien")
                with open(f"X:/links_echt/links_echt_{int(i/Speichern)}", "w") as file:
                    for a in Links_Echt:
                        file.write(a + "\n")
                Links_Echt = []

def redirects_überprüfen():
    Segmente_Downloaded = 0
    for i in os.listdir("X:/links_echt"):
        Temp = int(i.split("_")[-1])
        if Temp > Segmente_Downloaded:
            Segmente_Downloaded = Temp

    Redirects_Fehlend_Bisher = open("X:/redirects_fehlend.txt").read().split("\n")
    Redirects_Gefunden_Dateien = os.listdir("X:/links_echt")
    Anzahl_Bevor = len(Redirects_Fehlend_Bisher)
    print("wird überprüft...")

    for i in range(INFINITE):
        print("Fortschritt: " + str(round(i/Segmente_Downloaded*100, 2)) + "%")
        try:
            Redirects_Runtergeladen = open(f"X:/links_echt/links_echt_{i}").read().split("\n")
        except FileNotFoundError:
            break

        for a in Redirects_Runtergeladen:
            if a.split("=")[0] in Redirects_Fehlend_Bisher:
                Redirects_Fehlend_Bisher.remove(a.split("=")[0])

    Anzahl_Danach = len(Redirects_Fehlend_Bisher)
    print(f"{Anzahl_Bevor-Anzahl_Danach} runtergeladen von {Anzahl_Bevor}")
    print("Bei " + str((round(Anzahl_Bevor-Anzahl_Danach)/Anzahl_Bevor*100, 2)) + "%")
    input()



while True:
    I = input("prüfen oder laden?: ")
    if I == "prüfen":
        redirects_überprüfen()
        break
    elif I == "laden":
        redirects_zu_echten_Links()
        break

#redirects_zu_echten_Links()
#Ordner_prüfen()
#redirects_überprüfen()