# auto_eda_pro_app/app_pages/distributions.py
import streamlit as st # type: ignore
from auto_eda_pro import plot_histogram, plot_boxplot, plot_pairplot
import pandas as pd # type: ignore

def render():
    st.header("Distributions")
    df = st.session_state.get("df")
    if df is None or df.empty:
        st.warning("No dataset loaded. Please upload a CSV or select an example.")
        return

    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    st.subheader("Histogram")
    if num_cols:
        hist_col = st.selectbox("Choose column for histogram", num_cols)
        bins = st.slider("Bins", 5, 100, 30)
        if st.button("Plot histogram"):
            fig = plot_histogram(df, hist_col, bins=bins, show=False)
            st.pyplot(fig)
    else:
        st.info("No numeric columns available for histogram.")

    st.subheader("Boxplot")
    if num_cols:
        bp_col = st.selectbox("Column for boxplot", num_cols, key="bp_col")
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        by = st.selectbox("Group by (optional)", ["-- none --"] + cat_cols, index=0)
        if st.button("Plot boxplot"):
            by_arg = None if by == "-- none --" else by
            fig = plot_boxplot(df, bp_col, by=by_arg, show=False)
            st.pyplot(fig)
    else:
        st.info("No numeric columns available for boxplots.")

    st.subheader("Pairplot (pairwise relationships)")
    if num_cols:
        opts = st.multiselect("Choose numeric columns (empty = all numeric)", num_cols, default=num_cols[:4])
        hue_opts = df.select_dtypes(include=["object", "category"]).columns.tolist()
        hue = st.selectbox("Color by (hue) (optional)", ["-- none --"] + hue_opts, index=0)
        if st.button("Plot pairplot"):
            cols_arg = None if not opts else opts
            hue_arg = None if hue == "-- none --" else hue
            fig = plot_pairplot(df, cols=cols_arg, hue=hue_arg, show=False)
            st.pyplot(fig)
    else:
        st.info("No numeric columns available for pairplots.")
