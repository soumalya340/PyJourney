import streamlit as st
from load_json import load_job_data
import pandas as pd

def resource_tab1():
    job_data = load_job_data()
    st.header("Dashboard")
    st.subheader("Overview of your job search")
    
    # Placeholder for future dashboard content
    st.info(".This section will show statistics and visualizations of your job search progress.")
    
    # Empty containers for future metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Applications", value="0")
    with col2:
        st.metric(label="Interviews", value="0")
    with col3:
        st.metric(label="Response Rate", value="0%")

    # Create sub-tabs for different sections
    app_tab, = st.tabs(["Your Applications"])  # Note the comma to unpack the single tab
    # Tab 1: Applications List and Details
    with app_tab:  # Now app_tab is a single object, not a tuple
        # Create columns for table and details
        table_col, details_col = st.columns([2, 1])
        
        with table_col:
            st.subheader("Your Job Applications")
            if not job_data:
                st.info("No job applications yet. Start adding some!")
            else:
                # Convert to DataFrame for display
                df = pd.DataFrame(job_data)
                
                # Format DataFrame for display

                display_df = df.copy()
                
                # Reorder and select columns to display
                columns_to_display = ["company", "position", "country", "status", "source_of_application", "date_applied"]
                # Add salary column only if it exists
                if "salary" in display_df.columns:
                    columns_to_display.append("salary")
                    
                # Only select columns that exist in the dataframe
                display_df = display_df[columns_to_display]
                
                # Rename columns for better display - match the number of columns
                new_column_names = ["Company", "Position", "Country", "Status", "Source of Application", "Date Applied"]
                if "salary" in columns_to_display:
                    new_column_names.append("Salary")
                    
                display_df.columns = new_column_names
                
                # Display table
                st.dataframe(
                    display_df,
                    use_container_width=True,
                    height=400
                )
