import yfinance as yf
import lib as l
import streamlit as st

stock = l.Stock("aapl", "max")
print(stock.price)
st.title("Algo Trading Web App")