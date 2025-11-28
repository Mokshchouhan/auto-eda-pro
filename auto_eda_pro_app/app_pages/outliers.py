import streamlit as st # type: ignore
import pandas as pd # type: ignore
from auto_eda_pro import iqr_outlier_mask, zscore_outlier_mask, plot_boxplot

def render():
    st.header("Outliers")
    df = st.session_state.get("df")
    if df is None or df.empty:
        st.warning("No dataset loaded. Please upload a CSV or select an example.")
        return

    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if not num_cols:
        st.info("No numeric columns available for outlier detection.")
        return

    st.subheader("Outlier detection settings")
    iqr_k = st.slider("IQR multiplier (k)", 1.0, 5.0, 1.5, step=0.1)
    z_thresh = st.slider("Z-score threshold", 2.0, 6.0, 3.0, step=0.1)

    if st.button("Detect outliers"):
        iqr_mask = iqr_outlier_mask(df, cols=num_cols, k=iqr_k)
        z_mask = zscore_outlier_mask(df, cols=num_cols, threshold=z_thresh)

        col_iqr_counts = iqr_mask.sum(axis=0).sort_values(ascending=False)
        col_z_counts = z_mask.sum(axis=0).sort_values(ascending=False)
        st.write("Outliers per column (IQR):")
        st.dataframe(col_iqr_counts.rename("iqr_outlier_count").to_frame())
        st.write("Outliers per column (Z-score):")
        st.dataframe(col_z_counts.rename("zscore_outlier_count").to_frame())

        st.write("Rows with at least one outlier (IQR):")
        rows_with_iqr = iqr_mask.any(axis=1)
        st.dataframe(df[rows_with_iqr])

        st.write("Rows with at least one outlier (Z-score):")
        rows_with_z = z_mask.any(axis=1)
        st.dataframe(df[rows_with_z])

    st.subheader("Boxplot visual (select column)")
    col = st.selectbox("Choose numeric column to inspect", num_cols)
    group_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    by = st.selectbox("Group by (optional)", ["-- none --"] + group_cols, index=0)
    by_arg = None if by == "-- none --" else by
    if st.button("Show boxplot for column"):
        fig = plot_boxplot(df, col, by=by_arg, show=False)
        st.pyplot(fig)
