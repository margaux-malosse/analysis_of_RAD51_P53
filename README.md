# Analysis of RAD51 & TP53 (WGD)

Analyse de l’expression **RAD51** et de l’**effet gène TP53** (CRISPR) selon le statut **WGD**.

**Liens rapides :**
-  Notebook : [`notebooks/Analysis.ipynb`](notebooks/Analysis.ipynb)
-  Script Python : [`src/script.py`](src/script.py)
-  Rapport Word : [`docs/Analysis of RAD51 and TP53.docx`](docs/Analysis%20of%20RAD51%20and%20TP53.docx)
-  Données : [`data/`](data/) ·
-  Figures : [`figures/`](figures/)

---

## Aperçu des résultats

**WGD-**  
![RAD51 vs TP53 — WGD-](figures/Figure%20WGD-.png)

**WGD+**  
![RAD51 vs TP53 — WGD+](figures/Figure%20WGD%2B.png)

---

## Données

- [`data/CCLE_expression.csv`](data/CCLE_expression.csv) — expression génique (CCLE)
- [`data/Achilles_gene_effect.csv`](data/Achilles_gene_effect.csv) — gene effect CRISPR (Achilles/DepMap)
- [`data/merged_TP53_RAD51_WGD_norm.csv`](data/merged_TP53_RAD51_WGD_norm.csv) — table fusionnée
- [`data/cell_lines_WGD_oui.csv`](data/cell_lines_WGD_oui.csv) · [`data/cell_lines_WGD_non.csv`](data/cell_lines_WGD_non.csv) — listes WGD+/WGD-
- [`data/OmicsSignaturesProfile.csv`](data/OmicsSignaturesProfile.csv)

---

## Reproduire rapidement

### Option 1 — Notebook
```bash
git clone https://github.com/margaux-malosse/analysis_of_RAD51_P53.git
cd analysis_of_RAD51_P53
# Ouvrir notebooks/Analysis.ipynb dans Jupyter
