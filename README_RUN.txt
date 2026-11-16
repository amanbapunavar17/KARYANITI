KARYANITI — VISUALIZATION STARTER
=================================

CONTENTS
- app.py: Streamlit dashboard with four separate analytical modules
- requirements.txt: Python dependencies
- data/: the four cleaned datasets supplied for this project

RUN ON WINDOWS
1. Install Python 3.10 or newer.
2. Extract this ZIP.
3. Open Command Prompt inside the extracted KARYANITI_Visualization_Starter folder.
4. Create a virtual environment:
      py -m venv .venv
5. Activate it:
      .venv\Scripts\activate
6. Install packages:
      pip install -r requirements.txt
7. Start the dashboard:
      streamlit run app.py
8. Open the local URL shown in the terminal (usually http://localhost:8501).

IMPORTANT DATA NOTES
- The four datasets are analyzed independently; they are not joined together.
- The large Employee Well-being dataset is synthetic, not real employee/faculty records.
- The dashboard displays descriptive patterns and associations. It does not yet train or validate an attrition prediction model.
- Review unusual values and missing values before presenting conclusions.
- Burnout scores are displayed as supplied in the cleaned workbook; verify the score definition and valid range before interpreting them as a health measure.

NEXT DEVELOPMENT STEPS
1. Review every chart and verify the business interpretation.
2. Add data-quality summaries and exportable reports.
3. Add a validated predictive modelling module only after checking target labels and leakage.
4. Add faculty-specific analysis only when appropriate institution-specific data is collected with permission and privacy safeguards.
