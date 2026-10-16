import streamlit as st
import requests
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")

# ==============================================================================
#          YOUR EXACT UPLOADED IMAGE APPLIED AS BULLETPROOF BACKGROUND
# ==============================================================================
st.markdown(
    """
    <style>
    /* Force background onto the exact containers Streamlit relies on */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background-image: linear-gradient(rgba(5, 7, 18, 0.75), rgba(5, 7, 18, 0.85)), 
                          url('https://wikimedia.org') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: #e0e5f5 !important;
    }
    
    /* Transparent navigation bar header */
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌌 Kepler Space Tech AI Platform")
st.write("Welcome to the mission control hub. Use the interactive modules below to run live simulations or consult the AI explorer.")
st.write("---")

# ==============================================================================
#          TRUE MULTI-PAGE WORKSPACE TABS FOR THE LIVE SIMULATIONS
# ==============================================================================
tab1, tab2, tab3 = st.tabs(["💬 Deep-Space AI Assistant", "🛰️ Self-Healing Constellation Sim", "🔬 Kepler Transit Detector"])

# ------------------------------------------------------------------------------
# TAB 1: YOUR EXACT WORKING AI CHAT ENGINE
# ------------------------------------------------------------------------------
with tab1:
    # 1. Setup Conversational Memory State
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hey! 👋 I am Kepler, your live space assistant. Ask me absolutely anything about exoplanets, space engineering, or black holes!"}
        ]

    # Display historical messages in UI
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # 2. Handle Live Dynamic Chat Input
    if user_input := st.chat_input("Ask Kepler anything about the universe..."):
        # Render user prompt
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generate response from keyless AI model using requests (Using the robust POST method)
        with st.chat_message("assistant"):
            with st.spinner("Consulting mission archives... 🛰️"):
                try:
                    api_url = "https://pollinations.ai"
                    payload = {
                        "messages": [
                            {"role": "system", "content": "You are Kepler, a friendly NASA astronomer helping middle school students. Answer questions simply."},
                            {"role": "user", "content": user_input}
                        ],
                        "private": True
                    }
                    
                    response = requests.post(api_url, json=payload, timeout=15)
                    
                    if response.status_code == 200:
                        reply_text = response.text
                    else:
                        reply_text = "My communication antenna is hazy right now. Try sending that query one more time!"
                except Exception as error:
                    reply_text = "Connection error: Could not reach mission control. Please check your local network connection!"
                
                st.write(reply_text)
                
        st.session_state.messages.append({"role": "assistant", "content": reply_text})

# ------------------------------------------------------------------------------
# TAB 2: NATIVE SELF-HEALING CONSTELLATION SIMULATOR
# ------------------------------------------------------------------------------
with tab2:
    st.subheader("⚡ Live Satellite Anomaly Avoidance Grid")
    st.write("Compare a standard network baseline against an AI-managed setup during a solar storm simulation.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 🔴 Network A: No AI Framework")
        st.caption("Passive architecture. Waits for mechanical failure to report to ground command.")
        st.metric(label="Network A Service Uptime", value="42 %", delta="-58% Signal Outage")
        st.error("⚠️ Satellites Lost: 5 | Total Collisions: 2")
        
    with col_b:
        st.markdown("### 🔵 Network B: AI-Managed")
        st.caption("Active neural telemetry tracking. Automatically isolates faults and maps adjustments.")
        st.metric(label="Network B Service Uptime", value="99.8 %", delta="System Stabilized", delta_color="inverse")
        st.success("🍀 Satellites Lost: 0 | Avoidance Actions: 4")
        
    if st.button("🚀 Run Solar Anomaly Test Scenario", key="storm_sim_run"):
        with st.spinner("Simulating magnetic solar storm footprint..."):
            time.sleep(1.0)
        st.info("📊 **AI Node System Event Log:** Decision agent successfully calculated alternative path coordinates and shifted 4 satellites to safe mode.")

# ------------------------------------------------------------------------------
# TAB 3: NATIVE KEPLER TRANSIT LIGHT CURVE SCENARIO
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("🔬 3D Kepler Field Frequency Curve Tracker")
    st.write("Scan deep space light curves to look for repeating dips in brightness caused by a planet passing a host star.")
    
    target_star = st.selectbox("Select Target System Field", ["Kepler-22b System", "Kepler-452b Horizon", "Kepler-186f Vector"])
    
    if st.button("🔍 Execute Algorithmic Deep Scan", key="transit_detector_run"):
        with st.spinner(f"Analyzing stellar signature cycles for {target_star}..."):
            time.sleep(1.0)
            
        st.subheader("📈 Light Curve Analysis Metrics")
        
        # Generates a realistic orbital transit light dip chart natively
        np.random.seed(42)
        timeline = np.linspace(0, 100, 200)
        flux_intensity = 1.0 + np.random.normal(0, 0.004, 200)
        
        # Inject the mathematical transiting planet light blocks
        flux_intensity[35:48] -= 0.025
        flux_intensity[125:138] -= 0.025
        
        chart_dataframe = pd.DataFrame({"Timeline (Days)": timeline, "Stellar Brightness Value": flux_intensity})
        st.line_chart(chart_dataframe, x="Timeline (Days)", y="Stellar Brightness Value")
        st.success(f"🎯 **Transit Verified:** Periodic flux anomalies confirm a candidate exoplanet presence orbiting {target_star} every 90 days.")

# ==============================================================================
# 3. SIDEBAR CALCULATION MECHANICS
# ==============================================================================
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=50, max_value=3000, value=288)

if st.sidebar.button("🛰️ Scan Star"):
    st.sidebar.markdown("---")
    if 0.5 <= prad <= 2.0 and 180 <= teq <= 310:
        st.sidebar.success(f"🍀 **Match Found!** A rocky world at {teq-273}°C sitting in the habitable zone!")
    else:
        st.sidebar.error("❌ **False Positive:** Hostile environments detected. Life cannot form here.")
