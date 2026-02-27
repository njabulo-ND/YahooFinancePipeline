# Yahoo Finance Stock Statistics Pipeline

## Overview
This project is a **data engineering pipeline** that fetches, processes, and stores stock statistics from the Yahoo Finance API.  
It demonstrates **end-to-end data engineering skills**, including API integration, JSON parsing, data cleaning, structured storage in SQL Server, and version control.

The project is designed as a **portfolio-ready project** to showcase abilities in real-world data workflows for graduate programs or professional applications.

---

## Features
- Pulls **financial stock statistics** from Yahoo Finance API in JSON format
- Handles **API errors and exceptions**
- **Flattens and cleans** nested JSON data
- Converts timestamps to **human-readable dates**
- Stores cleaned data into **SQL Server (SSMS)**, with optional CSV/Parquet backup
- Designed for **scalability and automation**
- Version-controlled with **Git** for reproducibility

---

## Project Structure


StockStatsPipeline/
├── src/
│ ├── fetch_data.py # Fetch raw stock data from Yahoo Finance
│ ├── process_data.py # Flatten, clean, and process JSON
│ └── store_data.py # Save cleaned data to SQL Server (SSMS) or CSV/Parquet
├── data/ # Raw and processed datasets
├── notebooks/ # Optional exploration / verification notebooks
├── requirements.txt # Python dependencies
└── README.md # Project documentation


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