# PIR-Breizhcrops
Repository pour le Projet d'Initiation à la Recherche (no. 14, ING21)

# BreizhCrops:
#### A Time Series Dataset for Crop Type Mapping


Voilà l'[article BREIZHCROPS: A TIME SERIES DATASET FOR CROP TYPE MAPPING](https://github.com/ar8n/PIR-Breizhcrops/blob/main/data/BREIZHCROPS%20-%20A%20TIME%20SERIES%20DATASET%20FOR%20CROP%20TYPE%20MAPPING.pdf) consultable en ligne sur lequel nous avons appuyé toutes nos recherches. Cet article scientifique réalisé par Marc Rußwurm, Charlotte Pelletier, Maximilian Zollner, Sebastien Lefévre et Marco Korner présente un nouvel ensemble de données de référence pour la classification supervisée des grandes cultures à partir de séries chronologiques satellitaires en Bretagne. Ils comparent sept réseaux de neurones profonds récents qui s'appuie chacun sur l'algorithme Random Forest. 

Ils ont rédigé un tutoriel explicatif sur [Colab Notebook](https://colab.research.google.com/drive/1i0M_X5-ytFhF0NO-FjhKiqnraclSEIb0?usp=sharing) à partir duquel nous avons commencé à travailler.

Leur objectif est de proposer un jeu de donnée pertinent pour entraîner des algorithmes pour la classification : il met en évidences tous les problèmes que le classification peut rencontrer.

##### Reference

This work will be published in the proceedings of [ISPRS Archives 2020](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLIII-B2-2020/1545/2020/isprs-archives-XLIII-B2-2020-1545-2020.pdf). [Preprint available on ArXiv](https://arxiv.org/abs/1905.11893)
```
@article{breizhcrops2020,
  title={BreizhCrops: A Time Series Dataset for Crop Type Mapping},
  author={Ru{\ss}wurm, Marc and Pelletier, Charlotte and Zollner, Maximilian and Lef{\`e}vre, S{\'e}bastien and K{\"o}rner, Marco},
  journal={International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences ISPRS (2020)},
  year={2020}
}
```

ISPRS virtual congress video can be found [here](http://isprs.stream-up.tv/media-221-breizhcrops-a-time-series-dataset-for-crop-type-mapping)


### Train a model

Train a model via the example script `train.py`
```bash
python train.py TransformerEncoder --learning-rate 0.001 --weight-decay 5e-08 --preload-ram
```

This script uses the default model parameters from `breizhcrops.models.TransformerModel`.
When training multiple epochs, the `--preload-ram` flag speeds up training significantly


### Acknowledgements

The model implementations from this repository are based on the following papers and github repositories.

* TempCNN (reimplementation from [keras source code](https://github.com/charlotte-pel/igarss2019-dl4sits) ) [Pelletier et al., 2019](https://www.mdpi.com/2072-4292/11/5/523)
* LSTM Recurrent Neural Network adapted from [Rußwurm & Körner, 2017](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w18/html/Russwurm_Temporal_Vegetation_Modelling_CVPR_2017_paper.html)
* MS-ResNet implementation from [Fei Wang](https://github.com/geekfeiw/Multi-Scale-1D-ResNet)
* TransformerEncoder implementation was originally adopted from Yu-Hsiang Huang [GitHub](https://github.com/jadore801120/attention-is-all-you-need-pytorch), but later replaced by own implementation when `torch.nn.transformer` modules became available
* InceptionTime [Fawaz et al., 2019](https://arxiv.org/abs/1909.04939)
* StarRNN [Turkoglu et al., 2019](https://arxiv.org/abs/1911.11033)
* OmniscaleCNN [Tang et al., 2020](https://arxiv.org/abs/2002.10061)

The raw label data originates from  
* [Registre parcellaire graphique (RPG)](https://www.data.gouv.fr/fr/datasets/registre-parcellaire-graphique-rpg-contours-des-parcelles-et-ilots-culturaux-et-leur-groupe-de-cultures-majoritaire/) of the French National Geographic Institute (IGN)



### ICML workshop 2019

<a href=https://arxiv.org/abs/1905.11893><img height=300px src=doc/paper.png /></a>
<a href="doc/poster.pdf"><img height=300px src=doc/poster.png /></a>


