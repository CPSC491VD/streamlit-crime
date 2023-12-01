import streamlit as st
import pandas as pd
from pydeck.data_utils import assign_random_colors
import pydeck as pdk
from utils import init_connection

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

st.title("Geospatial data of Chicago Crimes")
st.divider()
st.header("Geospatial visualization of Chicago Crimes")

conn = st.session_state['conn']

query = "SELECT DISTINCT latitude, longitude FROM tbl_analytics;"
df = pd.DataFrame(conn.query(query)).dropna()

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