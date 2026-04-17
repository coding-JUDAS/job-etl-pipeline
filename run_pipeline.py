import time
from src.etl_pipeline import run_pipeline

if __name__ == "__main__":
    while True:
        try:
            run_pipeline()
        except Exception as e:
            print(f"Pipeline failed: {e}")
        
        # Wait for 5 minutes before running again
        time.sleep(60 * 5)    