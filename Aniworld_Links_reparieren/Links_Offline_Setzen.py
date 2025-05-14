def Links_Offline_Setzen(Original_Datei):
    Datei = open(Original_Datei, encoding="UTF-8").read().split('https://aniworld.to/')

    with open("index_test", "w", encoding="UTF-8") as file:
        for i in range(len(Datei)):
            file.write(Datei[i])