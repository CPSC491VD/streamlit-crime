import streamlit as st
import pandas as pd
import pydeck as pdk
import streamlit.components.v1 as components
from utils import init_connection
from utils import color_lookup

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

st.title("Crimes committed in the city of Chicago ")
st.divider()
st.header("Each recent crime committed in the city of Chicago, plotted and color-coded")

conn = st.session_state['conn']
df = pd.DataFrame(conn.query("SELECT DISTINCT latitude, longitude, primary_type FROM tbl_analytics;")).dropna()

color_lookup = color_lookup(df=df)

df['color'] = df['primary_type'].map(color_lookup)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    elevation_scale=50,
    get_position='[longitude,latitude]',
    get_radius=300,
    get_fill_color='color'
)

view_state = pdk.ViewState(
    latitude=df['latitude'].mean(),
    longitude=df['longitude'].mean(),
    zoom=10,
    pitch=0,
)

deck = pdk.Deck(
    map_style="mapbox://styles/mapbox/outdoors-v12",
    layers=[layer],
    initial_view_state=view_state
)

st.pydeck_chart(deck)
st.caption("Points indicating recent crimes in Chicago.")

st.subheader("Color code:")
for key, rgb in color_lookup.items():
    hex_value = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
    html = f'<p style="color:{hex_value}; font-family: Arial, Helvetica, sans-serif;">{key}</p>'
    components.html(html, height=35)