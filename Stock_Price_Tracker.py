import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""# Online Stock Price Tracker""")

# Define the ticker symbol
tickerSymbol = "WSM"

# Retrieve the data
tickerData = yf.Ticker(tickerSymbol)

# Get the historical price data
tickerDf = tickerData.history(period='id', start='2019-1-1', end='2023-03-1')

# Get the balance sheet and income statement data
balance_sheet = tickerData.balance_sheet
income_statement = tickerData.financials

# Display the balance sheet and income statement data
st.write("""## Balance Sheet""")
st.write(balance_sheet)

st.write("""## Income Statement""")
st.write(income_statement)

# Display the price and volume data
st.write("""## Price Data""")
st.line_chart(tickerDf.Close)

st.write("""## Volume Data""")
st.line_chart(tickerDf.Volume)
