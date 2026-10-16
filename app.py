import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")

# 2. Side-by-Side Screen Column Split (Left side: 45%, Right side: 55%)
left_col, right_col = st.columns([1, 1.2], gap="large")

# ==========================================
# LEFT COLUMN: YOUR WORKING AI CHATBOT LOOP
# ==========================================
with left_col:
    st.title("🌌 Kepler Exoplanet Detector AI")
    st.write("Welcome! This chatbot uses an open-access AI brain to discuss anything about space, astronomy, and exoplanets.")

    # Setup Conversational Memory State
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hey! 👋 I am Kepler, your live space assistant. Ask me absolutely anything about exoplanets, space engineering, or black holes!"}
        ]

    # Display historical messages in UI
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Handle Live Dynamic Chat Input
    if user_input := st.chat_input("Ask Kepler anything about the universe..."):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.chat_message("assistant"):
            with st.spinner("Consulting mission archives... 🛰️"):
                try:
                    system_instruction = "You are Kepler, a friendly NASA astronomer helping middle school students. Answer the following question simply: "
                    full_prompt = system_instruction + user_input
                    
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

# ==========================================
# SIDEBAR CONTROL PANEL MECHANICS
# ==========================================
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=50, max_value=3000, value=288)

if st.sidebar.button("🛰️ Scan Star"):
    st.sidebar.markdown("---")
    if 0.5 <= prad <= 2.0 and 180 <= teq <= 310:
        st.sidebar.success(f"🍀 **Match Found!** A rocky world at {teq-273}°C sitting in the habitable zone!")
    else:
        st.sidebar.error("❌ **False Positive:** Hostile environments detected. Life cannot form here.")

# ==========================================
# RIGHT COLUMN: STATIC IMAGING PANEL
# ==========================================
with right_col:
    st.subheader("🪐 Observable Observable Universe Map")
    
    # Streams a crisp, high-res deep space observatory overview photo directly
    space_map_image_url = "https://unsplash.com"
    
    st.image(
        space_map_image_url, 
        caption="Cosmic Deep Field Matrix Mapping Sector", 
        use_container_width=True
    )
