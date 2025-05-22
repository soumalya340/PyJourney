# Job Tracker Dashboard

A Streamlit application for tracking and managing job applications during your job search.

## Overview

This application provides a user-friendly interface to:

- Track all your job applications in one place
- Visualize your job search progress
- Manage application details and statuses
- Store application data persistently

## Files Structure

- `main.py` - The main application entry point
- `resource_tab1.py` - Dashboard and overview visualization
- `resources_tab2.py` - Job application management interface
- `load_json.py` - Helper functions for data loading
- `job_applications.json` - Data storage file (JSON)

## Setup Instructions

1. Make sure you have Python installed (3.7+ recommended)

2. Install required packages:

```bash
pip install streamlit pandas
```

3. Run the application:

```bash
streamlit run main.py
```

## Features

### Dashboard (Tab 1)

- Overview of application statistics
- Visual representation of job search progress
- Summary of recent applications

### Job Applications (Tab 2)

- Add new job applications with detailed information
- View and update existing application details
- Delete applications
- Track application statuses and interview rounds

## Data Structure

The application stores job applications with the following fields:

- Company name
- Position
- Status (Applied, Interview Scheduled, Rejected, etc.)
- Date applied
- Salary range
- Country
- Source of application
- Interview rounds
- Job posting age
- Notes and other details

## Streamlit Functions Used

### Layout Elements

- `st.tabs()` - Creates tabbed navigation
- `st.columns()` - Creates columnar layouts
- `st.header()`, `st.subheader()` - Section headings
- `st.form()` - Creates input forms

### Input Widgets

- `st.text_input()` - Text input fields
- `st.text_area()` - Multi-line text inputs
- `st.selectbox()` - Dropdown menus
- `st.date_input()` - Date picker
- `st.number_input()` - Numeric input with min/max values
- `st.form_submit_button()` - Form submission button

### Data Display

- `st.dataframe()` - Interactive data table
- `st.metric()` - Metric display with optional delta
- `st.write()` - General-purpose write function
- `st.info()` - Informational messages

### State Management

- `st.experimental_rerun()` - Reruns the app after state changes

### Application Configuration

- `st.set_page_config()` - Configures page title, layout, etc.

## How the App Works

1. The main entry point (`main.py`) sets up the application layout and tabs
2. Data is loaded from and saved to a JSON file for persistence
3. The dashboard tab (`resource_tab1.py`) displays metrics and summary data
4. The job applications tab (`resources_tab2.py`) provides a management interface
5. Users can add, view, update, and delete job applications

## Tips for Usage

- Keep your job applications organized by consistently entering data
- Update application statuses promptly to maintain accurate metrics
- Use the notes field to track important details about each application
- Regularly review your dashboard to understand your job search progress
