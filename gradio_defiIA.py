import argparse
import gradio as gr
import torch
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt #to plot graphs
import seaborn as sns #to plot graphs
import pylab 
#----- Machine Learning Preprocessing 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import scipy.stats as stats
import random
#save model 
import pickle 
import argparse #arguments à passer avec la ligne de commande :)
from math import *

#pour l'appeler : python gradio_defiIA.py --model_name "X_gboost_tuned_model.sav" --scaler_name 'Standard_Scaler.sav'
parser = argparse.ArgumentParser()

parser.add_argument('--model_name', type=str, default = "X_gboost_tuned_model.sav", help='name of the file corresponding to the modelfitted')
parser.add_argument('--scaler_name', type=str, default = 'Standard_Scaler.sav', help='name of the file corresponding to the scaler transform fitted')
parser.add_argument('--var_kept', type=int, default = 2, help='variables we have decided to kept')

args = parser.parse_args()
model = args.model_name
standard_scaler=args.scaler_name
variables_kept=args.var_kept
model_folder=".//models_sav/"

loaded_model = pickle.load(open(model_folder+model, 'rb'))
scalar_model = pickle.load(open(model_folder+standard_scaler, 'rb'))

def predict_price(hotel_id_g,stock_g,city_g,date_g,language_g,mobile_g, avatar_id_g,request_number_g ,group_g,brand_g,parking_g,pool_g,children_policy_g):
    
    if children_policy_g=="interdit aux mineurs":# récupération variable children_policy
        children_policy=2
    elif children_policy_g=="interdits aux moins de 12 ans":
        children_policy=1
    else :
        children_policy=0
        
    parking = 1 if parking_g else 0 #récupération var parking et transformation en int 
    pool = 1 if pool_g else 0  #récupération var piscine et transformation en int 
    mobile=1 if mobile_g else 0: #récupération var mobile et transformation en int 
        
    ar = np.array([[hotel_id_g,stock_g,city_g,date_g,language_g,mobile, avatar_id_g,request_number_g ,group_g,brand_g,parking,pool,children_policy]]) #création d'un np array avec les différentes valeurs des différentes variables
    
        df = pd.DataFrame(ar, index = ['a1'], columns = ["hotel_id","stock","city","date","language","mobile","avatar_id","request_number" ,"group","brand","parking","pool","children_policy"]) #création du dataframe avec les bons noms de colonnes 
    int_list = ["date","avatar_id","hotel_id","stock","request_number"] #variables quantitatives 
    df[int_list] = df[int_list].astype(int) #transformations en int 
    #--- Convert to categorical: 
    df["city"] = pd.Categorical(df["city"],ordered=False)
    df["language"] = pd.Categorical(df["language"],ordered=False)
    df["mobile"] = pd.Categorical(df["mobile"],ordered=False)
    df["parking"] = pd.Categorical(df["parking"],ordered=False)
    df["pool"] = pd.Categorical(df["pool"],ordered=False)
    df["children_policy"] = pd.Categorical(df["children_policy"],ordered=False)
    df["group"] = pd.Categorical(df["group"],ordered=False)
    df["brand"] = pd.Categorical(df["brand"],ordered=False)
    df["stock"]=df["stock"].map(lambda x: log(x+1))
    #-------------------------------------------------
    # Liste des variables categorical: 
    cat_list1 = ["city", "language", "brand","mobile","parking","pool","children_policy"] #avec brand
    
    
    if variables_kept==3:
        cat_list = ["city", "language", "brand", "group","mobile","parking","pool","children_policy"] #avec brand & group
    
        cat_list_dummies=['city_copenhagen', 'city_madrid',
       'city_paris', 'city_rome', 'city_sofia', 'city_valletta', 'city_vienna',
       'city_vilnius', 'language_belgian', 'language_bulgarian',
       'language_croatian', 'language_cypriot', 'language_czech',
       'language_danish', 'language_dutch', 'language_estonian',
       'language_finnish', 'language_french', 'language_german',
       'language_greek', 'language_hungarian', 'language_irish',
       'language_italian', 'language_latvian', 'language_lithuanian',
       'language_luxembourgish', 'language_maltese', 'language_polish',
       'language_portuguese', 'language_romanian', 'language_slovakian',
       'language_slovene', 'language_spanish', 'language_swedish',
       'brand_Ardisson', 'brand_Boss Western', 'brand_Chill Garden Inn',
       'brand_Corlton', 'brand_CourtYord', 'brand_Ibas', 'brand_Independant',
       'brand_J.Halliday Inn', 'brand_Marcure', 'brand_Morriot',
       'brand_Navatel', 'brand_Quadrupletree', 'brand_Royal Lotus',
       'brand_Safitel', 'brand_Tripletree', 'group_Boss Western',
       'group_Chillton Worldwide', 'group_Independant',
       'group_Morriott International', 'group_Yin Yang', 'mobile_1', 'parking_1', 'pool_1', 'children_policy_1','children_policy_2',"hotel_id", "stock", "request_number", "date"]
    if variables_kept==2:
        cat_list = ["city", "language", "group","mobile","parking","pool","children_policy"] #avec group
        cat_list_dummies=['city_copenhagen', 'city_madrid',
       'city_paris', 'city_rome', 'city_sofia', 'city_valletta', 'city_vienna',
       'city_vilnius', 'language_belgian', 'language_bulgarian',
       'language_croatian', 'language_cypriot', 'language_czech',
       'language_danish', 'language_dutch', 'language_estonian',
       'language_finnish', 'language_french', 'language_german',
       'language_greek', 'language_hungarian', 'language_irish',
       'language_italian', 'language_latvian', 'language_lithuanian',
       'language_luxembourgish', 'language_maltese', 'language_polish',
       'language_portuguese', 'language_romanian', 'language_slovakian',
       'language_slovene', 'language_spanish', 'language_swedish',
        'group_Boss Western',
       'group_Chillton Worldwide', 'group_Independant',
       'group_Morriott International', 'group_Yin Yang', 'mobile_1', 'parking_1', 'pool_1', 'children_policy_1','children_policy_2',"hotel_id", "stock", "request_number", "date"]
    # Liste des variables quantitatives: 
    quant_list1 = ["hotel_id", "stock","request_number", "date"] #on a enlevé avatar_id et price (=variable à expliquer)

    # Création de la dataframe train
    pricingDum  = pd.get_dummies(df[cat_list],drop_first = True) #mise en forme 0-1 hot
    pricingQuant = df[quant_list1]#récupération des var quantitatives 
    

    
    dfC_eval_set = pd.concat([pricingDum ,pricingQuant],axis=1)#concaténation quanti et quali pour former X 
    dfC_eval_set = dfC_eval_set.reindex(columns =cat_list_dummies, fill_value=0)#ajour des colonnes des autres modalités manquantes et mise à 0 (ex : si la politique d'enfants est 2, seule la colonne children_2 avait était créée avec un 1, on rajoute une colonne children_1 avec la valeur de 0, de manière à avoir les mêmes colonnes que X_train
    dfC_eval_setr=scalar_model.transform(dfC_eval_set) #scalar reduction 
    Xr_test_gradio=pd.DataFrame(dfC_eval_setr, index=dfC_eval_set.index, columns=dfC_eval_set.columns)#transformation en dataframe
    print("dfC_eval_setr", dfC_eval_setr)
    return "la chambre coutera" + str((loaded_model.predict(Xr_test_gradio))**2) + " €" #prédiction avec le modèle (on met au carré car on avait transformé avec une racine carrée 


