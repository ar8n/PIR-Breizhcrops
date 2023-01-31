import contextily as ctx
import matplotlib.pyplot as plt
from breizhcrops import BreizhCrops
import pandas as pd
import os
from matplotlib.colors import ListedColormap



def carte(df, algo):
    
    # tableau de conversions id culture -  nom culture
    dict_conversion = {0:'barley', 1:'wheat', 2:'rapeseed', 3:'corn', 4:'sunflower', 5:'orchards', 6:'nuts', 7:'permanent meadows', 8:'temporary meadows'}
     
    fileName = 'resultats/carte_resultat_'+algo+'.csv'
    data = pd.read_csv(fileName, sep=" ")
    predict = data['prediction'].tolist()
    
    # convertion du predict
    for i in range(len(predict)):
        name = dict_conversion[int(predict[i])]
        predict[i] = name
        
    # à ID égaux, changement de classname
    df_predict = df.copy()
    df_predict.drop(['classname'], axis=1, inplace = True)
    df_predict.insert(6, 'classname', predict)
    
    cmp1 = ListedColormap(['C0', 'C1', 'C2', 'C3', 'C5', 'C4', 'C8', 'C7', 'C9'])
    if algo == 'RF':
        cmp2 = ListedColormap(['C1', 'C5', 'C7', 'C9'])
    else:
        cmp2 = ListedColormap(['C0', 'C1', 'C5', 'C4', 'C8', 'C7', 'C9'])
    
    ### Carte entière
    fig,axs1 = plt.subplots(1,2, figsize=(24,12))
    ax = axs1[0]
    ax = df.to_crs(epsg=3857).plot(column="classname", ax=ax, legend=False, cmap = cmp1)
    ax.set_title("FRH04 - vérité terrain")
    ctx.add_basemap(ax)
    ax = axs1[1]
    # cmp = ListedColormap(['C1', 'C8', 'C9'])
    ax = df_predict.to_crs(epsg=3857).plot(column="classname", ax=ax, legend=False, cmap = cmp2)
    ax.set_title("FRH04 - prédiction par "+algo)
    ctx.add_basemap(ax)
    # On enregistre le graphique
    my_path = os.path.abspath('resultats')
    my_file = 'carte_entiere_'+algo
    fig.savefig(os.path.join(my_path, my_file))

    ### Carte zoom
    fig,axs2 = plt.subplots(1,2, figsize=(24,12))
    ax = axs2[0]
    ax = df.to_crs(epsg=3857).plot(column="classname", ax=ax, legend=False, cmap = cmp1)
    ax.set_title("FRH04 - vérité terrain")
    ax.set_xlim(-425000, -350000)
    ax.set_ylim(6.10e6,6.14e6)
    ctx.add_basemap(ax)
    ax = axs2[1]
    #cmp = ListedColormap(['C1', 'C8', 'C9'])
    ax = df_predict.to_crs(epsg=3857).plot(column="classname", ax=ax, legend=False, cmap = cmp2)
    ax.set_title("FRH04 - prédiction par "+algo)
    ax.set_xlim(-425000, -350000)
    ax.set_ylim(6.10e6,6.14e6)
    ctx.add_basemap(ax)
    # On enregistre le graphique
    my_path = os.path.abspath('resultats')
    my_file = 'carte_zoom_'+algo
    fig.savefig(os.path.join(my_path, my_file))
    
    return df, df_predict






if __name__ == '__main__':
    
    # Dataframe BreizhCrops : vérité terrain
    frh04 = BreizhCrops(region="frh04")
    df = frh04.geodataframe()
    
    # Résultat obtenu avec Random Forest
    print("\n Veuillez choisir l'algorithme à appliquer (RF ou MLP) :")
    algo = input()
    
    df, predict = carte(df, algo)
    
    
    
    
    
    
    
    