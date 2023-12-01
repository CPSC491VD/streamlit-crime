import streamlit as st
from utils import init_connection

if 'conn' not in st.session_state:
    st.session_state['conn'] = init_connection()

st.title("Chicago Crime Data Bubble Map :bar_chart:")
st.subheader("Each recent crime committed in the city of Chicago, plotted and color-coded")

markdown =  """
<iframe width="100%" height="600px" src="https://lookerstudio.google.com/embed/reporting/1b08c3ee-c01d-4535-939c-67afc990f1a9/page/051hD/?embed=true" frameborder="0" style="border:0" allowfullscreen></iframe>
"""

st.markdown(
    markdown,
    unsafe_allow_html=True
)