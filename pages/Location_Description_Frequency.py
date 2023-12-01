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

df = st.session_state['analytics_data']
df = df.replace({"PARKING LOT / GARAGE (NON RESIDENTIAL)": "PARKING LOT"})

st.title("Location Frequency")
st.divider()

markdown = """
    <div style="text-align: center;">
    <h4>Top 10 most common locations where crimes are committed in Chicago</h4>
    </div><br/>
"""

st.markdown(markdown, unsafe_allow_html=True)
  
fig, ax = plt.subplots(figsize=(10,10))

order = df['location_description'].value_counts().head(10).index

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