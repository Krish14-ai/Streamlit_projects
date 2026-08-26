import streamlit as st

st.title("Welcome to the Placement Predictor")

name = st.text_input("Enter Your name : ")
age = st.number_input("Please Enter your Age : ")
marks = st.number_input("Enter your marks : ")
internals = st.number_input("Enter your Internal Marks : ")
papers = st.number_input("Total Research Papers published : ")
projects = st.number_input("Total no of Projects submitted : ")