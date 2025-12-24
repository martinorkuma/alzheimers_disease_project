import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import ttest_ind, chi2_contingency

# Recall
df = pd.read_csv('alzheimers_disease_data.csv') 

# Age Distribution of Patien
plt.figure(figsize=(8, 5))
plt.hist(df["Age"], bins=15, edgecolor="black", alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Patients")
plt.show()

# Distribution of MMSE Scores
plt.figure(figsize=(8, 5))
plt.hist(df["MMSE"], bins=30, edgecolor="black", alpha=0.7, color="green")
plt.xlabel("MMSE Score")
plt.ylabel("Frequency")
plt.title("MMSE Score Distribution")
plt.show()

# Distribution of Ethnicity
plt.figure(figsize=(7, 5))
df["Ethnicity"].value_counts().plot(kind="bar", color=["teal", "violet", "lightblue", "yellow"], edgecolor="black")
plt.xlabel("Ethnicity")
plt.ylabel("Count")
plt.title("Ethnicity Distribution")
plt.xticks(rotation=0)
plt.show()

# Diagnosis Breakdown
plt.figure(figsize=(7, 5))
df["Diagnosis"].value_counts().plot(kind="bar", color=["pink", "red"], edgecolor="black")
plt.xlabel("Diagnosis (No: No Hx of Alzheimer’s Dx  Yes: Hx of Alzheimer’s Dx)")
plt.ylabel("Count")
plt.title("Diagnosis Distribution")
plt.xticks(rotation=0)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), cmap="coolwarm", annot=False, linewidths=0.5)
plt.title("Correlation Heatmap of Attributes")
plt.show()

# Boxplot of MMSE Scores by Diagnosis
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x=df["Diagnosis"], y=df["MMSE"], hue=df["Diagnosis"], palette=["lightblue", "orange"])
plt.xlabel("Diagnosis (No Alzheimer’s Dx | Alzheimer’s Dx)")
plt.ylabel("MMSE Score")
plt.title("MMSE Scores by Diagnosis")
plt.show()

# Boxplot of BMI by Diagnosis
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x=df["Diagnosis"], y=df["BMI"], hue="Diagnosis", palette=["lightblue", "orange"])
plt.xlabel("Diagnosis (No Alzheimer’s Dx | Alzheimer’s Dx)")
plt.ylabel("BMI")
plt.title("BMI Distribution by Diagnosis")
plt.show()

# Create contingency table
contingency_table = pd.crosstab(df["Diagnosis"], df["Hypertension"])

# Normalize to get proportions
contingency_norm = contingency_table.div(contingency_table.sum(axis=1), axis=0)

# Plot stacked bar chart
contingency_norm.plot(kind="bar", stacked=True, figsize=(8,5), colormap="RdYlGn")

plt.xlabel("Diagnosis (No Alzheimer’s Dx | Alzheimer’s Dx)")
plt.ylabel("Proportion")
plt.title("Proportion of Hypertension by Diagnosis")
plt.legend(title="Hypertension", labels=["No", "Yes"])
plt.show()

# Display contingency table
print(contingency_table)

# Normalize to get proportions
contingency_norm = contingency_table.div(contingency_table.sum(axis=1), axis=0)

# Plot stacked bar chart
contingency_norm.plot(kind="bar", stacked=True, figsize=(8,5), colormap="PiYG")

plt.xlabel("Diagnosis (No Alzheimer’s Dx | Alzheimer’s Dx)")
plt.ylabel("Proportion")
plt.title("Proportion of Diabetes by Diagnosis")
plt.legend(title="Diabetes", labels=["No", "Yes"])
plt.show()

# Contingency table showing Diabetes vs. Diagnosis.
print(pd.crosstab(df["Diagnosis"], df["Diabetes"]))

# Normalize to get proportions
contingency_norm = contingency_table.div(contingency_table.sum(axis=1), axis=0)

# Plot stacked bar chart
contingency_norm.plot(kind="bar", stacked=True, figsize=(8,5), colormap="PRGn")

plt.xlabel("Diagnosis (No Alzheimer’s Dx | Alzheimer’s Dx)")
plt.ylabel("Proportion")
plt.title("Proportion of Cardiovascular Disease by Diagnosis")
plt.legend(title="Cardiovascular Disease", labels=["No", "Yes"], loc="lower center")
plt.show()

# Contingency table showing Cardiovascular Disease vs. Diagnosis.
print(pd.crosstab(df["Diagnosis"], df["CardiovascularDisease"]))

# I combined in boxplots for Physical Activity and Diet Quality into one cell:

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Physical Activity
sns.boxplot(data=df, x=df["Diagnosis"], y=df["PhysicalActivity"], 
            hue="Diagnosis", palette=["lightblue", "gold"], ax=axes[0])
axes[0].set_xlabel("Diagnosis (No Alzheimer’s Dx | Alzheimer’s Dx)")
axes[0].set_ylabel("Physical Activity Score")
axes[0].set_title("Physical Activity by Diagnosis")

# Diet Quality
sns.boxplot(data=df, x=df["Diagnosis"], y=df["DietQuality"], 
            hue="Diagnosis", palette=["lightblue", "gold"], ax=axes[1])
axes[1].set_xlabel("Diagnosis (No Alzheimer’s Dx | Alzheimer’s Dx)")
axes[1].set_ylabel("Diet Quality Score")
axes[1].set_title("Diet Quality by Diagnosis")

plt.tight_layout()
plt.show()

