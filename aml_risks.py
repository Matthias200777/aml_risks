import streamlit as st
import random
from datetime import datetime

# Configure page
st.set_page_config(page_title="Client Risk Check", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    .header {
        background-color: #2c3e50;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
    }
    .risk-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #e74c3c;
    }
    .no-risk-card {
        background-color: #e8f5e9;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #2ecc71;
    }
    .search-btn {
        width: 100%;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Risk types
RISK_TYPES = [
    "Suspicious transactions",
    "Misuse of client accounts", 
    "Jurisdiction risk",
    "Unusual source of funds"
]

# App header
st.markdown("""
<div class="header">
    <h1>Client Risk Assessment</h1>
    <p>Mock Compliance Screening Tool</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'search_performed' not in st.session_state:
    st.session_state.search_performed = False

# Search form
with st.form("name_search"):
    st.write("### Client Name Search")
    full_name = st.text_input("Enter full name of applicant", placeholder="e.g. John Smith")
    
    if st.form_submit_button("Search", type="primary", use_container_width=True):
        st.session_state.search_performed = True
        st.session_state.search_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.client_name = full_name
        
        # Randomly determine if we find risks (30% chance of no risks)
        if random.random() < 0.7:  # 70% chance of finding risks
            num_risks = random.randint(1, 3)  # 1-3 risks
            st.session_state.risks_found = random.sample(RISK_TYPES, num_risks)
        else:
            st.session_state.risks_found = []

# Show results if search was performed
if st.session_state.search_performed:
    st.write(f"### Results for: {st.session_state.client_name}")
    st.caption(f"Search performed at: {st.session_state.search_time}")
    
    if st.session_state.risks_found:
        st.warning("Potential risks identified:")
        for risk in st.session_state.risks_found:
            st.markdown(f"""
            <div class="risk-card">
                <strong>⚠️ {risk}</strong>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("No matches found in risk database")
        st.markdown("""
        <div class="no-risk-card">
            <strong>✅ No risks detected</strong>
            <p>This client appears clean based on available records.</p>
        </div>
        """, unsafe_allow_html=True)

# Disclaimer
st.markdown("---")
st.caption("""
**Disclaimer:** This is a mock demonstration tool. All results are randomly generated and not based on actual client data. 
No real compliance screening is being performed.
""")