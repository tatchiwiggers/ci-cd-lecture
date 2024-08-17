import streamlit as st

from api.fast import root

st.write(root())

st.write('Welcome batch 1643')
st.write('This is obviously very simple, in reality one would rather use this page to display API results more nicely! :)')
