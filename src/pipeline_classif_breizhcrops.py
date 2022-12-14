#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:37:52 2022

@author: alexysren
"""

### Import des données Breizhcrops
from breizhcrops import BreizhCrops


### Import des algorithmes de classification

from sklearn.neighbors import KNeighborsClassifier





### Import des bibliothèques
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split











### Lancement du traitement
if __name__ == '__main__':
    
    """ Essai pour une région (pipeline à généraliser) """
    
    
    ### Import des données régionales et initialisation des variables pour la phase de préparation
    dataset = BreizhCrops(region="belle-ile")
    
    n_parcelles = dataset.index.shape[0]
    n_temps_frequence = dataset[0][0].shape[0] * dataset[0][0].shape[1] # taille des matrices d'observation vectorisés
    
    id_parcelle_tab = np.zeros(n_parcelles) # identifiants de parcelles
    X = np.zeros((n_parcelles, n_temps_frequence)) # données d'entrée 'obs' (réflectances par bande)
    Y = np.zeros(n_parcelles) # classes associées 'classes'
    
    
    
    ### Préparation du jeu de données (X, y)
    for i in range(n_parcelles):
        x, y, id_parcelle = dataset[i]
        x = x.numpy() # conversion en numpy array
        y = y.numpy()
          
        # # ajout de features statistiques 
        # mean = x.mean(0)
        # std = x.std(0)
        # min = x.min(0)
        # max = x.max(0)
        # median = np.median(x,0)
        # bandfeatures = np.hstack([mean,std,min,max,median])
        
        x_vectorise = x.flatten() # vectorisation de la matrice pour les calculs
        
        #x_vectorise = np.concatenate((x_vectorise, bandfeatures))
        
        X[i] = x_vectorise # matrice observation (Temps en 45 portions x Nombre de bandes [fréquence] B1 à B12) de la parcelle
        Y[i] = y # classe associée à la parcelle
        id_parcelle_tab[i] = id_parcelle # id de la parcelle
    
    
    
    ### Prétraitement du jeu de données, division en données d'entraînement et données de test
    
    X = StandardScaler().fit_transform(X) # standardisation des données
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.25, random_state=42
    )
    
    ### Entraînement du classifieur
    
    algo = KNeighborsClassifier(3)
    algo.fit(X_train,y_train)
    
    
    ### Classification
    
    score = algo.score(X_test, y_test)
    
    
    
    
    