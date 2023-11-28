import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import init_connection
import seaborn as sns

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

conn = st.session_state['conn']

st.title("Location Frequency")
st.divider()
st.header("Top 10 most common locations where crimes are committed in Chicago, sorted by frequency.")


df = pd.DataFrame(conn.query("SELECT location_description FROM tbl_analytics;", ttl="10m"))

fig, ax = plt.subplots(figsize=(10,10))

order = df['location_description'].value_counts().iloc[:10].index

sns.countplot(
    data=df, 
    y='location_description', 
    order=order,
    ax=ax,
    hue="location_description"
)

ax.legend().set_visible(False)
ax.set_xlabel("Count", fontsize=15)
ax.set_ylabel("Location Description", fontsize=15)

st.pyplot(fig)
st.caption("Frequency of crimes by location in Chicago.")