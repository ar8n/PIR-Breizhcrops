#                                          *
#                                          *
#                                          *
#                                          *
                                         
#                             ///     LISEZ-MOI      ///
                                
# Pour le bon fonctionnement du script, merci de faire en sorte que celui-ci soit
# placé dans le MÊME répertoire que le fichier "train_test_split.py" ET le dossier
# "data" (qui contient toutes les données par année !)
                                        
#                                         *
#                                         *
#                                         *
#                                         *



### Import de l'algorithme de classification étudié
from sklearn.neighbors import KNeighborsClassifier

### Import des bibliothèques
import numpy as np
import time
from tqdm import tqdm
import csv

from sklearn.metrics import f1_score
from sklearn.metrics import precision_score

### Import de nos programmes sur-mesure
from train_test_split import train_test_split


### Test de variations des résultats en fonction des paramètres du KNN

# nbr de voisins à considérer
K = np.arange(2, 5)

# Fonction de pondération utilisée dans la prédiction :
# 'uniforme' : poids uniformes
# 'distance' : pondère les points par l'inverse de leur distance
Weights = ['uniform', 'distance']

# Métrique à utiliser pour le calcul de distance
Dist = ['euclidean', 'manhattan', 'chebyshev']






def traitement(K, Weights, Dist):
    
    print("-----------------------------------------------------------------------------------\n")
    print("           Comparaison des paramètres du KNN              \n")
    print("     Lisa ARGENTO, Claire GIRARDIN, Alexys REN (Promo ING21, ENSG Géomatique)       \n")
    print("-----------------------------------------------------------------------------------\n\n")
    
    # Nombre d'itérations
    n = 3
    
    ### Division du jeu de données: entraînement / test
    X_train, X_test, y_train, y_test = train_test_split()
    start = time.time()
    
    file_name = 'poids.csv'
    file = open( file_name , "a", newline='')
    writer = csv.writer(file) # Création de l’écrivain CSV.
    writer.writerow( ('param', 'iterations', 'k', 'poids', 'accuracy', 'f1_score', 'precision') ) # Écriture de la ligne d’en-tête des colonnes
    
    
    for k in K:
        
        for w in Weights:
            
            algo = KNeighborsClassifier( n_neighbors = 4, weights = Weights[1], metric = Dist[0])
            
            ### Qualité moyenne de la classification
            accuracy_moy = 0
            f_score_moy = 0
            precision_moy = 0
            
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
                f_score_moy += f1_score(y_test, y_pred, average='weighted')
                precision_moy += precision_score(y_test, y_pred, average='weighted')
                print("\n------------- Calcul des indicateurs de qualité terminé ------------- ")
            
            
            ### Qualité moyenne de la classification
            accuracy_moy /= n
            f_score_moy /= n
            precision_moy /= n
            
            
            # Sauvergarde des résultats au fur et à mesure
            file = open( file_name , "a", newline='')
            writer = csv.writer(file) # Création de l’écrivain CSV.
            writer.writerow( ('poids', 3, k, w, accuracy_moy, f_score_moy, precision_moy) ) # Écriture des données
            file. close ()
    
    
    end = time.time()
    print("\n\n\n\nTemps de calcul total : " + str(round(end-start,2)) + " s ")
        
    
    



if __name__ == '__main__':
    
    traitement(K, Weights, Dist)
        
        
        
        