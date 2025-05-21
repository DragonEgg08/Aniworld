import os


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

Ordner_prüfen()