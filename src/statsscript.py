#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 15:40:28 2025

@author: malos
"""


import os, re
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.formula.api as smf
from pathlib import Path


DATA = "/Users/malos/Desktop/hugoinfo/merged_TP53_RAD51_WGD_norm.csv"  # <-- adapte si besoin


df0 = pd.read_csv(DATA)
need = ["RAD51", "p53", "WGD"]
missing = [c for c in need if c not in df0.columns]
if missing:
    raise SystemExit(f"Colonnes introuvables : {missing}\nColonnes dispo : {df0.columns.tolist()}")

df = df0[need].rename(columns={"RAD51":"RAD51_expr","p53":"TP53_effect"}).copy()


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


for c in ["RAD51_expr","TP53_effect"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df = df.dropna(subset=["RAD51_expr","TP53_effect","WGD"])
df["WGD"] = df["WGD"].astype(int)


counts = df["WGD"].value_counts().to_dict()
print("Lignes par groupe WGD:", counts)
if df.empty:
    raise SystemExit("Après nettoyage, 0 ligne exploitable. Vérifie que 'RAD51', 'p53' et 'WGD' contiennent des valeurs.")


desc = (df.groupby("WGD")
          .agg(n=("RAD51_expr","size"),
               RAD51_mean=("RAD51_expr","mean"),
               RAD51_sd=("RAD51_expr","std"),
               TP53_mean=("TP53_effect","mean"),
               TP53_sd=("TP53_effect","std"))
          .reset_index())
desc["group"] = desc["WGD"].map({0:"WGD-",1:"WGD+"})
desc = desc[["group","n","RAD51_mean","RAD51_sd","TP53_mean","TP53_sd"]]


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


if df["WGD"].nunique() >= 2:
    model = smf.ols("TP53_effect ~ RAD51_expr * WGD", data=df).fit()
    slope_minus = model.params.get("RAD51_expr", np.nan)
    slope_plus  = slope_minus + model.params.get("RAD51_expr:WGD", 0.0)
else:
    print("⚠️ Un seul groupe WGD présent → modèle sans interaction.")
    model = smf.ols("TP53_effect ~ RAD51_expr", data=df).fit()
    slope_minus = model.params.get("RAD51_expr", np.nan)
    slope_plus  = np.nan

slopes = pd.DataFrame({
    "group": ["WGD-","WGD+"],
    "slope_RAD51_to_TP53": [slope_minus, slope_plus]
})


out_dir = Path(DATA).parent / "results"
out_dir.mkdir(exist_ok=True)
desc.to_csv(out_dir / "summary_stats.csv", index=False)
corr.to_csv(out_dir / "correlations.csv", index=False)
slopes.to_csv(out_dir / "simple_slopes.csv", index=False)
with open(out_dir / "model_summary.txt","w") as f:
    f.write(model.summary().as_text())

print(f"OK ✓  Résultats écrits dans: {out_dir}")
