import streamlit as st
import time
import pandas as pd
import plotly.graph_objects as go
from predictor import get_data, generate_latest_signal

st.set_page_config(layout="wide")
st.title("📈 Sensex Options Price Movement Predictor (5-min)")

# Countdown timer
COUNTDOWN_TIME = 300  # 5 minutes
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

elapsed = time.time() - st.session_state.start_time
remaining = max(0, COUNTDOWN_TIME - int(elapsed))
minutes, seconds = divmod(remaining, 60)
st.sidebar.markdown(f"⏳ Next signal in: `{minutes:02d}:{seconds:02d}`")

# Refresh button
if st.sidebar.button("🔄 Refresh Now"):
    st.session_state.start_time = time.time()
    st.experimental_rerun()

# Load and process data
df = get_data()
latest_signal, latest = generate_latest_signal(df)

# Display latest signal
signal_colors = {
    "Buy Call": "green",
    "Sell Call": "red",
    "Buy Put": "blue",
    "Sell Put": "orange",
    "Hold": "gray"
}

st.metric(label="📌 Signal", value=latest_signal, delta_color="off")

st.markdown(
    f"""
    **Price:** ₹{latest['Close']:.2f}  
    **RSI:** {latest['RSI']:.2f}  
    **EMA20:** ₹{latest['EMA20']:.2f}  
    **MACD:** {latest['MACD']:.2f}  
    **MACD Signal:** {latest['MACD_signal']:.2f}  
    """
)

# Display chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close', line=dict(color='white')))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA20'], mode='lines', name='EMA20', line=dict(color='yellow')))

# Add markers
signal_colors_plot = {
    "Buy Call": "green",
    "Sell Call": "red",
    "Buy Put": "blue",
    "Sell Put": "orange"
}

for signal_type, color in signal_colors_plot.items():
    signal_data = df[df['Signal'] == signal_type]
    fig.add_trace(go.Scatter(
        x=signal_data.index,
        y=signal_data['Close'],
        mode='markers',
        name=signal_type,
        marker=dict(size=10, color=color, symbol='circle')
    ))

fig.update_layout(title="Sensex Price Chart with Signals", template="plotly_dark", height=500)
st.plotly_chart(fig, use_container_width=True)

# Table of last few signals
st.subheader("📊 Last 10 Signals")
st.dataframe(df
