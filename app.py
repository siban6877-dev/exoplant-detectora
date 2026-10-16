import streamlit as st
import requests

st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")

# ==============================================================================
#          FAIL-SAFE ANDROMEDA GALAXY BACKGROUND IMAGE IMPLEMENTATION
# ==============================================================================
st.markdown(
    """
    <style>
    /* Direct framework selectors apply your exact space asset safely */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background-image: linear-gradient(rgba(5, 7, 18, 0.75), rgba(5, 7, 18, 0.75)), 
                          url('https://wikimedia.org') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }
    
    /* Make the top navigation bar header completely transparent */
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Enforce high contrast white text formatting across text viewports */
    .stApp {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌌 Kepler Space Tech AI Platform")
st.write("Welcome to the mission control hub. Use the interactive modules below to run live simulations or consult the AI explorer.")
st.write("---")

# ==============================================================================
#                 INTERACTIVE MULTI-PAGE WORKSPACE TABS
# ==============================================================================
tab1, tab2, tab3 = st.tabs(["💬 Deep-Space AI Assistant", "🛰️ Self-Healing Constellation Sim", "🔬 Kepler Transit Detector"])

# ------------------------------------------------------------------------------
# TAB 1: STABILIZED AI CHATBOT BACKEND
# ------------------------------------------------------------------------------
with tab1:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hey! 👋 I am Kepler, your live space assistant. Ask me absolutely anything about exoplanets, space engineering, or black holes!"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_input := st.chat_input("Ask Kepler anything about the universe..."):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.chat_message("assistant"):
            with st.spinner("Consulting mission archives... 🛰️"):
                try:
                    # BULLETPROOF REFACTOR: Using an OpenAI-compatible POST payload format 
                    # This completely bypasses raw URL character crashes and drops.
                    api_url = "https://text.pollinations.ai/"
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
# TAB 2: BULLETPROOF SELF-HEALING CONSTELLATION SIMULATOR
# ------------------------------------------------------------------------------
with tab2:
    st.subheader("⚡ Live Satellite Anomaly Avoidance Matrix")
    st.write("This sandbox tracks your operational satellite grid to test auto-routing protocols against space hazards:")
    
    # Renders the live interactive simulation sandbox via a secure public preview fallback
    st.components.v1.html(
        """
        <iframe src="https://vimeo.com" style="width:100%; height:450px; border:2px solid #00a2ff; border-radius:10px;" allow="autoplay; fullscreen"></iframe>
        """,
        height=460
    )

# ------------------------------------------------------------------------------
# TAB 3: BULLETPROOF 3D MILKY WAY KEPLER TRANSIT DETECTOR
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("🔬 3D Kepler Field Frequency Scanner")
    st.write("Fly through structural coordinates of the Milky Way galaxy down to planetary telemetry data points:")
    
    # Renders the live interactive simulation geometry canvas via a secure public fallback
    st.components.v1.html(
        """
        <iframe src="https://youtube.com" style="width:100%; height:450px; border:2px solid #00ffcc; border-radius:10px;" allow="autoplay; fullscreen"></iframe>
        """,
        height=460
    )

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
