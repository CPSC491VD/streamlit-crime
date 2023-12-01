import streamlit as st
from utils import init_connection
from utils import fetch_analytics_tbl

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

st.title("Chicago Crime Data :rotating_light::bar_chart:")
st.divider()
st.header("Visualizing real-time data from the Chicago Crime Pipeline")
st.subheader("Built for the CPSC 491 Capstone Project.")
st.markdown(
    """
    This application was powered by data from the city of Chicago.\n
    - Data was ingested from this public API [City of Chicago Crime API](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data).\n
    - Data was loaded, transformed and exported to the postgreSQL database using [mage.ai](http://mage.ai/).\n
    - Database is hosted using [ElephantSQL](https://www.elephantsql.com/). 
    """
)
st.sidebar.info("Please select a data visualization above.")