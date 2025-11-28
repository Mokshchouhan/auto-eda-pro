from typing import Optional, List, Tuple
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import numpy as np # type: ignore

# Ensure seaborn default styling for nicer visuals
sns.set(style="whitegrid", context="notebook")

def plot_histogram(
    df: pd.DataFrame,
    col: str,
    bins: int = 30,
    figsize: Tuple[int, int] = (8, 4),
    show: bool = True,
) -> plt.Figure:
# Plot a histogram for a numeric column and return the Figure.
    fig, ax = plt.subplots(figsize=figsize)
    ser = df[col].dropna().astype(float)
    ax.hist(ser, bins=bins)
    ax.set_title(f"Histogram: {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("count")
    plt.tight_layout()
    if show:
        plt.show()
    return fig


def plot_boxplot(
    df: pd.DataFrame,
    col: str,
    by: Optional[str] = None,
    figsize: Tuple[int, int] = (8, 4),
    show: bool = True,
) -> plt.Figure:
# Plot a boxplot for a numeric column, optionally grouped by another column.
    fig, ax = plt.subplots(figsize=figsize)
    if by is None:
        sns.boxplot(x=df[col], ax=ax)
        ax.set_xlabel(col)
    else:
        sns.boxplot(x=by, y=col, data=df, ax=ax)
        ax.set_xlabel(by)
        ax.set_ylabel(col)
    ax.set_title(f"Boxplot: {col}" + (f" by {by}" if by else ""))
    plt.tight_layout()
    if show:
        plt.show()
    return fig


def plot_correlation_heatmap_from_df(
    df: pd.DataFrame,
    cols: Optional[List[str]] = None,
    method: str = "pearson",
    figsize: Tuple[int, int] = (10, 8),
    cmap: str = "coolwarm",
    annot: bool = True,
    show: bool = True,
) -> plt.Figure:
    if cols is None:
        num_df = df.select_dtypes(include=[np.number])
    else:
        num_df = df[cols].select_dtypes(include=[np.number])

    corr = num_df.corr(method=method)

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr, cmap=cmap, annot=annot, fmt=".2f", linewidths=0.5, ax=ax,
                cbar_kws={"label": f"{method} correlation"})
    ax.set_title(f"{method.capitalize()} Correlation Heatmap")
    plt.tight_layout()
    if show:
        plt.show()
    return fig


def plot_pairplot(
    df: pd.DataFrame,
    cols: Optional[List[str]] = None,
    hue: Optional[str] = None,
    corner: bool = False,
    show: bool = True,
) -> plt.Figure:
    
    if cols is None:
        num_df = df.select_dtypes(include=[np.number])
    else:
        num_df = df[cols]
    grid = sns.pairplot(data=df, vars=list(num_df.columns), hue=hue, corner=corner)
    if show:
        plt.show()
    return plt.gcf()
