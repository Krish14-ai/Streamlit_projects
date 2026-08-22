import streamlit as st
import requests 

st.title("Live Currency Coverter")

first_currency = st.selectbox("Convert From : ", ["INR", "USD", "EUR", "GBP"])
amount= st.number_input(f"Enter the amount in {first_currency}", min_value  = 1)

target_currency = st.selectbox("Convert to : ", ["USD", "EUR", "GBP"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/{first_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()


        rate = data["rates"][target_currency]
        converted_val = rate* amount

        st.success(f"{amount} {first_currency} = {converted_val:.2f} {target_currency}")
        
    else:
        st.error("Failed to Fetch Conversion Rate")

