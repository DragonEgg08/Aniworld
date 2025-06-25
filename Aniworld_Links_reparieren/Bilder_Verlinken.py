def Bilder_Verlinken(Dateien: list):

    count = 0
    for i in Dateien:
        count += 1
        print((count/len(Dateien))*100)
        Verlinkung = ""
        if len(i.split("/")) > 1:
            for a in range(len(i.split("/")) + 2):
                Verlinkung += "../"

        Datei = open("X:/Aniworld/Aniworld/aniworld.to/anime/stream/" + i, encoding="UTF-8").read().split('data-src="/')

        with open(i, "w", encoding="UTF-8") as file:
            for i in range(len(Datei)):
                file.write(Datei[i] + f'data-src="{Verlinkung}')