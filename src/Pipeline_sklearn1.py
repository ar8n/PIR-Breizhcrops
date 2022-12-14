# Réprésentation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Algorithmes
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Jeux de données
from sklearn.datasets import make_moons

# Séparation du jeu de données en données d'entrainement et données de test
from sklearn.model_selection import train_test_split

# Standardisation des données
from sklearn.preprocessing import StandardScaler

# Entrainement
from sklearn.inspection import DecisionBoundaryDisplay

# Matrice de confusion et grandeur remarquable
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import f1_score

# Les différents calculs de métrique (scores)
from sklearn.metrics import accuracy_score







# ----------------- Comparasion des différents algos ----------------------- #



### Noms des algorithmes à tester (pour le plot)
nomsAlgos = [ "KNN", "Random Forest" ]

### Algorithmes a tester
algos = [
    KNeighborsClassifier(3),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
]

### Jeux de donnees
datasets = [make_moons(noise=0.3, random_state=0)]
class_names = ['classe0', 'classe1']


figure = plt.figure(figsize=(24, 9))

i = 1

# iteration sur les datasets
for ds_cnt, ds in enumerate(datasets):
    # pretraitement du dataset, division en donnees d'entrainement et donnees de test
    X,y = ds
    X = StandardScaler().fit_transform(X) # standardisation des données
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    
    # affichage des donnees d'entree
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(["#FF0000", "#0000FF"])
    ax = plt.subplot(len(datasets), len(algos) + 1, i)
    if ds_cnt == 0:
        ax.set_title("Donnees d'entree")
    # affichage des donnees d'entrainement
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
    # affichage des donnees de test
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(())
    ax.set_yticks(())
    i += 1

    #iteration sur les algos
    for nom, algo in zip(nomsAlgos, algos):
        ax = plt.subplot(len(datasets), len(algos) + 1, i)
        
        # PHASE D'ENTRAINEMENT
        algo.fit(X_train,y_train)
        score = algo.score(X_test, y_test) # Accuracy
        DecisionBoundaryDisplay.from_estimator(
            algo, X, cmap=cm, alpha=0.8, ax=ax, eps=0.5
        )
        
        # affichage des donnees d'entrainement
        ax.scatter(
            X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k"
        )
        
        # affichage des donnees de test
        ax.scatter(
            X_test[:, 0],
            X_test[:, 1],
            c=y_test,
            cmap=cm_bright,
            edgecolors="k",
            alpha=0.6,
        )
        
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_xticks(())
        ax.set_yticks(())
        if ds_cnt == 0:
            ax.set_title(nom)
        ax.text(
            x_max - 0.3,
            y_min + 0.3,
            ("%.2f" % score).lstrip("0"),
            size=15,
            horizontalalignment="right",
        )
        i += 1

plt.tight_layout()
plt.show()
     







# ----------------- MATRICE DE CONFUSION ----------------------- #

# Source :
# https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html?highlight=confusion+matrix


# Plot normalized confusion matrix
for nom, algo in zip(nomsAlgos, algos):
    disp = ConfusionMatrixDisplay.from_estimator(
        algo,
        X_test,
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize='true',
    )
    disp.ax_.set_title(nom)

    print(nom)
    print(disp.confusion_matrix)

plt.show()



# ----------------- SCORES ----------------------- #





















