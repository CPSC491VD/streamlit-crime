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
df = df.replace({"PARKING LOT / GARAGE (NON RESIDENTIAL)": "PARKING LOT"})

st.title("Crime Frequency Data")
st.divider()
st.markdown("### Location")

markdown = """
    <div style="text-align: center;">
    <p>In Chicago, crime frequency reveals a distinct pattern on the city's crime graph, with the majority of incidents occurring on the streets. The bustling urban environment and diverse neighborhoods contribute to a higher prevalence of street-level crimes. Notably, the second most common location for criminal activities is within apartments, suggesting a significant portion of incidents takes place within residential settings. This dynamic distribution underscores the need for targeted law enforcement efforts in both public spaces and residential areas to address the unique challenges posed by Chicago's crime landscape. Understanding and addressing crime trends in these key locations is crucial for developing effective strategies to enhance public safety in the city.</p>
    </div><br/>
"""

st.markdown(markdown, unsafe_allow_html=True)


fig, ax = plt.subplots(figsize=(6,4))

order = df['location_description'].value_counts().head(10).index

sns.countplot(
    data=df, 
    y='location_description', 
    order=order,
    ax=ax,
    hue="location_description"
)

ax.legend().set_visible(False)
ax.set_xlabel("\nCount", fontsize=8)
ax.set_ylabel("\nLocation Description", fontsize=8)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=5)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=5)

st.pyplot(fig)


st.markdown("### Crime Type Frequency")
st.markdown("""
<p style='text-align:center;'>In the crime frequency graph for Chicago, theft emerges as the most prevalent crime type, underscoring its significant impact on the city's safety landscape. Following closely is battery, another frequent offense that demands attention in law enforcement efforts. Motor theft ranks third in the graph, highlighting the persistent challenge of vehicular crime in the urban setting. This distribution provides valuable insights into the predominant criminal activities, aiding authorities in devising targeted strategies to address and mitigate these specific threats.</p><br/>
""", unsafe_allow_html=True)
df = st.session_state['analytics_data']
fig, ax = plt.subplots(figsize=(5,3))
# Top 10 most frequent crimes
order = df['primary_type'].value_counts().head(10).index

sns.countplot(
    data=df, 
    x='primary_type', 
    order=order,
    ax=ax,
    hue="primary_type"
)

ax.set_xlabel("\nType of crimes", fontsize=7)
ax.set_ylabel("Amount\n", fontsize=7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=5)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=5)

st.pyplot(fig)