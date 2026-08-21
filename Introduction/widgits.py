import streamlit as st

st.title("Coffee Maker App")
st.subheader("Choose what you want")

cream = st.checkbox("Cream")
sugar = st.checkbox("Sugar")
choco = st.checkbox("Chocolate")


if st.button("Make Coffee"):
    if cream :
        st.write("Added Cream")
    if sugar :
        st.write("Added Sugar")
    if choco :
        st.write("Added Choco")

    st.write("Coffee is ready")
    st.success("bon appétit !")


