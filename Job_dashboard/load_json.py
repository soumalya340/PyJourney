import json
import os

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
