# Cookie Temperature Experiment
Module Project 2: Statistical Analysis

## Overview
This project investigates how oven temperature affects cookie circumference.
Three temperature conditions were tested — 325°F, 350°F, and 375°F — using 11 cookies per group.
Cookies were measured after baking, and statistical tests were used to determine whether differences in average cookie size were significant.

## Research Question
Does oven temperature significantly affect the circumference of cookies?

## Hypotheses
**Null Hypothesis (H₀)**: Oven temperature has no effect on cookie circumference.

**Alternative Hypothesis (H₁)**: Oven temperature affects cookie circumference.

## Repository Structure
```
├── data/
│   └── cookies_data.csv           # Raw data file (circumference measurements)
│
├── scripts/
│   ├── power_analysis.py          # Power analysis for sample size determination
│   └── t_test_analysis.py    # Performs t-tests and calculates effect sizes
│
├── README.md                      # This file
```

## Experimental Design
- Independent variable: Oven temperature (325°F, 350°F, 375°F)
- Dependent variable: Cookie circumference (cm)
- Design: Between-subjects; each group baked at a fixed temperature
- Sample size: 11 cookies per temperature condition

## Statistical Methods
- Independent-samples t-tests were performed to compare mean circumferences between each pair of temperature conditions.
- All comparisons yielded p < 0.001, indicating statistically significant differences in cookie size.

## Reproduction Instructions
Clone this repository:
`git clone https://github.com/ecooleyduke/cookie-circumference.git`
`cd cookie-temperature-experiment`
Install dependencies:
`pip install -r requirements.txt`

## Blog Post

📖 Read the full blog post on Byline:  
[Does baking temperature affect the average circumference of homemade cookies?](https://bylinedocs.com/published/0d37b701-067e-461f-819d-a310c2a23a74)