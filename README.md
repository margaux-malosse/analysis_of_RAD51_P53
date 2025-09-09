<div align="center">

# Analysis of RAD51 & TP53 (WGD)

[![Python](https://img.shields.io/badge/Python-3.x-blue)](#)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](#)
[![WGD](https://img.shields.io/badge/WGD-Plus%20%7C%20Minus-purple)](#)

**Étude de l’expression `RAD51` et de l’effet gène `TP53` (CRISPR) selon le statut WGD.**

</div>

---

## 🔗 Liens rapides
-  **Rapport (PDF)** : [`docs/Analysis_of_RAD51_and_TP53.pdf`](docs/Analysis_of_RAD51_and_TP53.pdf)
-  **Notebook** : [`notebooks/Analysis.ipynb`](notebooks/Analysis.ipynb)
-  **Script Python** : [`src/script.py`](src/script.py)
-  **Données** : [`data/`](data/) &nbsp;·&nbsp;
-  **Figures** : [`figures/`](figures/)

---

## 🖼️ Aperçu visuel

**WGD−**  
![RAD51 vs TP53 — WGD−](figures/Figure%20WGD-.png)

**WGD+**  
![RAD51 vs TP53 — WGD+](figures/Figure%20WGD%2B.png)

> 🔎 Les détails d’interprétation sont dans le PDF : [`docs/Analysis_of_RAD51_and_TP53.pdf`](docs/Analysis_of_RAD51_and_TP53.pdf)

---

## 📂 Données (chemins)
- [`data/merged_TP53_RAD51_WGD_norm.csv`](data/merged_TP53_RAD51_WGD_norm.csv)
- [`data/cell_lines_WGD_oui.csv`](data/cell_lines_WGD_oui.csv) · [`data/cell_lines_WGD_non.csv`](data/cell_lines_WGD_non.csv)
- [`data/OmicsSignaturesProfile.csv`](data/OmicsSignaturesProfile.csv)
-  `CCLE_expression.csv`, `Achilles_gene_effect.csv` → en **Releases** ou via **Git LFS**.

---

<details>
<summary><strong>🧪 Méthode (clique pour dérouler)</strong></summary>

**Objectif.** Tester si la relation entre l’expression **RAD51** et l’**effet gène TP53** diffère selon le statut **WGD**.

**Pipeline.**
1. **Statut WGD.** Construction de `WGD` (0/1) à partir des listes `cell_lines_WGD_oui.csv` (→1) et `cell_lines_WGD_non.csv` (→0) via un identifiant commun (idéalement `DepMap_ID`).
2. **Table d’analyse.** À partir de `merged_TP53_RAD51_WGD_norm.csv`, conserver au minimum :
   - `RAD51_expr` (expression normalisée),
   - `TP53_effect` (gene effect CRISPR),
   - `WGD` (0/1).
   Retirer les lignes incomplètes.
3. **Stats.**
   - Descriptif par groupe : `n`, moyenne, écart-type.
   - Corrélations **par groupe** (WGD−, WGD+).
   - Modèle avec interaction : `TP53_effect ~ RAD51_expr * WGD` (teste la différence de pente entre groupes).
4. **Plots.** Scatter RAD51 (x) vs TP53 (y) pour **WGD−** et **WGD+**, + régression par groupe.  
   Export PNG haute résolution dans `figures/`.

</details>

- 📁 **data/**
  - merged_TP53_RAD51_WGD_norm.csv
  - cell_lines_WGD_oui.csv
  - cell_lines_WGD_non.csv
  - OmicsSignaturesProfile.csv
- 📁 **figures/** → Figure WGD+.png, Figure WGD-.png
- 📁 **notebooks/** → Analysis.ipynb
- 📁 **src/** → script.py
- 📁 **docs/** → Analysis_of_RAD51_and_TP53.pdf, Analysis of RAD51 and TP53.docx
- 📄 **README.md**
