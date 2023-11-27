import streamlit as st
import pandas as pd
from utils import init_connection
from utils import add_location_link

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

st.title("Recent Crime Entries")
st.divider()
st.header("Condensed crime data from the past 25 most recent crimes committed in Chicago")

conn = st.session_state['conn']
df = pd.DataFrame(conn.query("SELECT id, crime_date, crime_description, latitude, longitude, primary_type FROM tbl_analytics limit 25;", ttl="10m"))

add_location_link(df)

st.dataframe(
    df,
    column_config={"google_link": st.column_config.LinkColumn("Google Maps API")}
)

st.caption("25 most recent crime records from the data pipeline.")

