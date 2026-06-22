from database import get_connection
import pandas as pd

def show_statistics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            service_name,
            COUNT(*) as checks,
            AVG(response_time) as avg_time
        FROM monitoring_logs
        GROUP BY service_name
    """)

    rows = cursor.fetchall()

    print("\n=== SERVICE STATISTICS ===")

    for row in rows:
        print(
            f"Service: {row[0]} | "
            f"Checks: {row[1]} | "
            f"Avg Response: {round(row[2], 3)} sec"
        )

    cursor.close()
    conn.close()

def export_report():

    conn = get_connection()

    query = """
        SELECT *
        FROM monitoring_logs
    """

    df = pd.read_sql(query, conn)

    df.to_csv(
        "monitoring_report.csv",
        index=False
    )

    conn.close()

    print("Report exported.")

def uptime_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            service_name,
            COUNT(*) as total_checks,
            COUNT(status_code) as successful_checks
        FROM monitoring_logs
        GROUP BY service_name
    """)

    rows = cursor.fetchall()

    print("\nUPTIME REPORT")

    for row in rows:

        uptime = (
            row[2] / row[1]
        ) * 100

        print(
            f"{row[0]} -> {uptime:.2f}%"
        )

    cursor.close()
    conn.close()