from typing import Optional, List, Tuple
import pandas as pd # type: ignore
import numpy as np # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore

def correlation_matrix(
    df: pd.DataFrame,
    cols: Optional[List[str]] = None,
    method: str = "pearson"
) -> pd.DataFrame:
#  Compute the correlation matrix for numeric columns in the DataFrame.
    if cols is None:
        # select numeric columns only
        num_df = df.select_dtypes(include=[np.number])
    else:
        num_df = df[cols].select_dtypes(include=[np.number])

    if num_df.shape[1] == 0:
        return pd.DataFrame()

    return num_df.corr(method=method)


def plot_correlation_heatmap(
    df: pd.DataFrame,
    cols: Optional[List[str]] = None,
    method: str = "pearson",
    figsize: Tuple[int, int] = (10, 8),
    cmap: str = "coolwarm",
    annot: bool = True,
    show: bool = True,
) -> plt.Figure:

    corr = correlation_matrix(df, cols, method)

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        corr,
        cmap=cmap,
        annot=annot,
        fmt=".2f",
        linewidths=0.5,
        cbar_kws={"label": f"{method} correlation"}
    )
    ax.set_title(f"{method.capitalize()} Correlation Heatmap")
    plt.tight_layout()

    if show:
        plt.show()

    return fig
