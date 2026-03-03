# Yahoo Finance Stock Statistics Pipeline
## PROJECT STILL IN PROGRESS
## Overview
This project is a **data engineering pipeline** that fetches, processes, and stores stock statistics from the Yahoo Finance API.  
It demonstrates **end-to-end data engineering skills**, including API integration, JSON parsing, data cleaning, structured storage in SQL Server, and version control.

The project is designed as a **portfolio-ready project** to showcase abilities in real-world data workflows for graduate programs or professional applications.

---

## Features
- Pulls **financial stock statistics** from Yahoo Finance API in JSON format
- Handles **API errors and exceptions**
- **Flattens and cleans** nested JSON data
- Converts unreadable data to **human-readable data**
- Stores cleaned data into **SQL Server (SSMS)**, with optional CSV/Parquet backup
- Designed for **scalability and automation**
- Version-controlled with **Git** for reproducibility

---

## Project Structure

```text
StockStatsPipeline/
├── ssource/
│   ├── fetch_data.py                    # Fetch raw stock data from Yahoo Finance
│   ├── process_data.py                  # Flatten, clean, and process JSON
│   └── store_data.py                    # Save cleaned data to SQL Server (SSMS) or CSV/Parquet
├── data/                                # Raw and processed datasets
├── notebooks/                           # Optional exploration / verification notebooks
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

# Environment Configuration
1. Create a file named .env in the root directory of the project.
2. Add the following variable inside the file:
API_KEY=your_api_key_here
3. Ensure the variable name matches exactly with the one in this project: API_KEY
4. The variable name must match the one used in the source code.
- If the name is different or missing, the application will fail to start.
5. Install dependencies by running:
pip install -r requirements.txt
6. Important Notes:
- Do NOT commit your .env file to version control.
- The .env file is ignored using .gitignore.
7. Each user must create their own .env file with their own credentials, but the variable must match the one in the project.
8. The variable in the code that will be assigned to the API key must be the same as in the project:
API_KEY = os.getenv("API_KEY")

---

## Pipeline Workflow

```text
Yahoo Finance API JSON (raw stock metrics)
               ↓
       fetch_data.py
               ↓
     process_data.py (flatten, clean, convert types)
               ↓
   store_data.py → SQL Server (SSMS)
               ↓
Optional: dashboards, analytics, or further applications


