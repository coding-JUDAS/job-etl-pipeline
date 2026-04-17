# Job Market ETL Pipeline (US)

## Overview
This project implements an end-to-end ETL pipeline that extracts raw job market data, transforms it into a clean format, and loads it into a structured SQL database for analysis.

## Tech Stack
- Python (pandas)
- SQL (SQLite)
- SQLAlchemy

## Pipeline
1. Extract raw CSV data
2. Clean and transform dataset
3. Load into SQL database
4. Run analytical queries

## Key Features
- Data cleaning and preprocessing
- Automated pipeline execution
- Structured database storage
- Query-ready dataset

## How to Run
```bash
pip install -r requirements.txt
cd src
python etl_pipeline.py