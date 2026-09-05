
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")

empleos = soup.find_all("div", class_="card-content")

datos = []

for empleo in empleos:

    puesto = empleo.find("h2").text.strip()
    empresa = empleo.find("h3").text.strip()
    ubicacion = empleo.find("p", class_="location").text.strip()
    fecha = empleo.find("time")["datetime"]
    enlace = empleo.find_all("a")[1]["href"]

    datos.append({
        "puesto": puesto,
        "empresa": empresa,
        "ubicacion": ubicacion,
        "fecha_publicacion": fecha,
        "enlace": enlace
    })

df = pd.DataFrame(datos)

df.to_csv("empleos_fake_jobs.csv", index=False, encoding="utf-8")

print("Scraping exitoso y archivo empleos_fake_jobs.csv creado.")
