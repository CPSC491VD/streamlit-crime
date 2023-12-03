import streamlit as st
import pandas as pd
import plotly.express as px
from utils import init_connection
from utils import fetch_analytics_tbl

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()
    
if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

df: pd.DataFrame = st.session_state['analytics_data']
df['crime_hour'] = df['crime_date'].dt.hour

hourly_crime_counts = df.groupby('crime_hour').size().reset_index(name='crime_count')
hourly_crime_df = pd.DataFrame(hourly_crime_counts)
hourly_crime_df = hourly_crime_df.reindex(range(24), fill_value=0)

df_theft_or_bat = df[(df['primary_type'] == 'THEFT') | (df['primary_type'] == 'BATTERY')]

fig_1 = px.scatter(
    df_theft_or_bat,
    x='latitude',
    y='longitude',
    facet_col='arrest',
    color='primary_type',
    trendline='ols',
    trendline_scope='overall'
)

fig_2 = px.scatter(
    hourly_crime_df,
    x='crime_hour',
    y='crime_count',
    trendline='ols'
)

st.plotly_chart(fig_1)
st.plotly_chart(fig_2)

st.write('test')