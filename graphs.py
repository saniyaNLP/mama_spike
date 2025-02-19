import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


def plot_graphs():
    time_series_df = st.session_state['count_data']
    print(time_series_df)

    time_series_df['Name'] = time_series_df['Name'].apply(lambda x: x.split("_")[-1])



    tab1, tab2 = st.tabs(["Time Series", "Topics"])
    with tab1:
        st.subheader('Time Series')
        all_possible_topics = time_series_df['Name'].unique()

        all_topics = ['All'] + list(all_possible_topics)
        selected_topic = st.selectbox('Select a topic:', all_topics)

        # Filter the dataframe based on the selected product
        if selected_topic == 'All':
            filtered_df = time_series_df
        else:
            filtered_df = time_series_df[time_series_df['Name']==selected_topic]
            print(filtered_df)


        fig, ax = plt.subplots(figsize=(10, 6))

        if selected_topic == 'All':
            fig = px.line(time_series_df, x='date', y='Document', color='Name', title="AVERAGE "
                                                                                        "count for "
                                                                                           f"All Topics",
                          )
        else:
            fig = px.line(filtered_df, x='date', y='Document', title=f"AVERAGE  "
                                                                                   f"for topic"
                                                                  f" {selected_topic}",
                          )

        fig.update_layout(showlegend=False)

        st.plotly_chart(fig)

