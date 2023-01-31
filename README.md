# PIR-Breizhcrops
Repository pour le Projet d'Initiation à la Recherche (no. 14, ING21)
Lisa ARGENTO, Claire GIRADIN, Alexys REN encadrés par Alexandre HIPPERT-FERRER

# BreizhCrops:
#### A Time Series Dataset for Crop Type Mapping


Voilà l'[article BREIZHCROPS: A TIME SERIES DATASET FOR CROP TYPE MAPPING](https://github.com/ar8n/PIR-Breizhcrops/blob/main/data/BREIZHCROPS%20-%20A%20TIME%20SERIES%20DATASET%20FOR%20CROP%20TYPE%20MAPPING.pdf) consultable en ligne sur lequel nous avons appuyé toutes nos recherches. Cet article scientifique réalisé par Marc Rußwurm, Charlotte Pelletier, Maximilian Zollner, Sebastien Lefévre et Marco Korner présente un nouvel ensemble de données de référence pour la classification supervisée des grandes cultures à partir de séries chronologiques satellitaires en Bretagne. Ils comparent sept réseaux de neurones profonds récents qui s'appuie chacun sur l'algorithme Random Forest. 

Ils ont rédigé un tutoriel explicatif sur [Colab Notebook](https://colab.research.google.com/drive/1i0M_X5-ytFhF0NO-FjhKiqnraclSEIb0?usp=sharing) à partir duquel nous avons commencé à travailler.

Leur objectif est de proposer un jeu de donnée pertinent pour entraîner des algorithmes pour la classification : il met en évidences tous les problèmes que le classification peut rencontrer.

Ils expliquent leur projet lors du congres en ligne ISPRS (si vous voulez en savoir plus [cliquez ici](http://isprs.stream-up.tv/media-221-breizhcrops-a-time-series-dataset-for-crop-type-mapping)).


### Introduction
Les auteurs présentent un nouveau jeu de données de parcelles agricoles pertinentes pour mettre en évidence toutes les difficultés que l’on peut rencontrer en faisant de la classification, c'est-à-dire en analysant des données de façon à regrouper les pixels selon leur appartenance à des régions homogènes. Il existe deux principaux types de classification en télédetection : la \textit{classification non supervisée} et la \textit{classification supervisée}. La première permet  de regrouper des objets spatiaux en un certain nombre de classes d’occupation du territoire en formant des groupes les plus homogènes possibles tandis que la seconde permet de répartir au mieux ces objets spatiaux dans des classes prédéfinies

L'intérêt est que \textit{Breizhcrops} présente de nombreux défis : données manquantes, déséquilibre de classes, autocorrélation spatiale, etc. Effectivement, pour regrouper des observations en groupes homogènes, il faut tout d’abord avoir une définition de ce que sont des observations similaires ou des observations différentes. Il faut donc être en mesure de quantifier la similarité ou la distance entre deux observations en fonction de leurs attributs. Cette première étape est souvent la plus difficile de tout le processus de classification et c’est souvent sur la définition des groupes que nous jouons pour obtenir la classification la plus précise possible.

Parmi les difficultés que présente le jeu de données \textit{Breizhcrops}, nous nous sommes intéressés à la \emph{sous-représentation}, appelée aussi \textit{déséquilibre} de classes. En effet, un déséquilibre important du nombre de représentants par classe entraîne des prédictions moins robustes car  cela augmente nettement la difficulté de l’apprentissage par l’algorithme. Si l’algorithme n’a que peu d’exemples de la classe minoritaire sur lesquels apprendre lors de la phase d'entraînement, il aura des difficultés à prédire les nouveaux objets de cette classe lors de la phase de généralisation (ou \textit{phase de test}).}
Afin de réduire le déséquilibre de classes, une solution peut consister à multiplier les sources d'observations des échantillons sous-représentés.

\noindent À partir de cet axe de réflexion, notre étude s'articule autour de trois objectifs : 
\begin{itemize}
\item[\textit{i) }] Appliquer certaines méthodes de l'état de l'art pour une tâche de classification supervisée des parcelles agricoles;
\item[\textit{ii) }] Contribuer au jeu de données \textit{Breizhcrops} en l'étendant aux années de 2018 à 2022, ce qui n'est pas le cas pour l'instant;
\item[\textit{iii) }] Etudier comment la prise en compte des données pluriannuelles permet d'améliorer la classification de parcelles agricoles sous-représentées à partir de cette extension. 
\end{itemize}

### Conclusion et perspectives

Notre étude a permis plusieurs avancées vis-à-vis de la manipulation du jeu de données Breizhcrops.

Nous avons, tout d'abord, mis en évidence les moyens de récupérer les données des parcelles pour une année souhaitée. Nous avons également explicité la chaîne de traitement nécessaire afin de réutiliser facilement différents algorithmes de classification dans le but d'une étude multi-temporelle des parcelles agricoles grâce à la librairie Scikit-Learn.

Cependant, nous n'avons pas réussi à mettre en place de classification multi-temporelle en raison du manque de temps pour produire cette extension du jeu de données.



### Persepectives

\begin{itemize}
    \item[\textit{- }] Poursuivre nos recherches en récupérant les données parcellaires post-2017 et les croiser dans la composition du jeu d'entraînement et jeu de test (évolution de la végétation au cours du temps).
    \item[\textit{- }] Généralisation de la classification de parcelles agricoles sur d'autres régions françaises.
    \item[\textit{- }] Prendre en compte des attributs spatiaux, en plus de la réflectance, comme des informations sur la géométrie et la topologie des parcelles.
\end{itemize}

### Rapport détaillé
<a href="doc/poster.pdf"><img height=300px src=doc/poster.png /></a>


