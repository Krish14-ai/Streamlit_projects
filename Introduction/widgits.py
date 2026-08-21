import streamlit as st

st.title("Coffee Maker App")
st.subheader("Choose what you want")

st.write("What kind of Coffee you want")

type = st.radio("Choose what you want",["Espresso","Black","Latte","Cappuccino","Custom"])

if type == "Custom":

    milk = st.checkbox("Milk")
    cream = st.checkbox("Cream")
    sugar = st.checkbox("Sugar")
    choco = st.checkbox("Choco Powder")


    if st.button("Make Coffee"):
        if milk :
            st.write("Added Milk")
        if cream :
            st.write("Added Cream")
        if sugar :
            st.write("Added Sugar")
        if choco :
            st.write("Added Chocolate")

        st.write("Coffee is ready")
        st.success("bon appétit !")


