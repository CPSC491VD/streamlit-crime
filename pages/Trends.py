import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from utils import init_connection
from utils import fetch_analytics_tbl

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

st.title("Crime Trend Data")
st.divider()
st.header("Visualized crime trends over time in the city of Chicago, over the course of some days.")

df: pd.DataFrame = st.session_state['analytics_data']
cutoff_date = df['crime_date'].max()
df = df[df['crime_date'] < cutoff_date]

start, end = df['crime_date'].min(), df['crime_date'].max()

fig, (ax1, ax2) = plt.subplots(2, figsize=(10,10))

crimes_by_hour = df.resample('H', on='crime_date').size().reset_index(name='count')
sns.lineplot(x='crime_date', y='count', data=crimes_by_hour, ax=ax1)
ax1.set_title(f'Hourly Crime Trend')
ax1.set_xlabel('Date and Time')
ax1.set_ylabel('Crime Count')

top_3_crimes = df['primary_type'].value_counts().head(5).index
df_top_3 = df[df['primary_type'].isin(top_3_crimes)]
df_top_3['crime_date'] = df_top_3['crime_date'].dt.date
df_top_3 = df_top_3.groupby(['crime_date', 'primary_type']).size().reset_index(name='count')
top_3 = sns.lineplot(x='crime_date', y='count', hue='primary_type', data=df_top_3, ax=ax2)
ax2.set_title(f'Hourly Crime Trend by Crime Type')
ax2.set_xlabel('Date and Time')
ax2.set_ylabel('Crime Count')

plt.tight_layout()
plt.legend(loc='lower left')
sns.set_style("darkgrid")
st.pyplot(fig)

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