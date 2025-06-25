import os

from Bilder_Verlinken import Bilder_Verlinken

# Nur für Dateien in /anime/stream
def Ordner_prüfen() -> str:
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
    return Folgen_Dateien

Bilder_Verlinken(Ordner_prüfen())
#for i in Ordner_prüfen():
#    Bilder_Verlinken(i)