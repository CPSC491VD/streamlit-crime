import streamlit as st
import pandas as pd
import pydeck as pdk
from utils import init_connection
from utils import fetch_analytics_tbl

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

st.title("Geospatial data of Chicago Crimes")
st.divider()
st.header("Geospatial visualization of Chicago Crimes")

df: pd.DataFrame = st.session_state['analytics_data']

layer = pdk.Layer(
    "HexagonLayer",
    data=df,
    elevation_scale=50,
    get_position='[longitude,latitude]',
    auto_highlight=True,
    extruded=True,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=df['latitude'].mean(),
    longitude=df['longitude'].mean(),
    zoom=8,
    pitch=45,
    bearing=10
)

deck = pdk.Deck(
    map_style="mapbox://styles/mapbox/dark-v11",
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "text": "Elevation Value: {elevationValue}"
    }
)

st.pydeck_chart(deck)
st.caption("Aggregated crime data based on latitude, longitude coordinates. Higher hexagons in red/orange indicate higher crime rates at that location.")