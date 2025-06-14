import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title('Hello Streamlit')

## Command to run 
## streamlit run app.py

## Display a simple text
## Writing in the page of the web app created with the help of streamlit
st.write('This is a simple text')

## Create a simple dataframe
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column' : [10,20,30,40]
})

## Display the dataframe
st.write("Here is the dataframe")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.random((20,3)), #20 rows, 3 columns
    columns = ['a','b','c']
)
st.line_chart(chart_data)