import os

Alle_Dateien = []
def alle_dateien_rekursiv_auflisten(ordner_pfad):
  """Listet alle Dateien in einem Ordner und seinen Unterordnern auf."""
  for root, dirs, files in os.walk(ordner_pfad):
    for datei in files:
      # Hier kannst du mit jeder gefundenen Datei etwas machen,
      # z.B. den vollständigen Pfad ausgeben.
      vollstaendiger_pfad = os.path.join(root, datei)
      Alle_Dateien.append(vollstaendiger_pfad)

# Beispielaufruf:
ordner = "X:\\Aniworld wie orig"  # Ersetze dies durch den tatsächlichen Pfad
alle_dateien_rekursiv_auflisten(ordner)
with open("Umgeschriebene Dateien (in verlinkten HTMLs ändern)", "w") as file:
    for i in Alle_Dateien:
        if "." not in i:
            os.rename(i, i+".html")
            file.write(i + "\n")