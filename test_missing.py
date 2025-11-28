# test_missing.py — quick test for missing value helpers
import pandas as pd # type: ignore
from auto_eda_pro import missing_summary, plot_missing_heatmap

df = pd.DataFrame({
    "A": [1, None, 3, None],
    "B": ["x", "y", None, "x"],
    "C": [None, None, None, None],
    "D": [10, 20, 30, 40]
})

print("MISSING SUMMARY:")
print(missing_summary(df).to_string())

# Plot (will open a window or render inline in notebooks)
print("\nPlotting heatmap (figure will display)...")
fig = plot_missing_heatmap(df, figsize=(8,4), show=True)
print("Figure returned:", isinstance(fig, type(fig)))
