import streamlit as st
import pickle
from all_topics import display_compaign_topics


st.set_page_config(
    page_title="Topic Insights",
    page_icon="👁️‍🗨️",
)
st.title("Topic Insights")

tab1 = st.tabs(["Resultant topics for baby food"])

with tab1:
    display_compaign_topics()


