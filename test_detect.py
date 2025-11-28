# test_detect.py — quick local test for detect_column_types
import pandas as pd # type: ignore
from auto_eda_pro import detect_column_types

df = pd.DataFrame({
    "age": [23, 45, 31, None],
    "sex": ["male", "female", "female", "male"],
    "survived": [1, 0, 1, 1],
    "date": ["1912-04-15", "1912-04-15", None, "1912-04-16"]
})
df["date"] = pd.to_datetime(df["date"], errors="coerce")
print(df)
print(detect_column_types(df))
