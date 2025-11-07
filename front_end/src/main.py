import pandas as pd
import requests as req
import streamlit as st

st.write("Hello World")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

def get_items():
    return req.get(
        url="http://localhost:8000/items/50"
    ).content

st.write(get_items())
