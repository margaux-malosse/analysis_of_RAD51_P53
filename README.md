# Analysis of RAD51 & TP53 (WGD)

Étude de l’expression **RAD51** et de l’**effet gène TP53** (CRISPR) en fonction du statut **WGD** (Whole-Genome Doubling).

**Liens rapides**
-  Rapport (PDF) : [`docs/Analysis_of_RAD51_and_TP53.pdf`](docs/Analysis_of_RAD51_and_TP53.pdf)
-  Notebook : [`notebooks/Analysis.ipynb`](notebooks/Analysis.ipynb)
-  Script Python : [`src/script.py`](src/script.py)
-  Données : [`data/`](data/) ·
-  Figures : [`figures/`](figures/)

---

## Contexte & objectif
L’objectif est de caractériser la relation entre **RAD51 (expression)** et **TP53 (gene effect CRISPR)** et de tester si cette relation **diffère selon le statut WGD** des lignées cellulaires.  
On produit des visualisations séparées **WGD+** et **WGD−**, ainsi qu’un test statistique avec **interaction** (voir Méthode).

---

## Données utilisées (dans `data/`)
- `merged_TP53_RAD51_WGD_norm.csv` — table de travail intégrant RAD51/TP53 et métadonnées
- `cell_lines_WGD_oui.csv` · `cell_lines_WGD_non.csv` — listes des lignées WGD+ / WGD−
- `OmicsSignaturesProfile.csv` — signatures (utilisées dans certaines analyses)
- *(optionnel / volumineux)* `CCLE_expression.csv` — expression génique (CCLE)
- *(optionnel / volumineux)* `Achilles_gene_effect.csv` — gene effect CRISPR (DepMap/Achilles)

> Si `CCLE_expression.csv` et `Achilles_gene_effect.csv` sont trop gros, place-les en **Release** ou gérez-les via **Git LFS**.  
> Le pipeline principal fonctionne déjà avec `merged_TP53_RAD51_WGD_norm.csv` + listes WGD.

---

## Méthode (détaillée)

1. **Harmonisation des identifiants**  
   - Colonnes d’identifiants attendues : `DepMap_ID` (prioritaire) ou `stripped_cell_line_name`.  
   - Normalisation des noms : minuscules, suppression des espaces/ponctuation pour la jointure si besoin.

2. **Attribution du statut WGD**  
   - Construction d’une variable binaire `WGD` à partir de `cell_lines_WGD_oui.csv` (→ `WGD=1`) et `cell_lines_WGD_non.csv` (→ `WGD=0`).  
   - Jointure sur l’identifiant choisi (idéalement `DepMap_ID`).

3. **Table d’analyse**  
   - Variables minimales :  
     - `RAD51_expr` (valeur normalisée telle que fournie dans les données)  
     - `TP53_effect` (gene effect CRISPR)  
     - `WGD` (0/1)  
   - Filtre : suppression des lignes sans valeur pour l’une des trois variables.

4. **Statistiques & tests**  
   - **Descriptif** : moyenne, écart-type, n par groupe WGD.  
   - **Corrélations** : Pearson et Spearman **dans chaque groupe** (WGD+ et WGD−).  
   - **Régression avec interaction** :  
     - Modèle : `TP53_effect ~ RAD51_expr * WGD`  
     - Interprétation : le terme d’interaction teste si la pente (lien RAD51→TP53) **diffère** entre WGD+ et WGD−.  
     - Robustesse : en cas d’outliers, estimation robuste (Huber) en plus du modèle OLS.

5. **Visualisations**  
   - Deux nuages de points :  
     - `RAD51_expr` (x) vs `TP53_effect` (y) **WGD−**  
     - `RAD51_expr` (x) vs `TP53_effect` (y) **WGD+**  
   - Ajout d’une ligne de tendance (régression simple par groupe).  
   - Export PNG haute résolution dans `figures/`.

6. **Exports**  
   - Figures : `figures/rad51_tp53_WGD_minus.png` et `figures/rad51_tp53_WGD_plus.png`  
     *(si tu gardes les noms actuels : `Figure WGD-.png` et `Figure WGD+.png`)*  
   - Tableau de synthèse (optionnel) : `results/summary_stats.csv` (corrélations, tailles d’échantillon, p-values).

---

## Résultats (aperçu)

**WGD−**  
![RAD51 vs TP53 — WGD−](figures/Figure%20WGD-.png)

**WGD+**  
![RAD51 vs TP53 — WGD+](figures/Figure%20WGD%2B.png)

> Les interprétations détaillées sont dans le **PDF** : [`docs/Analysis_of_RAD51_and_TP53.pdf`](docs/Analysis_of_RAD51_and_TP53.pdf).
