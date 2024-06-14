import langchain_helper as lch
import streamlit as st

st.title("Pet Names Generator")

animal_type = st.sidebar.selectbox("What kind of animal is your pet?", ("Cat", "Dog", "Rabbit", "Bird", "Hamster", "Mouse", "Horse"))
color = st.sidebar.text_area("What color is your pet?", max_chars=15)
size = st.sidebar.selectbox("How big is your pet?", ("Tiny", "Small", "Average-sized", "Fat", "Thin", "Large", "Huge"))
number = st.sidebar.number_input("How many names do you want to generate?", max_value=20, min_value=3)

button = st.sidebar.button("Submit")

if button:
    response = lch.generate_pet_names(animal_type, color, size, number)
    st.text(response)

