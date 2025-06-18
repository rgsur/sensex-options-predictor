import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from predictor import get_data, generate_signal

st.set_page_config(page_title="Sensex Options Signal App", layout="wide")

st.title("📈 Sensex Options Price Movement Predictor")
st.markdown("Get live Buy/Sell/Hold signals based on EMA, RSI, MACD, and ATR volatility filter.")

try:
    df = get_data()
    signal, reason = generate_signal(df)
    latest = df.iloc[-1]

    # Color logic
    color_map = {
        "Buy Call": "green",
        "Buy Put": "blue",
        "Sell Call": "red",
        "Sell Put": "orange",
        "Hold": "gray"
    }
    st.subheader(f"💡 Signal: **:{color_map.get(signal, 'gray')}[{signal}]**")
    st.caption(f"Reason: {reason}")
    st.caption(f"Last Updated: {latest.name.strftime('%Y-%m-%d %H:%M:%S')}")

    # Chart
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name="Price"
    ))

    fig.add_trace(go.Scatter(
        x=df.index, y=df['EMA20'], mode='lines', name='EMA20', line=dict(color='blue')
    ))
    fig.add_trace(go.Scatter(
        x=df.index, y=df['MACD'], name='MACD', line=dict(color='green', dash='dot')
    ))
    fig.add_trace(go.Scatter(
        x=df.index, y=df['MACD_signal'], name='MACD Signal', line=dict(color='red', dash='dot')
    ))

    fig.update_layout(title="Sensex 5-min Chart with Indicators", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"⚠️ Could not load data: {e}")
