# test_summary.py — quick test for summary_stats
import pandas as pd # type: ignore
from auto_eda_pro import summary_stats

df = pd.DataFrame({
    "age": [23, 45, 31, None],
    "fare": [7.25, 71.2833, 8.05, 7.925],
    "sex": ["male", "female", "female", "male"],
    "survived": [1, 0, 1, 1]
})
print(summary_stats(df).to_string())
