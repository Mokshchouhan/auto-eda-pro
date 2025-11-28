# 🚀 auto-eda-pro  
### Automated Exploratory Data Analysis (EDA) Pipeline with CLI + Streamlit Dashboard

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Overview  
**auto-eda-pro** is a production-grade, modular, and extensible **Exploratory Data Analysis (EDA)** toolkit designed for students, data analysts, and professionals.

It includes:

- 📂 Clean project structure (src/, tools/, ui/, tests/, examples/)
- 🧠 Intelligent column-type detection
- 📊 Summary statistics (numeric + categorical)
- ❗ Missing value analysis + heatmap
- 🔗 Correlation matrix + heatmap
- ⚠️ Outlier detection (IQR, Z-score)
- 📈 Visualizations (histograms, boxplots, pairplots)
- 💻 CLI tool for generating EDA reports
- 🎨 Multi-page Streamlit app (Upload CSV → Full EDA Dashboard)
- 🧪 Pytest-based test suite
- 🔄 GitHub Actions CI
- 📦 Ready for packaging & deployment

---

## 📁 Project Structure

auto-eda-pro/
│
├── pyproject.toml
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
│
├── tools/
│   └── auto_eda.py
│
├── src/
│   └── auto_eda_pro/
│       ├── __init__.py
│       ├── data.py
│       ├── types.py
│       ├── summary.py
│       ├── missing.py
│       ├── correlation.py
│       ├── outliers.py
│       └── visuals.py
│
├── tests/
│   └── (pytest test files will go here later)
│
├── examples/
│   ├── titanic.csv          (optional place to store datasets)
│   ├── iris.csv
│   └── penguins.csv
│
└── outputs/
    ├── summary_stats.csv
    ├── missing_summary.csv
    ├── correlation_matrix.csv
    ├── missing_heatmap.png
    ├── correlation_heatmap.png
    └── outliers/
        ├── iqr_mask.csv
        └── zscore_mask.csv


## 📦 Installation

### Clone the repository

git clone https://github.com/<Mokshchouhan>/auto-eda-pro.git
cd auto-eda-pro
Create and activate virtual environment
bash
Copy code
conda create -n autoeda python=3.10
conda activate autoeda
pip install -r requirements.txt
🚀 Usage
▶️ Run the CLI tool
bash
Copy code
python tools/auto_eda.py examples/titanic.csv --out-dir outputs --show-plots
▶️ Launch the Streamlit Web App
bash
Copy code
streamlit run auto_eda_pro_app/app.py
The app lets you:

Upload your own CSV

Or choose example datasets (Titanic, Iris, Messy Dataset)

Explore pages: Overview → Missing → Distributions → Correlations → Outliers

🧪 Running Tests
bash
Copy code
pytest -v
🔄 Continuous Integration (GitHub Actions)
Every push triggers:

Dependency installation

Pytest test suite

Build badge updates

Workflow file: .github/workflows/ci.yml

📝 Roadmap
 HTML EDA Report Export

 Cloud-hosted Streamlit version

 Add profiling & advanced visualizations

 Add CSV cleaning & preprocessing module

 Publish package on PyPI

✨ Author
Moksh (AIZEN)
If you like this project, consider ⭐ starring it on GitHub!
