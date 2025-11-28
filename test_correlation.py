# test_correlation.py — quick test for correlation helpers
import pandas as pd # type: ignore
from auto_eda_pro import correlation_matrix, plot_correlation_heatmap

df = pd.DataFrame({
    "age": [22, 38, 26, 35, 28],
    "fare": [7.25, 71.2833, 7.925, 53.1, 8.05],
    "survived": [0, 1, 1, 1, 0],
    "sex": ["male", "female", "female", "female", "male"]
})

print("CORRELATION MATRIX:")
print(correlation_matrix(df).to_string())

print("\nPlotting correlation heatmap...")
fig = plot_correlation_heatmap(df, show=True)
print("Figure returned:", isinstance(fig, type(fig)))
