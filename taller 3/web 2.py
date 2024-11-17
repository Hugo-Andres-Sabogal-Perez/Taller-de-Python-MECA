

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import numpy as np
from selenium.webdriver.common.by import By


url =  "https://www.metrocuadrado.com/apartamento/arriendo/chapinero"



r = requests.get(url)

# Verificamos que todo esté ok
r.status_code == 200

# Vamos a convertirlo en un formato más amigable para Python
soup = BeautifulSoup(r.content)


# Extraigamos todos los títulos principales
# Encuentra todos los elementos <li>
links = soup.find_all("a", href=True)
[i['href'] for i in links]



#### SELENIUM

driver = webdriver.Edge()
driver.get(url)

links1 = driver.find_elements(By.XPATH, '//li[contains(@class, "sc-gPEVay")]//a')  # Asegúrate de apuntar a los elementos <a>
href1 = [link.get_attribute("href") for link in links1]  # Extrae los atributos href
print(href1)

links2 = driver.find_elements(By.XPATH, '//a[contains(@class, "sc-bdVaJa")]')  # Asegúrate de apuntar a los elementos <a>
hrefs2 = [link.get_attribute("href") for link in links2]  # Extrae los atributos href
print(hrefs2)


resultado = list(set(filter(lambda x: x is not None, hrefs2)))

urls_filtradas = [url for url in resultado if '/inmueble' in url]

ultimos_segmentos = [url.rsplit('/', 1)[-1] for url in urls_filtradas]

"MC5297645" in ultimos_segmentos
