import streamlit as st
import time

st.title("Bevrege Maker App")
st.subheader("Choose what you want")

bev = st.selectbox("Select what you want to drink",["Chai", "Coffee"])

##-------------------------------## Coffee ##--------------------------------------
if bev == "Coffee" :

    st.write("What kind of Coffee you want")

    coffee_type = st.radio("Choose what you want",["Espresso","Black","Latte","Cappuccino","Custom"])

    if coffee_type == "Custom":

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
            st.success("Bon Appétit !")

    else : 
        st.write(f"Your {coffee_type} is ready")
        time.time.sleep(2)
        st.success("Bon Appétit")

##-------------------------------## Chai ##--------------------------------------
if bev == "Chai" :

    st.write("What kind of Chai you want")

    chai_type = st.