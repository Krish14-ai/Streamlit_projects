import streamlit as st 
import pandas as pd 


st.title("Welcome")

file = st.file_uploader("Upload your CSV file ", type = ["CSV"])

if file : 
    df  = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file : 
    st.subheader("Summary  Status")
    st.write(df.describe())

if file:
    cities = df['city'].unique()
    selected_city = st.selectbox("Filter by Cities", cities)
    filterd_cities = df[df["city"] == selected_city]
    st.dataframe(filterd_cities)