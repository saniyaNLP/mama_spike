import pickle
import boto3
import pandas as pd
import streamlit as st

session = boto3.Session(
    aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
)

s3 = session.resource('s3')

AWS_STORAGE_OPTIONS = {"key": st.secrets["AWS_ACCESS_KEY_ID"],  "secret": st.secrets["AWS_SECRET_ACCESS_KEY"]}

s3_bucket = "gumgum-research-sx"

class DownloadData():
    def __init__(self):
        self.entity= 'coke'


    def download_pickle(self):
        s3_key=(f"sn-models/category_entry_points/niche_anomaly/mama_spike/high_level_final_result.pkl")
        file = pickle.loads(s3.Bucket(s3_bucket).Object(s3_key).get()['Body'].read())
        return file

    def download_csv(self, filepath):
        df = pd.read_csv(f"{filepath}", storage_options=AWS_STORAGE_OPTIONS)
        return df