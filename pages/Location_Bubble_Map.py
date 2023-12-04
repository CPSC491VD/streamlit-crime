import streamlit as st
import pandas as pd
import plotly.express as px
from utils import init_connection
from utils import fetch_analytics_tbl
from utils import get_latitude_longitude_mean

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

df: pd.DataFrame = st.session_state['analytics_data']

st.title("Chicago Crime Data Bubble Map :bubble_tea:")
st.subheader("Each recent crime committed in the city of Chicago, plotted and color-coded")
st.divider()
st.write("This is an interactive map which allows users to hover over each point and view the legend to determine the crime committed at the datapoint.")

lat_mean, lon_mean = get_latitude_longitude_mean(df=df)
fig = px.scatter_mapbox(
    df,
    lat='latitude',
    lon='longitude',
    color='primary_type',
    mapbox_style='open-street-map',
    center={
        'lat': lat_mean,
        'lon': lon_mean
    },
    zoom=9,
    width=700,
    height=600
)


st.plotly_chart(fig)
st.caption("Aggregated data of crimes, color coded and labeled.")