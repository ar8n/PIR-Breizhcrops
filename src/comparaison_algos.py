#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:07:41 2022

@author: alexysren
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import DecisionBoundaryDisplay


### Noms des algorithmes a tester (pour le plot)
noms = [
        "KNN",
        "Random Forest"
]

### Algorithmes a tester
algos = [
    KNeighborsClassifier(3),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
]

### Jeux de donnees
datasets = [make_moons(noise=0.3, random_state=0)]


figure = plt.figure(figsize=(24, 9)) # ???
i = 1 # ???

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
    ax.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k"
    )
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(())
    ax.set_yticks(())
    i += 1

    #iteration sur les algos
    for nom, algo in zip(noms, algos):
        ax = plt.subplot(len(datasets), len(algos) + 1, i)
        algo.fit(X_train,y_train) # phase d'entrainement
        score = algo.score(X_test, y_test)
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
        




















# KNN = KNeighborsClassifier(n_neighbors=3)


# ### Prétraitement: séparation des données d'entraînement et de test
# X, y = make_classification(n_samples=100)
# X = StandardScaler().fit_transform(X) # standardisation des données
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.25, random_state=42
# )


# KNN.fit(X_train,y_train)  # phase d'entraînement

# y_predict = KNN.predict(X_test)  # classes prédites
# score = KNN.score(X_test,y_test)   # précision de la prédiction























# def erreur(y_prediction, y_realite):
#     """
#     Fonction qui estime l'erreur entre les classes prédites et les vraies classes
#     NB: il s'agit de la norme 2 (NORME EUCLIDIENNE)

#     Paramètres
#     ----------
#     y_prediction : numpy array
#         CLASSES PREDITES.
#     y_realite : numpy array
#         VRAIES CLASSES.

#     Retourne
#     -------
#     float.

#     """
#     y = y_prediction - y_realite
#     s = 0
#     for e in y:
#         s += e**2
#     return np.sqrt(s)
    












