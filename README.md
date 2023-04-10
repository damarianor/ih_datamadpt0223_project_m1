<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __ih_datamadpt0223_project_m1__

Madrid Sport Places

This project is for the Module 1 of Ironhack Data Analytics Bootcamp. 
This aspp was created for finding the closest bicimad station to a set of sport places of interest. 


To enjoy this app, you have two options:

For the school you choose, you can filter it by the closest bicimad station in meters.

For all the schools, you'll recieve by email all the schools with their closest bicimad station in meters.

Image

💻 Technology stack
SQL
Pandas
Python
Jupyter
DBeaver
💥 Core technical concepts and inspiration
The app offers you an alternative of transport, clean and healthy for moving between the school of your children and your home, work or wherever you want just introducing the name of the school. And you could use it as a finder of public schools choosing the option of all.

🔧 Configuration
import sqlalchemy from sqlalchemy import create_engine from sqlalchemy import inspect import pandas as pd import requests import re import json import math import numpy as pn import functools as ft from shapely.geometry import Point import geopandas as gpd import argparse import smtplib import imghdr from email.message import EmailMessage import os from dotenv import load_dotenv

🙈 Usage
Option 1: "one" the input should be the name of the school, and returns all the next information:

![Screenshot](Screenshot 2022-07-21 at 17.11.27.png)

Option 2: "all" returns all the schools by email:

![Screenshot](Screenshot 2022-07-21 at 17.08.51.png)

📁 Folder structure
└── project_ih_m1
    ├── trash
    |   ├── bicimad_coles.ipynb
    │   └── bicimad_colesyenfant-final.ipynb
    |   ├── bicimad_colesyenfant.ipynb
    │   └── geo_calculations.ipynb
    |   ├── bicimad_coles_escuelas.csv
    │   └── bicimad_coleyescuelas.py
    ├── mailmodule
    |   ├── mailmodule.ipnynb
    │   └── mail.py
    │
    ├── dev_notebook_.ipynb
    └── bicimad_coles_escuelas.csv
    ├── .gitignore
    └── img
    ├── .env
    ├── main.py
    └── README.md
ℹ️ Further info
[API_colegios públicos Madrid] https://datos.madrid.es/egob (/catalogo/202311-0-colegios-publicos.json)
[API escuelas infantiles Madrid] https://datos.madrid.es/egob (/catalogo/202318-0-escuelas-infantiles.json)
MySQL Online Database. The database contains information from the BiciMAD stations including their location (i.e.: latitude / longitude). In order to access the database you may need the following credentials: Server: SERVER_IP Database: BiciMAD
