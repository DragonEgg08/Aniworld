import os.path
import Anime_Grabbler
import Folgen_Download
import main_Unterprogramme
import Metadaten_schreiben_lesen

Linux = False
if input("Linux? [J/N]: ").lower() == "j":
    Linux = True

print("Ordner wählen...")
Download_Ordner = main_Unterprogramme.Download_Ordner_Auswahl()
URL = input("Gib den Link der Serie ein: ")
Staffeln, Serien_Name = Anime_Grabbler.Staffeln_Suchen(URL, Linux)
Serien_Name = Serien_Name.split(":")[0]

# Staffel auswählen
Staffel_ausgewählt, Filme = main_Unterprogramme.Staffelauswahl(Staffeln)

#       0            1             2             3       4      5          6             7
# Staffelname, Staffelnummer, Folgennummer, Folgenname, Name, Link, Nachhergehender Streaming-Link
Folgen_Metadaten = [Serien_Name, Staffel_ausgewählt, [], [], [], []]
Gespeicherte_Staffeln_Pfad = ""
if not Linux:
    Gespeicherte_Staffeln_Pfad = os.getenv("LOCALAPPDATA") + "\\Aniworld-Downloader\\"
else:
    Gespeicherte_Staffeln_Pfad = "/home/" + os.getlogin() + "/Aniworld-Downloader/"
if os.path.exists(Gespeicherte_Staffeln_Pfad + Serien_Name + "_" + str(Staffel_ausgewählt)):
    print("Metadaten im Cache gefunden, überspringe erneute Erkennung")
    Folgen_Metadaten = Metadaten_schreiben_lesen.Metadaten_lesen(Serien_Name + "_" + str(Staffel_ausgewählt), Gespeicherte_Staffeln_Pfad)

else:
    Index_Staffeln = Staffel_ausgewählt+2

    for m in range(10):
        print()
    Folgen_Metadaten = Anime_Grabbler.Videoza_Link_Suchen(
        Anime_Grabbler.Folgen_Suchen(URL, Staffel_ausgewählt, Index_Staffeln, Folgen_Metadaten, Linux, Filme), Linux)
    Metadaten_schreiben_lesen.Metadaten_schreiben(Folgen_Metadaten, Serien_Name, Gespeicherte_Staffeln_Pfad)

# Prüft die Eingabe des Benutzers für Folgennummern
while True:
    Bestimmte_Folgen = input(f"Möchtest du bestimmte Folgen runterladen? (1-{len(Folgen_Metadaten[2])}): ")
    if Bestimmte_Folgen == "":
        break
    else:
        Bestimmte_Folgen = Bestimmte_Folgen.split("-")
    if int(Bestimmte_Folgen[0]) < 0 or int(Bestimmte_Folgen[1]) > len(Folgen_Metadaten[2]):
        print("Folgennummern müssen zwischen 1 und", len(Folgen_Metadaten[2]), "liegen.")
    else:
        break
# Download der Folgen starten
Folgen_Download.Download(Folgen_Metadaten, Bestimmte_Folgen, Download_Ordner, Linux)
