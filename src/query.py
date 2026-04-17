from sqlalchemy import text
from db import get_engine

def run_queries():
    engine = get_engine()

    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM jobs"))
        print("Total records:", result.scalar())

        result = conn.execute(text("""
            SELECT job_title, COUNT(*) as count
            FROM jobs
            GROUP BY job_title
            ORDER BY count DESC
            LIMIT 5
        """))

        print("Top job roles:")
        for row in result:
            print(row)

if __name__ == "__main__":
    run_queries()