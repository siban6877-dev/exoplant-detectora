import streamlit as st
import requests

st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")

# ==============================================================================
#                 ANDROMEDA GALAXY BACKGROUND VISUAL THEME OVERLAY
# ==============================================================================
st.markdown(
    """
    <style>
    /* Force background onto the exact containers Streamlit relies on */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background-image: linear-gradient(rgba(5, 7, 18, 0.75), rgba(8, 12, 28, 0.85)), 
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
    
    /* Translucent glassmorphism sidebar menu matching your color palette */
    section[data-testid="stSidebar"] {
        background-color: rgba(6, 10, 26, 0.95) !important;
        border-right: 2px solid rgba(0, 162, 255, 0.25);
    }
    
    /* High-contrast styling for texts and titles */
    h1 {
        color: #ffffff !important;
        text-shadow: 0px 0px 15px rgba(0, 162, 255, 0.6);
    }
    
    div[data-testid="stChatInput"] {
        background-color: rgba(12, 19, 44, 0.95) !important;
        border: 2px solid rgba(0, 150, 255, 0.5) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌌 Kepler Exoplanet Detector AI")
st.write("Welcome! This chatbot uses an open-access AI brain to discuss anything about space, astronomy, and exoplanets.")

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

# 3. Sidebar Calculation Mechanics
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=50, max_value=3000, value=288)

if st.sidebar.button("🛰️ Scan Star"):
    st.sidebar.markdown("---")
    if 0.5 <= prad <= 2.0 and 180 <= teq <= 310:
        st.sidebar.success(f"🍀 **Match Found!** A rocky world at {teq-273}°C sitting in the habitable zone!")
    else:
        st.sidebar.error("❌ **False Positive:** Hostile environments detected. Life cannot form here.")
