import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import ttest_ind, chi2_contingency

df = pd.read_csv('alzheimers_disease_data.csv') # Load the data frame from the repo directory
df.head().T

# Understanding the Data Structure
print("\nDataset Information:")
df.info()

# Obtain summary statistics
print("\nSummary Statistics:")
df.describe().T

#Check for duplicate data
sum(df.duplicated())

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Define categorical mappings
custom_labels = {
    'Gender': ['Male', 'Female'],
    'Ethnicity': ['Caucasian', 'African American', 'Asian', 'Other'],
    'EducationLevel': ['None', 'High School', "Bachelor's Degree", 'Graduate Degree'],
    'Smoking': ['No', 'Yes'],
    'FamilyHistoryAlzheimers': ['No', 'Yes'],
    'CardiovascularDisease': ['No', 'Yes'],
    'Diabetes': ['No', 'Yes'],
    'Depression': ['No', 'Yes'],
    'HeadInjury': ['No', 'Yes'],
    'Hypertension': ['No', 'Yes'],
    'MemoryComplaints': ['No', 'Yes'],
    'BehavioralProblems': ['No', 'Yes'],
    'Confusion': ['No', 'Yes'],
    'Disorientation': ['No', 'Yes'],
    'PersonalityChanges': ['No', 'Yes'],
    'DifficultyCompletingTasks': ['No', 'Yes'],
    'Forgetfulness': ['No', 'Yes'],
    'Diagnosis': ['No', 'Yes']
}
# Convert numerical values to categorical labels in a simplified way
df[list(custom_labels.keys())] = df[list(custom_labels.keys())].apply(lambda col: col.map(lambda x: custom_labels[col.name][int(x)] if pd.notnull(x) else None))

# Display the first few rows to verify conversion
print(df.head())

