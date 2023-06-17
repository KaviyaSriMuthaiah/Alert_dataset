import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Alert",page_icon="⚠",layout='wide')

st.title("Prediction of Alert Using Machine Learing")
st.info("The Random Forest model was trained on the Alert dataset to classify incidents based on their attributes. With an accuracy of **95.3 %**, the model demonstrates a high level of accuracy in predicting incident categories. The dataset contains information such as Incident ID, Timestamp, Title, Description, Category, Priority, Status, Location, Department, Duration, Response Time, Resolution Time, and Class. The Random Forest model effectively leverages the provided attributes to make accurate predictions and classify incidents into relevant categories.")

@st.cache_resource(show_spinner="loading...")
def load_lottie():
    r = requests.get("https://assets3.lottiefiles.com/packages/lf20_egfRcnjTx8.json")
    if r.status_code != 200:
        return None
    return r.json()

with st.sidebar:
    lottie_json = load_lottie()
    st_lottie = st_lottie(lottie_json,speed=1,reverse=False,loop=True,quality="high",height=400, width=300)

@st.cache_data(show_spinner="loading...")
def load_data():
    df=pd.read_csv("D:\VS Code\Pandas\Streamlit\Preprocess_data.csv")
    df=df.drop(columns='Unnamed: 0')
    return df 

df=load_data()
with st.expander("Click here"):
    st.dataframe(df)

