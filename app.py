import streamlit as st
import json
import urllib.request

st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")
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
    
    # Generate response from keyless AI model
    with st.chat_message("assistant"):
        with st.spinner("Consulting mission archives... 🛰️"):
            try:
                # Constructing a clean prompt text
                system_instruction = "You are Kepler, a friendly NASA astronomer helping middle school students. Answer the following question simply: "
                full_prompt = system_instruction + user_input
                
                # Connect to a free open-access server
                url = f"https://pollinations.ai{urllib.parse.quote(full_prompt)}"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                
                with urllib.request.urlopen(req) as response:
                    reply_text = response.read().decode('utf-8')
            except Exception as error:
                reply_text = "Sorry, my deep space communication link encountered an error. Try asking again!"
            
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
