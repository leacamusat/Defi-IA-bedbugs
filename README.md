Petit document récapitulatif : https://www.overleaf.com/7664353796mnjshyqhnbwb 

# Defi-IA-bedbugs
https://www.kaggle.com/code/maxhalford/tutoriel-d-fi-ia-2023/notebook


clé : 
f80b400f-3d29-43f0-8049-214a756ff0b3

-------------------------------------------
# Organisation des fichiers 
**dossier_local /</br>
&emsp; &emsp;├─models_sav/</br>
&emsp; &emsp; &emsp; &emsp;├─ xgboost.sav </br>
&emsp; &emsp;&emsp; &emsp; ├─ .sav</br>
&emsp; &emsp;├─ application gradio </br>
&emsp; &emsp;├─ Modeles.ipynb</br>
&emsp; &emsp;├─ soumission_kaggle.ipynb

**
## Lancer l'application gradio 

python gradio_defiIA.py --model_name ``nom_modèle`` --scaler_name ``nom_standard_scaler_modèle``
ex : ``python gradio_defiIA.py --model_name "X_gboost_tuned_model.sav" --scaler_name 'Standard_Scaler.sav'``

## Note : le modèle Random forest est très lourd ( trop lours pour github) il est sur mon ordinateur

Réponses à Lila :
    Dans la commande chosen_idx = np.random.choice(idx_available, replace = False, size = nb_request), on tire aléatoirement sans remise len(df) = 468 éléments parmi une liste de taille 468: [0,1,...,467] ce qui revient exactement à choisir la liste [0,1,...,467] directement (sans avoir besoin du random.choice). Est-ce voulu ? 

    our_requests = pandas.read_csv('all_our_requests_done.csv', header = 0) au début, ce tableau est vide non ? Pour la première utilisation, il s'agit de allrequest.csv ? J'imagine qu'à l'origine il devait y avoir marqué allrequest.csv et non pas all_our_requests_done.csv. 
    ``Pour la première utilisation on a crée un tableau vide avec seulement les noms des colonnes qu'on souhaite ``

    On a days= np.random.choice(selected_days, number_days, replace=False) et days= np.random.choice(range(0,45), number_days, replace=False) à la suite donc seule la 2e version est prise en compte.
    

    On crée un "avatar_name" avec la date du jour mais après je n'ai pas l'impression qu'on stocke cette info quelque part. Une fois le tableau constitué, on ne peut pas retrouver cette info. ``en effet in stocke que l'ID c'est bizarre... j'ai créé à la fin du code une partie pour enregistrer une table de conversion entre les deux, a voir si tu veux fusionner dans nos datas, ou alor on ira juste lire ??? ``

    l'Id de a request est i dans la ligne add_to_our_requests = ... mais du coup, si on fait tourner plusieurs fois le même code, on n'aura pas des requêtes avec le même id ? comment on va faire pour les différencier ? Il ne faudrait pas mettre request_num à la place de i ? ``je ne suis pas sure d'avoir compris la question, mais je crois que le numéro de la requête c'est à quelle requete ca correspond dans notre tableau avec toutes les permutation de requests possibles qu'on a crées. 



Tâches à réasliser: 
======================

- [X] 1° analyser les habitudes de navigation (set d'évaluation) => optimisation des requêtes. (Lila et autre)
  * Première description du jeu de données
  * Calcul des villes et langues les plus recherchées
  * Répartition de la variable date
  * Calcul du nombre de requêtes par personne
  * Calul du nombre de personnes ayant utilisé plusieurs langues pour leurs requêtes
  * Calul du nombre de personnes ayant utilisé le téléphone et l'ordinateur

- [ ] 2° construire une grande matrice avec toutes les combinaisons possibles en ligne (ville, langue, mobile). Pour les dates faire un tirage aléatoire à posteriori (une au début puis plusieurs, ATTENTION : ranger dans l'ordre décroissant les requêtes 

- [ ] 3° créer le tirage et créer la requête. 


Historique des requêtes: 
========================


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
