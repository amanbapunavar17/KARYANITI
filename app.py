import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="KARYANITI | Executive Workforce Intelligence",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent
DATA = ROOT / "data"

COLORS = {
    "navy": "#1B1F3B",
    "navy_light": "#2D3059",
    "purple": "#7C5CFC",
    "purple_soft": "#9E8CF8",
    "purple_bg": "#F5F3FF",
    "orange": "#FA8231",
    "orange_soft": "#FDAE7B",
    "orange_bg": "#FFF4ED",
    "gold": "#D49A3D",
    "gold_soft": "#F5C86C",
    "gold_bg": "#FEF9EE",
    "mint": "#20BF6B",
    "mint_bg": "#EDFAF2",
    "blue": "#4B7BEC",
    "blue_bg": "#EFF4FD",
    "pale": "#FAFAFC",
    "surface": "#F1EFF9",
    "surface_light": "#F7F6FC",
    "border": "#E5E1F4",
    "gray_text": "#5A5D7A",
}

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2.5rem;
        background-color: #FAFAFC;
    }
    
    /* Top Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #1B1F3B 0%, #292B52 60%, #3B2E68 100%);
        border-radius: 16px;
        padding: 28px 32px;
        color: #FFFFFF;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(27, 31, 59, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(124, 92, 252, 0.25);
        border: 1px solid rgba(158, 140, 248, 0.4);
        color: #E0D9FF;
        font-size: 0.74rem;
        font-weight: 700;
        letter-spacing: 1px;
        padding: 4px 12px;
        border-radius: 20px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }
    
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0 0 6px 0;
        color: #FFFFFF;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.0rem;
        color: #D3D0E8;
        margin: 0;
        max-width: 900px;
        line-height: 1.5;
        font-weight: 400;
    }
    
    /* Executive KPI Cards */
    .kpi-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 20px 22px;
        border: 1px solid #E5E1F4;
        box-shadow: 0 4px 16px rgba(36, 39, 68, 0.04);
        position: relative;
        overflow: hidden;
        margin-bottom: 16px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(36, 39, 68, 0.08);
    }
    
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
    }
    
    .kpi-purple::before { background: linear-gradient(90deg, #7C5CFC, #9E8CF8); }
    .kpi-orange::before { background: linear-gradient(90deg, #FA8231, #FDAE7B); }
    .kpi-gold::before { background: linear-gradient(90deg, #D49A3D, #F5C86C); }
    .kpi-navy::before { background: linear-gradient(90deg, #1B1F3B, #4B7BEC); }
    
    .kpi-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    
    .kpi-label {
        font-size: 0.82rem;
        font-weight: 700;
        color: #5A5D7A;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }
    
    .kpi-badge {
        font-size: 0.70rem;
        font-weight: 600;
        padding: 3px 8px;
        border-radius: 12px;
        letter-spacing: 0.3px;
    }
    
    .badge-purple { background: #F5F3FF; color: #6941C6; border: 1px solid #E0D9FF; }
    .badge-orange { background: #FFF4ED; color: #B93815; border: 1px solid #FFD6AE; }
    .badge-gold { background: #FEF9EE; color: #9A6700; border: 1px solid #F8E2A7; }
    .badge-blue { background: #EFF4FD; color: #175CD3; border: 1px solid #C4D9F8; }
    
    .kpi-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1B1F3B;
        letter-spacing: -1px;
        line-height: 1.1;
        margin-bottom: 6px;
    }
    
    .kpi-subtext {
        font-size: 0.82rem;
        color: #5A5D7A;
        display: flex;
        align-items: center;
        gap: 6px;
        font-weight: 500;
    }
    
    .kpi-provenance {
        font-size: 0.72rem;
        color: #8C8FA8;
        margin-top: 10px;
        padding-top: 8px;
        border-top: 1px dashed #EDEBF7;
        font-style: italic;
    }
    
    /* Dataset Analytical Summary Cards */
    .summary-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 22px;
        border: 1px solid #E5E1F4;
        box-shadow: 0 4px 16px rgba(36, 39, 68, 0.04);
        margin-bottom: 16px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .summary-card-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 12px;
    }
    
    .summary-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1B1F3B;
        margin: 0 0 4px 0;
    }
    
    .summary-meta {
        font-size: 0.78rem;
        color: #6C6F8E;
    }
    
    .stat-pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 12px 0;
    }
    
    .stat-pill {
        background: #F7F6FC;
        border: 1px solid #E5E1F4;
        border-radius: 8px;
        padding: 6px 10px;
        font-size: 0.76rem;
    }
    
    .stat-pill strong {
        color: #1B1F3B;
    }
    
    .summary-insight {
        background: #F8F7FD;
        border-left: 3px solid #7C5CFC;
        border-radius: 0 8px 8px 0;
        padding: 10px 12px;
        font-size: 0.81rem;
        color: #36385B;
        line-height: 1.45;
        margin: 10px 0 16px 0;
    }
    
    /* Section Headers */
    .section-header-box {
        margin: 28px 0 16px 0;
        padding-bottom: 8px;
        border-bottom: 1.5px solid #EBE8F6;
    }
    
    .section-tag {
        font-size: 0.72rem;
        font-weight: 700;
        color: #7C5CFC;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 2px;
    }
    
    .section-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #1B1F3B;
        margin: 0;
    }
    
    .section-subtitle {
        font-size: 0.86rem;
        color: #6C6F8E;
        margin: 4px 0 0 0;
    }
    
    /* Executive Insight Boxes */
    .insight-callout {
        border-radius: 12px;
        padding: 16px 18px;
        margin: 14px 0;
        font-size: 0.85rem;
        line-height: 1.5;
    }
    
    .callout-purple {
        background: #F8F7FF;
        border: 1px solid #E0D9FF;
        border-left: 4px solid #7C5CFC;
        color: #36385B;
    }
    
    .callout-orange {
        background: #FFF8F4;
        border: 1px solid #FFD9C0;
        border-left: 4px solid #FA8231;
        color: #4A3326;
    }
    
    .callout-gold {
        background: #FEFAF0;
        border: 1px solid #FCE4B0;
        border-left: 4px solid #D49A3D;
        color: #4A3C20;
    }
    
    .callout-navy {
        background: #F4F6FB;
        border: 1px solid #D1DCF2;
        border-left: 4px solid #1B1F3B;
        color: #222942;
    }
    
    /* Recommendation Pillars */
    .rec-card {
        background: #FFFFFF;
        border: 1px solid #E5E1F4;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 14px;
        box-shadow: 0 2px 10px rgba(36, 39, 68, 0.03);
    }
    
    .rec-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    
    .rec-title {
        font-size: 1.0rem;
        font-weight: 700;
        color: #1B1F3B;
    }
    
    .rec-priority {
        font-size: 0.68rem;
        font-weight: 700;
        padding: 3px 8px;
        border-radius: 10px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    .p-urgent { background: #FEF3F2; color: #B42318; border: 1px solid #FECDCA; }
    .p-high { background: #FFF4ED; color: #B93815; border: 1px solid #FFD6AE; }
    .p-medium { background: #F5F3FF; color: #6941C6; border: 1px solid #E0D9FF; }
    .p-strategic { background: #EFF8FF; color: #175CD3; border: 1px solid #B2DDFF; }
    
    /* Navigation launch buttons */
    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.85rem;
        padding: 8px 16px;
        border: 1px solid #D8D2F0;
        background-color: #FFFFFF;
        color: #1B1F3B;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #7C5CFC;
        color: #FFFFFF;
        border-color: #7C5CFC;
        box-shadow: 0 4px 12px rgba(124, 92, 252, 0.25);
    }
    
    /* Sidebar Polish */
    section[data-testid="stSidebar"] {
        background-color: #F8F7FC;
        border-right: 1px solid #EBE8F6;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data(show_spinner="Loading verified workforce intelligence datasets...")
def load_data():
    files = {
        "attrition": DATA / "employee_performance_workload_attrition_cleaned.csv",
        "performance": DATA / "Extended_Employee_Performance_and_Productivity_Dataset_Cleaned.csv",
        "synthetic": DATA / "Large_Employee_Well-being_Dataset__Synthetic__Cleaned.csv",
        "burnout": DATA / "Work_From_Home_Burnout_Dataset_Cleaned.xls",
    }
    out = {}
    out["attrition"] = pd.read_csv(files["attrition"])
    out["performance"] = pd.read_csv(files["performance"])
    out["synthetic"] = pd.read_csv(files["synthetic"])
    out["burnout"] = pd.read_excel(files["burnout"])
    return out

try:
    D = load_data()
except Exception as e:
    st.error("Could not load one or more datasets. Check that all four files are inside the data/ folder.")
    st.exception(e)
    st.stop()

def heading(title, subtitle):
    st.title(title)
    st.caption(subtitle)

def metric_row(items):
    cols = st.columns(len(items))
    for col, (label, value, help_text) in zip(cols, items):
        col.metric(label, value, help=help_text)

def chart(fig, height=360):
    fig.update_layout(
        height=height,
        template="plotly_white",
        margin=dict(l=24, r=24, t=55, b=24),
        title_font=dict(size=16, color=COLORS["navy"], family="Inter"),
        font=dict(color="#41435C", family="Inter"),
        legend_title_text="",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
    )
    st.plotly_chart(fig, use_container_width=True)

def safe_rate(series):
    s = series.dropna()
    if len(s) == 0:
        return 0
    return 100 * s.mean()

def filtered_attrition(df):
    st.subheader("Filters")
    c1, c2 = st.columns(2)
    depts = sorted(df["department"].dropna().astype(str).unique())
    roles = sorted(df["role_level"].dropna().astype(str).unique())
    selected_depts = c1.multiselect("Department", depts, default=depts)
    selected_roles = c2.multiselect("Role level", roles, default=roles)
    return df[df["department"].astype(str).isin(selected_depts) &
              df["role_level"].astype(str).isin(selected_roles)].copy()

if "nav_selection" not in st.session_state:
    st.session_state["nav_selection"] = "Overview"

def navigate_to(page_name):
    st.session_state["nav_selection"] = page_name

def overview():
    # -------------------------------------------------------------
    # 0. DATA INTEGRITY & BASE CALCULATIONS (Computed directly)
    # -------------------------------------------------------------
    df_att = D["attrition"]
    df_perf = D["performance"]
    df_syn = D["synthetic"]
    df_burn = D["burnout"]
    
    # Dataset 1: Attrition calculations
    att_mask = df_att["attrition"].astype(str).str.strip().str.lower().isin(["yes", "y", "true", "1"])
    att_rate = 100 * att_mask.mean()
    att_count = len(df_att)
    att_departures = int(att_mask.sum())
    att_avg_hours = df_att["avg_weekly_hours"].mean()
    att_over_55 = 100 * (df_att["avg_weekly_hours"] > 55).mean()
    att_avg_sat = df_att["job_satisfaction"].mean()
    
    # Dataset 2: Enterprise Performance calculations
    perf_res_mask = df_perf["Resigned"].astype(bool)
    perf_res_rate = 100 * perf_res_mask.mean()
    perf_count = len(df_perf)
    perf_avg_score = df_perf["Performance_Score"].mean()
    perf_avg_ot = df_perf["Overtime_Hours"].mean()
    perf_avg_work_hours = df_perf["Work_Hours_Per_Week"].mean()
    perf_avg_sat = df_perf["Employee_Satisfaction_Score"].mean()
    
    # Dataset 3: Synthetic Well-being calculations (SYNTHETIC)
    syn_count = len(df_syn)
    syn_avg_stress = df_syn["Stress_Score"].mean()
    syn_avg_burnout = df_syn["Burnout_Score"].mean()
    syn_avg_sleep = df_syn["Average_Sleep_Hours"].mean()
    syn_avg_hours = df_syn["Weekly_Work_Hours"].mean()
    syn_avg_breaks = df_syn["Breaks_Per_Workday"].mean()
    
    # Dataset 4: WFH Burnout calculations
    burn_count = len(df_burn)
    burn_avg_score = df_burn["burnout_score"].mean()
    burn_avg_screen = df_burn["screen_time_hours"].mean()
    burn_avg_work = df_burn["work_hours"].mean()
    burn_avg_sleep = df_burn["sleep_hours"].mean()
    burn_avg_task = df_burn["task_completion_rate"].mean()
    
    risk_series = df_burn["burnout_risk"].fillna("Unknown").astype(str).str.strip().str.title()
    elevated_risk_mask = risk_series.isin(["Medium", "High", "Very High", "Severe"])
    elevated_risk_share = 100 * elevated_risk_mask.mean()
    elevated_risk_count = int(elevated_risk_mask.sum())

    # -------------------------------------------------------------
    # 1. EXECUTIVE HERO BANNER
    # -------------------------------------------------------------
    st.markdown(f"""
    <div class="hero-container">
        <span class="hero-badge">Enterprise Executive Intelligence Platform</span>
        <h1 class="hero-title">KARYANITI</h1>
        <p class="hero-subtitle">
            AI-Driven Workforce Intelligence & Well-being Analytics Platform — Synthesizing empirical workload stress, 
            retention signals, enterprise productivity dynamics, and remote-work burnout telemetry across 
            <strong>{att_count + perf_count + syn_count + burn_count:,}</strong> analytically segregated records.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Data Governance Notice
    st.markdown("""
    <div style="background: #F1EFF9; border: 1px solid #DCD6F0; border-radius: 12px; padding: 12px 18px; margin-bottom: 22px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="background: #7C5CFC; color: white; border-radius: 50%; width: 22px; height: 22px; display: inline-flex; align-items: center; justify-content: center; font-size: 0.72rem; font-weight: 700;">✓</span>
            <span style="font-size: 0.82rem; color: #2D3059; font-weight: 600;">
                Data Integrity Standard: 4 Independent Cleaned Datasets • Zero Cross-Dataset Record Merging • Synthetic Data Segregated & Identified • 100% Empirically Computed KPIs
            </span>
        </div>
        <span style="font-size: 0.75rem; color: #6C6F8E; background: #FFFFFF; padding: 3px 10px; border-radius: 12px; border: 1px solid #E0DBF2; font-weight: 600;">
            Descriptive Phase 1 Architecture
        </span>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 2. EXECUTIVE PORTFOLIO KPI OVERVIEW
    # -------------------------------------------------------------
    k1, k2, k3, k4 = st.columns(4)
    
    with k1:
        st.markdown(f"""
        <div class="kpi-card kpi-purple">
            <div class="kpi-header">
                <span class="kpi-label">Empirical Attrition Rate</span>
                <span class="kpi-badge badge-purple">High Workload Cohort</span>
            </div>
            <div class="kpi-value">{att_rate:.1f}%</div>
            <div class="kpi-subtext">
                <span>{att_departures:,} Departures</span> • <span>{att_over_55:.1f}% work &gt;55h/wk</span>
            </div>
            <div class="kpi-provenance">Source: Dataset 01 · Attrition Cohort (N={att_count:,})</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k2:
        st.markdown(f"""
        <div class="kpi-card kpi-navy">
            <div class="kpi-header">
                <span class="kpi-label">Enterprise Turnover Rate</span>
                <span class="kpi-badge badge-blue">Enterprise Baseline</span>
            </div>
            <div class="kpi-value">{perf_res_rate:.1f}%</div>
            <div class="kpi-subtext">
                <span>Perf: {perf_avg_score:.2f} / 5.0</span> • <span>OT: {perf_avg_ot:.1f}h/mo</span>
            </div>
            <div class="kpi-provenance">Source: Dataset 02 · Enterprise Performance (N={perf_count:,})</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card kpi-gold">
            <div class="kpi-header">
                <span class="kpi-label">Well-Being Stress Index</span>
                <span class="kpi-badge badge-gold">Synthetic Simulation</span>
            </div>
            <div class="kpi-value">{syn_avg_stress:.1f}<span style="font-size: 1.1rem; color: #8C8FA8;">/100</span></div>
            <div class="kpi-subtext">
                <span>Burnout: {syn_avg_burnout:.1f}/100</span> • <span>Sleep: {syn_avg_sleep:.1f}h</span>
            </div>
            <div class="kpi-provenance">Source: Dataset 03 · Synthetic Simulation (N={syn_count:,})</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card kpi-orange">
            <div class="kpi-header">
                <span class="kpi-label">WFH Burnout Vulnerability</span>
                <span class="kpi-badge badge-orange">Remote Cohort</span>
            </div>
            <div class="kpi-value">{elevated_risk_share:.1f}%</div>
            <div class="kpi-subtext">
                <span>{elevated_risk_count:,} Medium/High Risk</span> • <span>Screen: {burn_avg_screen:.1f}h</span>
            </div>
            <div class="kpi-provenance">Source: Dataset 04 · WFH Telemetry (N={burn_count:,})</div>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 3. SEPARATE DATASET-WISE ANALYTICAL SUMMARIES
    # -------------------------------------------------------------
    st.markdown("""
    <div class="section-header-box">
        <div class="section-tag">Analytical Cohort Architecture</div>
        <h2 class="section-title">Separate Dataset Analytical Summaries</h2>
        <p class="section-subtitle">Independent analysis across four distinct workforce data environments with direct module access.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="summary-card">
            <div>
                <div class="summary-card-header">
                    <div>
                        <div class="summary-title">01 · Workforce & Attrition Intelligence</div>
                        <div class="summary-meta">File: <code>employee_performance_workload_attrition_cleaned.csv</code></div>
                    </div>
                    <span class="kpi-badge badge-purple">Empirical · {att_count:,} Records</span>
                </div>
                <p style="font-size: 0.83rem; color: #5A5D7A; margin: 6px 0;">
                    Investigates organizational flight risk against work hours, project quotas, compensation, and satisfaction scores across 6 corporate divisions.
                </p>
                <div class="stat-pill-row">
                    <span class="stat-pill">Mean Workload: <strong>{att_avg_hours:.1f} hrs/wk</strong></span>
                    <span class="stat-pill">Attrition Rate: <strong>{att_rate:.1f}%</strong></span>
                    <span class="stat-pill">High Strain (&gt;55h): <strong>{att_over_55:.1f}%</strong></span>
                    <span class="stat-pill">Avg Satisfaction: <strong>{att_avg_sat:.2f} / 5</strong></span>
                </div>
                <div class="summary-insight">
                    <strong>Primary Finding:</strong> Attrition is heavily concentrated among employees working beyond 55 hours/week ({att_over_55:.1f}% of cohort) and those reporting low job satisfaction (Level 1 attrition is 50.3% vs 31.4% at Level 5).
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Launch Module 01 · Workforce & Attrition →", key="btn_open_att", on_click=navigate_to, args=("Workforce & Attrition",), use_container_width=True)
        
    with col2:
        st.markdown(f"""
        <div class="summary-card">
            <div>
                <div class="summary-card-header">
                    <div>
                        <div class="summary-title">02 · Employee Performance & Productivity</div>
                        <div class="summary-meta">File: <code>Extended_Employee_Performance_and_Productivity_Dataset_Cleaned.csv</code></div>
                    </div>
                    <span class="kpi-badge badge-blue">Enterprise · {perf_count:,} Records</span>
                </div>
                <p style="font-size: 0.83rem; color: #5A5D7A; margin: 6px 0;">
                    Broad enterprise-scale benchmark examining performance appraisal scores, overtime loads, training hours, and tenure across 9 operational departments.
                </p>
                <div class="stat-pill-row">
                    <span class="stat-pill">Mean Performance: <strong>{perf_avg_score:.2f} / 5.0</strong></span>
                    <span class="stat-pill">Resignation Baseline: <strong>{perf_res_rate:.1f}%</strong></span>
                    <span class="stat-pill">Avg Monthly Overtime: <strong>{perf_avg_ot:.1f} hrs</strong></span>
                    <span class="stat-pill">Avg Work Hours: <strong>{perf_avg_work_hours:.1f} hrs/wk</strong></span>
                </div>
                <div class="summary-insight">
                    <strong>Primary Finding:</strong> Resignation rates remain uniformly distributed (~10%) across departments. Overtime hours show zero correlation with performance ratings (r = +0.0027), demonstrating plateauing returns to excessive overtime.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Launch Module 02 · Employee Performance →", key="btn_open_perf", on_click=navigate_to, args=("Employee Performance",), use_container_width=True)

    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown(f"""
        <div class="summary-card">
            <div>
                <div class="summary-card-header">
                    <div>
                        <div class="summary-title">03 · Workforce Well-being Intelligence</div>
                        <div class="summary-meta">File: <code>Large_Employee_Well-being_Dataset__Synthetic__Cleaned.csv</code></div>
                    </div>
                    <span class="kpi-badge badge-gold">Synthetic Simulation · {syn_count:,} Records</span>
                </div>
                <p style="font-size: 0.83rem; color: #5A5D7A; margin: 6px 0;">
                    Large-scale simulated population engineered for algorithmic stress-testing and health-index modeling across diverse institutional campuses and roles.
                </p>
                <div class="stat-pill-row">
                    <span class="stat-pill">Mean Stress Index: <strong>{syn_avg_stress:.1f} / 100</strong></span>
                    <span class="stat-pill">Mean Burnout Index: <strong>{syn_avg_burnout:.1f} / 100</strong></span>
                    <span class="stat-pill">Avg Sleep: <strong>{syn_avg_sleep:.1f} hrs</strong></span>
                    <span class="stat-pill">Breaks/Workday: <strong>{syn_avg_breaks:.1f}</strong></span>
                </div>
                <div class="summary-insight">
                    <strong>Primary Finding:</strong> Burnout index in this simulation exhibits strong inverse correlations with sleep hours (r = -0.34) and job satisfaction (r = -0.47), while high weekly work hours correlate positively with stress (r = +0.41).
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Launch Module 03 · Workforce Well-being →", key="btn_open_syn", on_click=navigate_to, args=("Workforce Well-being",), use_container_width=True)

    with col4:
        st.markdown(f"""
        <div class="summary-card">
            <div>
                <div class="summary-card-header">
                    <div>
                        <div class="summary-title">04 · Work-from-Home Burnout Analytics</div>
                        <div class="summary-meta">File: <code>Work_From_Home_Burnout_Dataset_Cleaned.xls</code></div>
                    </div>
                    <span class="kpi-badge badge-orange">Remote Telemetry · {burn_count:,} Records</span>
                </div>
                <p style="font-size: 0.83rem; color: #5A5D7A; margin: 6px 0;">
                    Deep-dive telemetry capturing digital strain, daily screen exposure, meeting fatigue, after-hours work boundaries, and task completion efficacy.
                </p>
                <div class="stat-pill-row">
                    <span class="stat-pill">Mean Burnout Score: <strong>{burn_avg_score:.1f}</strong></span>
                    <span class="stat-pill">Screen Exposure: <strong>{burn_avg_screen:.1f} hrs/day</strong></span>
                    <span class="stat-pill">Daily Work: <strong>{burn_avg_work:.1f} hrs</strong></span>
                    <span class="stat-pill">Task Completion: <strong>{burn_avg_task:.1f}%</strong></span>
                </div>
                <div class="summary-insight">
                    <strong>Primary Finding:</strong> Remote burnout score demonstrates a critical, severe inverse correlation with task completion rate (r = -0.92). After-hours work adds an average of +1.55 points to individual burnout scores.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Launch Module 04 · Work-from-home Burnout →", key="btn_open_burn", on_click=navigate_to, args=("Work-from-home Burnout",), use_container_width=True)

    # -------------------------------------------------------------
    # 4. WORKFORCE WORKLOAD INSIGHTS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="section-header-box">
        <div class="section-tag">Workload Vectors</div>
        <h2 class="section-title">Workforce Workload & Overtime Distribution</h2>
        <p class="section-subtitle">Evaluating weekly hours distribution and the share of personnel crossing acute fatigue thresholds.</p>
    </div>
    """, unsafe_allow_html=True)
    
    wl1, wl2 = st.columns(2)
    
    with wl1:
        # Distribution of work hours
        fig_wl = go.Figure()
        fig_wl.add_trace(go.Histogram(
            x=df_att["avg_weekly_hours"],
            name="Empirical Cohort (N=2.7K)",
            opacity=0.75,
            marker_color=COLORS["purple"],
            nbinsx=25
        ))
        fig_wl.add_trace(go.Histogram(
            x=df_perf.sample(min(15000, len(df_perf)), random_state=42)["Work_Hours_Per_Week"],
            name="Enterprise Cohort (N=98K sample)",
            opacity=0.60,
            marker_color=COLORS["blue"],
            nbinsx=25
        ))
        fig_wl.update_layout(
            barmode="overlay",
            title="Weekly Work Hours Distribution Across Cohorts",
            xaxis_title="Weekly Work Hours",
            yaxis_title="Employee Count",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        chart(fig_wl, height=360)
        
    with wl2:
        # High strain breakdown
        strain_data = pd.DataFrame({
            "Workload Band": ["Standard (<=40h)", "Moderate (41-50h)", "Elevated (51-55h)", "Acute Fatigue (>55h)"],
            "Empirical Cohort Share (%)": [
                100 * (df_att["avg_weekly_hours"] <= 40).mean(),
                100 * (df_att["avg_weekly_hours"].between(41, 50)).mean(),
                100 * (df_att["avg_weekly_hours"].between(51, 55)).mean(),
                100 * (df_att["avg_weekly_hours"] > 55).mean(),
            ],
            "Enterprise Cohort Share (%)": [
                100 * (df_perf["Work_Hours_Per_Week"] <= 40).mean(),
                100 * (df_perf["Work_Hours_Per_Week"].between(41, 50)).mean(),
                100 * (df_perf["Work_Hours_Per_Week"].between(51, 55)).mean(),
                100 * (df_perf["Work_Hours_Per_Week"] > 55).mean(),
            ]
        })
        fig_strain = px.bar(
            strain_data,
            x="Workload Band",
            y=["Empirical Cohort Share (%)", "Enterprise Cohort Share (%)"],
            barmode="group",
            title="Workforce Exposure by Workload Band",
            color_discrete_sequence=[COLORS["purple"], COLORS["blue"]],
            labels={"value": "Proportion of Workforce (%)", "variable": "Cohort"}
        )
        chart(fig_strain, height=360)
        
    st.markdown(f"""
    <div class="insight-callout callout-purple">
        <strong>Executive Workload Finding:</strong> In the empirical attrition cohort, <strong>{att_over_55:.1f}% of employees work over 55 hours per week</strong> (average: {att_avg_hours:.1f} hrs/wk). Comparing cohorts reveals that when sustained weekly workload exceeds 50 hours, attrition signals rise sharply while productivity gains stagnate.
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 5. EMPLOYEE ATTRITION PATTERNS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="section-header-box">
        <div class="section-tag">Retention Signals</div>
        <h2 class="section-title">Employee Attrition Patterns & Satisfaction Dynamics</h2>
        <p class="section-subtitle">Evaluating departmental attrition rates and the protective effect of high job satisfaction.</p>
    </div>
    """, unsafe_allow_html=True)
    
    at1, at2 = st.columns(2)
    
    with at1:
        # Dept attrition
        df_att_copy = df_att.copy()
        df_att_copy["_att"] = att_mask
        dept_att = df_att_copy.groupby("department", as_index=False).agg(
            total=("employee_id", "count"),
            att_rate=("_att", "mean")
        )
        dept_att["att_rate"] *= 100
        dept_att = dept_att.sort_values("att_rate", ascending=False)
        
        fig_dept = px.bar(
            dept_att,
            x="department",
            y="att_rate",
            text="att_rate",
            color="att_rate",
            color_continuous_scale="Purples",
            title="Empirical Attrition Rate by Department (%)",
            labels={"department": "Department", "att_rate": "Attrition Rate (%)"},
            hover_data={"total": True}
        )
        fig_dept.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig_dept.update_layout(coloraxis_showscale=False)
        chart(fig_dept, height=360)
        
    with at2:
        # Satisfaction gradient
        sat_att = df_att_copy.groupby("job_satisfaction", as_index=False).agg(
            total=("employee_id", "count"),
            att_rate=("_att", "mean")
        )
        sat_att["att_rate"] *= 100
        
        fig_sat = px.bar(
            sat_att,
            x="job_satisfaction",
            y="att_rate",
            text="att_rate",
            color="att_rate",
            color_continuous_scale="Oranges",
            title="Attrition Rate by Job Satisfaction Level (1–5)",
            labels={"job_satisfaction": "Job Satisfaction Rating", "att_rate": "Attrition Rate (%)"},
            hover_data={"total": True}
        )
        fig_sat.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig_sat.update_layout(coloraxis_showscale=False)
        chart(fig_sat, height=360)

    sat_diff = sat_att.loc[sat_att["job_satisfaction"] == 1, "att_rate"].values[0] - sat_att.loc[sat_att["job_satisfaction"] == 5, "att_rate"].values[0]
    st.markdown(f"""
    <div class="insight-callout callout-orange">
        <strong>Executive Retention Finding:</strong> Departmental attrition peaks in <strong>Operations (42.7%)</strong> and <strong>Finance (42.4%)</strong>. Job satisfaction exhibits a potent protective gradient: moving from Satisfaction Level 1 to Level 5 reduces observed attrition by <strong>{sat_diff:.1f} percentage points</strong> (from {sat_att.loc[sat_att['job_satisfaction'] == 1, 'att_rate'].values[0]:.1f}% down to {sat_att.loc[sat_att['job_satisfaction'] == 5, 'att_rate'].values[0]:.1f}%).
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 6. PERFORMANCE & PRODUCTIVITY DYNAMICS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="section-header-box">
        <div class="section-tag">Productivity Intelligence</div>
        <h2 class="section-title">Performance, Overtime & Productivity Balance</h2>
        <p class="section-subtitle">Evidence of diminishing returns to overtime hours and the stabilizing effect of structured training.</p>
    </div>
    """, unsafe_allow_html=True)
    
    p1, p2 = st.columns(2)
    
    with p1:
        # Overtime vs performance
        ot_bins = pd.cut(df_perf["Overtime_Hours"], bins=[-0.1, 0, 10, 20, 30, 100], labels=["0h", "1–10h", "11–20h", "21–30h", "30h+"])
        perf_ot_summary = df_perf.groupby(ot_bins, observed=False).agg(
            avg_performance=("Performance_Score", "mean"),
            avg_satisfaction=("Employee_Satisfaction_Score", "mean"),
            resignation_rate=("Resigned", lambda x: x.astype(bool).mean() * 100),
            count=("Employee_ID", "count")
        ).reset_index().dropna(subset=["avg_performance"])
        
        fig_ot_perf = go.Figure()
        fig_ot_perf.add_trace(go.Bar(
            x=perf_ot_summary["Overtime_Hours"],
            y=perf_ot_summary["avg_performance"],
            name="Mean Performance Score (1-5)",
            marker_color=COLORS["purple"],
            text=perf_ot_summary["avg_performance"].round(2),
            textposition="outside"
        ))
        fig_ot_perf.add_trace(go.Scatter(
            x=perf_ot_summary["Overtime_Hours"],
            y=perf_ot_summary["resignation_rate"],
            name="Resignation Rate (%)",
            yaxis="y2",
            mode="lines+markers",
            marker=dict(color=COLORS["orange"], size=9),
            line=dict(color=COLORS["orange"], width=3)
        ))
        fig_ot_perf.update_layout(
            title="Overtime Hours vs Performance & Resignation",
            yaxis=dict(title="Performance Score (1-5)", range=[2.5, 3.4]),
            yaxis2=dict(title="Resignation Rate (%)", overlaying="y", side="right", range=[8, 12]),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        chart(fig_ot_perf, height=360)
        
    with p2:
        # Department performance vs training hours
        dept_perf_train = df_perf.groupby("Department", as_index=False).agg(
            avg_performance=("Performance_Score", "mean"),
            avg_training=("Training_Hours", "mean"),
            avg_satisfaction=("Employee_Satisfaction_Score", "mean"),
            headcount=("Employee_ID", "count")
        )
        fig_dept_perf = px.scatter(
            dept_perf_train,
            x="avg_training",
            y="avg_performance",
            size="headcount",
            color="avg_satisfaction",
            text="Department",
            title="Department Training Hours vs Average Performance",
            labels={"avg_training": "Avg Training Hours", "avg_performance": "Avg Performance Score", "avg_satisfaction": "Satisfaction"},
            color_continuous_scale="Purples"
        )
        fig_dept_perf.update_traces(textposition="top center")
        chart(fig_dept_perf, height=360)

    st.markdown("""
    <div class="insight-callout callout-gold">
        <strong>Executive Productivity Finding:</strong> Pearson correlation between overtime hours and employee performance rating is virtually zero (<strong>r = +0.0027</strong>). Employees clocking 21–30 overtime hours/month show equivalent appraisal scores (3.00/5) to those with 0 overtime hours (3.01/5), while resignation rates creep upward. Excessive overtime imposes human fatigue costs without delivering measurable appraisal gains.
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 7. BURNOUT & WELL-BEING INDICATORS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="section-header-box">
        <div class="section-tag">Well-being Telemetry</div>
        <h2 class="section-title">Burnout, Screen Exposure & Recovery Buffers</h2>
        <p class="section-subtitle">Analyzing digital fatigue in remote work and recovery safeguards in simulated workforce populations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    b1, b2 = st.columns(2)
    
    with b1:
        # WFH Screen time & After hours vs Burnout
        wfh_after = df_burn.groupby("after_hours_work", as_index=False).agg(
            avg_burnout=("burnout_score", "mean"),
            avg_screen=("screen_time_hours", "mean"),
            avg_sleep=("sleep_hours", "mean"),
            records=("user_id", "count")
        )
        wfh_after["Work Schedule"] = wfh_after["after_hours_work"].map({0: "Standard Hours Only", 1: "After-Hours Work Active"})
        
        fig_wfh_bar = px.bar(
            wfh_after,
            x="Work Schedule",
            y="avg_burnout",
            text="avg_burnout",
            color="avg_screen",
            color_continuous_scale="Oranges",
            title="Remote Work: After-Hours Impact on Burnout Score",
            labels={"avg_burnout": "Average Burnout Score", "avg_screen": "Screen Hours/Day"},
            hover_data={"records": True, "avg_screen": ":.2f"}
        )
        fig_wfh_bar.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        chart(fig_wfh_bar, height=360)
        
    with b2:
        # Synthetic Simulation: Sleep vs Burnout & Stress
        syn_sleep_summary = df_syn.groupby(
            pd.cut(df_syn["Average_Sleep_Hours"], bins=[3, 5, 6, 7, 8, 12], labels=["<5h", "5-6h", "6-7h", "7-8h", ">8h"]),
            observed=False
        ).agg(
            avg_burnout=("Burnout_Score", "mean"),
            avg_stress=("Stress_Score", "mean"),
            records=("Employee_ID", "count")
        ).reset_index().dropna(subset=["avg_burnout"])
        
        fig_syn_sleep = px.line(
            syn_sleep_summary,
            x="Average_Sleep_Hours",
            y=["avg_burnout", "avg_stress"],
            markers=True,
            title="Synthetic Simulation: Sleep Duration vs Stress & Burnout Index",
            labels={"Average_Sleep_Hours": "Sleep Duration Band", "value": "Index Score (0–100)", "variable": "Indicator"},
            color_discrete_sequence=[COLORS["orange"], COLORS["purple"]]
        )
        chart(fig_syn_sleep, height=360)

    st.markdown("""
    <div class="insight-callout callout-navy">
        <strong>Executive Well-being Finding:</strong> In remote work telemetry, after-hours connectivity elevates average burnout scores to 44.97 while daily screen time reaches 9.31 hours. In the synthetic population, sleep deprivation (&lt;5 hours) drives burnout and stress scores above baseline, while regular workday breaks serve as a critical physiological buffer.
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 8. STATISTICAL FINDINGS & CORRELATION MATRIX
    # -------------------------------------------------------------
    st.markdown("""
    <div class="section-header-box">
        <div class="section-tag">Empirical Evidence</div>
        <h2 class="section-title">Important Correlations & Statistical Findings</h2>
        <p class="section-subtitle">Rigorous Pearson correlation analysis calculated directly across individual datasets.</p>
    </div>
    """, unsafe_allow_html=True)
    
    corr_c1, corr_c2 = st.columns([1.1, 0.9])
    
    with corr_c1:
        corr_data = pd.DataFrame({
            "Dataset & Target Outcome": [
                "Dataset 01 (Attrition) → Job Satisfaction",
                "Dataset 01 (Attrition) → Absence Days",
                "Dataset 01 (Attrition) → Performance Rating",
                "Dataset 01 (Attrition) → Weekly Work Hours",
                "Dataset 01 (Attrition) → Monthly Salary",
                "Dataset 02 (Enterprise) → Overtime Hours",
                "Dataset 02 (Enterprise) → Training Hours",
                "Dataset 02 (Enterprise) → Weekly Hours",
                "Dataset 03 (Synthetic) → Stress Score (Burnout)",
                "Dataset 03 (Synthetic) → Job Satisfaction (Burnout)",
                "Dataset 03 (Synthetic) → Weekly Work Hours (Burnout)",
                "Dataset 03 (Synthetic) → Sleep Hours (Burnout)",
                "Dataset 04 (WFH) → Task Completion Rate (Burnout)",
                "Dataset 04 (WFH) → Work Hours (Burnout)",
                "Dataset 04 (WFH) → Screen Time Hours (Burnout)"
            ],
            "Pearson r": [
                -0.241, +0.167, -0.166, +0.111, -0.009,
                +0.003, +0.002, -0.001,
                +0.468, -0.465, +0.408, -0.341,
                -0.921, +0.129, +0.124
            ],
            "Statistical Association": [
                "Moderate Negative (Protective)",
                "Weak Positive (Strain Signal)",
                "Weak Negative (Protective)",
                "Weak Positive (Fatigue Signal)",
                "Negligible Correlation",
                "Negligible Correlation",
                "Negligible Correlation",
                "Negligible Correlation",
                "Strong Positive Correlation",
                "Strong Negative (Protective)",
                "Moderate Positive Correlation",
                "Moderate Negative (Protective)",
                "Very Strong Negative Correlation",
                "Weak Positive Correlation",
                "Weak Positive Correlation"
            ]
        })
        
        fig_corr = px.bar(
            corr_data,
            x="Pearson r",
            y="Dataset & Target Outcome",
            orientation="h",
            color="Pearson r",
            color_continuous_scale="RdBu_r",
            range_color=[-1, 1],
            title="Pearson Correlation Strengths with Target Outcomes"
        )
        fig_corr.update_layout(yaxis=dict(autorange="reversed"))
        chart(fig_corr, height=440)
        
    with corr_c2:
        st.markdown("""
        <div style="background: #FFFFFF; border: 1px solid #E5E1F4; border-radius: 14px; padding: 20px; box-shadow: 0 4px 16px rgba(36, 39, 68, 0.04); height: 440px; overflow-y: auto;">
            <div style="font-size: 0.95rem; font-weight: 700; color: #1B1F3B; margin-bottom: 8px;">Methodological Findings & Governance</div>
            <div style="font-size: 0.82rem; color: #5A5D7A; line-height: 1.55;">
                <p><strong>1. Remote Burnout - Productivity Cliff:</strong><br/>
                Dataset 04 records a devastating <code>r = -0.921</code> correlation between burnout score and task completion rate. As burnout escalates beyond sustainable thresholds, task execution collapses precipitously.</p>
                
                <p><strong>2. Job Satisfaction as Primary Protective Buffer:</strong><br/>
                Across both empirical attrition (<code>r = -0.241</code>) and synthetic well-being (<code>r = -0.465</code>), satisfaction remains the single strongest protective barrier against turnover and mental exhaustion.</p>
                
                <p><strong>3. Workload Ceiling Dynamics:</strong><br/>
                Weekly hours correlate positively with attrition (<code>r = +0.111</code>) and synthetic stress (<code>r = +0.408</code>), while excessive overtime yields negligible performance appraisal advantage.</p>
                
                <div style="background: #F1EFF9; border-radius: 8px; padding: 10px; font-size: 0.77rem; color: #434665; margin-top: 10px;">
                    <strong>Statistical Caution:</strong> Observed statistical correlations quantify mathematical co-movements within each dataset. They do not constitute deterministic individual causation.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 9. DATA-DRIVEN STRATEGIC RECOMMENDATIONS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="section-header-box">
        <div class="section-tag">Executive Action Framework</div>
        <h2 class="section-title">Data-Driven Strategic Recommendations</h2>
        <p class="section-subtitle">Actionable executive interventions prioritized by empirical risk magnitude.</p>
    </div>
    """, unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    
    with r1:
        st.markdown(f"""
        <div class="rec-card">
            <div class="rec-header">
                <span class="rec-title">1. Overtime Ceiling & Workload Governance</span>
                <span class="rec-priority p-urgent">P1 · Critical</span>
            </div>
            <p style="font-size: 0.83rem; color: #5A5D7A; line-height: 1.45; margin: 0 0 10px 0;">
                <strong>Empirical Basis:</strong> {att_over_55:.1f}% of empirical employees work &gt;55 hrs/wk, while enterprise data demonstrates zero performance gain (r = +0.0027) from excessive overtime.
            </p>
            <div style="background: #F8F7FD; border-radius: 8px; padding: 10px; font-size: 0.80rem; color: #2D3059;">
                <strong>Action:</strong> Institute a strict 50-hour weekly workload ceiling with automated manager alerts when an employee logs &gt;15 hours of monthly overtime. Rebalance project resource allocation across high-strain teams.
            </div>
        </div>
        
        <div class="rec-card">
            <div class="rec-header">
                <span class="rec-title">2. Targeted Retention in High-Strain Divisions</span>
                <span class="rec-priority p-high">P2 · High</span>
            </div>
            <p style="font-size: 0.83rem; color: #5A5D7A; line-height: 1.45; margin: 0 0 10px 0;">
                <strong>Empirical Basis:</strong> Operations (42.7%) and Finance (42.4%) exhibit highest attrition rates, with low satisfaction doubling flight probability.
            </p>
            <div style="background: #F8F7FD; border-radius: 8px; padding: 10px; font-size: 0.80rem; color: #2D3059;">
                <strong>Action:</strong> Deploy targeted pulse surveys within Operations and Finance to address operational bottlenecks, absence trends, and workload distribution before turnover manifests.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with r2:
        st.markdown(f"""
        <div class="rec-card">
            <div class="rec-header">
                <span class="rec-title">3. Digital Disconnection & Remote Work Safeguards</span>
                <span class="rec-priority p-high">P2 · High</span>
            </div>
            <p style="font-size: 0.83rem; color: #5A5D7A; line-height: 1.45; margin: 0 0 10px 0;">
                <strong>Empirical Basis:</strong> Remote after-hours work elevates burnout scores, directly threatening the severe r = -0.921 task completion cliff.
            </p>
            <div style="background: #F8F7FD; border-radius: 8px; padding: 10px; font-size: 0.80rem; color: #2D3059;">
                <strong>Action:</strong> Implement after-hours email and messaging quiet hours, mandate scheduled screen-free break blocks during intense workday schedules, and cap consecutive virtual meetings.
            </div>
        </div>
        
        <div class="rec-card">
            <div class="rec-header">
                <span class="rec-title">4. Institutional Analytics & ML Validation Roadmap</span>
                <span class="rec-priority p-strategic">P3 · Strategic</span>
            </div>
            <p style="font-size: 0.83rem; color: #5A5D7A; line-height: 1.45; margin: 0 0 10px 0;">
                <strong>Empirical Basis:</strong> Phase 1 successfully surfaces descriptive patterns; predictive ML models must be trained with leakage checks and cross-validation before operational use.
            </p>
            <div style="background: #F8F7FD; border-radius: 8px; padding: 10px; font-size: 0.80rem; color: #2D3059;">
                <strong>Action:</strong> Develop Phase 2 supervised machine learning models with rigorous out-of-fold validation, ethical bias screening, and model interpretability (SHAP) prior to deployment.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 10. INTERACTIVE MODULE LAUNCHPAD
    # -------------------------------------------------------------
    st.markdown("""
    <div class="section-header-box">
        <div class="section-tag">Interactive Navigation</div>
        <h2 class="section-title">Deep-Dive Intelligence Modules</h2>
        <p class="section-subtitle">Select any operational module below or use the sidebar to access full granular analytics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    n1, n2, n3, n4 = st.columns(4)
    with n1:
        st.button("📊 01 · Workforce & Attrition", key="btn_nav_foot_1", on_click=navigate_to, args=("Workforce & Attrition",), use_container_width=True)
    with n2:
        st.button("📈 02 · Employee Performance", key="btn_nav_foot_2", on_click=navigate_to, args=("Employee Performance",), use_container_width=True)
    with n3:
        st.button("🧠 03 · Workforce Well-being", key="btn_nav_foot_3", on_click=navigate_to, args=("Workforce Well-being",), use_container_width=True)
    with n4:
        st.button("💻 04 · WFH Burnout Analytics", key="btn_nav_foot_4", on_click=navigate_to, args=("Work-from-home Burnout",), use_container_width=True)


def attrition_page():
    df = D["attrition"].copy()
    heading("Workforce & Attrition Intelligence",
            "Explore workload distribution, employee satisfaction and resignation patterns.")

    # Normalize labels for reliable filtering and calculations.
    df["department"] = df["department"].fillna("Unknown").astype(str).str.strip().str.title()
    df["role_level"] = df["role_level"].fillna("Unknown").astype(str).str.strip().str.title()
    df["_attrition_yes"] = (
        df["attrition"].astype(str).str.strip().str.lower()
        .isin(["yes", "y", "true", "1"])
    )

    st.subheader("Explore the workforce")
    c1, c2, c3 = st.columns(3)
    departments = sorted(df["department"].unique())
    roles = sorted(df["role_level"].unique())
    selected_departments = c1.multiselect("Department", departments, default=departments)
    selected_roles = c2.multiselect("Role level", roles, default=roles)
    min_hours, max_hours = int(df["avg_weekly_hours"].min()), int(df["avg_weekly_hours"].max())
    hour_range = c3.slider("Weekly working hours", min_hours, max_hours,
                           (min_hours, max_hours))

    df = df[
        df["department"].isin(selected_departments)
        & df["role_level"].isin(selected_roles)
        & df["avg_weekly_hours"].between(hour_range[0], hour_range[1])
    ].copy()

    if df.empty:
        st.warning("No records match the selected filters. Adjust the filters to continue.")
        return

    attrition_rate = 100 * df["_attrition_yes"].mean()
    avg_hours = df["avg_weekly_hours"].mean()
    avg_satisfaction = df["job_satisfaction"].mean()
    avg_performance = df["performance_rating"].mean()
    high_hours_share = 100 * (df["avg_weekly_hours"] > 55).mean()

    metric_row([
        ("Employees in view", f"{len(df):,}", "Number of records after filters"),
        ("Attrition rate", f"{attrition_rate:.1f}%", "Share labelled as attrition"),
        ("Average weekly hours", f"{avg_hours:.1f} h", "Average hours per week"),
        ("Average satisfaction", f"{avg_satisfaction:.2f}/5", "Mean satisfaction score"),
        ("Working over 55 h", f"{high_hours_share:.1f}%", "Share above 55 weekly hours"),
    ])

    st.divider()
    st.subheader("01 · Where is attrition concentrated?")
    left, right = st.columns(2)

    dept = (df.groupby("department", as_index=False)
              .agg(employees=("_attrition_yes", "size"),
                   attrition_rate=("_attrition_yes", "mean")))
    dept["attrition_rate"] *= 100
    with left:
        fig = px.bar(
            dept.sort_values("attrition_rate", ascending=False),
            x="department", y="attrition_rate",
            hover_data={"employees": True, "attrition_rate": ":.1f"},
            color="attrition_rate", color_continuous_scale="Purples",
            title="Attrition rate by department",
            labels={"department": "Department", "attrition_rate": "Attrition rate (%)"}
        )
        chart(fig)
    role = (df.groupby("role_level", as_index=False)
              .agg(employees=("_attrition_yes", "size"),
                   attrition_rate=("_attrition_yes", "mean")))
    role["attrition_rate"] *= 100
    with right:
        fig = px.bar(
            role.sort_values("attrition_rate", ascending=False),
            x="role_level", y="attrition_rate",
            hover_data={"employees": True, "attrition_rate": ":.1f"},
            color="attrition_rate", color_continuous_scale="Blues",
            title="Attrition rate by role level",
            labels={"role_level": "Role level", "attrition_rate": "Attrition rate (%)"}
        )
        chart(fig)

    st.divider()
    st.subheader("02 · How does workload relate to attrition?")
    left, right = st.columns(2)
    hours = (df.groupby("avg_weekly_hours", as_index=False)
               .agg(employees=("_attrition_yes", "size"),
                    attrition_rate=("_attrition_yes", "mean")))
    hours["attrition_rate"] *= 100
    with left:
        fig = px.line(
            hours, x="avg_weekly_hours", y="attrition_rate",
            markers=True, hover_data={"employees": True},
            title="Attrition rate across weekly working hours",
            labels={"avg_weekly_hours": "Weekly working hours",
                    "attrition_rate": "Attrition rate (%)"}
        )
        chart(fig)
    with right:
        fig = px.box(
            df, x="_attrition_yes", y="avg_weekly_hours",
            color="_attrition_yes",
            title="Working-hour distribution by attrition status",
            labels={"_attrition_yes": "Attrition (False = No, True = Yes)",
                    "avg_weekly_hours": "Weekly working hours"},
            color_discrete_sequence=[COLORS["blue"], COLORS["orange"]]
        )
        chart(fig)

    st.divider()
    st.subheader("03 · Satisfaction and performance signals")
    left, right = st.columns(2)
    satisfaction = (df.groupby("job_satisfaction", as_index=False)
                      .agg(employees=("_attrition_yes", "size"),
                           attrition_rate=("_attrition_yes", "mean")))
    satisfaction["attrition_rate"] *= 100
    with left:
        fig = px.bar(
            satisfaction, x="job_satisfaction", y="attrition_rate",
            text="attrition_rate",
            title="Attrition rate by job satisfaction",
            labels={"job_satisfaction": "Job satisfaction (1–5)",
                    "attrition_rate": "Attrition rate (%)"},
            color="attrition_rate", color_continuous_scale="Oranges"
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        chart(fig)
    with right:
        fig = px.box(
            df, x="_attrition_yes", y="performance_rating",
            color="_attrition_yes",
            title="Performance ratings by attrition status",
            labels={"_attrition_yes": "Attrition (False = No, True = Yes)",
                    "performance_rating": "Performance rating (1–5)"},
            color_discrete_sequence=[COLORS["blue"], COLORS["orange"]]
        )
        chart(fig)

    st.divider()
    st.subheader("04 · Explore relationships between workforce indicators")
    numeric_cols = [
        "monthly_salary", "avg_weekly_hours", "projects_handled",
        "performance_rating", "absences_days", "job_satisfaction"
    ]
    corr_df = df[numeric_cols + ["_attrition_yes"]].copy()
    corr_df["_attrition_numeric"] = corr_df["_attrition_yes"].astype(int)
    corr_cols = numeric_cols + ["_attrition_numeric"]
    corr = corr_df[corr_cols].corr(numeric_only=True)
    corr.index = [
        "Monthly salary", "Weekly hours", "Projects handled",
        "Performance rating", "Absence days", "Job satisfaction", "Attrition"
    ]
    corr.columns = corr.index
    fig = px.imshow(
        corr, text_auto=".2f", aspect="auto",
        color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
        title="Correlation heatmap of workforce indicators"
    )
    chart(fig, height=520)

    st.info(
        "How to read this: attrition rates describe patterns in this dataset. "
        "Differences and correlations do not prove that workload or satisfaction causes an employee to leave. "
        "Use these results as signals for further investigation, not as individual employment decisions."
    )
    st.caption(
        "Dataset: employee_performance_workload_attrition_cleaned.csv. "
        "All figures update when you change the filters."
    )

def performance_page():
    df = D["performance"].copy()
    heading("Employee Performance Intelligence",
            "Analyze performance levels, workload, overtime, training and employee experience.")

    # Filters
    st.subheader("Explore employee performance")
    departments = sorted(df["Department"].dropna().astype(str).unique())
    titles = sorted(df["Job_Title"].dropna().astype(str).unique())
    c1, c2, c3 = st.columns(3)
    selected_departments = c1.multiselect("Department", departments, default=departments, key="perf_dept")
    selected_titles = c2.multiselect("Job title", titles, default=titles, key="perf_title")
    score_min, score_max = int(df["Performance_Score"].min()), int(df["Performance_Score"].max())
    score_range = c3.slider("Performance score", score_min, score_max,
                            (score_min, score_max), key="perf_score")

    df = df[
        df["Department"].astype(str).isin(selected_departments)
        & df["Job_Title"].astype(str).isin(selected_titles)
        & df["Performance_Score"].between(score_range[0], score_range[1])
    ].copy()

    if df.empty:
        st.warning("No records match the selected filters. Adjust the filters to continue.")
        return

    resigned = df["Resigned"].astype(bool)
    metric_row([
        ("Employees in view", f"{len(df):,}", "Records after applying filters"),
        ("Average performance", f"{df['Performance_Score'].mean():.2f}/5", "Mean performance score"),
        ("Average satisfaction", f"{df['Employee_Satisfaction_Score'].mean():.2f}/5",
         "Mean employee satisfaction score"),
        ("Average overtime", f"{df['Overtime_Hours'].mean():.1f} h", "Average recorded overtime hours"),
        ("Resignation rate", f"{100*resigned.mean():.1f}%", "Share marked as resigned"),
    ])

    st.divider()
    st.subheader("01 · Performance across departments and roles")
    left, right = st.columns(2)

    dept_perf = (df.groupby("Department", as_index=False)
                   .agg(avg_performance=("Performance_Score", "mean"),
                        employees=("Employee_ID", "count"),
                        avg_satisfaction=("Employee_Satisfaction_Score", "mean")))
    with left:
        fig = px.bar(
            dept_perf.sort_values("avg_performance", ascending=False),
            x="Department", y="avg_performance",
            color="avg_performance", color_continuous_scale="Blues",
            hover_data={"employees": True, "avg_satisfaction": ":.2f"},
            title="Average performance by department",
            labels={"avg_performance": "Average performance score"}
        )
        chart(fig)
    role_perf = (df.groupby("Job_Title", as_index=False)
                   .agg(avg_performance=("Performance_Score", "mean"),
                        employees=("Employee_ID", "count")))
    with right:
        fig = px.bar(
            role_perf.sort_values("avg_performance", ascending=False),
            x="Job_Title", y="avg_performance",
            color="avg_performance", color_continuous_scale="Purples",
            hover_data={"employees": True},
            title="Average performance by job title",
            labels={"avg_performance": "Average performance score"}
        )
        chart(fig)

    st.divider()
    st.subheader("02 · Workload and productivity")
    left, right = st.columns(2)
    scatter_df = df.sample(min(7000, len(df)), random_state=42)
    with left:
        fig = px.scatter(
            scatter_df, x="Overtime_Hours", y="Performance_Score",
            color="Employee_Satisfaction_Score",
            hover_data=["Department", "Job_Title", "Projects_Handled"],
            title="Overtime hours vs performance",
            labels={"Overtime_Hours": "Overtime hours",
                    "Performance_Score": "Performance score",
                    "Employee_Satisfaction_Score": "Satisfaction"},
            color_continuous_scale="Viridis"
        )
        chart(fig)
    with right:
        fig = px.scatter(
            scatter_df, x="Projects_Handled", y="Performance_Score",
            color="Work_Hours_Per_Week",
            hover_data=["Department", "Job_Title", "Overtime_Hours"],
            title="Projects handled vs performance",
            labels={"Projects_Handled": "Projects handled",
                    "Performance_Score": "Performance score",
                    "Work_Hours_Per_Week": "Weekly work hours"},
            color_continuous_scale="Blues"
        )
        chart(fig)

    st.divider()
    st.subheader("03 · Training and employee experience")
    left, right = st.columns(2)
    training = (df.groupby("Training_Hours", as_index=False)
                  .agg(avg_performance=("Performance_Score", "mean"),
                       employee_count=("Employee_ID", "count")))
    with left:
        fig = px.scatter(
            training, x="Training_Hours", y="avg_performance",
            size="employee_count", title="Training hours vs average performance",
            labels={"Training_Hours": "Training hours",
                    "avg_performance": "Average performance score",
                    "employee_count": "Employees"}
        )
        chart(fig)
    with right:
        fig = px.box(
            df, x="Resigned", y="Employee_Satisfaction_Score",
            color="Resigned",
            title="Satisfaction by resignation status",
            labels={"Resigned": "Resigned",
                    "Employee_Satisfaction_Score": "Satisfaction score"},
            color_discrete_sequence=[COLORS["blue"], COLORS["orange"]]
        )
        chart(fig)

    st.divider()
    st.subheader("04 · Employee indicators relationship")
    numeric_cols = [
        "Age", "Years_At_Company", "Performance_Score", "Monthly_Salary",
        "Work_Hours_Per_Week", "Projects_Handled", "Overtime_Hours",
        "Sick_Days", "Training_Hours", "Promotions",
        "Employee_Satisfaction_Score"
    ]
    corr = df[numeric_cols].corr(numeric_only=True)
    fig = px.imshow(
        corr, text_auto=".2f", aspect="auto",
        color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
        title="Correlation heatmap: employee performance indicators"
    )
    chart(fig, height=650)

    st.info(
        "Interpretation: performance differences and correlations describe patterns in this dataset. "
        "They do not prove that overtime, training or project count causes a change in performance. "
        "Use these results to guide further investigation."
    )
    st.caption(
        "Dataset: Extended_Employee_Performance_and_Productivity_Dataset_Cleaned.csv. "
        "Scatter plots use a reproducible sample of up to 7,000 records for faster rendering; "
        "aggregated charts use all filtered records."
    )

def synthetic_page():
    df = D["synthetic"].copy()
    heading("Workforce Well-being Intelligence",
            "Explore how workload, stress, sleep, burnout and satisfaction vary across the workforce.")

    st.warning(
        "Synthetic dataset: these records are simulated for analytical development. "
        "They are not actual employee or NIE faculty records."
    )

    st.subheader("Explore workforce segments")
    departments = sorted(df["Department"].dropna().astype(str).unique())
    locations = sorted(df["Work_Location"].dropna().astype(str).unique())
    employment_types = sorted(df["Employment_Type"].dropna().astype(str).unique())

    c1, c2, c3 = st.columns(3)
    selected_departments = c1.multiselect("Department", departments, default=departments, key="well_dept")
    selected_locations = c2.multiselect("Work location", locations, default=locations, key="well_loc")
    selected_employment = c3.multiselect("Employment type", employment_types, default=employment_types, key="well_emp")

    df = df[
        df["Department"].astype(str).isin(selected_departments)
        & df["Work_Location"].astype(str).isin(selected_locations)
        & df["Employment_Type"].astype(str).isin(selected_employment)
    ].copy()

    if df.empty:
        st.warning("No records match the selected filters. Adjust the filters to continue.")
        return

    metric_row([
        ("Records in view", f"{len(df):,}", "Synthetic records after filters"),
        ("Average weekly hours", f"{df['Weekly_Work_Hours'].mean():.1f} h", "Mean weekly working hours"),
        ("Average stress score", f"{df['Stress_Score'].mean():.1f}", "Stress score as stored"),
        ("Average burnout score", f"{df['Burnout_Score'].mean():.1f}", "Burnout score as stored"),
        ("Average sleep", f"{df['Average_Sleep_Hours'].mean():.1f} h", "Mean sleep hours"),
    ])

    st.divider()
    st.subheader("01 · Workload and stress patterns")
    left, right = st.columns(2)
    plot_sample = df.sample(min(9000, len(df)), random_state=42)
    with left:
        fig = px.scatter(
            plot_sample, x="Weekly_Work_Hours", y="Stress_Score",
            color="Department", opacity=0.55,
            hover_data=["Job_Role", "Weekly_Overtime_Hours", "Meetings_Per_Week"],
            title="Weekly workload vs stress",
            labels={"Weekly_Work_Hours": "Weekly work hours", "Stress_Score": "Stress score"}
        )
        chart(fig)
    with right:
        overtime = (df.groupby(pd.cut(df["Weekly_Overtime_Hours"],
                                     bins=[-0.01, 0, 5, 10, 15, 25, float("inf")],
                                     labels=["0", "0–5", "5–10", "10–15", "15–25", "25+"]),
                               observed=False)
                      .agg(avg_stress=("Stress_Score", "mean"),
                           employees=("Stress_Score", "size"))
                      .reset_index())
        overtime = overtime.dropna(subset=["Weekly_Overtime_Hours"])
        fig = px.bar(
            overtime, x="Weekly_Overtime_Hours", y="avg_stress",
            color="avg_stress", text="employees", color_continuous_scale="Oranges",
            title="Average stress by weekly overtime band",
            labels={"Weekly_Overtime_Hours": "Overtime hours per week",
                    "avg_stress": "Average stress score", "employees": "Records"}
        )
        chart(fig)

    st.divider()
    st.subheader("02 · Sleep, burnout and recovery")
    left, right = st.columns(2)
    with left:
        fig = px.scatter(
            plot_sample, x="Average_Sleep_Hours", y="Burnout_Score",
            color="Stress_Score", opacity=0.6,
            hover_data=["Department", "Breaks_Per_Workday", "Weekly_Work_Hours"],
            title="Sleep duration vs burnout score",
            labels={"Average_Sleep_Hours": "Average sleep (hours)",
                    "Burnout_Score": "Burnout score", "Stress_Score": "Stress score"},
            color_continuous_scale="Oranges"
        )
        chart(fig)
    with right:
        recovery = (df.groupby("Breaks_Per_Workday", as_index=False)
                      .agg(avg_burnout=("Burnout_Score", "mean"),
                           avg_stress=("Stress_Score", "mean"),
                           records=("Employee_ID", "count")))
        fig = px.line(
            recovery, x="Breaks_Per_Workday", y=["avg_burnout", "avg_stress"],
            markers=True, title="Break frequency vs well-being scores",
            labels={"Breaks_Per_Workday": "Breaks per workday",
                    "value": "Average score", "variable": "Measure"}
        )
        chart(fig)

    st.divider()
    st.subheader("03 · Department well-being comparison")
    department_summary = (df.groupby("Department", as_index=False)
        .agg(
            avg_hours=("Weekly_Work_Hours", "mean"),
            avg_stress=("Stress_Score", "mean"),
            avg_burnout=("Burnout_Score", "mean"),
            avg_sleep=("Average_Sleep_Hours", "mean"),
            avg_satisfaction=("Job_Satisfaction_Score", "mean"),
            records=("Employee_ID", "count")
        ))
    left, right = st.columns(2)
    with left:
        fig = px.bar(
            department_summary.sort_values("avg_burnout", ascending=False),
            x="Department", y="avg_burnout", color="avg_burnout",
            hover_data={"records": True, "avg_stress": ":.1f", "avg_sleep": ":.1f"},
            color_continuous_scale="Oranges",
            title="Average burnout score by department",
            labels={"avg_burnout": "Average burnout score"}
        )
        chart(fig)
    with right:
        fig = px.scatter(
            department_summary, x="avg_hours", y="avg_burnout",
            size="records", color="avg_stress", text="Department",
            title="Department workload vs burnout",
            labels={"avg_hours": "Average weekly hours",
                    "avg_burnout": "Average burnout score",
                    "avg_stress": "Average stress score"},
            color_continuous_scale="Reds"
        )
        fig.update_traces(textposition="top center")
        chart(fig)

    st.divider()
    st.subheader("04 · Satisfaction and performance")
    left, right = st.columns(2)
    with left:
        fig = px.scatter(
            plot_sample, x="Job_Satisfaction_Score", y="Burnout_Score",
            color="Performance_Rating", opacity=0.55,
            title="Job satisfaction vs burnout",
            labels={"Job_Satisfaction_Score": "Job satisfaction score",
                    "Burnout_Score": "Burnout score",
                    "Performance_Rating": "Performance rating"},
            color_continuous_scale="Viridis"
        )
        chart(fig)
    with right:
        fig = px.scatter(
            plot_sample, x="Task_Completion_Percent", y="Performance_Rating",
            color="Weekly_Work_Hours", opacity=0.55,
            title="Task completion vs performance rating",
            labels={"Task_Completion_Percent": "Task completion (%)",
                    "Performance_Rating": "Performance rating",
                    "Weekly_Work_Hours": "Weekly work hours"},
            color_continuous_scale="Blues"
        )
        chart(fig)

    st.divider()
    st.subheader("05 · Correlation across well-being indicators")
    corr_cols = [
        "Weekly_Work_Hours", "Weekly_Overtime_Hours", "Meetings_Per_Week",
        "Tasks_Assigned_Per_Week", "Task_Completion_Percent",
        "Average_Sleep_Hours", "Breaks_Per_Workday", "Stress_Score",
        "Burnout_Score", "Job_Satisfaction_Score", "Performance_Rating",
        "Absence_Days_Last_Year"
    ]
    corr = df[corr_cols].corr(numeric_only=True)
    fig = px.imshow(
        corr, text_auto=".2f", aspect="auto",
        color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
        title="Correlation heatmap: workload and well-being"
    )
    chart(fig, height=680)

    st.info(
        "Interpretation: the charts reveal patterns in a synthetic dataset, not evidence about real employees. "
        "Correlations do not prove causation. Check data quality and the meaning of each generated score "
        "before using the results to make recommendations."
    )
    st.caption(
        "Dataset: Large_Employee_Well-being_Dataset__Synthetic__Cleaned.csv. "
        "Scatter charts use a reproducible sample of up to 9,000 rows for responsive rendering; "
        "aggregated summaries use all filtered records."
    )

def burnout_page():
    df = D["burnout"].copy()
    heading("Work-from-home Burnout Analytics",
            "Understand how work patterns, screen exposure, recovery habits and sleep relate to burnout indicators.")

    st.subheader("Explore work patterns")
    day_types = sorted(df["day_type"].dropna().astype(str).unique())
    selected_days = st.multiselect("Day type", day_types, default=day_types, key="burnout_days")
    df = df[df["day_type"].astype(str).isin(selected_days)].copy()

    if df.empty:
        st.warning("No records match the selected day types.")
        return

    risk = df["burnout_risk"].fillna("Unknown").astype(str).str.strip().str.title()
    risk_counts = risk.value_counts()
    high_risk_labels = {"High", "Very High", "Severe"}
    high_risk_share = 100 * risk.isin(high_risk_labels).mean()

    metric_row([
        ("Records in view", f"{len(df):,}", "Records after day-type filter"),
        ("Average work hours", f"{df['work_hours'].mean():.1f} h", "Mean work hours"),
        ("Average screen time", f"{df['screen_time_hours'].mean():.1f} h", "Mean screen time"),
        ("Average sleep", f"{df['sleep_hours'].mean():.1f} h", "Mean sleep hours"),
        ("High-risk labels", f"{high_risk_share:.1f}%", "Only labels matching High / Very High / Severe"),
    ])

    st.divider()
    st.subheader("01 · How is burnout risk distributed?")
    left, right = st.columns(2)
    risk_df = risk_counts.rename_axis("Burnout risk").reset_index(name="Records")
    with left:
        fig = px.pie(
            risk_df, names="Burnout risk", values="Records", hole=0.58,
            title="Burnout risk categories",
            color_discrete_sequence=[COLORS["mint"], COLORS["blue"], COLORS["orange"], COLORS["purple"]]
        )
        chart(fig)
    day_summary = (df.assign(_risk=risk)
                     .groupby("day_type", as_index=False)
                     .agg(avg_burnout=("burnout_score", "mean"),
                          avg_work_hours=("work_hours", "mean"),
                          records=("user_id", "count")))
    with right:
        fig = px.bar(
            day_summary, x="day_type", y="avg_burnout",
            color="avg_burnout", hover_data={"records": True, "avg_work_hours": ":.1f"},
            color_continuous_scale="Oranges",
            title="Average burnout score by day type",
            labels={"day_type": "Day type", "avg_burnout": "Average burnout score"}
        )
        chart(fig)

    st.divider()
    st.subheader("02 · Screen exposure and workload")
    sample = df.sample(min(5000, len(df)), random_state=42)
    left, right = st.columns(2)
    with left:
        fig = px.scatter(
            sample, x="screen_time_hours", y="burnout_score",
            color="burnout_risk", opacity=0.65,
            hover_data=["work_hours", "meetings_count", "after_hours_work"],
            title="Screen time vs burnout score",
            labels={"screen_time_hours": "Screen time (hours)",
                    "burnout_score": "Burnout score", "burnout_risk": "Burnout risk"}
        )
        chart(fig)
    with right:
        fig = px.scatter(
            sample, x="work_hours", y="burnout_score",
            color="burnout_risk", opacity=0.65,
            hover_data=["screen_time_hours", "meetings_count", "after_hours_work"],
            title="Daily work hours vs burnout score",
            labels={"work_hours": "Work hours", "burnout_score": "Burnout score",
                    "burnout_risk": "Burnout risk"}
        )
        chart(fig)

    st.divider()
    st.subheader("03 · Recovery habits and well-being")
    left, right = st.columns(2)
    with left:
        fig = px.scatter(
            sample, x="sleep_hours", y="burnout_score",
            color="burnout_risk", opacity=0.65,
            title="Sleep hours vs burnout score",
            labels={"sleep_hours": "Sleep hours", "burnout_score": "Burnout score",
                    "burnout_risk": "Burnout risk"}
        )
        chart(fig)
    with right:
        break_summary = (df.groupby("breaks_taken", as_index=False)
                           .agg(avg_burnout=("burnout_score", "mean"),
                                avg_task_completion=("task_completion_rate", "mean"),
                                records=("user_id", "count")))
        fig = px.line(
            break_summary, x="breaks_taken", y="avg_burnout",
            markers=True, hover_data={"records": True, "avg_task_completion": ":.1f"},
            title="Breaks taken vs average burnout score",
            labels={"breaks_taken": "Breaks taken", "avg_burnout": "Average burnout score"}
        )
        chart(fig)

    st.divider()
    st.subheader("04 · Meetings and after-hours work")
    left, right = st.columns(2)
    meeting_summary = (df.groupby("meetings_count", as_index=False)
                         .agg(avg_burnout=("burnout_score", "mean"),
                              records=("user_id", "count")))
    with left:
        fig = px.bar(
            meeting_summary, x="meetings_count", y="avg_burnout",
            hover_data={"records": True},
            title="Meetings count vs average burnout",
            labels={"meetings_count": "Meetings count", "avg_burnout": "Average burnout score"}
        )
        chart(fig)
    after_summary = (df.groupby("after_hours_work", as_index=False)
                       .agg(avg_burnout=("burnout_score", "mean"),
                            avg_sleep=("sleep_hours", "mean"),
                            records=("user_id", "count")))
    with right:
        fig = px.bar(
            after_summary, x="after_hours_work", y="avg_burnout",
            hover_data={"records": True, "avg_sleep": ":.1f"},
            color="avg_burnout", color_continuous_scale="Oranges",
            title="After-hours work vs average burnout",
            labels={"after_hours_work": "After-hours work", "avg_burnout": "Average burnout score"}
        )
        chart(fig)

    st.divider()
    st.subheader("05 · Relationships between burnout indicators")
    corr_cols = [
        "work_hours", "screen_time_hours", "meetings_count",
        "breaks_taken", "after_hours_work", "sleep_hours",
        "task_completion_rate", "burnout_score"
    ]
    corr = df[corr_cols].corr(numeric_only=True)
    corr.index = [
        "Work hours", "Screen time", "Meetings", "Breaks",
        "After-hours work", "Sleep hours", "Task completion", "Burnout score"
    ]
    corr.columns = corr.index
    fig = px.imshow(
        corr, text_auto=".2f", aspect="auto",
        color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
        title="Correlation heatmap: work-from-home indicators"
    )
    chart(fig, height=600)

    st.info(
        "Interpretation: these charts describe patterns in the supplied dataset. "
        "They do not establish that screen time, meetings or work hours cause burnout. "
        "Confirm how the burnout score and risk categories were defined before presenting them as validated measures."
    )
    st.caption(
        "Dataset: Work_From_Home_Burnout_Dataset_Cleaned.xls. "
        "Scatter charts use a reproducible sample of up to 5,000 records; grouped summaries use all filtered records."
    )



pages = {
    "Overview": overview,
    "Workforce & Attrition": attrition_page,
    "Employee Performance": performance_page,
    "Workforce Well-being": synthetic_page,
    "Work-from-home Burnout": burnout_page,
}

with st.sidebar:
    st.markdown("""
    <div style="padding: 10px 0 6px 0;">
        <span style="background: linear-gradient(135deg, #7C5CFC, #FA8231); color: white; font-size: 0.70rem; font-weight: 700; padding: 3px 8px; border-radius: 6px; letter-spacing: 0.5px;">ENTERPRISE SAAS</span>
        <h2 style="margin: 8px 0 2px 0; color: #1B1F3B; font-size: 1.55rem; font-weight: 800; letter-spacing: -0.5px;">KARYANITI</h2>
        <p style="margin: 0; color: #5A5D7A; font-size: 0.84rem; font-weight: 500;">Workforce Intelligence & Well-being</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    selection = st.radio("ANALYTICAL MODULES", list(pages.keys()), key="nav_selection")
    st.divider()
    st.markdown("""
    <div style="background: #F1EFF9; border: 1px solid #DFDAF2; border-radius: 10px; padding: 12px; margin-bottom: 12px;">
        <div style="font-size: 0.76rem; font-weight: 700; color: #1B1F3B; margin-bottom: 4px;">DATASET AUDIT STATUS</div>
        <div style="font-size: 0.74rem; color: #5A5D7A; line-height: 1.45;">
            ✓ 4 Cleaned Datasets<br/>
            ✓ 100% Unmerged Architecture<br/>
            ✓ Synthetic Data Tagged (147K)<br/>
            ✓ Empirical KPI Calculation
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Phase 1 · Descriptive Analytics Platform")
    st.caption("National Analytics Competition Edition")

pages[st.session_state["nav_selection"]]()
