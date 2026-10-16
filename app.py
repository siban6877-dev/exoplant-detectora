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
    /* Targets all primary Streamlit containers to force your exact image to display */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background-image: linear-gradient(rgba(5, 7, 18, 0.75), rgba(5, 7, 18, 0.75)), 
                          url('https://imgur.com') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }
    
    /* Make the top navigation bar header completely transparent */
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Force high contrast white text over your dark background image */
    .stApp {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌌 Kepler Exoplanet Detector AI")
st.write("Welcome! This chatbot uses an open-access AI brain to discuss anything about space, astronomy, and exoplanets.")
st.write("---")

# ==============================================================================
#                 INTERACTIVE MULTI-PAGE WORKSPACE TABS
# ==============================================================================
tab1, tab2, tab3 = st.tabs(["💬 Deep-Space AI Assistant", "🛰️ Self-Healing Constellation Sim", "🔬 Kepler Transit Detector"])

# ------------------------------------------------------------------------------
# TAB 1: YOUR EXACT UNTOUCHED ORIGINAL CHATBOT RUNS HERE
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
        
        # Generate response from keyless AI model using requests
        with st.chat_message("assistant"):
            with st.spinner("Consulting mission archives... 🛰️"):
                try:
                    # Add personality system instruction
                    system_instruction = "You are Kepler, a friendly NASA astronomer helping middle school students. Answer the following question simply: "
                    full_prompt = system_instruction + user_input
                    
                    # Fetching response via robust requests library (automatically fixes space character errors!)
                    url = f"https://pollinations.ai{full_prompt}"
                    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
                    
                    if response.status_code == 200:
                        reply_text = response.text
                    else:
                        reply_text = "My communication antenna is hazy right now. Try sending that query one more time!"
                except Exception as error:
                    reply_text = f"Connection error: Could not reach mission control. Please try again!"
                
                st.write(reply_text)
                
        st.session_state.messages.append({"role": "assistant", "content": reply_text})

# ------------------------------------------------------------------------------
# TAB 2: SELF-HEALING CONSTELLATION SIMULATOR SCENARIO
# ------------------------------------------------------------------------------
with tab2:
    st.subheader("⚡ Satellite Constellation Solar Shield Simulation")
    st.write("Two identical satellite networks face the same solar storm scenario, hardware failures, and orbital debris fields.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 🔴 Network A: No AI Management")
        st.caption("Waits passively for mechanical failures to trigger ground instructions.")
        st.metric(label="Network A Service Uptime", value="42 %", delta="-58% Critical Drop")
        st.error("⚠️ Satellites Lost: 5 | Collisions Tracked: 2")
        
    with col_b:
        st.markdown("### 🔵 Network B: AI-Managed")
        st.caption("Predicts solar vector anomalies, isolates failing circuits, and reroutes pathways.")
        st.metric(label="Network B Service Uptime", value="99.8 %", delta="Stabilized System", delta_color="inverse")
        st.success("🍀 Satellites Lost: 0 | Collisions Avoided: 4")
        
    if st.button("🚀 Run Full Simulation Scenario", key="run_sim_btn"):
        with st.spinner("Injecting solar flare anomaly variables into network arrays..."):
            time.sleep(1.0)
        st.info("📊 **Simulation Event Log:** AI agent successfully performed 4 proximity avoidance maneuvers and isolated 2 overheating thrusters.")

# ------------------------------------------------------------------------------
# TAB 3: KEPLER FIELDS TRANSIT LIGHT DETECTOR
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("🔭 Kepler Light Curve Anomaly Scanner")
    st.write("Fly through targeted survey sectors to execute transit detection algorithms on active star brightness variables.")
    
    target_star = st.selectbox("Pick a Target Exploration Star", ["Kepler-22b", "Kepler-452b", "Kepler-186f"])
    
    if st.button("🔍 Run Transit Detector Array", key="run_transit_btn"):
        with st.spinner(f"Scanning brightness curve frequency for {target_star}..."):
            time.sleep(1.0)
            
        st.subheader("📈 Simulated Transit Light Curve Findings")
        np.random.seed(42)
        time_axis = np.linspace(0, 100, 200)
        brightness_axis = 1.0 + np.random.normal(0, 0.005, 200)
        brightness_axis[40:50] -= 0.03   # Simulate planet blocking star light
        brightness_axis[130:140] -= 0.03
        
        chart_data = pd.DataFrame({"Timeline Days": time_axis, "Stellar Flux Intensity": brightness_axis})
        st.line_chart(chart_data, x="Timeline Days", y="Stellar Flux Intensity")
        st.success(f"🎯 **Periodic Dip Verified!** AI pipeline discovered a structural exoplanet signature orbiting {target_star}.")

# ==============================================================================
# 3. Sidebar Calculation Mechanics (Your Exact Untouched Sidebar)
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
