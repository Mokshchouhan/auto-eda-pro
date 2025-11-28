"""
Column type detection helpers for auto_eda_pro.
Return a dictionary with lists of column names by detected type.
"""
from typing import Dict, List
import pandas as pd # type: ignore
import numpy as np # type: ignore

def detect_column_types(
    df: pd.DataFrame,
    max_unique_for_categorical: int = 50,
    categorical_ratio: float = 0.05,
) -> Dict[str, List[str]]:
#Detect column types in a DataFrame.

    nrows = len(df)
    numerical = []
    categorical = []
    datetime = []
    boolean = []
    other = []

    for col in df.columns:
        ser = df[col]
        if pd.api.types.is_bool_dtype(ser):
            boolean.append(col)
            continue
        if pd.api.types.is_datetime64_any_dtype(ser) or pd.api.types.is_period_dtype(ser):
            datetime.append(col)
            continue
        if pd.api.types.is_numeric_dtype(ser):
            nunique = ser.nunique(dropna=True)
            if nunique <= max_unique_for_categorical or (nunique / max(1, nrows)) < categorical_ratio:
                categorical.append(col)
            else:
                numerical.append(col)
            continue
        if pd.api.types.is_categorical_dtype(ser) or pd.api.types.is_object_dtype(ser):
            # try to detect datetime-like strings
            import warnings
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")   # suppress UserWarning from pandas
                    parsed = pd.to_datetime(
                        ser.dropna().iloc[:100],
                        errors="coerce",
                        infer_datetime_format=False 
                    )
                if parsed.notna().sum() / max(1, parsed.shape[0]) > 0.6:
                    datetime.append(col)
                else:
                    categorical.append(col)
            except Exception:
                categorical.append(col)
            continue
        other.append(col)

    return {
        "numerical": numerical,
        "categorical": categorical,
        "datetime": datetime,
        "boolean": boolean,
        "other": other,
    }
