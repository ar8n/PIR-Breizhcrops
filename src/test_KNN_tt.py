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
import time
from tqdm import tqdm
import csv

from sklearn.metrics import f1_score
from sklearn.metrics import precision_score

### Import de nos programmes sur-mesure
from train_test_split import train_test_split


### Test de variations des résultats en fonction des paramètres du KNN

# nbr de voisins à considérer
K = [2, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]

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
    
    file_name = 'belle_ile_tout.csv'
    file = open( file_name , "a", newline='')
    writer = csv.writer(file) # Création de l’écrivain CSV.
    writer.writerow( ('id', 'iterations', 'k', 'poids', 'metric', 'accuracy', 'f1_score', 'precision', 'temps') ) # Écriture de la ligne d’en-tête des colonnes
    
    i = 1
    
    for k in K:
        
        for w in Weights:
            
            for d in Dist:
                
        
                algo = KNeighborsClassifier( n_neighbors = k, weights = w, metric = d)
        
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
                end = time.time()
                temps_moy = round(end-start,2) / 3
                writer.writerow( (i, 3, k, w, d, accuracy_moy, f_score_moy, precision_moy, temps_moy) ) # Écriture des données
                file. close ()
                start = time.time()
                
                i += 1




if __name__ == '__main__':
    
    traitement(K, Weights, Dist)
    


    
        