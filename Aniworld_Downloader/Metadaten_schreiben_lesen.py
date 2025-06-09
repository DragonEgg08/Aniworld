import os
import pathlib

Aktueller_Ordner = str(pathlib.Path().absolute())

def Metadaten_schreiben(Folgen_Metadaten, Serien_Name, Gespeicherte_Staffeln_Pfad):
    # Metadaten:
    # Staffel, Staffelnummer, Folgennummer, Folge, Name, Link

    if not os.path.exists(Gespeicherte_Staffeln_Pfad):
        os.makedirs(Gespeicherte_Staffeln_Pfad)
    Folgen_Metadaten[4] = ""
    with open(Gespeicherte_Staffeln_Pfad + Serien_Name + "_" + str(Folgen_Metadaten[1]), encoding="UTF-8", mode="a") as file:
        file.write(
            f"{Folgen_Metadaten[0]}/{Folgen_Metadaten[1]}\n")

        for i in range(2,6):
            if i != 4:
                for a in range(len(Folgen_Metadaten[2])):
                    if a == len(Folgen_Metadaten[2])-1:
                        file.write(str(Folgen_Metadaten[i][a]))
                    else:
                        file.write(str(Folgen_Metadaten[i][a]) + ";")
            file.write("\n")

def Metadaten_lesen(Dateiname, Gespeicherte_Staffeln_Pfad):
    with open(Gespeicherte_Staffeln_Pfad+ Dateiname) as file:
        # Staffel, Staffelnummer, Folgennummer, Folge, Name, Link
        Folgen_Metadaten = [[], [], [], [], [], [], []]
        Inhalt_Datei = file.read().split("\n")
        Folgen_Metadaten[0] = Inhalt_Datei[0].split("/")[0]
        Folgen_Metadaten[1] = int(Inhalt_Datei[0].split("/")[1])
        Folgen_Metadaten[6] = Inhalt_Datei[5]

        for i in range(len(Inhalt_Datei[1].split(";"))):
            Folgen_Metadaten[2].append(Inhalt_Datei[1].split(";")[i])
            Folgen_Metadaten[3].append(Inhalt_Datei[2].split(";")[i])
            Folgen_Metadaten[5].append(Inhalt_Datei[4].split(";")[i])
    return Folgen_Metadaten