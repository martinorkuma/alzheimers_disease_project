## Exploratory and Statistical Analysis of Alzheimer’s Disease Risk Factors

### Introduction

Alzheimer’s disease (AD) is a progressive neurodegenerative disorder that primarily affects memory and cognitive function. The purpose of this analysis is to explore demographic, clinical, and lifestyle factors associated with an Alzheimer’s disease diagnosis using a dataset of 2,149 patients and a structured, reproducible Python workflow. The analysis combines data cleaning, exploratory visualization, and formal statistical testing to identify meaningful differences between diagnosed and non-diagnosed individuals.

The data set, obtained [Rabie El Kharoua](https://www.kaggle.com/rabieelkharoua) as part of the [Alzheimer's Disease Dataset](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data) on Kaggle, includes demographic information, lifestyle habits, medical history, cognitive assessments, and behavioral symptoms. The data is synthetic and for educational purposes only.

### Data Loading and Preparation

The dataset was loaded and inspected using pandas and numpy to understand structure, completeness, and variable types.

Key preparation steps included:

-   Verification of dataset structure and dimensions

-   Summary statistics for all numeric variables

-   Duplicate record checks

-   Conversion of binary and categorical variables (e.g., Diagnosis, Gender, Hypertension) into human-readable labels

### Exploratory Data Analysis

Exploratory visualizations were produced to characterize the population and identify potential associations with Alzheimer’s diagnosis.

**Demographic Distributions**

-   Age: The age distribution shows a broad adult population, with higher representation in older age ranges.

-   Ethnicity: The dataset is dominated by Caucasian individuals, followed by African American, Asian, and Other groups.

<!-- -->

-   Diagnosis: Both diagnosed and non-diagnosed groups are well represented, enabling comparative analysis.

**Cognitive and Clinical Measures**

-   MMSE scores exhibit a clear separation between diagnosed and non-diagnosed individuals, with lower median scores among those diagnosed with Alzheimer’s disease.

-   BMI distributions show overlap between groups, suggesting BMI alone is not a strong discriminator.

**Correlation Structure**

A correlation heatmap of numeric variables reveals:

-   Strong associations among lipid profile measures

-   Moderate relationships between age, cognitive scores, and diagnosis-related outcomes

**Comorbidities and Lifestyle Factors**

Stacked bar charts and boxplots highlight group-level differences in:

-   Hypertension

-   Diabetes

-   Cardiovascular disease

-   Physical activity

-   Diet quality

Diagnosed individuals tend to show higher prevalence of cardiovascular and metabolic comorbidities, alongside lower physical activity and diet quality scores.

### Statistical Analysis

Formal hypothesis testing was conducted to evaluate whether observed differences were statistically significant.

**Categorical Variables (Chi-Square Tests)**

Chi-square tests were applied to assess independence between diagnosis status and selected categorical risk factors:

-   Hypertension

-   Diabetes

-   Cardiovascular disease

-   Smoking status

Results indicate statistically significant associations for several cardiovascular and metabolic conditions, supporting their relevance in Alzheimer’s disease risk profiles.

**Continuous Variables (ANOVA)**

One-way ANOVA tests were performed comparing diagnosed vs. non-diagnosed groups across multiple numeric variables:

-   Age

-   BMI

-   Lipid measures

-   Physical activity

-   Diet quality

Several variables demonstrated statistically significant group differences, particularly age and lifestyle-related measures, reinforcing the multifactorial nature of Alzheimer’s disease.

### Key Insights

The combined exploratory and statistical results suggest:

-   Alzheimer’s diagnosis is strongly associated with cognitive performance, as indicated by the difference in MMSE scores among individuals with AD and those without an AD diagnosis.

-   Age and LDL cholesterol are not significantly associated with Alzheimer's diagnosis in this dataset.

-   Although several studies, Edwards III et al. (2019), have shown the association between lifestyle factors (BMI, diet, physical activity) and chronic diseases, this dataset does not show strong statistical associations.

-   Lifestyle factors (physical activity and diet quality) differ meaningfully between groups, highlighting potential intervention targets.

-   HDL cholesterol levels are significantly different across groups. Further investigation (e.g., Tukey's post-hoc test) can determine which groups differ.

-   Further analysis (e.g., logistic regression) is needed to determine potential risk factors and predictors of AD.

No single variable explains diagnosis status in isolation, emphasizing the importance of multivariate and integrative analytical approaches.

### Limitations

-   The analysis is cross-sectional and cannot establish causal relationships.

-   Diagnostic status is treated as binary, without accounting for disease stage or progression.

-   Potential confounding factors were not controlled simultaneously (e.g., via regression modeling).

### Conclusion

This project demonstrates a complete exploratory and inferential workflow for analyzing Alzheimer’s disease data using Python. By combining structured data preparation, visual exploration, and hypothesis testing, the analysis provides evidence-based insights into demographic, clinical, and lifestyle factors associated with Alzheimer’s diagnosis.

The results establish a strong foundation for future work, including predictive modeling, feature importance analysis, and longitudinal investigation.

### Reproducibility

All results in this report are derived from the following scripts:

-   01_load_clean_data.py – data loading, validation, and pre-processing.

-   02_data_viz.py – exploratory visualizations and descriptive plots.

-   03_stat_analysis.py – chi-square and ANOVA statistical testing.

### References

-   Arevalo‐Rodriguez, I., Smailagic, N., i Figuls, M. R., Ciapponi, A., Sanchez‐Perez, E., Giannakou, A., ... & Cullum, S. (2015). [Mini‐Mental State Examination (MMSE) for the detection of Alzheimer's disease and other dementias in people with mild cognitive impairment (MCI).](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD010783.pub2/full) Cochrane database of systematic reviews, (3).

-   Edwards III, G. A., Gamez, N., Escobedo Jr, G., Calderon, O., & Moreno-Gonzalez, I. (2019). [Modifiable risk factors for Alzheimer’s disease.](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2019.00146/full) Frontiers in aging neuroscience, 11, 146.

-   [Rabie El Kharoua](https://www.kaggle.com/rabieelkharoua) (2024). [Alzheimer's Disease Dataset](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data). DOI: [10.34740/KAGGLE/DSV/8668279]. Kaggle.

-   Yoelin, A. B., & Saunders, N. W. (2017). [Score Disparity Between the MMSE and the SLUMS.](https://journals.sagepub.com/doi/full/10.1177/1533317517705222) American Journal of Alzheimer's Disease & Other Dementias®, 32(5), 282-288.
