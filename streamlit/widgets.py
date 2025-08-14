import streamlit as st
import pandas as pd 
import numpy as np
st.title("Streamlit Text Input")

name = st.text_input("Enter your Name:")

age = st.slider("Select your Age:",0,100,25)
st.write(f"Your Age is {age}")

options = ["Mercedes Benz","Morris garages","Toyota","Honda","Ather"]
choice = st.selectbox("Choose your favourite brand:",options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")


data = {
    'name':["Prathmesh","Sujal","Ved","Arya","Sanjay","Uday"],
    'Age':[22,21,25,67,8,1],
    'City':["New York","Paris","Los Angeles","Hyderabad","Pune","Alandi"]
}

df = pd.DataFrame(data)
df.to_csv("Sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)