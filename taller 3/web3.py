# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:20:07 2024

@author: hugos
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import numpy as np
from selenium.webdriver.common.by import By
import json


url =  "https://www.metrocuadrado.com/arriendo/bogota/chapinero"

lista_links = []
#### SELENIUM

driver = webdriver.Chrome()
driver.get(url)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

for i in range(19):
    # Encuentra enlaces
    links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "sc-gPEVay")]//a'))
    )
    href = [link.get_attribute("href") for link in links if link.get_attribute("href") is not None]
    urls_filtradas = [url for url in href if '/inmueble' in url]
    lista_links.extend(urls_filtradas)  # Extiende en lugar de append para evitar listas anidadas
   
    # Encuentra y haz clic en el botón "Next"
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Next']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        next_button.click()
    except Exception as e:
        print(f"No se pudo hacer clic en el botón Next: {e}")
        break

lista_links = pd.unique(lista_links).tolist()

## Extraer los datos de cada apartamento

url_apto=lista_links[7]

r = requests.get(url_apto)

soup = BeautifulSoup(r.content)

prueba = soup.find_all(attrs={"id":"__NEXT_DATA__"})

contenido = prueba[0].contents[0]

datos_apto = json.loads(contenido)

datos_apto.keys()

url_apto