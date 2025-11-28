"""
Summary statistics helpers for auto_eda_pro.
Provides a tidy DataFrame with numeric and categorical summaries.
"""
from typing import Optional, List
import pandas as pd # type: ignore
import numpy as np # type: ignore

from .types import detect_column_types

def summary_stats(
    df: pd.DataFrame,
    cols: Optional[List[str]] = None,
    include_percentiles: bool = True,
    percentiles: List[float] = [0.25, 0.5, 0.75],
    detect_kwargs: Optional[dict] = None,
) -> pd.DataFrame:
# Generate summary statistics for the DataFrame.
    if cols is None:
        cols = list(df.columns)
    detect_kwargs = detect_kwargs or {}
    types = detect_column_types(df, **detect_kwargs)
    numeric_cols = [c for c in types["numerical"] if c in cols]
    cat_cols = [c for c in types["categorical"] if c in cols]
    other_cols = [c for c in types["other"] if c in cols]
    rows = []

    for c in numeric_cols:
        ser = df[c]
        cnt = int(ser.count())
        miss = int(ser.isna().sum())
        miss_ratio = float(miss) / max(1, len(ser))
        mean = float(np.nanmean(ser))
        median = float(np.nanmedian(ser))
        std = float(np.nanstd(ser, ddof=1)) if cnt > 1 else float("nan")
        mn = float(np.nanmin(ser)) if cnt > 0 else float("nan")
        mx = float(np.nanmax(ser)) if cnt > 0 else float("nan")
        row = {
            "column": c,
            "dtype": "numeric",
            "count": cnt,
            "missing_count": miss,
            "missing_ratio": round(miss_ratio, 6),
            "mean": mean,
            "median": median,
            "std": std,
            "min": mn,
            "max": mx,
        }
        if include_percentiles:
            q = ser.quantile(percentiles)
            for p, val in zip(percentiles, q):
                row[f"p{int(p*100)}"] = float(val) if pd.notna(val) else float("nan")
        rows.append(row)

    for c in cat_cols:
        ser = df[c].astype("object")
        cnt = int(ser.count())
        miss = int(ser.isna().sum())
        miss_ratio = float(miss) / max(1, len(ser))
        nunique = int(ser.nunique(dropna=True))
        top = ser.mode().iloc[0] if nunique > 0 else None
        top_freq = int(ser.value_counts(dropna=True).iloc[0]) if nunique > 0 else 0
        row = {
            "column": c,
            "dtype": "categorical",
            "count": cnt,
            "missing_count": miss,
            "missing_ratio": round(miss_ratio, 6),
            "unique": nunique,
            "top": top,
            "top_freq": top_freq,
        }
        rows.append(row)

    for c in other_cols:
        ser = df[c]
        cnt = int(ser.count())
        miss = int(ser.isna().sum())
        miss_ratio = float(miss) / max(1, len(ser))
        row = {
            "column": c,
            "dtype": "other",
            "count": cnt,
            "missing_count": miss,
            "missing_ratio": round(miss_ratio, 6),
        }
        rows.append(row)

    res = pd.DataFrame(rows).set_index("column", drop=True).sort_index()
    return res
