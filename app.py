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



# Optional: refresh every X seconds in deployment
# st.experimental_rerun()  # not needed unless auto refresh is desired
