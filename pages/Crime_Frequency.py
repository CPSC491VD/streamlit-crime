import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import init_connection

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

st.title("Crime Frequency")
st.divider()

conn = st.session_state['conn']

df = pd.DataFrame(conn.query("SELECT * FROM tbl_analytics", ttl="10m"))

fig, ax = plt.subplots(figsize=(6,6))

crime_type_counts = df['primary_type'].value_counts()
crime_type_counts.plot(ax=ax, kind='bar', color='red')

ax.set(title='Frequency of Each Crime Type', xlabel='Crime Committed', ylabel='Frequency')

plt.xticks(rotation=35, ha='right')

st.subheader("Frequency of each kind of categorized crime in the city of Chicago")
st.pyplot(fig)

