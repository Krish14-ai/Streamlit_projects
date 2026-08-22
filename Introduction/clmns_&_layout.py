import streamlit as st 

st.title("Welcome")

col1, col2= st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://www.indianhealthyrecipes.com/wp-content/uploads/2023/05/indian-masala-chai-tea.webp", width = 200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Ginger Chai")
    st.image("https://i0.wp.com/dailyteatime.com/wp-content/uploads/2021/04/ginger-chai-12001800.jpg?resize=1024%2C1536&ssl=1", width = 200)
    vote2 = st.button("Vote Ginger Chai")

if vote1:
    st.write("You voted for Masala Chai")

if vote2:
    st.write("You voted for Ginger Chai")
    