import streamlit as st

st.markdown("# Main page test")
st.sidebar.markdown("# Sidebar main test")
if st.checkbox("Show text"):
    st.write("Hidden text")
