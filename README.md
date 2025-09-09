# Analysis of RAD51 & TP53 (WGD)

Analyse de l’expression **RAD51** et de l’**effet gène TP53** (CRISPR) selon le statut **WGD**.

**Liens rapides :**
- 📓 Notebook : [`notebooks/Analysis.ipynb`](notebooks/Analysis.ipynb)
- 🧮 Script Python : [`src/script.py`](src/script.py)
- 📄 Rapport : [PDF](docs/Analysis_RAD51_TP53.pdf)
- 📊 Données : [`data/`](data/) · 🖼️ Figures : [`figures/`](figures/)

---

## Contexte & objectif
On sépare les lignées en **WGD+** vs **WGD-** pour étudier l’expression **RAD51** et l’effet gène **TP53** (CRISPR).  
Question : le statut WGD influence-t-il la relation **RAD51 ↔ TP53** ?

## Méthode (résumé)
- Lecture des données (`OmicsSignaturesProfile.csv`, table fusionnée `merged_TP53_RAD51_WGD_norm.csv`).
- **Split WGD** : création de deux sous-ensembles (_WGD=1_ → WGD+, _WGD=0_ → WGD-) et export en CSV.
- Visualisation : nuages de points **RAD51 (x)** vs **TP53 gene effect (y)** pour **WGD+** et **WGD-**.
- (Dans le code/nb : utiliser des **chemins relatifs** type `data/...` et enregistrer les figures dans `figures/`.)

---

## Résultats (aperçu)

**WGD-**  
![RAD51 vs TP53 — WGD-](figures/Figure%20WGD-.png)

**WGD+**  
![RAD51 vs TP53 — WGD+](figures/Figure%20WGD%2B.png)

---

## Données
- [`data/CCLE_expression.csv`](data/CCLE_expression.csv) — expression génique (CCLE)
- [`data/Achilles_gene_effect.csv`](data/Achilles_gene_effect.csv) — gene effect CRISPR (Achilles/DepMap)
- [`data/merged_TP53_RAD51_WGD_norm.csv`](data/merged_TP53_RAD51_WGD_norm.csv) — table fusionnée
- [`data/cell_lines_WGD_oui.csv`](data/cell_lines_WGD_oui.csv) · [`data/cell_lines_WGD_non.csv`](data/cell_lines_WGD_non.csv) — listes WGD+/WGD−
- [`data/OmicsSignaturesProfile.csv`](data/OmicsSignaturesProfile.csv)

---

## Reproduire rapidement

### Optio

