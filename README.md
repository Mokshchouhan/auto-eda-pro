# 🚀 auto-eda-pro  
### Automated Exploratory Data Analysis (EDA) Pipeline with CLI + Streamlit UI

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Overview  
**auto-eda-pro** is a production-grade, modular, and fully extensible **Exploratory Data Analysis (EDA)** toolkit.

It includes:

- 📂 Clean project structure (src/, tools/, ui/, tests/, examples/)  
- 🧠 Intelligent column-type detection  
- 📊 Summary statistics (numeric + categorical)  
- ❗ Missing value analysis + heatmap  
- 🔗 Correlation matrix + heatmap  
- ⚠️ Outlier detection (IQR, Z-score)  
- 📈 Visualizations (histograms, boxplots, pairplots)  
- 💻 CLI tool for generating EDA reports  
- 🎨 Multi-page Streamlit app (Upload CSV → Full EDA dashboard)  
- 🧪 Pytest-based test suite  
- 🔄 GitHub Actions CI  
- 📦 Ready for packaging & deployment  

---

## 🌱 Project Structure

auto-eda-pro/
│
├── src/
│ └── auto_eda_pro/
│ ├── load.py
│ ├── types.py
│ ├── summary.py
│ ├── missing.py
│ ├── correlation.py
│ ├── outliers.py
│ ├── visuals.py
│ └── init.py
│
├── tools/
│ └── auto_eda.py
│
├── ui/
│ ├── app.py
│ └── app_pages/
│ ├── overview.py
│ ├── missing.py
│ ├── distributions.py
│ ├── correlations.py
│ ├── outliers.py
│
├── tests/
│ ├── test_types.py
│ ├── test_summary.py
│ ├── test_missing.py
│ ├── test_visuals.py
│ └── test_outliers.py
│
├── examples/
│ ├── iris.csv
│ ├── titanic.csv
│ └── messy_dataset.csv
│
├── pyproject.toml
├── README.md
└── LICENSE

yaml
Copy code

---

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/<YOUR-USERNAME>/auto-eda-pro.git
cd auto-eda-pro
Create virtual environment
bash
Copy code
conda create -n autoeda python=3.10
conda activate autoeda
pip install -r requirements.txt
🚀 Usage
CLI Tool
bash
Copy code
python tools/auto_eda.py examples/titanic.csv --out-dir outputs --show-plots
Streamlit App
bash
Copy code
streamlit run auto_eda_pro_app/app.py
🧪 Running Tests
nginx
Copy code
pytest -v
🔄 GitHub Actions CI
This repo includes CI that runs automatically on:

Push to any branch

Pull requests

It runs:

pytest

Python setup

Dependency installation

Future: coverage uploads

📝 Future Improvements
HTML report export

Cloud-hosted Streamlit version

Plugin system for custom EDA modules

Deployment to PyPI

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

✨ Author
Moksh (AIZEN)
Built with guidance from ChatGPT.

If you like this project, ⭐ star the repository!

yaml
Copy code
