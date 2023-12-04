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

tab1, tab2, tab3, tab4 = st.tabs(["Location Frequency", "Crime Type Frequency", "Arrests", "Description Frequency"])

with tab1:
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
    plt.title('Frequency of Crimes by Location')
    plt.xlabel("Count")
    plt.ylabel("Location Description")
    ax.set_xticklabels(ax.get_xticklabels(), ha='right')

    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(figsize=(5,3))
    order = df['primary_type'].value_counts().head(10).index

    sns.countplot(
        data=df, 
        x='primary_type', 
        order=order,
        ax=ax,
        hue="primary_type"
    )

    plt.title('Frequency of Crimes by Type')
    plt.xlabel("Type of crimes")
    plt.ylabel("Amount")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=7)

    st.pyplot(fig)

with tab3:
    fig, ax = plt.subplots(figsize=(8,6))

    sns.countplot(x='arrest', data=df, hue='arrest')

    plt.title('Frequency of Arrests (True/False)')
    plt.xlabel('Arrests')
    plt.ylabel('Count')

    st.pyplot(fig)

with tab4:
    fig, ax = plt.subplots(figsize=(5,3))
    order = df['crime_description'].value_counts().head(10).index

    sns.countplot(
        data=df, 
        x='crime_description', 
        order=order,
        ax=ax,
        hue="crime_description"
    )

    plt.title('Frequency of Crimes by Crime Desc.')
    plt.xlabel('Crime Description')
    plt.ylabel('Amount')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=7)

    st.pyplot(fig)