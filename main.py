import lib as l
import matplotlib.pyplot as plt
import streamlit as st
import datetime as dt

st.title("Algo Trading Web App")

start_date = st.date_input("Starting Date")
end_date = st.date_input("Ending Date")
code = st.text_input("Stock Code:")
sma = st.slider("Select SMA", min_value=5, max_value=100)

if st.button("Enter"):
    stock = l.Stock(stockName=code, start=start_date, end=end_date)

    stock.keyPointAlgo()
    stock.smaAlgo(sma)

    fig = plt.figure()

    plt.plot(stock.date, stock.keylist, label="Key", marker="^", color="red")
    plt.plot(stock.date, stock.buylist, label="Buy", marker="o", color="green")
    plt.plot(stock.date, stock.selllist, label="Sell", marker="o", color="red")
    plt.plot(stock.date, stock.price, label = stock.stockName)
    plt.plot(stock.date, stock.sma(30), label = "SMA30", color="purple")
    plt.plot(stock.date, stock.sma(50), label = "SMA50", color="orange")
    plt.plot(stock.date, stock.sma(20), label= "SMA20", color="blue")
    plt.title(stock.stockName.upper())
    plt.xlabel("Day")
    plt.ylabel("Adj Close Price USD($)")
    plt.legend(loc="upper left")

    st.pyplot(fig)