# ---------- Import Libraries ----------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier

import warnings
warnings.filterwarnings("ignore")

# ---------- Import Data and Perform EDA ----------

df = pd.read_csv("kidney_disease.csv")
df.drop("id", axis=1, inplace=True)

df.columns = [
    'age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar',
    'red_blood_cells', 'pus_cell', 'pus_cell_clumps', 'bacteria',
    'blood_glucose_random', 'blood_urea', 'serum_creatinine', 'sodium',
    'potassium', 'hemoglobin', 'packed_cell_volume',
    'white_blood_cell_count', 'red_blood_cell_count', 'hypertension',
    'diabetes_mellitus', 'coronary_artery_disease', 'appetite',
    'peda_edema', 'aanemia', 'class' ]

df.info()

describe = df.describe()

df["packed_cell_volume"] = pd.to_numeric(df["packed_cell_volume"], errors="coerce")
df["white_blood_cell_count"] = pd.to_numeric(df["white_blood_cell_count"], errors="coerce")
df["red_blood_cell_count"] = pd.to_numeric(df["red_blood_cell_count"], errors="coerce")

cat_cols = [col for col in df.columns if df[col].dtype == "object"]
num_cols = [col for col in df.columns if df[col].dtype != "object"]

for col in cat_cols:
    print(f"{col}: {df[col].unique()}")

df["diabetes_mellitus"].replace(to_replace={"\tno": "no", "\tyes": "yes", " yes": "yes"}, inplace=True)
df["coronary_artery_disease"].replace(to_replace={"\tno": "no"}, inplace=True)
df["class"].replace(to_replace={"ckd\t": "ckd"}, inplace=True)

df["class"] = df["class"].map({"ckd":0, "notckd":1})


plt.figure(figsize=(15, 15))
plotnumber = 1

for col in num_cols:
    if plotnumber <= 14:
        ax = plt.subplot(3, 5, plotnumber)
        sns.histplot(df[col], kde=True)
        plt.xlabel(col)

    plotnumber += 1

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 8))
numeric_df = df.select_dtypes(include=["number"])  # Sadece sayısal sütunları seç
sns.heatmap(numeric_df.corr(), annot=True, linecolor="white", linewidths=2)
plt.title("Feature Correlation Heatmap")
plt.show()

























