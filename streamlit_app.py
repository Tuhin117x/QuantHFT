import streamlit as st
import pandas as pd
from datetime import datetime
from momentum_strategy_1_api import *
from api.momentum_2 import *

st.sidebar.image("logo.jpg")

st.sidebar.write('--------------')

strategies=['Momentum Strategy - Type 1','Momentum Strategy - Type 2']
# Add a selectbox to the sidebar:
strategy_selectbox_side = st.sidebar.selectbox('Select your Quant Strategy', (strategies))
df1=momentum_strategy_1('2024-11-21')
df2=strategy()
st.dataframe(df2)
st.write("Data Refresh Date: "+datetime.today().strftime('%Y-%m-%d'))
'Below are the stock recommendations for ', strategy_selectbox_side
st.dataframe(df1,hide_index=True,
    column_config=dict(
      R1Y_return=st.column_config.NumberColumn('R1Y Return', format='%.2f %%'),
      R6M_return=st.column_config.NumberColumn('R6M Return', format='%.2f %%'),
      R3M_return=st.column_config.NumberColumn('R3M Return', format='%.2f %%'),
      R1M_return=st.column_config.NumberColumn('R1M Return', format='%.2f %%'),
      Momentum_Score=st.column_config.NumberColumn('Momentum Score', format='%.2f')
      )

    )



