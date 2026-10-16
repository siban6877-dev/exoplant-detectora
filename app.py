import streamlit as st
import requests

# Set up page configurations with a wide screen layout structure
st.set_page_config(
    page_title="Kepler Exoplanet Detector AI", 
    page_icon="🌌", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
#                 BULLETPROOF ANDROMEDA GALAXY VISUAL BACKGROUND OVERLAY
# ==============================================================================
st.markdown(
    """
    <style>
    /* Direct framework target properties inject your exact image asset reliably */
    [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background-image: linear-gradient(rgba(5, 7, 18, 0.8), rgba(8, 12, 28, 0.9)), 
                          url('https://upload.wikimedia.org/wikipedia/commons/9/98/Andromeda_Galaxy_%28with_h-alpha%29.jpg');
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: #e0e5f5 !important;
    }
    
    /* Make top navigation headers blend seamlessly without flat block colors */
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Premium Glassmorphism styling configuration for the Left Navigation Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(6, 10, 26, 0.95) !important;
        border-right: 2px solid rgba(0, 162, 255, 0.25);
        box-shadow: 5px 0px 25px rgba(0, 0, 0, 0.7);
    }
    
    /* Neon glow effect layout mapping for key title typography elements */
    h1 {
        color: #ffffff !important;
        text-shadow: 0px 0px 20px rgba(0, 162, 255, 0.8), 0px 0px 40px rgba(0, 80, 255, 0.4);
        font-weight: 800 !important;
        letter-spacing: 1px;
    }
    
    h2, h3 {
        color: #00d2ff !important;
        text-shadow: 0px 0px 10px rgba(0, 210, 255, 0.3);
        font-weight: 600 !important;
    }

    /* Transform native chat input box interface to look like an operational space helmet HUD */
    div[data-testid="stChatInput"] {
        background-color: rgba(12, 19, 44, 0.95) !important;
        border: 2px solid rgba(0, 210, 255, 0.5) !important;
        border-radius: 12px !important;
        box-shadow: 0px 0px 15px rgba(0, 210, 255, 0.3) !important;
    }

    /* Custom styles for metrics dashboards */
    div[data-testid="stMetricValue"] {
        color: #00ffcc !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
#                               MAIN APPLICATION HEADER
# ==============================================================================
st.title("🌌 Kepler Exoplanet Detector AI")
st.write("Welcome! This chatbot uses an open-access AI brain to discuss anything about space, astronomy, and exoplanets.")
st.write("---")

# 1. Setup Conversational Memory State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey! 👋 I am Kepler, your live space assistant. Ask me absolutely anything about exoplanets, space engineering, or black holes!"}
    ]

# Display historical messages in UI
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 2. Handle Live Dynamic Chat Input Stream
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
                
                # Fetching response via robust requests library 
                url = f"https://pollinations.ai{full_prompt}"
                response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
                
                if response.status_code == 200:
                    reply_text = response.text
                else:
                    reply_text = "My communication antenna is hazy right now. Try sending that query one more time!"
            except Exception as error:
                reply_text = "Connection error: Could not reach mission control. Please try again!"
            
            st.write(reply_text)
            
    st.session_state.messages.append({"role": "assistant", "content": reply_text})

# ==============================================================================
#                 SIDEBAR INPUT CONTROL INTERFACE (THE PLANET DETECTOR)
# ==============================================================================
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=50, max_value=3000, value=288)

if st.sidebar.button("🛰️ Scan Star"):
    st.sidebar.markdown("---")
    # Original baseline target decision conditions
    if 0.5 <= prad <= 2.0 and 180 <= teq <= 310:
        st.sidebar.success(f"🍀 **Match Found!** A rocky world at {teq-273}°C sitting in the habitable zone!")
    else:
        st.sidebar.error("❌ **False Positive:** Hostile environments detected. Life cannot form here.")
