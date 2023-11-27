import streamlit as st
import pandas as pd
from pydeck.data_utils import assign_random_colors

@st.cache_resource
def init_connection():
    """Create a connection to the postgreSQL database."""
    conn = st.connection("postgresql", type="sql")
    return conn

@st.cache_data
def color_lookup(df: pd.DataFrame):
    """Assign colors to the crime committed."""
    color_lookup = assign_random_colors(df['primary_type'])
    return color_lookup

def add_location_link(df: pd.DataFrame):
    """Add a location link to dataframe based on latitude, longitude."""
    df['google_link'] = df.apply(
        lambda row: f"https://www.google.com/maps/search/?api=1&query={row['latitude']},{row['longitude']}" if pd.notna(row['latitude']) and pd.notna(row['longitude']) else 'N/A', 
        axis=1
    )

def get_latitude_longitude_mean(df: pd.DataFrame):
    """Get the mean of latitude, longitude columns."""
    latitude_mean, longitude_mean = df['latitude'].mean(), df['longitude'].mean()
    return latitude_mean, longitude_mean