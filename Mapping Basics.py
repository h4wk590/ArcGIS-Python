#!/usr/bin/env python
# coding: utf-8

# # Maps with ArcGIS Python API
# [Guide](https://developers.arcgis.com/python/guide/using-the-map-widget/)

# ## Create Map

# In[21]:


# Import modules
import arcgis
from arcgis.gis import GIS
# Initialize module as anon
gis = GIS()
# constructor to hold map data
map1 = gis.map('Nanaimo')
# Call constructor
map1



# In[22]:


# Zoom into map
map1.zoom = 11


# In[15]:


# manipulaing rotation of map through code
map1.rotation = 0


# ## Map Center

# In[23]:


map2 = gis.map()
map2


# In[25]:


# Centering map coordinates
map2.center = [34, -118]


# In[26]:


location = arcgis.geocoding.geocode('Times Square, NY', max_locations=1)[0]
map2.extent = location['extent']


# ## Basemaps

# >Basemap are layers on your map over which all other operational layers that you add are displayed. Basemaps typically span the >full extent of the world and provide context to your GIS layers. It helps viewers understand where each feature is located as >they pan and zoom to various extents. 
# >--<cite>[Basemaps](https://developers.arcgis.com/python/guide/using-the-map-widget/)</cite>

# In[30]:


map3 = gis.map()
# Adding colour to basemap layer
map3.basemap = 'dark-gray-vector'
map3


# In[31]:


map4 = gis.map('Nanaimo, BC')
map4


# In[32]:


import time
# Cylcling through basemaps in map extent map4
for basemap in map4.basemaps:
    map4.basemap = basemap
    time.sleep(3)


# ## Adding Layers to Maps

# In[36]:


import getpass

gis = GIS(
    url="https://arcgis.com",
    username="abrownj1996",
    password=getpass.getpass("Enter Password:")
)
cad_map = gis.map('Canada', zoomlevel=3)
cad_map


# In[37]:


flayer_search_result = gis.content.search("owner:esri", "Feature Layer", outside_org=True)
flayer_search_result

