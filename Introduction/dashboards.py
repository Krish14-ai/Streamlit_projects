import streamlit as st 

st.title("Welcome")

col1, col2= st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Ginger Chai")
    vote2 = st.button("Vote Ginger Chai")

if col1.button("Vote Masala Chai"):
    st.write("You voted for Masala Chai")

if col2.button("Vote Ginger Chai"):
    st.write("You voted for Ginger Chai")