import streamlit as st
import numpy as np

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.predictor import train


st.title("Welcome to the Placement Predictor")

name = st.text_input("Enter Your name : ")
age = st.number_input("Please Enter your Age : ", min_value=18, max_value=99, step = 1)
marks = st.number_input("Enter your marks : ",min_value=0, max_value=99, step = 1)
internals = st.number_input("Enter your Internal Marks : ",min_value=0, max_value=30, step = 1)
papers = st.number_input("Total Research Papers published : ",min_value=0, max_value=99, step = 1)
projects = st.number_input("Total no of Projects submitted : ",min_value=0, max_value=10, step = 1)

if st.button("Submit"):
    l = np.array([age,marks,internals,papers,projects])
    pred = train(l)

    if pred ==[1]:
        st.success("You will be Placed 🥳")

    else: 
        st.error("Sorry! You will not be placed, But better luck next time ☺️")