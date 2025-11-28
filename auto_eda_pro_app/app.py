import streamlit as st # type: ignore
import pandas as pd # type: ignore
import sys
from pathlib import Path

# Ensure project root is on sys.path so package imports work
ROOT = Path(__file__).resolve().parents[1]   # parent of auto_eda_pro_app
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Import pages via absolute package path (no relative imports)
from auto_eda_pro_app.app_pages import (
    overview,
    missing,
    distributions,
    correlations,
    outliers,
)


EXAMPLES = {
    "Titanic (examples/titanic.csv)": Path("examples/titanic.csv"),
    "Iris (examples/iris.csv)": Path("examples/iris.csv"),
    "Messy Dataset (examples/messy_dataset.csv)": Path("examples/messy_dataset.csv"),
}

st.set_page_config(page_title="auto-eda-pro", layout="wide")

def load_example(name: str) -> pd.DataFrame:
    p = EXAMPLES.get(name)
    if p and p.exists():
        return pd.read_csv(p)
    return pd.DataFrame()

def main():
    st.sidebar.title("auto-eda-pro")
    st.sidebar.markdown("Simple EDA with Matplotlib + Seaborn")
    uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    example_choice = st.sidebar.selectbox("Or choose an example", ["-- none --"] + list(EXAMPLES.keys()))

    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded)
            st.session_state["df"] = df
            st.sidebar.success("Uploaded dataset loaded")
        except Exception as e:
            st.sidebar.error(f"Could not read CSV: {e}")
    elif example_choice != "-- none --":
        df = load_example(example_choice)
        if not df.empty:
            st.session_state["df"] = df
            st.sidebar.success(f"Loaded example: {example_choice}")
        else:
            st.sidebar.warning("Example file not found in examples/ folder")

    if "df" not in st.session_state:
        st.info("No dataset loaded. Upload a CSV or pick an example (place example CSVs in examples/).")
        st.stop()

    page = st.sidebar.radio("Pages", ["Overview", "Missing values", "Distributions", "Correlations", "Outliers"])
    st.sidebar.markdown("---")
    st.sidebar.caption("Built with auto_eda_pro")

    if page == "Overview":
        overview.render()
    elif page == "Missing values":
        missing.render()
    elif page == "Distributions":
        distributions.render()
    elif page == "Correlations":
        correlations.render()
    elif page == "Outliers":
        outliers.render()

if __name__ == "__main__":
    main()
