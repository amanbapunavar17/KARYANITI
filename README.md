# KARYANITI — AI-Driven Workforce Intelligence & Well-being Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.20%2B-3F4F75.svg)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-Proprietary-purple.svg)]()

> **KARYANITI** is a workforce intelligence and well-being analytics platform designed to synthesize empirical workload stress, retention signals, enterprise productivity dynamics, and remote-work burnout telemetry across analytically segregated cohorts.

---

## 🏛️ Platform Architecture

The platform operates on strict **Data Governance and Integrity Standards**:
- **Zero Cross-Dataset Record Merging:** Datasets represent distinct analytical cohorts and are analyzed independently.
- **Explicit Synthetic Demarcation:** The 147K-record well-being dataset is explicitly identified and treated as a simulated stress-testing population.
- **Empirical KPI Calculation:** All metrics, distributions, and correlation coefficients are computed directly from the source datasets.
- **Descriptive & Diagnostic Foundation:** Observed associations are clearly distinguished from predictive claims, laying the groundwork for Phase 2 validated machine learning.

---

## 🧭 Analytical Modules

### 1. Executive Intelligence Dashboard
- **Top-Level KPI Matrix:** Empirical attrition rate (40.6%), enterprise turnover baseline (10.0%), well-being stress index (20.6/100), and remote burnout vulnerability (15.1%).
- **Workforce Workload Insights:** Cross-cohort weekly hours distribution and acute fatigue threshold analysis (>55 hours/week).
- **Retention & Attrition Signals:** Departmental attrition gradients and the protective effect of job satisfaction.
- **Productivity & Overtime Balance:** Empirical proof of diminishing returns to excessive overtime ($r = +0.0027$).
- **Burnout & Recovery Buffers:** Remote work after-hours screen fatigue and sleep recovery buffers.
- **Pearson Correlation Matrix:** Full correlation matrix across monitored outcomes.
- **Data-Driven Strategic Recommendations:** Prioritized executive action pillars (P1 Critical to P3 Strategic).
- **Interactive Module Launchpad:** Direct two-way navigation across deep-dive modules.

### 2. Workforce & Attrition Intelligence
- Detailed workload distribution, salary brackets, absence records, and voluntary flight risk.
- Departmental and role-level attrition filtering.

### 3. Employee Performance Intelligence
- Large-scale enterprise benchmark across 9 departments (98,195 records).
- Performance ratings, overtime hours, training duration, and employee experience.

### 4. Workforce Well-being Intelligence (Synthetic Simulation)
- Multi-dimensional well-being simulation (147,296 records).
- Stress, burnout, sleep hours, workday breaks, and institutional campus locations.

### 5. Work-from-Home Burnout Analytics
- Digital remote-work telemetry (1,750 records).
- Daily screen exposure, meeting counts, after-hours work boundaries, and task completion impact ($r = -0.921$).

---

## 📂 Project Structure

```text
KARYANITI/
├── .streamlit/
│   └── config.toml             # Custom theme configuration
├── data/
│   ├── employee_performance_workload_attrition_cleaned.csv
│   ├── Extended_Employee_Performance_and_Productivity_Dataset_Cleaned.csv
│   ├── Large_Employee_Well-being_Dataset__Synthetic__Cleaned.csv
│   └── Work_From_Home_Burnout_Dataset_Cleaned.xls
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Platform documentation
├── README_RUN.txt              # Quick run instructions
└── .gitignore                  # Git ignore rules
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/amanbapunavar17/KARYANITI.git
cd KARYANITI
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
py -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard
```bash
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## 🎨 Enterprise Design System
- **Background:** Warm white (`#FAFAFC` / `#FFFFFF`)
- **Typography:** Deep navy typography (`#1B1F3B`, `#242744`)
- **Surfaces:** Soft lavender surfaces (`#F1EFF9`, `#F7F6FC`) with border accenting (`#E5E1F4`)
- **Highlights:** Royal purple (`#7C5CFC`), vibrant orange (`#FA8231`), subtle gold (`#D49A3D`), and mint (`#20BF6B`)
- **Visualizations:** Fully interactive, responsive Plotly figures matching the enterprise palette
