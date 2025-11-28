import streamlit as st # type: ignore
import pandas as pd # type: ignore
import io

from auto_eda_pro import (
    detect_column_types,
    summary_stats,
    plot_histogram,
    plot_correlation_heatmap_from_df,
)

def render():
    """
    Render the Overview page for the Streamlit app.
    Expects the DataFrame to be present in st.session_state["df"].
    """
    st.header("Overview")
    df = st.session_state.get("df")
    if df is None or df.empty:
        st.warning("No dataset loaded. Please upload a CSV or select an example.")
        return

    st.subheader("Quick dataset info")
    cols = df.shape[1]
    rows = df.shape[0]
    st.write(f"Rows: **{rows}**, Columns: **{cols}**")
    if st.checkbox("Show raw data (first 10 rows)"):
        st.dataframe(df.head(10))

    st.subheader("Detected column types")
    types = detect_column_types(df)
    for tname, clist in types.items():
        st.write(f"**{tname}** — {len(clist)} columns")
        if st.checkbox(f"Show columns: {tname}", key=f"cols_{tname}"):
            st.write(clist)

    st.subheader("Summary statistics")
    detect_override = st.checkbox("Treat low-cardinality numeric as numeric (override)", value=False)
    detect_kwargs = {"max_unique_for_categorical": 2} if detect_override else {}
    try:
        summary_df = summary_stats(df, detect_kwargs=detect_kwargs)
        st.dataframe(summary_df)
        csv_buf = io.StringIO()
        summary_df.to_csv(csv_buf)
        csv_bytes = csv_buf.getvalue().encode("utf-8")
        st.download_button("Download summary CSV", data=csv_bytes, file_name="summary_stats.csv")
    except Exception as e:
        st.error(f"Could not compute summary statistics: {e}")

    st.subheader("Example distribution (histogram)")
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if numeric_cols:
        sel = st.selectbox("Choose numeric column for histogram", numeric_cols, index=0)
        if st.button("Plot histogram"):
            fig = plot_histogram(df, sel, show=False)
            st.pyplot(fig)
    else:
        st.info("No numeric columns available for histogram.")
