import pandas as pd

NUMERIC_FEATURES = ["age", "avg_glucose_level", "bmi"]

def load_data(path):
    return pd.read_csv(path)

def data_quality_summary(df):
    return pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing": df.isna().sum(),
        "unique": df.nunique(),
    })

def observed_stroke_rate(df, feature):
    out = df.groupby(feature, dropna=False)["stroke"].agg(["count", "sum", "mean"])
    out = out.rename(columns={"sum": "stroke_cases", "mean": "observed_stroke_rate"})
    out["observed_stroke_rate"] *= 100
    return out.sort_values("observed_stroke_rate", ascending=False)
