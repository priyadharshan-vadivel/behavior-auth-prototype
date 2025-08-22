import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# ===============================
# 🔹 Load Training Data
# ===============================
df = pd.read_csv("behavior.csv")
X = df[["keystroke_latency_mean", "swipe_speed_mean", "login_hour", "device_change_flag"]]

# Train anomaly detection model on genuine data
clf = IsolationForest(contamination=0.3, random_state=42)
clf.fit(X[df["label"] == "Genuine"])

# ===============================
# 🔹 Decision Engine
# ===============================
def decision_engine(score):
    if score > 0.2:
        return "✅ Access Granted"
    elif score > -0.2:
        return "🔒 Challenge User"
    else:
        return "🚫 Block Access"

# ===============================
# 🔹 Streamlit App Layout
# ===============================
st.set_page_config(page_title="Behavior-Based Authentication", page_icon="🛡️", layout="centered")

st.title("Behavior-Based Authentication Prototype")
st.markdown("### Hackathon Demo – Detect Fraudulent Banking Logins")
st.write("Enter simulated user behavior below to test the system:")

# User inputs
col1, col2 = st.columns(2)
with col1:
    keystroke = st.number_input("⌨️ Keystroke Latency (ms)", min_value=100, max_value=1000, value=220)
    hour = st.slider("🕒 Login Hour (0-23)", 0, 23, 14)
with col2:
    swipe = st.number_input("📱 Swipe Speed (px/sec)", min_value=100, max_value=1500, value=950)
    device_flag = st.selectbox("💻 New Device?", [0, 1])

# Track login history
if "history" not in st.session_state:
    st.session_state.history = []

# Authentication button
if st.button("🔑 Authenticate"):
    user_input = [[keystroke, swipe, hour, device_flag]]
    score = clf.decision_function(user_input)[0]
    prediction = clf.predict(user_input)[0]
    prediction = "Genuine" if prediction == 1 else "Fraud"
    decision = decision_engine(score)

    # Save to history
    st.session_state.history.append({
        "keystroke": keystroke,
        "swipe": swipe,
        "hour": hour,
        "device_flag": device_flag,
        "prediction": prediction,
        "decision": decision,
        "score": round(score, 3)
    })

    # Show result
    st.subheader("🔎 Authentication Result")
    st.write(f"**Prediction:** {prediction}")
    st.write(f"**Decision:** {decision}")
    st.progress(min(max((score + 1) / 2, 0.0), 1.0))  # visual confidence bar

# ===============================
# 🔹 History Log
# ===============================
if st.session_state.history:
    st.subheader("📜 Login Attempts History")
    st.dataframe(st.session_state.history)

# ===============================
# 🔹 Visualization
# ===============================
if st.checkbox("📊 Show Training Data"):
    st.dataframe(df)

if st.checkbox("📈 Show Anomaly Scores (Training Data)"):
    scores = clf.decision_function(X)
    plt.figure(figsize=(6,3))
    plt.plot(scores, marker="o", linestyle="--")
    plt.axhline(0, color="red", linestyle="--", label="Fraud Threshold")
    plt.title("Anomaly Scores (Red line = fraud threshold)")
    plt.xlabel("Session Index")
    plt.ylabel("Score")
    plt.legend()
    st.pyplot(plt)

# ===============================
# 🔹 Footer
# ===============================
st.markdown("---")
st.markdown("👨‍💻 Developed for Hackathon Demo | **Behavior-Based Authentication System**")
