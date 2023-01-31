### Import des bibliothèques
import numpy as np

def stat():
        
    file = "//Users/Claire/Desktop/ENSG/ING2/PIR/Notre_Projet/scrip_python/data/2017/"
    
    ID_frh01 = np.load(file+"frh01/Y.npy")
    ID_frh02 = np.load(file+"frh02/Y.npy")
    ID_frh03 = np.load(file+"frh03/Y.npy")
    ID_frh04 = np.load(file+"frh04/Y.npy")
    
    ID = [ID_frh01, ID_frh02, ID_frh03, ID_frh04]
    
    stat_01 = np.zeros(9)
    stat_02 = np.zeros(9)
    stat_03 = np.zeros(9)
    stat_04 = np.zeros(9)
    
    STAT = [stat_01, stat_02, stat_03, stat_04]
    
    # Comptage du nombre de parcelles par classe
    for id_frh, stat in zip(ID, STAT) :
        for k in range(len(id_frh)):
            stat[int(id_frh[k])] += 1
    
    
    # vérification de cohérence sur le nombre de parcelles total
    for id_frh, stat in zip(ID, STAT) :
        
        valid = np.shape(id_frh)
        test = np.sum(stat)
        
        if valid == test :
            print('True')
        else:
            print('False')



if __name__ == '__main__':

    stat()

    
    
    s