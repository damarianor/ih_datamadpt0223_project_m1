import duckdb
import pandas as pd
import requests

def get_bicimad():
    conn = duckdb.connect('../data/bicimad.db')
    database = conn.sql("SELECT * from bicimad_stations")
    bicimad = database.df()
    return bicimad

url = 'https://datos.madrid.es/egob/catalogo/212808-0-espacio-deporte.json'

def get_espacios_deporte(url):
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    espacios_json = response.json()
    espacios_fd = pd.json_normalize(espacios_json, ['@graph'])
    espacios_final = espacios_fd[['title', 'location.latitude', 'location.longitude', 'address.street-address']]
    return espacios_final