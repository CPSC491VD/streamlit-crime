import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import init_connection
from utils import fetch_analytics_tbl

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

df: pd.DataFrame = st.session_state['analytics_data']

fig, ax = plt.subplots(figsize=(11,5))

crimes_by_date = df.groupby(df['crime_date']).size().reset_index(name='crime_count')

sns.lineplot(x='crime_date', y='crime_count', data=crimes_by_date)

st.pyplot(fig)

print(df['crime_date'].to_string())