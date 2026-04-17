# Job Market ETL Pipeline (US)

## Overview
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline that processes raw job market data into a structured, queryable database.

## Architecture
ETL pipeline with validation and logging layers
Raw Data → Extract → Transform → Load → SQL Database → Query


The pipeline demonstrates real-world data engineering workflows including data cleaning, transformation, and database integration.
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
- Config-driven pipeline
- Data validation checks
- Logging system
- Modular architecture
- SQL database integration

## Future Improvements
- Airflow orchestration
- Cloud deployment (AWS)
- API-based data ingestion

## How to Run
```bash
pip install -r requirements.txt
cd src
python etl_pipeline.py