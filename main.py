import lib as l
import matplotlib.pyplot as plt
import streamlit as st


st.title("Algo Trading Web App")
code = st.text_input("Stock Code:")
stock = l.Stock(code, "max")

st.line_chart(stock.price)