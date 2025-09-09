#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 15:58:26 2025

@author: malos
"""

# local_analysis.py  —  Analyse locale à partir du CSV (pas de GitHub)
# Colonnes attendues dans ton CSV : RAD51, p53, WGD

import os, re
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# ====== 1) METS ICI LE CHEMIN ABSOLU DE TON CSV ======
DATA = "/Users/malos/Desktop/hugoinfo/merged_TP53_RAD51_WGD_norm.csv"  # <-- à adapter

csv_path = Path(DATA)
if not csv_path.exists():
    raise FileNotFoundError(f"CSV introuvable: {csv_path}")

# ====== 2) LECTURE + SÉLECTION COLONNES ======
df0 = pd.read_csv(csv_path)
need = ["RAD51","p53","WGD"]
missing = [c for c in need if c not in df0.columns]
if missing:
    raise SystemExit(f"Colonnes manquantes: {missing}\nColonnes dispo: {df0.columns.tolist()}")

df = df0[need].rename(columns={"RAD51":"RAD51_expr","p53":"TP53_effect"}).copy()

# ====== 3) NORMALISATION WGD (gère 1/0, WGD+/WGD-, oui/non, true/false) ======
def normalize_wgd(x):
    if pd.isna(x): return np.nan
    s = str(x).strip().lower().replace("−","-")
    if re.search(r"\bwgd\+\b|plus|oui|\b1\b|true|yes", s): return 1
    if re.search(r"\bwgd-\b|minus|non|\b0\b|false|no", s): return 0
    try:
        v = float(s)
        if v in (0.0, 1.0): return int(v)
    except Exception:
        pass
    return np.nan

df["WGD"] = df["WGD"].apply(normalize_wgd)

# Numérisation + nettoyage
for c in ["RAD51_expr","TP53_effect"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df = df.dropna(subset=["RAD51_expr","TP53_effect","WGD"]).astype({"WGD":int})

# Debug : effectifs par groupe
counts = df["WGD"].value_counts().to_dict()
print("Lignes par groupe WGD:", counts)
if df.empty:
    raise SystemExit("Après nettoyage, 0 ligne exploitable. Vérifie 'RAD51', 'p53', 'WGD' dans ton CSV.")

# ====== 4) RÉSULTATS CHIFFRÉS ======
out_dir = csv_path.parent / "results"
fig_dir = csv_path.parent / "figures"
out_dir.mkdir(exist_ok=True)
fig_dir.mkdir(exist_ok=True)

# Descriptif
desc = (df.groupby("WGD")
          .agg(n=("RAD51_expr","size"),
               RAD51_mean=("RAD51_expr","mean"),
               RAD51_sd=("RAD51_expr","std"),
               TP53_mean=("TP53_effect","mean"),
               TP53_sd=("TP53_effect","std"))
          .reset_index())
desc["group"] = desc["WGD"].map({0:"WGD-",1:"WGD+"})
desc = desc[["group","n","RAD51_mean","RAD51_sd","TP53_mean","TP53_sd"]]
desc.to_csv(out_dir/"summary_stats.csv", index=False)

# Corrélations par groupe
rows = []
for g, sub in df.groupby("WGD"):
    if len(sub) >= 3:
        pr = stats.pearsonr(sub["RAD51_expr"], sub["TP53_effect"])
        sr = stats.spearmanr(sub["RAD51_expr"], sub["TP53_effect"])
        rows.append({
            "group": "WGD+" if g==1 else "WGD-",
            "n": len(sub),
            "pearson_r": float(pr[0]), "pearson_p": float(pr[1]),
            "spearman_r": float(sr.correlation), "spearman_p": float(sr.pvalue)
        })
corr = pd.DataFrame(rows)
corr.to_csv(out_dir/"correlations.csv", index=False)

# Régression : interaction si 2 groupes, sinon simple
if df["WGD"].nunique() >= 2:
    model = smf.ols("TP53_effect ~ RAD51_expr * WGD", data=df).fit()
    slope_minus = model.params.get("RAD51_expr", np.nan)
    slope_plus  = slope_minus + model.params.get("RAD51_expr:WGD", 0.0)
else:
    print("⚠️ Un seul groupe WGD → modèle sans interaction.")
    model = smf.ols("TP53_effect ~ RAD51_expr", data=df).fit()
    slope_minus = model.params.get("RAD51_expr", np.nan)
    slope_plus  = np.nan

slopes = pd.DataFrame({
    "group": ["WGD-","WGD+"],
    "slope_RAD51_to_TP53": [slope_minus, slope_plus]
})
slopes.to_csv(out_dir/"simple_slopes.csv", index=False)
with open(out_dir/"model_summary.txt","w") as f:
    f.write(model.summary().as_text())

# ====== 5) FIGURES ======
def scatter_with_fit(sub, title, outfile):
    x = sub["RAD51_expr"].values
    y = sub["TP53_effect"].values
    plt.figure(figsize=(6,5))
    plt.scatter(x, y, alpha=0.7)
    if len(sub) >= 2:
        m, b = np.polyfit(x, y, 1)
        xs = np.linspace(np.nanmin(x), np.nanmax(x), 100)
        plt.plot(xs, m*xs + b)
    if len(sub) >= 3:
        pr = stats.pearsonr(x, y)
        sr = stats.spearmanr(x, y)
        txt = f"Pearson r={pr[0]:.3f}, p={pr[1]:.3g}\nSpearman r={sr.correlation:.3f}, p={sr.pvalue:.3g}"
        plt.gcf().text(0.02, 0.02, txt)
    plt.title(title)
    plt.xlabel("RAD51 expression")
    plt.ylabel("TP53 gene effect (CRISPR)")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(fig_dir/outfile, dpi=200, bbox_inches="tight")
    plt.close()

# Scatter par groupe
scatter_with_fit(df[df["WGD"]==0], "RAD51 vs TP53 — WGD−", "rad51_vs_tp53_WGD_minus.png")
scatter_with_fit(df[df["WGD"]==1], "RAD51 vs TP53 — WGD+",  "rad51_vs_tp53_WGD_plus.png")

# Boxplots
plt.figure(figsize=(6,5))
plt.boxplot([df.loc[df["WGD"]==0,"TP53_effect"].dropna(),
             df.loc[df["WGD"]==1,"TP53_effect"].dropna()],
            labels=["WGD−","WGD+"], showfliers=False)
plt.title("TP53 gene effect par groupe WGD")
plt.ylabel("TP53 gene effect")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(fig_dir/"tp53_by_WGD_box.png", dpi=200, bbox_inches="tight")
plt.close()

plt.figure(figsize=(6,5))
plt.boxplot([df.loc[df["WGD"]==0,"RAD51_expr"].dropna(),
             df.loc[df["WGD"]==1,"RAD51_expr"].dropna()],
            labels=["WGD−","WGD+"], showfliers=False)
plt.title("RAD51 expression par groupe WGD")
plt.ylabel("RAD51 expression")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(fig_dir/"rad51_by_WGD_box.png", dpi=200, bbox_inches="tight")
plt.close()

print(f"OK ✓  Résultats: {out_dir}")
print(f"OK ✓  Figures : {fig_dir}")
