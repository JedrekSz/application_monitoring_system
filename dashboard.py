import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT")
}


@st.cache_data
def load_data():

    conn = psycopg2.connect(**DB_CONFIG)

    query = """
        SELECT *
        FROM monitoring_logs
        ORDER BY check_time DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


st.title("Application Monitoring Dashboard")

df = load_data()

st.metric(
    "Total Checks",
    len(df)
)

st.dataframe(df)

if not df.empty:

    avg_times = (
        df.groupby("service_name")["response_time"]
        .mean()
        .reset_index()
    )

    st.subheader("Average Response Time")

    st.bar_chart(
        avg_times.set_index("service_name")
    )
if not df.empty:

    uptime = (
        df.groupby("service_name")
        .agg(
            total=("id", "count"),
            success=("status_code", "count")
        )
    )

    uptime["uptime"] = (
        uptime["success"] /
        uptime["total"]
    ) * 100

    st.subheader("Uptime")

    st.dataframe(
        uptime[["uptime"]]
    )