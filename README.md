# Alzheimer’s Disease: Exploratory and Statistical Analysis

## Overview

This project presents an exploratory data analysis (EDA) and statistical assessment of an Alzheimer’s disease dataset using Python. The goal is to identify demographic, clinical, and lifestyle factors associated with an Alzheimer’s diagnosis through reproducible data preparation, visualization, and hypothesis testing.

The analysis is designed to emphasize clarity, reproducibility, and appropriate use of statistical methods rather than predictive modeling or causal claims. All analyses were conducted in a local Python environment using JupyterLab on a desktop.

---

## Project Objectives

* Inspect and validate the structure and quality of Alzheimer’s disease data
* Explore demographic and clinical distributions across diagnosis groups
* Visualize relationships between diagnosis status and key risk factors
* Perform statistical tests (Chi-square, ANOVA) to evaluate group differences
* Generate figures and summary tables

---

## Repository Structure

```
.
├── alzheimers_disease_data.csv      # Input dataset
├── output/                          # Saved figures from Python visualizations
│   ├── age_distribution.png
│   ├── mmse_distribution.png
│   ├── ethnicity_distribution.png
│   ├── diagnosis_distribution.png
│   ├── correlation_heatmap.png
│   ├── mmse_by_diagnosis.png
│   ├── bmi_by_diagnosis.png
│   ├── hypertension_by_diagnosis.png
│   ├── diabetes_by_diagnosis.png
│   ├── cardiovascular_by_diagnosis.png
│   └── activity_diet_by_diagnosis.png
├── 01_load_clean_data.py            # Data loading, inspection, and cleaning
├── 02_data_viz.py                   # Exploratory visualizations
├── 03_stat_analysis.py              # Statistical hypothesis testing
└── README.md                        # Project documentation
```

---

## Analysis Workflow

### 1. Data Loading and Validation (`01_load_clean_data.py`)

* Load the dataset using `pandas.`
* Inspect data types and structure
* Generate summary statistics
* Check for duplicates and missing values
* Convert binary and categorical variables into interpretable labels

### 2. Exploratory Data Analysis (`02_data_viz.py`)

* Age and MMSE score distributions
* Diagnosis and ethnicity breakdowns
* Correlation heatmap of numeric variables
* Boxplots comparing diagnosis groups across:

  * MMSE
  * BMI
  * Physical activity
  * Diet quality
* Stacked bar charts for comorbidities:

  * Hypertension
  * Diabetes
  * Cardiovascular disease

All figures are automatically saved to the `output/` directory.

### 3. Statistical Analysis (`03_stat_analysis.py`)

* **Chi-square tests** for associations between diagnosis and categorical variables:

  * Hypertension
  * Diabetes
  * Cardiovascular disease
  * Smoking status
* **One-way ANOVA** tests comparing diagnosis groups across numeric variables:

  * Age
  * BMI
  * Lipid measures
  * Physical activity
  * Diet quality

Statistical results are printed in a structured, interpretable format.

---

## Methods and Tools

* **Python**: pandas, numpy, seaborn, matplotlib, scipy
* **Statistical methods**: Chi-square tests, ANOVA
* **Visualization**: histograms, boxplots, stacked bar charts, correlation heatmaps

---

## Key Findings (Summary)

* Cognitive performance (MMSE) differs substantially by diagnosis status
* Age is strongly associated with Alzheimer’s diagnosis, but does not fully explain group differences
* Cardiovascular and metabolic comorbidities show significant associations with diagnosis
* Lifestyle factors such as physical activity and diet quality differ between diagnosis groups

These results support a multifactorial understanding of Alzheimer’s disease risk.

---

## Limitations

* Cross-sectional data; no causal inference
* Diagnosis treated as a binary outcome without disease staging
* Potential confounding factors not jointly modeled

---

## Reproducibility

To reproduce the analysis in a **local Python environment** (Windows, macOS, or Linux):

```bash
pip install pandas numpy seaborn matplotlib scipy
python 01_load_clean_data.py
python 02_data_viz.py
python 03_stat_analysis.py
```

All generated figures will appear in the `output/` directory.

---

## Author

**Martin Orkuma**

---

## Future Extensions

* Multivariate regression or classification models
* Feature importance and model interpretability
* Longitudinal analysis (if data become available)
* Integration into a Quarto or Markdown report

---

*This project is intended for educational and portfolio purposes and does not constitute clinical guidance.*
