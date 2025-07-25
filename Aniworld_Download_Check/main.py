import os
from selenium import webdriver
import Checker_Staffeln

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

Staffeln = []

if not os.path.exists("Staffeln_gefunden"):
    Checker_Staffeln.Staffeln_Suchen(webdriver)
else:
    Checker_Staffeln.Staffeln_Prüfen(open("Staffeln_gefunden").read().split("\n"))