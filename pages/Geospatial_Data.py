import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
from utils import get_latitude_longitude_mean
from utils import init_connection
from utils import fetch_analytics_tbl

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

st.title("Geospatial Chicago Crimes :world_map:")
st.divider()
st.header("A geospatial representation of Chicago crimes.")
markdown = "The crime hexagon map shows the distribution of crimes in Chicago. From this, we can see the peak in red symbolizes the area where the most crimes have occurred. This allows us to better explore the data and understand crime trends in a large city."
st.markdown(markdown)

df: pd.DataFrame = st.session_state['analytics_data']
lat_mean, lon_mean = get_latitude_longitude_mean(df=df)

layer_hex = pdk.Layer(
    "HexagonLayer",
    data=df,
    elevation_scale=50,
    get_position='[longitude,latitude]',
    auto_highlight=True,
    extruded=True,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=lat_mean,
    longitude=lon_mean,
    zoom=8,
    pitch=45,
    bearing=10
)

deck = pdk.Deck(
    map_style="mapbox://styles/mapbox/dark-v11",
    layers=[layer_hex],
    initial_view_state=view_state,
    tooltip={
        "text": "Elevation Value: {elevationValue}"
    }
)

st.pydeck_chart(deck)
st.caption("Aggregated crime data based on latitude, longitude coordinates. Higher hexagons in red/orange indicate higher crime rates at that location.")

fig = px.density_mapbox(
    df,
    lat='latitude',
    lon='longitude',
    hover_name='primary_type',
    center={
        'lat': lat_mean,
        'lon': lon_mean
    },
    radius=10,
    mapbox_style='open-street-map'
)
markdown = "The crime heatmap allows us to zoom in and see how data points aggregate in the city of Chicago. It produces a representation of crime density within the city"
st.markdown(markdown)
st.plotly_chart(fig)
st.caption("Heatmap that aggregates crimes committed by points in the dataframe.")