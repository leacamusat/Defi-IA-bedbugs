Petit document récapitulatif : https://www.overleaf.com/7664353796mnjshyqhnbwb 

# Defi-IA-bedbugs
https://www.kaggle.com/code/maxhalford/tutoriel-d-fi-ia-2023/notebook


clé : 
f80b400f-3d29-43f0-8049-214a756ff0b3


```diff
- ATTENTION
! AVANT DE GENERER LA SOUMISSION FAIRE CORRESPONDRE LE NOM DU JEU DE SET DE VARIABLES QUALITATIVES ENTRE LE FICHIER SOUMISSION ET MODELES ET GRADIO 
! Avant de soumettre toujours vérifier qu'on a bien appliqué la transformation sur les Y (cad mettre au carré)
```

-------------------------------------------


# Organisation des fichiers 

/</br> 
**dossier_local /</br>
&emsp; &emsp;├─models_sav/ </br>
&emsp; &emsp; &emsp; &emsp;├─ xgboost.sav/ </br>
&emsp; &emsp;&emsp; &emsp; ├─ .sav/ </br>
&emsp; &emsp;├─ application gradio </br>
&emsp; &emsp;├─application  all_our_requests_done.csv (requêtes testées) </br>
&emsp; &emsp;├─ Modeles.ipynb (modèles testés et analyse descriptive des variables d'entrainement) </br>
&emsp; &emsp;├─ pricing_requests_done.csv (résultats requêtes testées) </br>
&emsp; &emsp;├─ ExploreTestSet.ipynb (stat descriptive sur le jeu de données d'évaluation kaggle)</br>
&emsp; &emsp;├─ allrequest.csv (toutes les combinaisons de variables qualitatives possibles) </br>
&emsp; &emsp;├─ sample_submission.csv (génération du fichier de soumission à l'aide du modèle enregistré en .sav)**



## Lancer l'application gradio 

python gradio_defiIA.py --model_name ``nom_modèle`` --scaler_name ``nom_standard_scaler_modèle``
ex : ``python gradio_defiIA.py --model_name "X_gboost_tuned_model.sav" --scaler_name 'Standard_Scaler.sav'``

## Note : le modèle Random forest est très lourd ( trop lours pour github) il est sur mon ordinateur

Modèles testés et améliorations (le 6 novembre 2022)  : 
====================== 

On a commencé par testé des modèles en modifiant les deux variables quantitatives (en appliquant un log sur le stock et un racine carré sur le prix). 
Ensuite, on a transformé les variables qualitatives en 0-1 hot en enlevant la première modalité pour éviter que la même information soit codée deux fois (si la variable n'appartient pas aux n-1 premières modalités, on sait en fait qu'elle appartient à la n-ième, ce qui permet d'éviter d'avoir une colonne en trop). On a également centré et réduit nos variables. 

Nos premiers modèles ont été appliqués quand on avait 1 requete par utilisateur, que nous avions enlevé la variable qualitative brand car nous avions supposé que le nombre de modalité de cette variable était inclus dans la variable qualitative group, elle portait moins d'informations. 
On a testé X_Gboost, RandomForest des modèles d'aggrégation souvent utilisés en ML car ils permettent de combiner plusieurs modèles faibles. 
On a testé une régression lasso mais elle a donné de très faibles résultats. On a également réalisé un CatBoost un modèle aussi basé sur l'agrégation. 

Ensuite, on a re réalisé des requêtes pour avoir plusieurs requêtes par utilisateur (un utilisateur peut faire deux requêtes à un jour d'intervalle). 

On a aussi décidé de rajouter la variable qualitative brand. et on a retesté nos modèles : 
On a que l'accuracy liée au MSE a fortement augmenté pour le modèle XGboost. 

Tâches à réasliser: 
======================

- [ ] 1° Continuer le travail sur l'interprétabilité (en utilisant le TP précédent d'IA framework) 

- [ ] 2° Faire le docker 

- [ ] 3° requêtes avec plusieurs utilisateurs encore 

- [ ] 4° Chercher des nouveaux features à créer 

- [ ] 5° créer des pipelines de manière à n'avoir à enregistrer que le modèle et pas aussi le standard_scaler (easier)

Historique des requêtes: 
========================
14/11/2022 (lundi) : 500 requêtes
* 243 * 2 = requ^tes : 1 avatar fait la même requete a j et j+5
* 14 requêtes un peu random et pour jour 34

05/11/2022 (samedi) :
* 486 * 2 =  requêtes : 1 utilisateur fait la même requête à j et j+1
    - 162 fois dans A 
    - 162 fois dans B
    - 131 fois dans C (moins car on à plus de requêtes snirf)

03/11/2022 :
* 5 * 18 requêtes pour le belge qui n'était pas presents

Flavie 16/10/2022 : 
 * 3 * 629 requêtes sur les jours suivants (d'après la répartition de la variable date en prenant un dépassement de 2)
(1 requêtes par ligne du tableau minimum)
 selected_daysA = [0,1,2,3,4,5,6,7,8]
 selected_daysB = [13,14,15,16,17,18,19,20,21,22,23]
 selected_daysC = [32,33,24,35,36,37,38,39,40]
* 1 avatar = 1 jour = 1 requête

Flavie 15/10/2022 : 
 * 629 requêtes sur les jours suivants (d'après la répartition de la variable date en prenant un dépassement de 2)
(1 requêtes par ligne du tableau minimum)
* 5 requêtes 1 avatar = 1 requetes = 1 jour, jour aléatoire dans la liste : 
selected_days = [0,1, 2, 3, 4 , 5, 6, 7, 8, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 , 32, 33, 24, 35, 36, 37, 38,39, 40]
* 1 avatar = 1 jour = 1 requête


Flavie & Léa 13/10/2022 & 14/10/2022 : 
* 10 requêtes 1 avatar = 1 requetes = 1 jour, jour aléatoire

Remarques:
======================
**/.\ Attention** En exporant le set de test, on voit que le pays **belgian** est présent alors qu'il n'était pas mentionné dans la description des features fournie. Il faut donc le rajouter dans le tableau allrequest.csv
