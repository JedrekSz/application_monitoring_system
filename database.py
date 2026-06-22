import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT")
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monitoring_logs (
            id SERIAL PRIMARY KEY,
            service_name VARCHAR(100),
            url TEXT,
            status_code INTEGER,
            response_time FLOAT,
            check_time TIMESTAMP,
            error_message TEXT
        )
    """)

    conn.commit()

    cursor.close()
    conn.close()

def save_log(data):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO monitoring_logs (
            service_name,
            url,
            status_code,
            response_time,
            check_time,
            error_message
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        data["service_name"],
        data["url"],
        data["status_code"],
        data["response_time"],
        data["check_time"],
        data["error_message"]
    ))

    conn.commit()

    cursor.close()
    conn.close()