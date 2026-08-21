import streamlit as st
import time

st.title("Bevrege Maker App")
st.subheader("Choose what Makes you Happy :)")

name = st.text_input("Enter your name : ")

if name:

    st.write(f"Welcome {name}")
    
    bev = st.selectbox("Select what you want to drink",["Chai", "Coffee"])

    ##-------------------------------## Coffee ##--------------------------------------
    if bev == "Coffee" :

        st.write("What kind of Coffee you want")

        coffee_type = st.radio("Choose what you want",["Espresso","Black","Latte","Cappuccino","Custom"])

        if coffee_type == "Custom":

            ## Check boxes
            milk = st.checkbox("Milk")
            cream = st.checkbox("Cream")
            sugar = st.checkbox("Sugar")
            choco = st.checkbox("Choco Powder")

            if sugar:
                sug_cubes= st.slider("Amount of Sugar Cubes you prefer", 0,5,2)
            
            ## Buttons
            if st.button("Brew Coffee"):
                if milk :
                    st.write("Added Milk")
                if cream :
                    st.write("Added Cream")
                if sugar :
                    st.write(f"Added {sug_cubes} cubes of Sugar")
                if choco :
                    st.write("Added Chocolate")

                st.write("Coffee is ready")
                st.success("Bon Appétit !")

        else : 
            if st.button("Brew Coffee"):
                st.write(f"Your {coffee_type} is ready")
                st.success("Bon Appétit")

    ##-------------------------------## Chai ##--------------------------------------
    if bev == "Chai" :

        st.write("What kind of Chai you want")

        chai_type = st.radio("Choose what tea you want",["Normal Tea", "Ginger", "Green","Macha","Rose","Masala","Tulsi","Custom"])

        cups = st.number_input("How many cups of Chai you want",1,10,1)

        if chai_type != "Custom":
            if st.button("Brew Tea"):
                st.write(f"Your {cups} cups of {chai_type} tea are Ready!")
                st.success("Bon Appétit")

        

        if chai_type == "Custom":
            sugar = st.checkbox("Sugar")
            Ginger = st.checkbox("Ginger")
            Masala = st.checkbox("Masala")
            Milk  =  st.checkbox("Milk")

            if sugar :
                sug_cubes = st.slider("Amount of Sugar Cubes you prefer", 0,5,2)

            if st.button("Brew Chai"):
                if sugar:
                    st.write(f"Added {sug_cubes} Cubes of Sugar")
                if Ginger:
                    st.write("Added Ginger")
                if Milk :
                    st.write("Added Milk")
                if Masala : 
                    st.write("Added Masala")
        
                st.write(f"Your {cups} cups of Chai are Ready!")
                st.success("Bon Appétit")
    



