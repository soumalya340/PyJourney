import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
from load_json import load_job_data
from load_json import JSON_FILE

def save_job_data(data):
    """Save job application data to JSON file"""
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

def resources_tab2():
    """Render the content for the Job Applications tab"""
    st.header("Job Applications")
    
    # Load existing job data
    job_data = load_job_data()
    df = pd.DataFrame(job_data)
    # Create sub-tabs for different sections
    new_tab, details_tab = st.tabs(["Add New", "Application Details"])
    # Tab 1: Add New Application
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
            salary_range = st.text_input("Salary Range (Optional)")

            #Country 
            country = st.selectbox("Country (Optional)", [
                # North America
                "United States", "Canada", "Mexico",
                # South America 
                "Brazil", "Argentina", "Chile", "Colombia", "Peru", "Venezuela", "Uruguay", "Paraguay", "Bolivia", "Ecuador",
                # Europe
                "United Kingdom", "Germany", "France", "Italy", "Spain", "Netherlands", "Belgium", "Switzerland", "Sweden", 
                "Norway", "Denmark", "Finland", "Ireland", "Portugal", "Austria", "Poland", "Czech Republic", "Hungary",
                # Asia
                "India", "Singapore", "Japan", "Hong Kong", "Taiwan", "Thailand", "United Arab Emirates", "Turkey",
                # Other
                "Other"
            ])
            
            # Notes
            notes = st.text_area("Notes")

            source_of_application = st.text_input("Source of Application (Optional)")

            how_many_rounds = st.number_input("How many rounds of interviews/tests happened?", min_value=0, max_value=10, value=0)

            how_days_ago_posted = st.number_input("How many days ago was the job posted?", min_value=0, max_value=30, value=0)

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
                    "salary_range": salary_range,
                    "country": country,
                    "notes": notes,
                    "source_of_application": source_of_application,
                    "how_many_rounds": how_many_rounds,
                    "how_days_ago_posted": how_days_ago_posted,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # Add to job data
                job_data.append(new_job)
                
                # Save updated data
                save_job_data(job_data)
                
                st.success("Job application added successfully!")
                st.experimental_rerun()
    
    # Tab 2: Application Details
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
                        if 'salary' in selected_job and selected_job['salary']:
                            st.write(f"**Salary:** {selected_job['salary']}")
                        elif 'salary_range' in selected_job and selected_job['salary_range']:
                            st.write(f"**Salary Range:** {selected_job['salary_range']}")
                        st.write(f"**Country:** {selected_job['country']}")
                        st.write(f"**Notes:**")
                        st.text_area("", selected_job['notes'], disabled=True, label_visibility="collapsed")
                        st.write(f"**Source of Application:** {selected_job['source_of_application']}")
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
                                if new_status == "Rejected":
                                    notes = st.text_area("Notes")
                                    selected_job['notes'] = notes

                                save_job_data(job_data)
                                st.success("Status updated!")
                                st.experimental_rerun()
                        
                        #Update Number of Rounds
                        if st.button("Update Number of Rounds"):
                            new_how_many_rounds = st.number_input("How many rounds of interviews/tests happened?", min_value=1, max_value=10, value=1)
                            selected_job['how_many_rounds'] = new_how_many_rounds
                            save_job_data(job_data)
                            st.success("Number of rounds updated!")
                            st.experimental_rerun()

                        st.write(f"**How many rounds of interviews/tests happened?** {selected_job['how_many_rounds']}")
                        st.write(f"**How many days ago was the job posted?** {selected_job['how_days_ago_posted']}") 
                        # Delete button
                        if st.button("Delete", key=f"delete_{selected_id}"):
                            job_data = [job for job in job_data if job["id"] != selected_id]
                            save_job_data(job_data)
                            st.success("Job application deleted!")
                            st.experimental_rerun()