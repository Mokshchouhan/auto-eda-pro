
from typing import Optional, List, Tuple
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

def missing_summary(df: pd.DataFrame, cols: Optional[List[str]] = None) -> pd.DataFrame:
    # Return a DataFrame summarizing missing values per column.
    if cols is None:
        cols = list(df.columns)
    rows = []
    n = len(df)
    for c in cols:
        ser = df[c]
        miss = int(ser.isna().sum())
        non_miss = int(ser.count())
        miss_ratio = round(miss / max(1, n), 6)
        unique_non_missing = int(ser.dropna().nunique())
        rows.append({
            "column": c,
            "missing_count": miss,
            "missing_ratio": miss_ratio,
            "non_missing_count": non_miss,
            "unique_non_missing": unique_non_missing
        })
    return pd.DataFrame(rows).set_index("column").sort_values("missing_ratio", ascending=False)

def missing_matrix(df: pd.DataFrame, cols: Optional[List[str]] = None) -> pd.DataFrame:
    if cols is None:
        cols = list(df.columns)
    return df[cols].isna()

def plot_missing_heatmap(
    df: pd.DataFrame,
    cols: Optional[List[str]] = None,
    figsize: Tuple[int, int] = (10, 6),
    cmap: str = "viridis",
    show: bool = True,
) -> plt.Figure:
    mat = missing_matrix(df, cols)
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(mat.astype(int).T, cbar=True, ax=ax, cmap=cmap,
                cbar_kws={"label": "missing (1=yes, 0=no)"})
    ax.set_ylabel("columns")
    ax.set_xlabel("rows (index)")
    ax.set_title("Missing value heatmap (columns × rows)")
    plt.tight_layout()
    if show:
        plt.show()
    return fig
