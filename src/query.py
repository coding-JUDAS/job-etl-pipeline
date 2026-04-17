import sqlite3

def run_queries():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM jobs"
    cursor.execute(query)

    result = cursor.fetchone()
    print("Total records:", result[0])

    conn.close()

if __name__ == "__main__":
    run_queries()