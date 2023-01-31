### Import des données Breizhcrops
from breizhcrops import BreizhCrops

### Import des bibliothèques
import numpy as np


def save():
    regions = ["belle-ile", "frh01", "frh02", "frh03",  "frh04"]

    for reg in regions:
            
        ### Import des données régionales et initialisation des variables pour la phase de préparation
        dataset = BreizhCrops(region = reg)
            
        n_parcelles = dataset.index.shape[0]
        n_temps_frequence = dataset[0][0].shape[0] * dataset[0][0].shape[1] # taille des matrices d'observation vectorisées
            
        X = np.zeros((n_parcelles, n_temps_frequence)) # données d'entrées 'obs' (réflectances par bande)
        Y = np.zeros(n_parcelles) # classes associées 'classes'
        id_parcelle_tab = np.zeros(n_parcelles) # identifiants des parcelles
        
        
        ### Préparation du jeu de données (X, y)
        for i in range(n_parcelles): # enregistrement ligne par ligne ie parcelle par parcelle
            x, y, id_parcelle = dataset[i]
            
            # conversion en numpy array
            x = x.numpy() 
            y = y.numpy()
            
            # vectorisation de la matrice pour les calculs
            x_vectorise = np.reshape(x, n_temps_frequence)
            
            # matrice d'observation (Temps en 45 portions x Nombre de bandes [fréquence] B1 à B12) de la parcelle
            X[i] = x_vectorise
            # classe associée à la parcelle
            Y[i] = y
            # id de la parcelle
            id_parcelle_tab[i] = id_parcelle
        
        
        file = "data/2017/"+reg+"/"
    
        
        np.save(file+"X.npy", X)
        np.save(file+"Y.npy", Y)
        np.save(file+"id.npy", id_parcelle_tab)
        
        print("enregistrement fini de "+reg)
        
        


### Lancement du traitement
if __name__ == '__main__':
    
    save()

