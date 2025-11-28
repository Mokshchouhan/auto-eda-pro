#!/usr/bin/env python
import os
from pathlib import Path
import click
import pandas as pd # type: ignore

from auto_eda_pro import (
    load_csv,
    detect_column_types,
    summary_stats,
    missing_summary,
    correlation_matrix,
    iqr_outlier_mask,
    zscore_outlier_mask,
    plot_missing_heatmap,
    plot_correlation_heatmap_from_df,
)

@click.command()
@click.argument("csv_path", type=click.Path(exists=True))
@click.option("--out-dir", "-o", default="outputs", help="Directory to save reports/figures")
@click.option("--show-plots/--no-show-plots", default=False, help="Show plots interactively")
@click.option("--detect-max-unique", default=None, type=int,
              help="Override max_unique_for_categorical for type detection (optional)")
def main(csv_path, out_dir, show_plots, detect_max_unique):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    click.echo(f"Loading CSV: {csv_path}")
    df = load_csv(csv_path)

    # Type detection (allow override)
    detect_kwargs = {}
    if detect_max_unique is not None:
        detect_kwargs["max_unique_for_categorical"] = detect_max_unique
    types = detect_column_types(df, **detect_kwargs)
    click.echo("Detected column types:")
    for k, v in types.items():
        click.echo(f"  {k}: {len(v)} cols")

    # Summary stats
    click.echo("Computing summary statistics...")
    summary = summary_stats(df, detect_kwargs=detect_kwargs)
    summary_csv = out / "summary_stats.csv"
    summary.to_csv(summary_csv)
    click.echo(f"Saved summary stats -> {summary_csv}")

    # Missing
    click.echo("Computing missing value summary...")
    msum = missing_summary(df)
    msum_csv = out / "missing_summary.csv"
    msum.to_csv(msum_csv)
    click.echo(f"Saved missing summary -> {msum_csv}")

    # Correlation
    click.echo("Computing correlations (numeric only)...")
    corr = correlation_matrix(df)
    if not corr.empty:
        corr_csv = out / "correlation_matrix.csv"
        corr.to_csv(corr_csv)
        click.echo(f"Saved correlation matrix -> {corr_csv}")
        fig_corr = plot_correlation_heatmap_from_df(df, show=show_plots)
        fig_corr.savefig(out / "correlation_heatmap.png")
        click.echo(f"Saved correlation heatmap -> {out/'correlation_heatmap.png'}")
    else:
        click.echo("No numeric columns found for correlation.")

    # Outliers
    click.echo("Detecting outliers (IQR and Z-score)...")
    iqr_mask = iqr_outlier_mask(df)
    z_mask = zscore_outlier_mask(df)
    (out / "outliers").mkdir(exist_ok=True, parents=True)
    iqr_mask.astype(int).to_csv(out / "outliers" / "iqr_mask.csv", index=True)
    z_mask.astype(int).to_csv(out / "outliers" / "zscore_mask.csv", index=True)
    click.echo(f"Saved outlier masks -> {out/'outliers'}")

    # Missing heatmap (visual)
    try:
        fig_missing = plot_missing_heatmap(df, show=show_plots)
        fig_missing.savefig(out / "missing_heatmap.png")
        click.echo(f"Saved missing heatmap -> {out/'missing_heatmap.png'}")
    except Exception as e:
        click.echo(f"Could not create missing heatmap: {e}")

    click.echo("EDA complete. Reports and figures are in: " + str(out.resolve()))

if __name__ == "__main__":
    main()
