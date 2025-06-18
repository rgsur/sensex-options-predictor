import streamlit as st
import matplotlib.pyplot as plt
from predictor import get_data, generate_signal
from backtest import backtest

st.set_page_config(page_title="Sensex Options Predictor", layout="wide")

st.title("📈 Sensex Options Trading Predictor")
st.markdown("Real-time predictor with RSI + EMA. Updated every 15 minutes.")

# Fetch Data
df = get_data()
signal, latest = generate_signal(df)

try:
    df = get_data()
    signal, latest = generate_signal(df)
except Exception as e:
    st.error(f"Failed to load data or calculate indicators.\n\n{e}")
    st.stop()

# Live Signal
st.subheader("📊 Current Signal")
st.success(signal)
st.write("Latest Close:", round(latest['Close'], 2))
st.write("RSI:", round(latest['RSI'], 2))
st.write("EMA20:", round(latest['EMA20'], 2))

# Chart
st.subheader("📉 Price Chart with EMA20")
fig, ax = plt.subplots(figsize=(12, 5))
df['Close'].plot(ax=ax, label="Close")
df['EMA20'].plot(ax=ax, label="EMA20", color='orange')
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)

# Backtest Results
st.subheader("🧪 Backtest (Last 60 Days)")
results = backtest(df)
for action, time, price in results[-5:]:
    st.write(f"{time} → {action} @ {round(price, 2)}")

# Auto Refresh every 15 minutes
st.experimental_rerun()  # Add timer in deployment to trigger rerun
