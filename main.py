import lib as l
import matplotlib.pyplot as plt
import streamlit as st
import datetime as dt
from idea import *

st.title("Algo Trading Web App (Idea Version)")
tmr = dt.date.today()+dt.timedelta(days=1)

start_date = st.date_input("Starting Date")
end_date = st.date_input("Ending Date (Date of tmr for latest data)", value=tmr)
code = st.text_input("Stock Code:")
#sma = st.slider("Select SMA", min_value=5, max_value=100)

stock = l.Stock(code, start=start_date, end=end_date)
if st.button("Enter"):


    st.pyplot(idea(stock))