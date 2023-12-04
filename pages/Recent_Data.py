import streamlit as st
import pandas as pd
from utils import init_connection
from utils import add_location_link
from utils import fetch_analytics_tbl

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()
    
if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

st.title("Recent Crime Entries :date:")
st.header("Condensed crime data from the past 25 most recent crimes committed in Chicago")
st.divider()

df: pd.DataFrame = st.session_state['analytics_data']
df = df[['id', 'crime_date', 'primary_type', 'crime_description', 'latitude', 'longitude']]
df['crime_date'] = pd.to_datetime(df['crime_date'])
df = df.head(25)

add_location_link(df)

paragraph = """
The data table below presents the latest crime updates in our database, 
reflecting the most recent incidents recorded from the last pipeline run. 
\nEach row details specific information about individual crimes, including the type of offense, date, time, and location. 
\nThis comprehensive dataset serves as a valuable resource for analyzing crime trends and understanding where these crimes occur.
"""
st.write(paragraph)
st.dataframe(
    df,
    column_config={
        "google_link": st.column_config.LinkColumn("Google Maps API")
    }
)

st.caption("25 most recent crime records from the data pipeline.")

