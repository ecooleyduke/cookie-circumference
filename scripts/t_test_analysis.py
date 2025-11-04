import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


def calculate_t_test_statistics(df):
    group_325 = df[df["Temperature"] == 325]["Circumference"].values
    group_350 = df[df["Temperature"] == 350]["Circumference"].values
    group_375 = df[df["Temperature"] == 375]["Circumference"].values

    def cohens_d(x, y):
        nx, ny = len(x), len(y)
        pooled_std = np.sqrt(((nx - 1)*np.var(x, ddof=1) + (ny - 1)*np.var(y, ddof=1)) / (nx + ny - 2))
        d = (np.mean(x) - np.mean(y)) / pooled_std
        return d

    pairs = {
        "325 vs 350": (group_325, group_350),
        "325 vs 375": (group_325, group_375),
        "350 vs 375": (group_350, group_375)
    }

    for label, (a, b) in pairs.items():
        t_stat, p_val = ttest_ind(a, b, equal_var=True)
        d = cohens_d(a, b)
        print(f"\nComparison: {label}")
        print(f"Mean A: {np.mean(a):.2f}, Mean B: {np.mean(b):.2f}")
        print(f"t = {t_stat:.2f}, p = {p_val:.4f}, Cohen's d = {abs(d):.2f}")