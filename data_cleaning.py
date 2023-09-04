!git clone https://github.com/chippymint/Project129

import pandas as pd

final_stars_df = pd.read_csv("Projects/Project 127/scraper.py")
print(final_stars_df.shape)

final_stars_df.head()
final_stars_df.columns
final_stars_df.drop(columns=['Luminosity'], inplace=True)
final_stars_df.dropna()
print(final_stars_df.shape)

final_stars_df = final_stars_df.rename({
    'pl_hostname' : "solar_system_name",
    'pl_discmethod' : "planet_discovery_method",
    'st_mass' : "host_mass",
    'st_teff' : "host_temperature",
    'st_rad' : "host_radius"

}, axis='columns')

final_stars_df.head(5)

final_stars_df.to_csv('main.csv')
from google.colab import files
files.download('main.csv')