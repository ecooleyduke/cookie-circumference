import pandas as pd
import numpy as np
from statsmodels.stats.power import TTestIndPower


def calculate_sample_size(cohen_d):
    analysis = TTestIndPower()

    alpha = 0.05 # significance level
    power = 0.80 # desired power (80%)
    alternative = 'two-sided' # we use two-sided since we are checking for a difference between multiple groups

    sample_size = analysis.solve_power(effect_size=cohen_d, power=power, alpha=alpha, alternative=alternative)

    print(f"Required sample size per group: {sample_size:.2f}")

