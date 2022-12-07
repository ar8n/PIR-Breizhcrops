#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:58:55 2022

@author: alexysren
"""

#import breizhcrops
from breizhcrops import BreizhCrops

import numpy as np
import pandas as pd
# import geopandas as gpd
import matplotlib.pyplot as plt




# let's define identity transforms to avoid any preprocessing (we will see later)
def raw_transform(input_timeseries):
  return input_timeseries[:,:-1]



belle_ile = BreizhCrops(region="belle-ile")

field_parcels_geodataframe = belle_ile.geodataframe()


# initialize datasets at both processing levels
# datasets = dict(
#     L1C = BreizhCrops(region="belle-ile", level="L1C", transform=raw_transform),
#     L2A = BreizhCrops(region="belle-ile", level="L2A", transform=raw_transform)
# )



""" ---------------------------------------------------------------------- 

                        TESTS

    ----------------------------------------------------------------------
"""

data_class = field_parcels_geodataframe[["id","classid","classname"]] # id des parcelles & classes associées
# time_series, label, field_id = belle_ile[0]

# time_series_converted = time_series.numpy()[:, :]
# label_converted = label.numpy()

dataset = BreizhCrops(region="belle-ile", transform = raw_transform)
x,y,field_id = dataset[0]  # une parcelle, x contient les valeurs de reflectance sur un intervalle de temps pour les 13 bandes spectrales
fig,ax = plt.subplots()
ax.plot(x)
ax.set_title("raw transform")
ax.set_xlabel("time index")
ax.set_ylabel("reflectance")


# On sélectionne une bande pour tester (B1 par exemple)
r_b1 = x[:, 0] # toutes les reflectances B1 en 2017 sur une parcelle
r_b1_moy = np.mean(r_b1) # reflectance B1 moyenne en 2017 sur une parcelle



### [TEST] Colonne de reflectances concatenee au dataframe des classes
# n_parcelles = data_class.shape[0]
# reflectance_tab = np.zeros(n_parcelles)
# for i in range(n_parcelles):
#     x, y, field_id = dataset[i]
#     r = x[:, 0]
#     r_moy = np.mean(r)
#     reflectance_tab[i] = r_moy
    
#data_class = data_class.assign(reflectance = reflectance_tab.tolist())

### [/TEST]


    


