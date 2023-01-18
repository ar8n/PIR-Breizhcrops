#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 13:40:25 2023

@author: alexysren
"""

import time
import numpy as np
from sklearn.preprocessing import StandardScaler


def train_test_split():
    
    print("--------------------------------------------------------\n")
    print("           GENERATEUR DE JEU D'ENTRAINEMENT              \n")
    print("                 ET DE JEU DE TEST                       \n")
    print("--------------------------------------------------------\n\n")
    
    print("*** Jeu d'entrainement ***\n")
    n_regions_train = int(input("Nombre de régions : "))
    
    print("\n Pour chacun des choix suivants, veuillez indiquer le tuple (region,annee)")
    print("    [Regions : frh01, frh02, frh03, frh04]\n    [Annees : 2017, 2018, 2019, 2021]\n")
    
    train = []
    for i in range(n_regions_train):
        temp = input("Choix n°" + str(i+1) + " : ")
        train.append(list(temp.split(',')))
    
    start = time.time()
    
    region, annee = train[0]
    X_train = np.load("data/" + annee + "/" + region + "/X.npy")
    y_train = np.load("data/" + annee + "/" + region + "/Y.npy")
    id_parcelle_tab_train = np.load("data/" + annee + "/" + region + "/id.npy")
    
    if n_regions_train > 1:
        for i in range(1,len(train)):
            
            region, annee = train[i]
            
            X_temp = np.load("data/" + annee + "/" + region + "/X.npy")
            Y_temp = np.load("data/" + annee + "/" + region + "/Y.npy")
            id_parcelle_tab_temp = np.load("data/" + annee + "/" + region + "/id.npy")
            
            X_train = np.concatenate((X_train, X_temp))
            y_train = np.concatenate((y_train, Y_temp))
            id_parcelle_tab_train = np.concatenate((id_parcelle_tab_train, id_parcelle_tab_temp))
            
    X_train = StandardScaler().fit_transform(X_train) # standardisation des données
            
    end = time.time()
    print("\n\n------------- Chargement du jeu d'entraînement OK — Temps écoulé : " + str(round(end-start,2)) + " s ------------- ")
        
    
    
    print("\n\n*** Jeu de test ***\n")
    n_regions_test = int(input("Nombre de régions : "))
    
    print("\n Pour chacun des choix suivants, veuillez indiquer le tuple (region,annee)")
    print("    [Regions : frh01, frh02, frh03, frh04]\n    [Annees : 2017, 2018, 2019, 2021]\n")
    
    test = []
    for i in range(n_regions_test):
        temp = input("Choix n°" + str(i+1) + " : ")
        test.append(list(temp.split(',')))
    
    start = time.time()
    
    region, annee = test[0]
    X_test = np.load("data/" + annee + "/" + region + "/X.npy")
    y_test = np.load("data/" + annee + "/" + region + "/Y.npy")
    id_parcelle_tab_test = np.load("data/" + annee + "/" + region + "/id.npy")
    
    if n_regions_test > 1:
        for i in range(1,len(test)):
            
            region, annee = test[i]
            
            X_temp = np.load("data/" + annee + "/" + region + "/X.npy")
            Y_temp = np.load("data/" + annee + "/" + region + "/Y.npy")
            id_parcelle_tab_temp = np.load("data/" + annee + "/" + region + "/id.npy")
            
            X_test = np.concatenate((X_test, X_temp))
            y_test = np.concatenate((y_test, Y_temp))
            id_parcelle_tab_test = np.concatenate((id_parcelle_tab_test, id_parcelle_tab_temp))
    
    X_test = StandardScaler().fit_transform(X_test) # standardisation des données
    
    end = time.time()
    print("\n\n------------- Chargement du jeu de test OK — Temps écoulé : " + str(round(end-start,2)) + " s ------------- ")
    
    return X_train, X_test, y_train, y_test
    



if __name__ == '__main__':
    
    X_train, X_test, y_train, y_test = train_test_split()
    
    
    
        
    