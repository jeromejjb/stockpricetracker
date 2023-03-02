import streamlit as st 
import yfinance as yf 
import pandas as pandas 

st.write(""" # Online Stock Price Tracker""")


tickerSymbol = "WSM"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2019-1-1', end='2023-03-1')

st.write("""Data for William Sonoma INC price over Time period 1/1/2019-3/1/2023 """)                                                    
st.line_chart(tickerDf.Close)

st.write(""" WSM Trading volume over the time period of  1/1/2019-3/1/2023""" )
st.line_chart(tickerDf.Volume)

st.title(""" This is a Jerome J Brown Production""")