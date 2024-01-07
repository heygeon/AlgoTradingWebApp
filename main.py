import lib as l
import matplotlib.pyplot as plt
import streamlit as st
import datetime as dt
from idea import *
from PIL import Image

col1, col2, col3 = st.beta_columns(3)
st.write("hi")
with col1:
    image = Image.open("IDEAT Logo 50%.png")
    st.image(image)
with col2:
    st.title("")
    st.title("Algo Trading Web App")

tmr = dt.date.today()+dt.timedelta(days=1)

with st.beta_container():
    period = st.select_slider("Period:", options=["5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"])
    col_market, col_code = st.beta_columns(2)
    with col_market:
        market = st.selectbox("Market:", options=["HK", "US"])
    with col_code:
        code = st.text_input("Stock Code:")
    #sma = st.slider("Select SMA", min_value=5, max_value=100)

if market == "HK":
    while len(code) < 4:
        code = "0"+code
    code += ".hk"

stock = l.Stock(code, period=period)
if st.button("Enter"):


    st.pyplot(idea(stock))