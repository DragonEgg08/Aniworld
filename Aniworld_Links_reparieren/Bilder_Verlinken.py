def Bilder_Verlinken(Original_Datei):
    Datei = open(Original_Datei, encoding="UTF-8").read().split('data-src="/')

    with open(Original_Datei, "w", encoding="UTF-8") as file:
        for i in range(len(Datei)):
            file.write(Datei[i] + 'data-src="')