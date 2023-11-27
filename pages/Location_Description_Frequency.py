import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import init_connection
import seaborn as sns

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

st.title("Location Frequency")
st.divider()
st.header("Top 10 most common locations where crimes are committed in Chicago, sorted by frequency.")

conn = st.session_state['conn']

df = pd.DataFrame(conn.query("SELECT location_description FROM tbl_analytics;", ttl="10m"))

fig, ax = plt.subplots(figsize=(10,10))

sns.countplot(
    data=df, 
    y='location_description', 
    order=df['location_description'].value_counts().iloc[:10].index,
    palette="husl",
    ax=ax
)

ax.set_xlabel("Count", fontsize=15)
ax.set_ylabel("Location Description", fontsize=15)

st.pyplot(fig)
st.caption("Frequency of crimes by location in Chicago.")