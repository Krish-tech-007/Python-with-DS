import streamlit as st
import pandas as pd
## Interactive application

st.title("Streamlit Text Input")
name = st.text_input("Enter your name: ")

## Slider
age = st.slider("Select your age",0,100,25) #0 to 100, default 25
st.write(f"Your age is {age}")

## Select box - Drop down box
options = ['Python','C','C++','Java']
choice = st.selectbox("Choose your preferred programming language", options)
st.write("You have selected", choice)

if name:
    st.write(f"Hello {name}")

data = {
    "Name":["Krish","Anant","Titas"],
    "Age":[19,19,21],
    "City":['Kolkata','Howrah','Kharagpur']
}
df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)