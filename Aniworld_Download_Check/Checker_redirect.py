import os
import subprocess


def Ordner_prüfen():
    Folgen_Dateien = []
    Pfad = "X:/Aniworld/aniworld.to/anime/stream/"
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
    Pfad = "X:/Aniworld/aniworld.to/anime/stream/"
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
        except UnicodeDecodeError:
            Zähler_Fehler += 1
    redirects_checken(Redirects)

def redirects_checken(Redirects):
    Redirects_Anzahl_Vorher = len(Redirects)
    Redirects_Vorhanden = os.listdir("X:/Aniworld/aniworld.to/redirect")
    Fehler = 0
    Zähler = 0
    for i in range(Zähler, len(Redirects_Vorhanden)):
        Zähler = i
        print("Redirects checken: " + str(int(i/len(Redirects_Vorhanden)*100)) + "%")
        i = Redirects_Vorhanden[i]
        try:
            Redirects.remove(i)
        except ValueError:
            Fehler += 1
    with open("X:/redirects", "w") as file:
        for i in Redirects:
            file.write(i + "\n")
    redirects_nachladen(Redirects)

def redirects_nachladen(Redirects):
    len(Redirects)
    for i in range(len(Redirects)):
        print("Redirects runterladen:", round(i/len(Redirects)*100, 3), "%")
        subprocess.run(["cmd.exe", "/c", f"X: && cd redirects nachladen && wget https://aniworld.to/redirect/{Redirects[i]}"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

Redirects = []
if True:
    with open("X:/redirects", "r") as file:
        Redirects = file.read().split("\n")
    redirects_nachladen(Redirects)
else:
    Ordner_prüfen()