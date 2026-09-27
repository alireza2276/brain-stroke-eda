# Brain Stroke Exploratory Data Analysis

Exploratory data analysis of a public brain-stroke dataset using **Python, Pandas, NumPy, Matplotlib, and Jupyter**.

This repository is a refactored and reproducible version of an earlier Data Science course project.
The original purpose was to practice data manipulation, descriptive statistics, grouping, and visualization.
It intentionally remains an **EDA project** rather than being retrofitted into a machine-learning demo.

> **Educational project:** associations observed in this dataset do not establish causation.
> This repository is not a medical diagnostic or clinical risk tool.

## Dataset at a glance

- **4,981** observations
- **11** variables
- **248** stroke-labelled records
- **4,733** non-stroke records
- Stroke-labelled records: **4.98%**
- Missing values: **0**
- Duplicate rows: **0**

Original dataset page:

https://www.kaggle.com/datasets/zzettrkalpakbal/full-filled-brain-stroke-dataset

![Class distribution](figures/class_distribution.png)

## Questions explored

The notebook examines the observed stroke label in relation to age, hypertension, heart disease,
marital status, work type, residence type, average glucose level, BMI, smoking status, and gender.

## Selected descriptive findings

These are **dataset-specific associations**, not causal or clinical conclusions.

- Mean age: **67.8 years** for stroke-labelled records versus **42.1 years** for non-stroke records.
- Observed stroke percentage: **13.8%** among records with hypertension versus **4.0%** without hypertension.
- Observed stroke percentage: **17.1%** among records with heart disease versus **4.3%** without heart disease.
- The target is strongly imbalanced, so raw accuracy-style intuition or raw counts alone can be misleading.

![Mean age](figures/mean_age_by_stroke.png)

![Hypertension](figures/stroke_rate_hypertension.png)

## Analysis workflow

1. Load and inspect the dataset
2. Verify shape, data types, missing values, and duplicates
3. Examine target-class imbalance
4. Calculate descriptive statistics
5. Compare numerical variables by observed stroke status
6. Calculate within-category observed stroke percentages
7. Visualize numerical and categorical patterns
8. Inspect correlations among numerical/binary variables
9. Document limitations and avoid causal interpretation

## Repository structure

```text
brain-stroke-eda/
├── data/
│   ├── brain_stroke.csv
│   └── README.md
├── figures/
│   ├── class_distribution.png
│   ├── mean_age_by_stroke.png
│   └── stroke_rate_hypertension.png
├── notebooks/
│   └── brain_stroke_eda.ipynb
├── reports/
│   └── original_course_notebook.html
├── src/
│   └── analysis.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Run locally

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

```bash
pip install -r requirements.txt
jupyter lab
```

Then open `notebooks/brain_stroke_eda.ipynb`.

The notebook committed to this repository has already been executed against the included dataset,
so its verified outputs render directly on GitHub.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- JupyterLab

## Project history

The first version was created as a Data Science course project while learning **Pandas, NumPy,
Matplotlib, descriptive statistics, and exploratory data analysis**.

It was later refactored for reproducibility, clearer communication, cleaner organization, and
portfolio presentation. The original exported course notebook is preserved in `reports/`.

## Limitations

- This is observational exploratory analysis, so causal claims are not justified.
- The target is strongly imbalanced.
- The sample should not be interpreted as population stroke prevalence.
- Important clinical variables may be absent.
- `Unknown` smoking status means unavailable information, not confirmed non-smoking.
- Findings are specific to this dataset.
- This project is educational and is not medical advice, diagnosis, or a clinical prediction system.

## License

Project code is released under the **MIT License**.

The dataset remains governed by the terms of its original source.
