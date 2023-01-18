#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:37:52 2022

@author: alexysren
"""

#                                          *
#                                          *
#                                          *
#                                          *
                                         
#                             ///     LISEZ-MOI      ///
                                
# Pour le bon fonctionnement du script, merci de faire en sorte que celui-ci est
# placé dans le MÊME répertoire que le fichier "train_test_split.py" ET le dossier
# "data" (qui contient toutes les données par année !)
                                        
#                                         *
#                                         *
#                                         *
#                                         *




"""
------------------------------------------------------------------------------
                        
                        [PREPARATION DU TRAITEMENT]

------------------------------------------------------------------------------
"""



### Import des algorithmes de classification

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier



### Import des bibliothèques
import numpy as np

from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

import time
from tqdm import tqdm


### Import de nos programmes sur-mesure

from train_test_split import train_test_split


### Algorithmes de classification utilisés

algos = [
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=2),
    KNeighborsClassifier(3),
    MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
]

names = [
    "Random Forest",
    "KNN",
    "MLP"
]




"""
------------------------------------------------------------------------------
                        
                                * TRAITEMENT *

------------------------------------------------------------------------------
"""




if __name__ == '__main__':
    
    
    print("-----------------------------------------------------------------------------------\n")
    print("           PIPELINE DE CLASSIFICATION BREIZHCROPS              \n")
    print("     Lisa ARGENTO, Claire GIRARDIN, Alexys REN (Promo ING21, ENSG Géomatique)       \n")
    print("-----------------------------------------------------------------------------------\n\n")
    
    
    print("Quel algorithme souhaitez-vous utiliser?\n")
    print("    [Algos: Random Forest, KNN, MLP]\n")
    selected_algo = input("algo = ")
    algo = algos[names.index(selected_algo)]
    
    
    n = int(input("Nombre d'itérations = "))
    
    print("\n\n")
    
    

    
    ### Division du jeu de données: entraînement / test
    X_train, X_test, y_train, y_test = train_test_split()
    start = time.time()
    
    

        
    if n == 1:
        """
        
        Pour une itération, on affiche le détail des temps mis pour chaque étape
        
        """
        
        ### Entraînement du classifieur
        
        print("\n\nTrain en cours ...")
        algo.fit(X_train,y_train)
        t1 = time.time()
        print("\n------------- Phase d'entraînement terminé — Temps écoulé : " + str(round(t1-start,2)) + " s ------------- ")
        
        
        ### Classification
        
        print("\n\nPrédiction en cours ...")
        y_pred = algo.predict(X_test) # classes prédites
        t2 = time.time()
        print("\n------------- Prédiction des classes terminé — Temps écoulé : " + str(round(t2-t1,2)) + " s ------------- ")
        
        
        
        ### Qualité de la classification
        
        print("\n\nQualification de la classification en cours ...")
        accuracy = algo.score(X_test, y_test)
        matrice_de_confusion = confusion_matrix(y_test, y_pred, labels=np.arange(9))
        f_score = f1_score(y_test, y_pred, average='weighted')
        
        end = time.time() 
        print("\n------------- Calcul des indicateurs de qualité terminé — Temps écoulé : " + str(round(end-t2,2)) + " s ------------- ")
        
        
        print("\n\n\n\nTemps de calcul total : " + str(round(end-start,2)) + " s ")
        
    else:
        
        """
        
        Pour plusieurs itérations, on met en place une barre de progression qui avance
        d'un pas à chaque itération
        
        """
        
        ### Qualité moyenne de la classification (initialisation des variables)
        
        accuracy_moy = 0
        matrice_de_confusion_moy = np.zeros((9,9))
        f_score_moy = 0
        
        
        for it in tqdm(range(n)):
            
            ### Entraînement du classifieur
            
            print("\n\nTrain en cours ...")
            algo.fit(X_train,y_train)
            print("\n------------- Phase d'entraînement terminé ------------- ")
            
            
            ### Classification
            
            print("\n\nPrédiction en cours ...")
            y_pred = algo.predict(X_test) # classes prédites
            print("\n------------- Prédiction des classes terminé ------------- ")
            
            
            
            ### Qualité de la classification
            
            print("\n\nQualification de la classification en cours ...")
            accuracy_moy += algo.score(X_test, y_test)
            matrice_de_confusion_moy += confusion_matrix(y_test, y_pred, labels=np.arange(9))
            f_score_moy += f1_score(y_test, y_pred, average='weighted')
            print("\n------------- Calcul des indicateurs de qualité terminé ------------- ")
        
        
        ### Qualité moyenne de la classification
        
        accuracy_moy /= n
        matrice_de_confusion_moy /= n
        f_score_moy /= n
        
        end = time.time()
        print("\n\n\n\nTemps de calcul total : " + str(round(end-start,2)) + " s ")
    
    
    