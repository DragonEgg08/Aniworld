from selenium.webdriver.common.by import By
import main_Unterprogramme

Staffelsucher_XPATH = "/html/body/div/div[2]/div[2]/div[2]/ul[1]/li["

#Web_Grabbler == Selenium-Driver

def Staffeln_Suchen(URL, Linux):
    Web_Grabbler = main_Unterprogramme.Selenium_vorbereiten(Linux, False)
    Web_Grabbler.get(URL)
    Staffel_Speicher = []
    while True:
        try:
            Serien_Name = Web_Grabbler.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/section/div[2]/div[2]/div[1]/h1/span").text
            if Serien_Name != "":
                break
        except:
            None

    for i in range(2, 9999):
        try:
            Staffel_Speicher.append(Web_Grabbler.find_element(By.XPATH, Staffelsucher_XPATH + str(i) + "]").text)
        except:
            break
    Web_Grabbler.close()
    return Staffel_Speicher, Serien_Name


def Folgen_Suchen(URL, Staffeln_zum_Downloaden, Index_Staffel, Folgen_Metadaten, Linux, Filme):
    Web_Grabbler = main_Unterprogramme.Selenium_vorbereiten(Linux, True)
    Web_Grabbler.get(URL)

    Folgensucher_XPATH = "/html/body/div/div[2]/div[2]/div[3]/table/tbody/tr["

    if not Filme:
        Index_Staffel -= 1

    if type(Staffeln_zum_Downloaden) != "<class 'list'>":
        Web_Grabbler.find_element(By.XPATH, Staffelsucher_XPATH + str(Index_Staffel) + "]/a").click()
        # Metadaten:
        # Staffel, Staffelnummer, Folgennummer, Name, Link, Nachhergehender Videoza_Link

        for i in range(1, 9999):
            try:
                XPATH_Folge = Folgensucher_XPATH + str(i) + "]"
                Folgenname = Web_Grabbler.find_element(By.XPATH, XPATH_Folge + "/td[2]/a/strong").text
                if Folgenname != "":
                    Folgen_Metadaten[3].append(Folgenname)
                else:
                    Folgen_Metadaten[3].append(Web_Grabbler.find_element(By.XPATH, XPATH_Folge + "/td[2]/a/span").text)
                Folgen_Metadaten[4].append(
                    Web_Grabbler.find_element(By.XPATH, XPATH_Folge + "/td[3]/a").get_attribute("href"))
                Folgen_Metadaten[2].append(i)
            except:
                break
        Web_Grabbler.close()
        return Folgen_Metadaten


def Videoza_Link_Suchen(Folgen_Metadaten, Linux):
    Web_Grabbler = main_Unterprogramme.Selenium_vorbereiten(Linux, True)
    Temporäre_Folgen_Links = []

    Hoster_Auswahl = ""
    # Metadaten:
    # Staffel, Staffelnummer, Folgennummer, Name, Link, Nachhergehender Videoza_Link

    print("Die Aniworld-Folgenlinks werden gelesen...")
    for i in range(len(Folgen_Metadaten[4])):
        print(str(i) + "/" + str(len(Folgen_Metadaten[2])))
        Web_Grabbler.get(Folgen_Metadaten[4][i])
        Zwei_Sprachen = False
        try:
            Web_Grabbler.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[3]/div[5]/div[1]/div/img[3]")
        except:
            if Web_Grabbler.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[3]/div[5]/div[1]/div/img[1]").get_attribute("title") != "Deutsch":
                Zwei_Sprachen = True

        #Um bestimmte Hoster zu suchen
        Hoster = []
        for a in range(1,999999):
            try:
                Temp_Hoster = Web_Grabbler.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[{a}]/div/a/h4").text
                if Temp_Hoster != "":
                    Hoster.append(Temp_Hoster)
            except:
                break
        if Hoster_Auswahl == "":
            Temp_Hoster_Auswahl = input(f"Es wurden folgende Hoster gefunden: {Hoster}: ")
            if Temp_Hoster_Auswahl in Hoster:
                Hoster_Auswahl = Temp_Hoster_Auswahl
        while True:
            if Temp_Hoster_Auswahl in Hoster:
                if not Zwei_Sprachen:
                    Temporäre_Folgen_Links.append(Web_Grabbler.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[{Hoster.index(Hoster_Auswahl)+1}]/div/a").get_attribute("href"))
                else:
                    Temporäre_Folgen_Links.append(Web_Grabbler.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[{Hoster.index(Hoster_Auswahl)+len(Hoster)}]/div/a").get_attribute("href"))
                break
            print("Bitte einen vorhandenen Hoster auswählen\n")
    print("Die Folgenlinks des Streaminganbieters werden gelesen...")
    for i in range(len(Temporäre_Folgen_Links)):
        print(str(i) + "/" + str(len(Folgen_Metadaten[2])))
        Web_Grabbler.get(Temporäre_Folgen_Links[i])
        Folgen_Metadaten[5].append(Web_Grabbler.current_url)
    Web_Grabbler.close()
    return Folgen_Metadaten
