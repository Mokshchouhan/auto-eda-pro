import streamlit as st # type: ignore
import io
from auto_eda_pro import missing_summary, missing_matrix, plot_missing_heatmap

def render():
    st.header("Missing values")
    df = st.session_state.get("df")
    if df is None or df.empty:
        st.warning("No dataset loaded. Please upload a CSV or select an example.")
        return

    st.subheader("Missing summary (per column)")
    try:
        msum = missing_summary(df)
        st.dataframe(msum)
        buf = io.StringIO()
        msum.to_csv(buf)
        st.download_button("Download missing summary CSV", data=buf.getvalue().encode("utf-8"), file_name="missing_summary.csv")
    except Exception as e:
        st.error(f"Error computing missing summary: {e}")

    st.subheader("Missing matrix heatmap")
    show_preview = st.checkbox("Show heatmap preview", value=True)
    cmap = st.selectbox("Choose colormap", ["viridis", "magma", "coolwarm", "YlGnBu"], index=0)
    figsize_x = st.slider("Figure width", 6, 20, 10)
    figsize_y = st.slider("Figure height", 3, 12, 4)
    if show_preview:
        try:
            fig = plot_missing_heatmap(df, figsize=(figsize_x, figsize_y), cmap=cmap, show=False)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Could not render heatmap: {e}")

    st.info("Columns with high missing_ratio may need imputation or removal.")
