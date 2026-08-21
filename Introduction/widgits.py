import streamlit as st

st.title("Coffee Maker App")
st.subheader("Choose what you want")

cream = st.checkbox("Cream")
sugar = st.checkbox("Sugar")
choco = st.checkbox("Chocolate")

st.write(sugar, choco)
if st.button("Make Coffee"):
    st.write(f"Added {cream}")
    st.write("Coffee is ready")
    st.success("bon appétit !")


