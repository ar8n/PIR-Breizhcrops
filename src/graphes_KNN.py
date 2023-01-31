import pandas as pd
import matplotlib.pyplot as plt
import os



def KNN_1_frh04():
    # param, iterations, k, accuracy, f1_score, precision, recall
    fileName = 'resultats/voisins_frh04.csv'
    data = pd.read_csv(fileName)
    K = data['k'].tolist()
    accuracy = data['accuracy'].tolist()
    f1_score = data['f1_score'].tolist()
    precision = data['precision'].tolist()
    
    fig, ax = plt.subplots()  
    plt.title('Etude de la variation du nombre de voisins (frh04)')
    plt.plot(K, accuracy, 'm', label='accuracy')
    plt.scatter(K, accuracy, c='m', marker ='x')
    plt.plot(K, f1_score, 'b', label='f1_score')
    plt.scatter(K, f1_score, c='b', marker ='x')
    plt.plot(K, precision, 'k', label='precision')
    plt.scatter(K, precision, c='k', marker ='x')
    ax.set_xlabel('nombre de voisins')
    ax.set_ylabel('valeurs des paramètres')
    plt.legend()
    
    # On enregistre le graphique
    my_path = os.path.abspath('resultats')
    my_file = 'voisins_frh04'
    fig.savefig(os.path.join(my_path, my_file))
    
    return data, K

def KNN_1_belle_ile():
    # param, iterations, k, accuracy, f1_score, precision, recall
    fileName = 'resultats/voisins_belle-ile.csv'
    data = pd.read_csv(fileName)
    K = data['k'].tolist()
    accuracy = data['accuracy'].tolist()
    f1_score = data['f1_score'].tolist()
    precision = data['precision'].tolist()
    
    fig, ax = plt.subplots()  
    plt.title('Etude de la variation du nombre de voisins (Belle-ile)')
    plt.plot(K, accuracy, 'm', label='accuracy')
    plt.plot(K, f1_score, 'b', label='f1_score')
    plt.plot(K, precision, 'k', label='precision')
    ax.set_xlabel('nombre de voisins')
    ax.set_ylabel('valeurs des paramètres')
    plt.legend()
    
    # On enregistre le graphique
    my_path = os.path.abspath('resultats')
    my_file = 'voisins_belle-ile'
    fig.savefig(os.path.join(my_path, my_file))
    
    return data, K


def KNN_voisins():
    # param, iterations, k, accuracy, f1_score, precision, recall
    fileName_frh = 'resultats/voisins_frh04.csv'
    fileName_belle = 'resultats/voisins_belle-ile.csv'
    
    data_frh = pd.read_csv(fileName_frh)
    data_belle = pd.read_csv(fileName_belle)
    
    K_frh = data_frh['k'].tolist()
    K_belle = data_belle['k'].tolist()
    accuracy_frh = data_frh['accuracy'].tolist()
    accuracy_belle = data_belle['accuracy'].tolist()
    f1_score_frh = data_frh['f1_score'].tolist()
    f1_score_belle = data_belle['f1_score'].tolist()
    precision_frh = data_frh['precision'].tolist()
    precision_belle = data_belle['precision'].tolist()
    
    fig, ax = plt.subplots()  
    plt.title('Comparaison de la variation du nombre de voisins (Frh04 et Belle-ile)')
    
    plt.plot(K_frh, accuracy_frh, 'purple', label='accuracy frh04')
    plt.plot(K_frh, f1_score_frh, 'mediumblue', label='f1_score frh04')
    plt.plot(K_frh, precision_frh, 'black', label='precision frh04')
    
    plt.plot(K_belle, accuracy_belle, 'violet', label='accuracy Belle-Ile')
    plt.plot(K_belle, f1_score_belle, 'dodgerblue', label='f1_score Belle-Ile')
    plt.plot(K_belle, precision_belle, 'dimgray', label='precision Belle-Ile')

    ax.set_xlabel('nombre de voisins')
    ax.set_ylabel('valeurs des paramètres')
    ax.set_xlim(0,200)
    plt.legend()
    
    # On enregistre le graphique
    my_path = os.path.abspath('resultats')
    my_file = 'voisins_comp_frh_belle'
    fig.savefig(os.path.join(my_path, my_file))
    
    return data_frh, K_frh, data_belle, K_belle
    






if __name__ == "__main__":
    
    print('-------- Enregistrement des graphiques --------')
    
    KNN_1_frh04()
    
    KNN_1_belle_ile()
    
    KNN_voisins()
    

    
    
    
    