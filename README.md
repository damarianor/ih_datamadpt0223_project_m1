<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __ih_datamadpt0223_project_m1__

⚽ **Madrid Sport Places**

This project is for the Module 1 of Ironhack Data Analytics Bootcamp. 
This aspp was created for finding the closest bicimad station to a set of sport places of interest. 

❓ **How to use it?**

There are two options to use and enjoy this app:

1) You can filter in meters by the closest BiciMAD station
2) You can also receive an email with the Sport Places and their closest BiciMAD stations.

- INCLUDE IMAGE

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

Option 1: "one" the input should be the name of the school, and returns all the next information:


Option 2: "all" returns all the schools by email:


📁 **Folder structure**

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
    
ℹ️ **Further info**

**SQLite Database.** The database contains information from the BiciMAD stations including their location (i.e.: latitude / longitude). You may find .db file in the data folder.
**API REST.** We will use the API REST from the Portal de datos abiertos del Ayuntamiento de Madrid, where you can find the Catálogo de datos with more than 70 datasets. The API endpoint is https://datos.madrid.es/egob.
