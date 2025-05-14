import subprocess
import pathlib

def Download(Folgen_Metadaten, Bestimmte_Folgen, Download_Ordner, Linux):
    # Metadaten:
    # Staffel, Staffelnummer, Folgennummer, Name, Link, Nachhergehender Videoza_Link
    Bestimmte_Folgen_Leer = False
    Aktueller_Pfad = pathlib.Path().absolute()

    if Bestimmte_Folgen == "":
        Bestimmte_Folgen_Leer = True

    for i in range(len(Folgen_Metadaten[5])):
        if Bestimmte_Folgen_Leer or int(Bestimmte_Folgen[0]) - 1 <= i <= int(Bestimmte_Folgen[1]) - 1:
            # Syntax yt-dlp:
            # -o: Output-Filename; -P: Output-Path;

            if not Linux:
                subprocess.run(
                    f'"Aniworld_Downloader/yt-dlp.exe" --external-downloader "Aniworld_Downloader/aria2c.exe" --external-downloader-args "-x 16 -s 16 -k 1M" {Folgen_Metadaten[5][i]} '
                    f'-o "{Folgen_Metadaten[0]} S{Folgen_Metadaten[1]} F{Folgen_Metadaten[2][i]} {chr(39) + Folgen_Metadaten[3][i] + chr(39)}.mp4" -P "{Download_Ordner}"', cwd=Aktueller_Pfad)
            else:
                try:
                    subprocess.run(
                        f'yt-dlp --external-downloader aria2c --external-downloader-args "-x 16 -s 16 -k 1M" {Folgen_Metadaten[5][i]} '
                        f'-o "{Folgen_Metadaten[0]} S{Folgen_Metadaten[1]} F{Folgen_Metadaten[2][i]} {chr(39) + Folgen_Metadaten[3][i] + chr(39)}.mp4" -P "{Download_Ordner}"', shell=True)
                except:
                    print("Bitte installiere yt-dlp, aria2c und chromium-browser")