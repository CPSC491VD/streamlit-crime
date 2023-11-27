import streamlit as st
import pandas as pd
import psycopg2 as pg2
from utils import init_connection

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

st.title("Chicago Crime Data")
st.divider()
st.header("Visualizing real-time data from the Chicago Crime Pipeline")
st.subheader("Built for the CPSC 491 Capstone Project")
st.sidebar.success("Select a visualization above.")
