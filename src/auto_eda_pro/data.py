"""Simple data loading utility for auto_eda_pro."""
from typing import Optional
import pandas as pd # type: ignore

def load_csv(path: str, nrows: Optional[int] = None, encoding: str = "utf-8") -> pd.DataFrame:
    return pd.read_csv(path, nrows=nrows, encoding=encoding)
