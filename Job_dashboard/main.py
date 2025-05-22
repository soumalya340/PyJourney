import streamlit as st
from resource_tab1 import resource_tab1
from resources_tab2 import resources_tab2

# Set page configuration and title
st.set_page_config(
    page_title="My Job Tracker",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",   
)

# Main title with custom styling
st.markdown('<h1 class="main-header">My Job Tracker Dashboard 💼</h1>', unsafe_allow_html=True)
# Create tabs for navigation instead of sidebar
tab1, tab2 = st.tabs(["Dashboard", "Job Applications"])

# Section 1: Dashboard
with tab1:
    resource_tab1()
# Section 2: Job Applications
with tab2:
    resources_tab2()