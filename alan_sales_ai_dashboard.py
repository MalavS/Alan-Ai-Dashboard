import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Alan Sales AI Dashboard", page_icon="📊", layout="wide")

# Dark theme
st.markdown("""
<style>
.main {background-color: #0f172a;}
.stButton > button {border-radius: 12px; height: 50px;}
h1 {color: #60a5fa !important;}
</style>
""", unsafe_allow_html=True)

st.title("📊 Alan Sales AI Dashboard")
st.markdown("**3 AI systems to 4x deals in 12 months** - Live demo")

# Generate sample data
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range("2026-01-01", periods=90, freq="D")
    data = []
    for date in dates:
        data.append({
            "Date": date,
            "Website_Visits": np.random.randint(200, 800),
            "Bear_Views": np.random.randint(50, 200),
            "Marmot_Views": np.random.randint(30, 150),
            "Hot_Leads": np.random.randint(5, 25),
            "Email_Responses": np.random.randint(2, 15),
            "Demo_Booked": np.random.choice([0,1], p=[0.8, 0.2]) * np.random.randint(1, 5)
        })
    return pd.DataFrame(data)

df = load_data()

# Tabs for 3 AI use cases
tab1, tab2, tab3 = st.tabs(["1️⃣ Lead Intelligence", "2️⃣ Smart Marketing", "3️⃣ Sales Coach"])

with tab1:
    st.markdown("### **AI Lead Scoring** - Find hot prospects automatically")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Website Visits", f"{df['Website_Visits'].sum():,}")
    with col2:
        st.metric("Bear Plan Views", f"{df['Bear_Views'].sum():,}", "↑ 23%")
    with col3:
        st.metric("Hot Leads Found", f"{df['Hot_Leads'].sum():,}", "↑ 47%")
    
    st.line_chart(df.set_index('Date')[['Bear_Views', 'Marmot_Views']])
    st.markdown("*AI identifies: '32-employee tech firm viewed Marmot 3x → Call now!'*")

with tab2:
    st.markdown("### **AI Marketing Engine** - 3x response rates")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Emails Sent", "45,000")
        st.metric("Open Rate", "47%", "vs 15% baseline")
    with col2:
        st.metric("Responses", f"{df['Email_Responses'].sum():,}")
        st.metric("Click Rate", "28%")
    
    st.bar_chart(df.set_index('Date')['Email_Responses'])
    st.markdown("*AI crafts: 'Your 35-person team saves 20% on Bear Group'*")

with tab3:
    st.markdown("### **AI Sales Coach** - 25% higher close rates")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Demos Booked", f"{df['Demo_Booked'].sum():,}")
    with col2:
        st.metric("Win Rate", "32%", "↑ 25%")
    with col3:
        st.metric("Avg Deal Size", "$28K")
    
    st.line_chart(df.set_index('Date')['Demo_Booked'])
    st.markdown("""
    **Live coaching examples:**
    • "Price objection → Offer Bear discount"
    • "Next action: Send Marmot brochure (72% conversion)"
    """)

# Bottom summary
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Pipeline Growth", "3.2x", label_visibility="collapsed")
with col2:
    st.metric("Deal Velocity", "41 days", "↓ 19 days")
with col3:
    st.metric("Close Rate", "32%", "↑ 25%")
with col4:
    st.metric("Revenue Impact", "$2.4M", label_visibility="collapsed")

st.markdown("**💡 Built to show exactly how AI 4x's Alan sales - Q1 Assignment**")
