<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# DATA MAD PT 0223 PROJECT_M1

⚽ **Madrid Sport Places**

This project is for the Module 1 of Ironhack Data Analytics Bootcamp. 
This aspp was created for finding the closest bicimad station to a set of sport places of interest. 

❓ **How to use it?**

There are two options to use and enjoy this app:

1) You can get the closest bike station for all sport places in Madrid
2) You can also the closest bike station for an specific sport place. 

💻 **Technology used:**

- SQL
- Pandas
- Python
- Jupyter Notebook
- DBeaver

⏳ **CODE**

- **import** pandas **as** pd
- **import** numpy **as** np
- **import** requests
- **import** duckdb
- **from** shapely.geometry **import** Point
- **import** sys
- **import** sqlalchemy
- **import** IPython
- **from** dotenv **import** load_dotenv
- **import** json
- **from** urllib.request **import** urlopen
- **import** geopandas **as** gpd

💥 Core technical concepts and inspiration


✔ **Examples**

Option 1: The input should be the name of each sport place and the closest BiciMAD station.

Option 2: The input should be the specific sport place and its closest BiciMAD station.

📁 **Folder structure**


└── ih_datamadpt0223_project_m1

    ├── data
    |   ├── bicimad_stations.csv
    │   └── bicimad.db
    |   ├── espacio-deporte.csv
    │   └── geo_calculations.ipynb
    |   ├── bicimad_coles_escuelas.csv
    │   └── bicimad_coleyescuelas.py
    ├── modules
    |   ├── geo_calculations.py   
    │
    ├── notebooks
    │   ├── dev_notebook_.ipynb
    │   ├── bicimad.db
    |   ├── main.py
    |   ├── notebook.ipynb
    ├── p_acquisition
    |   ├── m_acquisition.ipynb
    │   ├── m_acquisition.py
    |   ├── main.py
    |
    └── README.md
    
ℹ️ **Further info**

**SQLite Database.** The database contains information from the BiciMAD stations including their location (i.e.: latitude / longitude). You may find .db file in the data folder.

**API REST.** We will use the API REST from the Portal de datos abiertos del Ayuntamiento de Madrid, where you can find the Catálogo de datos with more than 70 datasets. The API endpoint is https://datos.madrid.es/egob.
