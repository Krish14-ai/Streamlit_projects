import streamlit as st

st.title("Hello World")
st.subheader("I am Krish")
st.text("Welcome to my first app!")

food = st.selectbox("What is your fav Food ", ["Pizza","Burger","Pasta","Salad"])
st.write("Well my Fav Food is Everthing :)")

st.write(f"Well i like {food} too :)")

st.success("Thank you for choosing :) ")