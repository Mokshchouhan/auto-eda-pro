import streamlit as st # type: ignore
import io
from auto_eda_pro import correlation_matrix, plot_correlation_heatmap_from_df
import pandas as pd # type: ignore

def render():
    st.header("Correlations")
    df = st.session_state.get("df")
    if df is None or df.empty:
        st.warning("No dataset loaded. Please upload a CSV or select an example.")
        return

    st.subheader("Correlation matrix (numeric only)")
    method = st.selectbox("Method", ["pearson", "spearman", "kendall"], index=0)
    try:
        corr = correlation_matrix(df, method=method)
        if corr.empty:
            st.info("No numeric columns to compute correlations.")
            return
        st.dataframe(corr)
        buf = io.StringIO()
        corr.to_csv(buf)
        st.download_button("Download correlation CSV", data=buf.getvalue().encode("utf-8"), file_name="correlation_matrix.csv")
    except Exception as e:
        st.error(f"Could not compute correlation matrix: {e}")

    st.subheader("Correlation heatmap")
    figsize_x = st.slider("Figure width", 6, 20, 10)
    figsize_y = st.slider("Figure height", 4, 16, 8)
    if st.button("Plot correlation heatmap"):
        try:
            fig = plot_correlation_heatmap_from_df(df, method=method, figsize=(figsize_x, figsize_y), show=False)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Could not render heatmap: {e}")
