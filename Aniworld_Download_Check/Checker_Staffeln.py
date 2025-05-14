import os.path
from selenium.webdriver.common.by import By

def Staffeln_Suchen(webdriver):
    webdriver.get("https://aniworld.to/animes")
    Staffeln = []

    for i in range(1, 99999999999):
        try:
            webdriver.find_element(By.XPATH, f"/html/body/div/div[2]/div[4]/div[{i}]")
        except:
            break
        for a in range(1, 9999999999):
            print(str(i) + "-" + str(a))
            try:
                Staffeln.append(webdriver.find_element(By.XPATH, f"/html/body/div/div[2]/div[4]/div[{i}]/ul/li[{a}]/a").get_attribute("href").split("/")[-1])
            except:
                break
    with open("Staffeln_gefunden", "w") as file:
        for i in Staffeln:
            file.write(i + "\n")
    Staffeln_Prüfen(Staffeln)

def Staffeln_Prüfen(Staffeln):
    Fehlende_Staffeln = []

    for i in Staffeln:
        if not os.path.exists(f"X:\\Aniworld\\aniworld.to\\anime\\stream\\{i}"):
            Fehlende_Staffeln.append(i)

    with open("Staffeln_Fehlend", "w") as file:
        for i in Fehlende_Staffeln:
            file.write(i + "\n")