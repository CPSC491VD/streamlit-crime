import streamlit as st
import pandas as pd
from pydeck.data_utils import assign_random_colors

@st.cache_resource
def init_connection():
    conn = st.connection("postgresql", type="sql")
    return conn

@st.cache_data
def color_lookup(df: pd.DataFrame):
    color_lookup = assign_random_colors(df['primary_type'])
    return color_lookup

def add_location_link(df: pd.DataFrame):
    df['google_link'] = df.apply(
        lambda row: f"https://www.google.com/maps/search/?api=1&query={row['latitude']},{row['longitude']}" if pd.notna(row['latitude']) and pd.notna(row['longitude']) else 'Not Available', 
        axis=1
    )


