import lib as l
import matplotlib.pyplot as plt
import streamlit as st
import datetime as dt
from idea import *
from PIL import Image

col1, col2, col3 = st.beta_columns(3)

with col1:
    image = Image.open("IDEAT Logo 50%.png")
    st.image(image)
with col2:
    st.title("")
    st.title("Algo Trading Web App")

tmr = dt.date.today()+dt.timedelta(days=1)

with st.beta_container():
    start_date = st.date_input("Starting Date:")
    end_date = st.date_input("Ending Date (Date of tmr for latest data):", value=tmr)
    col_market, col_code = st.beta_columns(2)
    with col_market:
        market = st.selectbox("Market:", options=["US", "HK"])
    with col_code:
        code = st.text_input("Stock Code:")
    #sma = st.slider("Select SMA", min_value=5, max_value=100)

if market == "HK":
    while len(code) < 4:
        code = "0"+code
    code += ".hk"

stock = l.Stock(code, start=start_date, end=end_date)
if st.button("Enter"):


    st.pyplot(idea(stock))