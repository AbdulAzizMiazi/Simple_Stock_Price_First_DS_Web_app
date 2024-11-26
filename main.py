import yfinance as yf
import streamlit as st
import pandas as pd

# Fatching Data from yfinance for Apple
tickerSymbol = "AAPL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# Showcasing the data in the webapp using Streamlit
st.write("""
# Simple Stock Price App        
Shown are the **closing price** and ***valume*** of Apple!
""")

st.write("""### Closing Price""")

st.line_chart(tickerDf.Close)

st.write("""### Volume Price""")

st.line_chart(tickerDf.Volume)