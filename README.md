# Yahoo Finance Stock Statistics Pipeline  
## PROJECT STATUS: Work in Progress  

## Overview  
This project is a **data engineering pipeline** that fetches, processes, and stores stock statistics from the Yahoo Finance API.  
It demonstrates **end-to-end data engineering skills**, including API integration, JSON parsing, data cleaning, structured storage in SQL Server, and version control.  

The project is designed as a **portfolio-ready example** to showcase abilities in real-world data workflows for graduate programs or professional applications.  

---

## Features  
- Pulls **financial stock statistics** from Yahoo Finance API in JSON format  
- Handles **API errors and exceptions**  
- **Flattens and cleans** nested JSON data  
- Converts unreadable data to **human-readable formats**  
- Stores cleaned data into **SQL Server (SSMS)**, with optional CSV/Parquet backup  
- Designed for **scalability and automation**  
- Version-controlled with **Git** for reproducibility  

> ✅ **Current status:** Data fetching from the API is fully implemented.              
> ✅ **Current status:**  Transforming, cleaning, and storing the useful data into new json is fully implemented.    
> ⬜ **Next steps:** Retrieve cleaned and useful data from json and store into CSV/SQL formats.  

---

## Project Structure  

```text
StockStatsPipeline/
├── source/
│   ├── fetch_data.py      # Fetch raw stock data from Yahoo Finance
│   ├── process_data.py    # Flatten, clean, and process JSON (in progress)
│   └── store_data.py      # Save cleaned data to SQL Server (SSMS) or CSV/Parquet (pending)
├── data/                  # Raw and processed datasets
├── notebooks/             # Optional exploration / verification notebooks
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

Environment Configuration
1.Create a file named .env in the root directory of the project.
2.Add the following variable inside the file:
-API_KEY=your_api_key_here
3.Ensure the variable name matches exactly with the one used in this project: API_KEY
4.The variable name must match the one used in the source code.
-If the name is different or missing, the application will fail to start.
5.Install dependencies by running:
-pip install -r requirements.txt

6.Important Notes:
-Do NOT commit your .env file to version control.
-The .env file is ignored using .gitignore.
7.Each user must create their own .env file with their own credentials, but the variable must match the one in the project.
8.The variable in the code that will be assigned to the API key must be the same as in the project:
-API_KEY = os.getenv("API_KEY")

Pipeline Workflow
Yahoo Finance API JSON (raw stock metrics)
               ↓
       fetch_data.py (completed)
               ↓
     process_data.py (flatten, clean, convert types — in progress)
               ↓
   store_data.py → SQL Server (SSMS) / CSV (pending)
               ↓
Optional: dashboards, analytics, or further applications


