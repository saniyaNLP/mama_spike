import streamlit as st
import os
import pandas as pd
from download_data import DownloadData
from graphs import plot_graphs

os.environ["TOKENIZERS_PARALLELISM"] = "false"

def display_compaign_topics():
    @st.cache_data
    def load_data():
        object_file = download_data_obj.download_pickle()
        return object_file

    download_data_obj = DownloadData()
    if "raw_data" not in st.session_state.keys():
        raw_data = load_data()
        st.session_state['topics_df'] = raw_data
    if "count_data" not in st.session_state.keys():
        count_df = download_data_obj.download_csv("s3://gumgum-research-sx/sn-models/category_entry_points/niche_anomaly/mama_spike/high_level_count.csv")
        st.session_state['count_data'] = count_df


    valid_topics = [kp for kp in st.session_state['topics_df'] if 'NO link found' not in kp['reasoning']]



    final_df = pd.DataFrame(valid_topics)

    #
    # st.session_state['topics_df'] = st.session_state['topics_df'].sort_values(by = ['Topic']).reset_index(drop=True)
    st.dataframe(final_df[['topic_name', 'reasoning']])
    plot_graphs()





