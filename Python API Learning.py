from arcgis.gis import GIS
my_gis = GIS()
m = my_gis.map()
m

# Import packages
from arcgis.gis import GIS

# Create variable to hold package data
gis = GIS()

# create variable to hold query 
webmap_search = gis.content.search(
    query="LA Parks and Trails Map (styled) tags:tutorial owner:esri_devlabs",
    item_type="Web Map"
)
# query using variable
webmap_search

# Create variable and add webmap_search query into array
webmap_item = webmap_search[0]
# Initialize array
webmap_item

# Import WebMap module
from arcgis.mapping import WebMap

# Create variable for webmap containing webmap_item array
nan_park_trails = WebMap(webmap_item)
# Initialize
nan_park_trails

# Import Module
from arcgis.gis import GIS

# Variable for public ID data
trailheads_id = "883cedb8c9fe4524b64d47666ed234a7"

# Connection to ArcGIS Online
gis = GIS()

# Access the GIS item data
trailheads_item = gis.content.get(trailheads_id)
trailheads_item

# Create map
m = gis.map()
m.add_layer(trailheads_item)
m

# Center Map
m.center = [34.09042, -118.71511]  # [latitude, longitude]
m.zoom = 11



# Import modules
from arcgis.gis import GIS
from pathlib import Path
from zipfile import ZipFile

# Connect to ArcGIS Online

gis = GIS()

# `ContentManager.get` will return `None` if there is no Item with ID `a04933c045714492bda6886f355416f2`
public_data_item_id = 'a04933c045714492bda6886f355416f2'
data_item = gis.content.get(public_data_item_id)
data_item

# configure where to save data, and where the ZIP file is located
data_path = Path('./data')
if not data_path.exists():
    data_path.mkdir()
zip_path = data_path.joinpath('LA_Hub_Datasets.zip')
extract_path = data_path.joinpath('LA_Hub_datasets.zip')
data_item.download(save_path=data_path)

# Get the ZIP file from the zip_path variable, unzip data from it
zip_file = ZipFile(zip_path)
zip_file.extractall(path=data_path)


files = [file.name for file in extract_path.glob('*')]
files


from arcgis.gis import GIS
import getpass

# Using getpass to sign into ArcGIS with password prompt
gis = GIS(
    url="https://www.arcgis.com",
    username="abrownj1996",
    password=getpass.getpass("Enter password:")
)

# Keypair values for property descriptions
trailhead_properties = {
    "title": "Trailheads",
    "description": "trailheads imported from csv file",
    "tags": "LA trailheads"
}

# create path for csv data to live and add the data
csv_file = './data/LA_Hub_datasets/LA_Hub_datasets/Trailheads.csv'
csv_item = gis.content.add(trailhead_properties, csv_file)

trailhead_service = csv_item.publish()
trailhead_service







