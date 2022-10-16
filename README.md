# Defi-IA-bedbugs
https://www.kaggle.com/code/maxhalford/tutoriel-d-fi-ia-2023/notebook

clé : 
f80b400f-3d29-43f0-8049-214a756ff0b3

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
======================
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
** /.\ Attention ** En exporant le set de test, on voit que le pays **belgian** est présent alors qu'il n'était pas mentionné dans la description des features fournie. Il faut donc le rajouter dans le tableau allrequest.csv
