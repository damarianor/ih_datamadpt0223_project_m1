import pandas as pd
import numpy as np
import requests
import duckdb
from shapely.geometry import Point
import sqlalchemy
import IPython
from dotenv import load_dotenv
import json
from urllib.request import urlopen
import geopandas as gpd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', help= " '-a all' (Get the closest bike station for all sport places in Madrid)\n '-a select' (Select a set of bike stations from Madrid's database) ")
    parser.add_argument('-c', '--singleSportPlace', help= " Get the closest bike station to the sport place\n Example: '-c Campo de Golf del Centro Nacional de Golf")
    args = parser.parse_args()
    variables = vars(args)
    
    conn = duckdb.connect('../data/bicimad.db')
    database = conn.execute('SELECT * from bicimad_stations').fetch_df()
    bicimad = database.copy()
    bicimad["Type of Place"] = "Principales espacios de deporte"
    bicimad["Longitude"] = bicimad["geometry.coordinates"].apply(lambda geo: str(geo).replace("[","").replace("]","").split(",")[0].strip())
    bicimad["Latitude"] = bicimad["geometry.coordinates"].apply(lambda geo: str(geo).replace("[","").replace("]","").split(",")[1].strip())
    bicimad_final = bicimad[['name', 'address', 'Type of Place', 'Longitude', 'Latitude']]
    
    url = 'https://datos.madrid.es/egob/catalogo/212808-0-espacio-deporte.json' 
    headers = {'Accept': 'application/json'}
    espacios_json = requests.get(url, headers=headers).json()
    espacios_fd = pd.json_normalize(espacios_json, ['@graph'])
    espacios_final = espacios_fd[['title', 'location.latitude', 'location.longitude', 'address.street-address']]
    tabla_final = espacios_final.assign(key=1).merge(bicimad_final.assign(key=1), how='outer', on='key').reset_index(drop=True)
    
    def distance_meters(Latitude1, Longitude1, Latitude, Longitude):
        # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
        start = to_mercator(Latitude1, Longitude1)
        finish = to_mercator(Latitude, Longitude)
        return start.distance(finish)

    def to_mercator(lat, long):
        #transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
        c = gpd.GeoSeries([Point(lat, long)], crs=4326)
        c = c.to_crs(3857)
        return c

    tabla_final['Longitude'] = tabla_final['Longitude'].astype(float)
    tabla_final['Latitude'] = tabla_final['Latitude'].astype(float)
    tabla_final.rename(columns={'location.latitude':'Latitude1', 'location.longitude':'Longitude1'}, inplace=True)
    tabla_final['Distance'] = tabla_final.apply(lambda x: distance_meters(x["Latitude1"], x["Longitude1"], x["Latitude"], x["Longitude"]), axis=1)
    tabla_final.rename(columns={'title':'Place of interest', 'address.street-address':'Place Address', 'name':'BiciMAD Station', 'address':'Station Location'}, inplace=True)
    tabla_final = tabla_final[['Place of interest', 'Type of Place', 'Place Address', 'BiciMAD Station', 'Station Location', 'Distance']]
    tabla_final_sorted = tabla_final.sort_values(by=['Place of interest', 'Distance'])
    grouped = tabla_final_sorted.groupby('Place of interest')
    resultado_final = grouped.head(1)
    csv = resultado_final.to_csv('./main_challenge.csv', index=False)

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--all', action='store_true', help="Get the closest bike station for all sport places in Madrid")
parser.add_argument('-p', '--place', help="Select a specific sport place to find the closest bike station")

args = parser.parse_args()

if args.all:
    for index, row in espacios_final.iterrows():
        place = row['title']
        latitude = row['location.latitude']
        longitude = row['location.longitude']
        closest_station = tabla_final_sorted.loc[tabla_final_sorted['Place of interest'] == place].iloc[0]['BiciMAD Station']
        distance = tabla_final_sorted.loc[tabla_final_sorted['Place of interest'] == place].iloc[0]['Distance']
        print(f"The closest BiciMAD station to all the sport places at a distance of {round(distance,2)} meters.")
elif args.place:
    place = args.place
    closest_station = tabla_final_sorted.loc[tabla_final_sorted['Place of interest'] == place].iloc[0]['BiciMAD Station']
    distance = tabla_final_sorted.loc[tabla_final_sorted['Place of interest'] == place].iloc[0]['Distance']
    print(f"The closest BiciMAD station to {place} is {closest_station}, at a distance of {round(distance,2)} meters.")
else:
    print(f'ERROR! No sé que está mal')
