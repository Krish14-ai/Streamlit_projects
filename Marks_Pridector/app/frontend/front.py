import streamlit as st
import numpy as np
st.title("Welcome to the Placement Predictor")

name = st.text_input("Enter Your name : ")
age = st.number_input("Please Enter your Age : ")
marks = st.number_input("Enter your marks : ")
internals = st.number_input("Enter your Internal Marks : ")
papers = st.number_input("Total Research Papers published : ")
projects = st.number_input("Total no of Projects submitted : ")

if st.button("Submit"):
    l = np.array([age,marks,internals,papers,projects])
    st.success(f"{l}")