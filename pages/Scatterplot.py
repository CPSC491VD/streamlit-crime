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

st.title("Scatterplots :pushpin:")
st.header("Scatterplot graphs produced from latitude and longitude data, showing distribution of different phenomena")
tab1, tab2, tab3 = st.tabs(["Latitude vs longitude plot of theft and battery", "Crime scatterplot trend", "Arrest distribution"])

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
    trendline_scope='overall',
    title='Latitude vs longitude plot of theft and battery crimes'
)

fig_2 = px.scatter(
    hourly_crime_df,
    x='crime_hour',
    y='crime_count',
    trendline='ols',
    title='Crime trendline over the course of a full 24 hr cycle'
)

df_arrest_rate = df
df_arrest_rate['latitude'] = df_arrest_rate['latitude'].round(2)
df_arrest_rate['longitude'] = df_arrest_rate['longitude'].round(2)
df_arrest_rate = df_arrest_rate.groupby(['latitude', 'longitude']).agg({'case_number': 'count'}).reset_index()
df_arrest_rate = df_arrest_rate.rename(columns={'case_number': 'count'})

fig_3 = px.scatter(
    df_arrest_rate,
    x='latitude',
    y='longitude',
    color='count',
    title='Distribution of arrests over latitude, longitude pairs'
)

with tab1:
    st.plotly_chart(fig_1)

with tab2:
    st.plotly_chart(fig_2)
    
with tab3:
    st.plotly_chart(fig_3)
