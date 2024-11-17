

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import numpy as np
from selenium.webdriver.common.by import By


url =  "https://www.metrocuadrado.com/apartamento/arriendo/chapinero"


#### SELENIUM

driver = webdriver.Edge()
driver.get(url)

links1 = driver.find_elements(By.XPATH, '//li[contains(@class, "sc-gPEVay")]//a')  # Asegúrate de apuntar a los elementos <a>
href1 = [link.get_attribute("href") for link in links1]  # Extrae los atributos href
print(href1)



resultado = list(set(filter(lambda x: x is not None, href1)))
urls_filtradas = [url for url in resultado if '/inmueble' in url]
ultimos_segmentos = [url.rsplit('/', 1)[-1] for url in urls_filtradas]

"MC5297645" in ultimos_segmentos



