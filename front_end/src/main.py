import pandas as pd
import streamlit as st

import utils

st.write("Hello World")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write(utils.fetch.get_items())
