import os
import re

def Metadaten_lesen(Datei):
    with open(Datei) as file:
        # Staffel, Staffelnummer, Folgennummer, Folge, Name, Link
        Folgen_Metadaten = [[], [], [], [], [], [], []]
        Inhalt_Datei = file.read().split("\n")
        Folgen_Metadaten[0] = Inhalt_Datei[0].split("/")[0]
        Folgen_Metadaten[1] = int(Inhalt_Datei[0].split("/")[1])
        Folgen_Metadaten[6] = Inhalt_Datei[5]

        for i in range(len(Inhalt_Datei[1].split(";"))):
            Folgen_Metadaten[2].append(Inhalt_Datei[1].split(";")[i])
            Folgen_Metadaten[3].append(Inhalt_Datei[2].split(";")[i])
            #Folgen_Metadaten[5].append(Inhalt_Datei[4].split(";")[i])
    return Folgen_Metadaten

Metadaten = input("Bitte Datei mit absolutem Pfad eingeben: ")
if '"' in Metadaten:
    Metadaten = Metadaten.replace('"', "")
Metadaten = Metadaten_lesen(Metadaten)

Pfad_Folgen = input("Bitte den Ordner der Folgen, die umbenannt werden sollen eingeben: ")
if '"' in Pfad_Folgen:
    Pfad_Folgen = Pfad_Folgen.replace('"', "")

Folgen = os.listdir(Pfad_Folgen)
#von hier
def extrahiere_zahl(text):
    match = re.search(r'\d+', text)
    if match:
        return int(match.group(0))
    else:
        return 0
Sortierte_Folgen = sorted(Folgen, key=extrahiere_zahl)
#bis hier: Ai-Generated


if len(Folgen[0].split("Folge")) > 1:
    for i in range(len(Folgen)):
        os.rename(f"{Pfad_Folgen}/{Sortierte_Folgen[i]}" , f"{Pfad_Folgen}/{Metadaten[0]} S{Metadaten[1]} F{Metadaten[2][i]} '{Metadaten[3][i]}'.mp4")
else:
    #für die Folgen mit S1F1-Benennung
    pass