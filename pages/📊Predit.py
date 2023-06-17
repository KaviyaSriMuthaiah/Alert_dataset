import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

align="""
<style>
    [data-testid="stMarkdownContainer"]{
        background-color: rgba(0,0,0,0);
        text-align: center;
    }

</style>
"""
st.markdown(align,unsafe_allow_html=True)
st.title("Predict Your Result")
col1,col2=st.columns([6,6])

@st.cache_data
def load_data():
    df=pd.read_csv("Alert_dataset/Preprocess_data.csv")
    return df

df=load_data()

Status={"Open":1,"In Progress":2,"Resolved":3}
Department={"Applications":1,"IT":2,"Infrastructure":3,"Security":4}
Location={"Office":1,"Server Room":2,"Data Center":3}
category={'Application': 0, 'Application Issue': 1, 'Performance Issue': 2, 'Infrastructure': 3, 'Performance': 4, 'Network Issue': 5, 'Network': 6, 'Maintenance': 7, 'Infrastructure Issue': 8, 'Hardware': 9, 'Security Breach': 10, 'Data': 11, 'Security': 12, 'Data Issue': 13, 'Configuration Issue': 14, 'Safety Issue': 15, 'Security Issue': 16, 'Configuration': 17, 'Bug Report': 18, 'Hardware Issue': 19, 'Request': 20, 'Integration Issue': 21, 'User Interface Issue': 22, 'Permission Issue': 23, 'Storage Issue': 24, 'Feature Request': 25, 'Licensing Issue': 26, 'Installation Issue': 27, 'User Account Issue': 28}

with col1:
    f1=st.selectbox("Select status of alert",options=Status.keys())
    f2=st.selectbox("Select the Department",options=Department.keys())
with col2:
    f3=st.selectbox("Select the Location",options=Location.keys())
    f4=st.selectbox("Select the Category",options=category.keys())

st.markdown("""___""")

@st.cache_resource(show_spinner="Loadig model...")
def load_model():
    # Load the model from the pkl file
    with open('pages/model (4).pkl', 'rb') as file:
        loaded_model = pickle.load(file)
        return loaded_model
model=load_model()


class_={0:"Application",1:"Performance",2:"Infrastructure",3:"Network",4:"Hardware",5:"Security",6:"Data",7:"Configuration"}


def predict():
    p1,p2,p3=st.columns([3.35,0.9,3])
    result=""
    with p2:
        click=st.button("Predict")
        if click:
            features=[[Status[f1],Department[f2],Location[f3],category[f4]]]
            result=model.predict(features)
            return int(result)

def predict1():
    prediction = predict()
    if prediction is not None:
        if prediction in class_:
            st.success(f" The Alert is related to {class_[prediction]}",icon="✅")
        else:
            st.write("Invalid prediction key")
    else:
        st.write("")
predict1()
