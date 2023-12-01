import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import init_connection
from utils import fetch_analytics_tbl
import seaborn as sns

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

if 'analytics_data' not in st.session_state:
    conn = st.session_state['conn']
    st.session_state['analytics_data'] = fetch_analytics_tbl(conn)

st.title("Crime Frequency")
st.title("Test")
st.divider()

df = st.session_state['analytics_data']

fig, ax = plt.subplots(figsize=(10,10))

# Top 10 most frequent crimes
order = df['primary_type'].value_counts().head(10).index

sns.countplot(
    data=df, 
    x='primary_type', 
    order=order,
    ax=ax,
    hue="primary_type"
)

ax.set_xlabel("Count", fontsize=15)
ax.set_ylabel("Crime committed", fontsize=15)

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

st.pyplot(fig)