from extractor import extract_data
from transform import clean_data
from load import load_to_db

def run_pipeline():
    # Step 1: Extract
    df = extract_data("./data/jobs_raw.csv")

    # Step 2: Transform
    cleaned_df = clean_data(df)

    # Step 3: Load
    load_to_db(cleaned_df)
    print("ETL pipeline executed successfully.")

if __name__ == "__main__":
    run_pipeline()