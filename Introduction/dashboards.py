import streamlit as st 

st.title("Welcome")

col1, col2= st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Ginger Chai")
    vote2 = st.button("Vote Ginger Chai")

