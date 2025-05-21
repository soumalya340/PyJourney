import streamlit as st
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
tab1, tab2, tab3 = st.tabs(["Dashboard", "Job Applications", "Resources"])

# Section 1: Dashboard
with tab1:
    st.header("Dashboard")
    st.subheader("Overview of your job search")
    
    # Placeholder for future dashboard content
    st.info("This section will show statistics and visualizations of your job search progress.")
    
    # Empty containers for future metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Applications", value="0")
    with col2:
        st.metric(label="Interviews", value="0")
    with col3:
        st.metric(label="Response Rate", value="0%")

# Section 2: Job Applications
with tab2:
    resources_tab2()

# Section 3: Resources
with tab3:
    st.header("Resources")
    st.subheader("Helpful resources for your job search")
    
    # Placeholder for future resources
    st.info("This section will contain helpful resources, links, and notes for your job search.")
    
    # Placeholder for resource categories
    st.write("Resource categories will appear here.")