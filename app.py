import streamlit as st
from predictor import get_data, generate_signal
from backtest import backtest
import time

st.set_page_config(page_title="Sensex Options Predictor", layout="wide")

st.title("📈 Sensex Options Price Movement Predictor (5-minute)")

df = get_data()
latest_signal, latest = generate_signal(df)

st.title("Sensex Options Price Movement Predictor - 5 Min")

st.metric(label="Signal", value=latest_signal)
st.dataframe(df[['Close', 'EMA20', 'RSI', 'Signal']].tail(10), height=250)

row = latest.iloc[0]

st.write(
    f"**Price:** ₹{row['Close'].values[0]:.2f} | "
    f"**RSI:** {row['RSI'].values[0]:.2f} | "
    f"**EMA20:** {row['EMA20'].values[0]:.2f}"
)

import streamlit as st
import time
from datetime import datetime

# Show last updated time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"🕒 **Last updated:** {now}")

# Refresh control
REFRESH_INTERVAL = 300  # 5 minutes
countdown = st.empty()

# Manual refresh button
if st.button("🔄 Refresh Now"):
    st.experimental_rerun()

# Countdown loop
for seconds_left in range(REFRESH_INTERVAL, 0, -1):
    mins, secs = divmod(seconds_left, 60)
    countdown.markdown(f"⏳ Auto-refresh in **{mins:02d}:{secs:02d}**", unsafe_allow_html=True)
    time.sleep(1)

# Auto rerun
st.experimental_rerun()
