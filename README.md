<div align="center">

# Analysis of RAD51 & TP53 (WGD)

[![Python](https://img.shields.io/badge/Python-3.x-blue)](#)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](#)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](#)

**Étude de l’expression `RAD51` et de l’effet gène `TP53` (CRISPR) selon le statut WGD.**

</div>

---

## 🔗 Liens directs

- 📄 **Rapports**
  - PDF : [`docs/Analysis_of_RAD51_and_TP53.pdf`](docs/Analysis_of_RAD51_and_TP53.pdf)
  - Word : [`docs/Analysis of RAD51 and TP53.docx`](docs/Analysis%20of%20RAD51%20and%20TP53.docx)

- 📓 **Notebook**
  - [`notebooks/Analysis.ipynb`](notebooks/Analysis.ipynb)

- 🧮 **Scripts**
  - Analyse statistiques : [`src/stats.py`](src/stats.py)
  - Figures : [`src/plots.py`](src/plots.py)
  - Pipeline/Autres : [`src/script.py`](src/script.py)

- 📊 **Données**
  - [`data/merged_TP53_RAD51_WGD_norm.csv`](data/merged_TP53_RAD51_WGD_norm.csv)
  - [`data/cell_lines_WGD_oui.csv`](data/cell_lines_WGD_oui.csv)
  - [`data/cell_lines_WGD_non.csv`](data/cell_lines_WGD_non.csv)
  - [`data/OmicsSignaturesProfile.csv`](data/OmicsSignaturesProfile.csv)
  - *(volumineux → mettre en Releases/LFS au besoin)* `CCLE_expression.csv`, `Achilles_gene_effect.csv`

- 📦 **Résultats**
  - Descriptif : [`results/summary_stats.csv`](results/summary_stats.csv)  
  - Corrélations : [`results/correlations.csv`](results/correlations.csv)  
  - Pentes (slopes) : [`results/simple_slopes.csv`](results/simple_slopes.csv)  
  - Régression (texte) : [`results/model_summary.txt`](results/model_summary.txt)

---

## 🖼️ Figures (aperçu)

**Scatter RAD51 ↔ TP53 (WGD− / WGD+)**  
<br>
<img src="figures/rad51_vs_tp53_WGD_minus.png" width="48%"> <img src="figures/rad51_vs_tp53_WGD_plus.png" width="48%">

**Boxplots par groupe WGD**  
<br>
<img src="figures/rad51_by_WGD_box.png" width="48%"> <img src="figures/tp53_by_WGD_box.png" width="48%">

**Figures initiales**  
<br>
<img src="figures/Figure%20WGD-.png" width="48%"> <img src="figures/Figure%20WGD%2B.png" width="48%">

---

## 🧪 Méthode (résumé)

- Construction du statut **WGD** (0/1) à partir des listes WGD+/WGD−.  
- Table minimale : `RAD51_expr` (depuis `RAD51`), `TP53_effect` (depuis `p53`), `WGD`.  
- **Stats** : descriptif par groupe, corrélations par groupe, régression `TP53_effect ~ RAD51_expr * WGD`.  
- **Figures** : scatters (régression par groupe) + boxplots.  
- Sorties écrites dans `results/` et `figures/`.

---

## ▶️ Reproduire localement
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pandas numpy scipy statsmodels matplotlib
python src/stats.py   # -> results/
python src/plots.py   # -> figures/

## 🗂️ Arborescence

- 📁 **data/**
  - merged_TP53_RAD51_WGD_norm.csv
  - cell_lines_WGD_oui.csv • cell_lines_WGD_non.csv
  - OmicsSignaturesProfile.csv
- 📁 **figures/**
  - rad51_vs_tp53_WGD_minus.png • rad51_vs_tp53_WGD_plus.png
  - tp53_by_WGD_box.png • rad51_by_WGD_box.png
  - Figure WGD+.png • Figure WGD-.png
- 📁 **results/** → summary_stats.csv, correlations.csv, simple_slopes.csv, model_summary.txt
- 📁 **src/** → script.py, stats.py, plots.py
- 📁 **notebooks/** → Analysis.ipynb
- 📁 **docs/** → Analysis_of_RAD51_and_TP53.pdf, Analysis of RAD51 and TP53.docx
- 📄 **README.md**


