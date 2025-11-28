from typing import Optional, List, Tuple, Dict
import pandas as pd # type: ignore
import numpy as np # type: ignore

def iqr_outlier_mask(
    df: pd.DataFrame,
    cols: Optional[List[str]] = None,
    k: float = 1.5,
) -> pd.DataFrame:
# Return a boolean DataFrame where True indicates an IQR-based outlier.
    if cols is None:
        cols = list(df.select_dtypes(include=[np.number]).columns)

    mask = pd.DataFrame(False, index=df.index, columns=cols)
    for c in cols:
        ser = df[c].astype(float)
        q1 = ser.quantile(0.25)
        q3 = ser.quantile(0.75)
        iqr = q3 - q1
        if iqr == 0 or np.isnan(iqr):
            continue
        lower = q1 - k * iqr
        upper = q3 + k * iqr
        mask[c] = (ser < lower) | (ser > upper)
    return mask

def zscore_outlier_mask(
    df: pd.DataFrame,
    cols: Optional[List[str]] = None,
    threshold: float = 3.0,
) -> pd.DataFrame:
    
    if cols is None:
        cols = list(df.select_dtypes(include=[np.number]).columns)

    mask = pd.DataFrame(False, index=df.index, columns=cols)
    for c in cols:
        ser = df[c].astype(float)
        mean = ser.mean()
        std = ser.std(ddof=1)
        if std == 0 or np.isnan(std):
            continue
        z = (ser - mean) / std
        mask[c] = z.abs() > threshold
    return mask
