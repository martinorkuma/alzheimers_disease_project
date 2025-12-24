# Load libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import ttest_ind, chi2_contingency

# Recall
df = pd.read_csv('alzheimers_disease_data.csv') 

# Chi-square tests for categorical variables
hypertension_chi2 = chi2_contingency(pd.crosstab(df["Diagnosis"], df["Hypertension"]))
diabetes_chi2 = chi2_contingency(pd.crosstab(df["Diagnosis"], df["Diabetes"]))
cardiovascular_chi2 = chi2_contingency(pd.crosstab(df["Diagnosis"], df["CardiovascularDisease"]))
smoking_chi2 = chi2_contingency(pd.crosstab(df["Diagnosis"], df["Smoking"]))

# Print Statistical Test Results
stat_results = {
    "Hypertension Chi-square p-value": hypertension_chi2[1],
    "Diabetes Chi-square p-value": diabetes_chi2[1],
    "Cardiovascular Disease Chi-square p-value": cardiovascular_chi2[1],
    "Smoking Chi-square p-value": smoking_chi2[1],
}

print("\nStatistical Test Results:")
for key, value in stat_results.items():
    print(f"{key}: {value:.5f}")

# Perform ANOVA tests for selected numerical variables based on Diagnosis groups
anova_results = {}
anova_vars = ["Age", "BMI", "CholesterolTotal", "CholesterolLDL", "CholesterolHDL", 
              "CholesterolTriglycerides", "PhysicalActivity", "DietQuality"]

# Loop through each variable and perform ANOVA
for var in anova_vars:
    groups = [df[var][df["Diagnosis"] == d] for d in df["Diagnosis"].unique()]
    f_stat, p_value = stats.f_oneway(*groups)
    anova_results[var] = {"F-Statistic": f_stat, 
                          "P-Value": round(p_value, 7)}

# Convert results to a DataFrame for better visualization
anova_df = pd.DataFrame.from_dict(anova_results, orient="index")

# Display results
display(anova_df)

