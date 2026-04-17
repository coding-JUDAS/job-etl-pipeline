from extractor import extract_data
from transform import clean_data
from load import load_to_db
from validation import validate_data
from logger import get_logger

def run_pipeline():
    logger = get_logger()
    
    try:
        logger.info("Starting ETL pipeline")

        df = extract_data()
        logger.info(f"Extracted {len(df)} records")

        df_clean = clean_data(df)
        logger.info("Data transformation complete")

        validate_data(df_clean)
        logger.info("Data validation passed")

        load_to_db(df_clean)
        logger.info("Data loaded into database")

        logger.info("ETL pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    try:
     run_pipeline()
    except Exception as e:
        print(f"Pipeline failed: {e}")