import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from predictor import get_data, generate_signal

st.set_page_config(page_title="Sensex Options Predictor", layout="wide")

st.title("📈 Sensex Options Price Movement Predictor")
st.markdown("Predicts **Buy Call**, **Sell Call**, **Buy Put**, **Sell Put**, or **Hold** based on EMA, RSI, and MACD indicators.")

try:
    df = get_data()
    signal = generate_signal(df)
    latest_price = df['Close'].iloc[-1]
    st.subheader(f"🔔 Latest Signal: **{signal}**")
    st.write(f"Latest Price: ₹{latest_price:.2f}")

    # Color coding signal
    signal_colors = {
        "Buy Call": "green",
        "Sell Call": "red",
        "Buy Put": "blue",
        "Sell Put": "orange",
        "Hold": "gray"
    }
    st.markdown(f"<h3 style='color:{signal_colors.get(signal, 'black')}'>{signal}</h3>", unsafe_allow_html=True)

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Datetime'], df['Close'], label='Close Price', color='black')
    ax.plot(df['Datetime'], df['EMA20'], label='EMA20', linestyle='--', color='blue')
    ax.set_title("Sensex Price with EMA20")
    ax.set_xlabel("Datetime")
    ax.set_ylabel("Price (₹)")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

except Exception as e:
    st.error(f"⚠️ Error: {e}")
    st.stop()
