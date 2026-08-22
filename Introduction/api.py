import streamlit as st
import requests 

st.title("Live Currency Coverter")
amount= st.number_input("Enter the amount in INR", min_value  = 1)

target_currency = st.selectbox("Convert to : ", ["USD", "EUR", "GBP"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        rate = data["rates"][target_currency]
        converted_val = rate* amount

        st.success(f"{amount}/- INR = {converted_val:.2f}{target_currency}")
        
    else:
        st.error("Failed to Fetch Conversion Rate")

