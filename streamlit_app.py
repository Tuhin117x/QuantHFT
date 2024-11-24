import streamlit as st
import pandas as pd
from datetime import datetime

st.sidebar.image("logo.jpg")

st.sidebar.write('--------------')

strategies=['Momentum Strategy - Type 1','Momentum Strategy - Type 2']
# Add a selectbox to the sidebar:
strategy_selectbox_side = st.sidebar.selectbox('Select your Quant Strategy', (strategies))




