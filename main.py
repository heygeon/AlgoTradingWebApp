import lib as l
import streamlit as st

stock = l.Stock("aapl", "max")

st.title("Algo Trading Web App")
st.write(stock.price)