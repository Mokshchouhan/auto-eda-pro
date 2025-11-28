import pandas as pd # type: ignore
from auto_eda_pro import (
    plot_histogram,
    plot_boxplot,
    plot_correlation_heatmap_from_df,
    plot_pairplot,
)

df = pd.DataFrame({
    "age": [22, 38, 26, 35, 28, 120],
    "fare": [7.25, 71.2833, 7.925, 53.1, 8.05, 500],
    "survived": [0, 1, 1, 1, 0, 1],
    "sex": ["male", "female", "female", "female", "male", "male"]
})

print("Plotting histogram for 'age' (window should appear)...")
fig1 = plot_histogram(df, "age", show=True)
print("Returned Figure:", isinstance(fig1, type(fig1)))

print("Plotting boxplot for 'fare' by 'sex'...")
fig2 = plot_boxplot(df, "fare", by="sex", show=True)
print("Returned Figure:", isinstance(fig2, type(fig2)))

print("Plotting correlation heatmap...")
fig3 = plot_correlation_heatmap_from_df(df, show=True)
print("Returned Figure:", isinstance(fig3, type(fig3)))

print("Plotting pairplot (may take a moment)...")
fig4 = plot_pairplot(df, hue="survived", show=True)
print("Returned Figure:", isinstance(fig4, type(fig4)))
