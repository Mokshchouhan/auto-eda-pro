# test_outliers.py — quick test for outlier detection
import pandas as pd # type: ignore
from auto_eda_pro import iqr_outlier_mask, zscore_outlier_mask

df = pd.DataFrame({
    "age": [22, 23, 24, 25, 120],
    "fare": [7.25, 7.5, 7.3, 7.4, 500],
    "survived": [0, 1, 1, 0, 1]
})

print("DATAFRAME:")
print(df)

print("\nIQR OUTLIER MASK:")
print(iqr_outlier_mask(df).to_string())

print("\nZ-SCORE OUTLIER MASK:")
print(zscore_outlier_mask(df).to_string())