if __name__=='__main__':
   
    
    gr.Interface(fn=predict_price, 
                inputs=[gr.Slider(0, 998, 1, label="hotel_id"), #curseur entre 0 et 998 de 1 en 1 
                gr.Slider(0, 199, 1, label="stock"), #curseur de 1 et 1 
                gr.Dropdown(['amsterdam', 'copenhagen', 'madrid','paris', 'rome', 'sofia', 'valletta', 'vienna', 'vilnius'], label="ville"),#liste déroulante 
                gr.Slider(0,44, 1, label="date"),
                gr.Dropdown(['austrian', 'belgium', 'bulgarian', 'croatian', 'cypriot', 'czech', 'danish', 'dutch', 'estonian', 'finnish', 'french', 'german', 'greek', 'hungarian', 'irish', 'italian', 'latvian', 'lithuanian', 'luxembourgish', 'maltese', 'polish', 'portuguese', 'romanian', 'slovakian', 'slovene', 'spanish','swedish'], label="langage"),
                gr.Checkbox(label="mobile?"), #case à cocher 
                gr.Textbox(label="User_ID"),
                gr.Textbox(label="request_number"), #case à remplir
                gr.Dropdown(['Accar Hotels', 'Boss Western'], label="group"),
                gr.Dropdown(['Marcure', 'Independant'], label="brand"),

                gr.Checkbox(label="Parking?"),
                gr.Checkbox(label="Piscine?"),
                gr.Radio(["interdit aux mineurs", "interdits aux moins de 12 ans", "pas de restriction"], label="Politique enfant" )], 
                outputs="text", #sortie de l'application (ici un int)
                live=True,
                description="Prédit le prix d'une nuit à l'hotel donnée par l'application de voyage",
                ).launch(debug=True, share=True);