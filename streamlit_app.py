# Code snippets from https://github.com/janrswong/testingthesis

import streamlit as st
import yfinance as yf

st.title('🎈 yfinance app')

def getInterval(argument):
    switcher = {
        "W": "1wk",
        "M": "1mo",
        "Q": "3mo",
        "D": "1d"
    }
    return switcher.get(argument)

interv = st.select_slider('Select Time Series Data Interval for Prediction', options=[
                          'Weekly', 'Monthly', 'Quarterly', 'Daily'])

df = yf.download('BZ=F', interval=getInterval(interv[0]))

st.info(getInterval(interv[0]))
st.warning(df.shape)
st.write(df)

st.subheader('Test')

df2 = yf.download('BZ=F', interval='1d')
st.info('1d')
st.warning(df2.shape)
st.write(df2)
