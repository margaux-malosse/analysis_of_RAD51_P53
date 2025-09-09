#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:41:12 2025

@author: malos
"""

#ici on importe la variable panda qui nous permet d'étudier des caractères biologiques 
import pandas as pd

#ici on crée une dataframe donc un cadre de l'ecture qui nous permet d'ouvrir le fichier
# de le lire et de l'étudier 
df = pd.read_csv("/Users/malos/Desktop/hugoinfo/OmicsSignaturesProfile.csv")

#Ici on groupe les lignés en fonction de leur atribut donc WGD oui ou non 
df_wgd_oui = df[df["WGD"] == 1.0]
df_wgd_non = df[df["WGD"] == 0.0]

#ici on affiche les ligné qui sont oui et non pour vérifier que bien groupé. 
print("Lignées WGD = oui :")
print(df_wgd_oui)

print("\nLignées WGD = non :")
print(df_wgd_non)


# la on save les lignées dans deux fichiers en fonction de leur caractéristique
# donc WGD = oui ou WGD = non
df_wgd_oui.to_csv("cell_lines_WGD_oui.csv", index=False)
df_wgd_non.to_csv("cell_lines_WGD_non.csv", index=False)

#la on affiche que les fichiers on été créee pour valider le code et les récupérer 
print("Fichiers créés :")
print(" cell_lines_WGD_oui.csv")
print(" cell_lines_WGD_non.csv")



# importe les variable bio python pour récupéré les info biologiques 
import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier final qui comporte les différentes colonne d'intéret 
df_final = pd.read_csv("/Users/malos/Desktop/hugoinfo/merged_TP53_RAD51_WGD_norm.csv")

# Vérifie les colonnes comporte les bonnes info donc p53, RAD51 et WGD
print(df_final.columns.tolist())  

# Séparer par statut WGD donc oui ou non 
df_oui = df_final[df_final["WGD"] == "oui"]
df_non = df_final[df_final["WGD"] == "non"]

# on fait le graph avec le parametre WGD oui 
plt.figure(figsize=(6, 5))
plt.scatter(df_oui["p53"], df_oui["RAD51"], alpha=0.6, color="blue")
plt.xlabel("Expression RAD51")
plt.ylabel("TP53 gene effect")
plt.title("RAD51 expression vs TP53 knockout (CRISPR) WGD +")
plt.grid(True, linestyle="--", alpha=0.5)
# plt.show()

# on fait le graph avec le paramettre WGD non 
plt.figure(figsize=(6, 5))
plt.scatter(df_non["p53"], df_non["RAD51"], alpha=0.6, color="red")
plt.xlabel("Expression RAD51")
plt.ylabel("TP53 gene effect")
plt.title("RAD51 expression vs TP53 knockout (CRISPR) WGD -")
plt.grid(True, linestyle="--", alpha=0.5)
# plt.show()
