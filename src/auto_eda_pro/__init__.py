"""auto_eda_pro package - lightweight EDA helpers."""
__version__ = "0.0.1"

from .data import load_csv  # noqa: F401
from .types import detect_column_types  # noqa: F401
from .summary import summary_stats  # noqa: F401
from .missing import missing_summary, missing_matrix, plot_missing_heatmap  # noqa: F401
from .correlation import correlation_matrix, plot_correlation_heatmap  # noqa: F401
from .outliers import iqr_outlier_mask, zscore_outlier_mask  # noqa: F401
from .visuals import (
    plot_histogram,
    plot_boxplot,
    plot_correlation_heatmap_from_df,
    plot_pairplot,
)  # noqa: F401
