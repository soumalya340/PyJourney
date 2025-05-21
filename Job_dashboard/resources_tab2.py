import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# File path for job applications data
JSON_FILE = "job_applications.json"

def load_job_data():
    """Load job application data from JSON file"""
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Return empty list if file is empty or invalid
            return []
    return []

def save_job_data(data):
    """Save job application data to JSON file"""
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

def resources_tab2():
    """Render the content for the Job Applications tab"""
    st.header("Job Applications")
    
    # Load existing job data
    job_data = load_job_data()
    
    # Create sub-tabs for different sections
    app_tab, new_tab, details_tab = st.tabs(["Your Applications", "Add New", "Application Details"])
    
    # Tab 1: Applications List and Details
    with app_tab:
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
                columns_to_display = ["company", "position", "status", "date_applied"]
                # Add salary column only if it exists
                if "salary" in display_df.columns:
                    columns_to_display.append("salary")
                    
                # Only select columns that exist in the dataframe
                display_df = display_df[columns_to_display]
                
                # Rename columns for better display
                display_df.columns = ["Company", "Position", "Status", "Date Applied", "Salary"]
                
                # Display table
                st.dataframe(
                    display_df,
                    use_container_width=True,
                    height=400
                )           
    # Tab 2: Add New Application
    with new_tab:
        st.subheader("Add New Application")
        
        with st.form(key="add_job_form"):
            company_name = st.text_input("Company Name")
            position = st.text_input("Position")
            
            # Application status dropdown
            status_options = ["Applied", "Interview Scheduled", "Rejected", "Offer Received", "Accepted", "Declined"]
            status = st.selectbox("Status", status_options)
            
            # Date applied
            date_applied = st.date_input("Date Applied", datetime.now())
            
            # Salary if available
            salary = st.text_input("Salary (Optional)")
            
            # Notes
            notes = st.text_area("Notes")
            
            # Submit button
            submit_button = st.form_submit_button(label="Add Job Application")
            
            if submit_button:
                # Create new job entry
                new_job = {
                    "id": len(job_data) + 1,
                    "company": company_name,
                    "position": position,
                    "status": status,
                    "date_applied": date_applied.strftime("%Y-%m-%d"),
                    "salary": salary,
                    "notes": notes,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # Add to job data
                job_data.append(new_job)
                
                # Save updated data
                save_job_data(job_data)
                
                st.success("Job application added successfully!")
                st.experimental_rerun()
    
    # Tab 3: Statistics
    with details_tab:
        st.subheader("Application Details")
        if job_data:   
            # Button to select entry for detailed view or editing
                selected_id = st.selectbox(
                    "Select application to view details:",
                    options=df["id"].tolist(),
                    format_func=lambda x: f"{df[df['id']==x]['company'].iloc[0]} - {df[df['id']==x]['position'].iloc[0]}"
                )
                
                # Display selected job details
                if selected_id:
                    selected_job = next((job for job in job_data if job["id"] == selected_id), None)
                    
                    if selected_job:
                        st.write(f"**Details: {selected_job['company']} - {selected_job['position']}**")
                        st.write(f"**Status:** {selected_job['status']}")
                        st.write(f"**Applied on:** {selected_job['date_applied']}")
                        if selected_job['salary']:
                            st.write(f"**Salary:** {selected_job['salary']}")
                        st.write(f"**Notes:**")
                        st.text_area("", selected_job['notes'], disabled=True, label_visibility="collapsed")
                        
                        # Update status
                        status_options = ["Applied", "Interview Scheduled", "Rejected", "Offer Received", "Accepted", "Declined"]
                        new_status = st.selectbox(
                            "Update Status",
                            options=status_options,
                            index=status_options.index(selected_job['status'])
                        )
                        
                        if new_status != selected_job['status']:
                            if st.button("Update Status"):
                                for job in job_data:
                                    if job["id"] == selected_id:
                                        job["status"] = new_status
                                        break
                                
                                save_job_data(job_data)
                                st.success("Status updated!")
                                st.experimental_rerun()
                        
                        # Delete button
                        if st.button("Delete", key=f"delete_{selected_id}"):
                            job_data = [job for job in job_data if job["id"] != selected_id]
                            save_job_data(job_data)
                            st.success("Job application deleted!")
                            st.experimental_rerun()