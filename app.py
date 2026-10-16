GEMINI_API_KEY = st.secrets["GEMINI_KEY"]
import streamlit as st
from google import genai

st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")
st.title("🌌 Kepler Exoplanet Detector AI")
st.write("Welcome! This chatbot is powered by Google Gemini to discuss anything about space, astronomy, and exoplanets.")

# 1. Securely initialize the Gemini AI Client
# Replace the placeholder text below with your actual API key string inside the quotation marks
GEMINI_API_KEY = "PASTE_YOUR_API_KEY_HERE"

try:
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception as e:
    st.error("AI Brain Connection Error. Make sure your Gemini API Key is pasted correctly in the code!")

# 2. Setup Conversational Memory State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey! 👋 I am Kepler, a live AI space assistant. Ask me absolutely anything about exoplanets, space engineering, or mission timelines, and I will generate an answer for you!"}
    ]

# Display historical messages in UI
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 3. Handle Live Dynamic Chat Input
if user_input := st.chat_input("Ask Kepler anything about the universe..."):
    # Render user prompt
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate response from live LLM model
    with st.chat_message("assistant"):
        with st.spinner("Consulting mission archives... 🛰️"):
            try:
                # System prompt sets the personality and constraints for the AI
                system_instruction = (
                    "You are Kepler, an elite NASA astronomer chatbot helping middle school students. "
                    "Be friendly, conversational, explain complex space physics using simple terminology, "
                    "and handle any arbitrary space question accurately."
                )
                
                # Fetch output from gemini-2.5-flash
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input,
                    config={'system_instruction': system_instruction}
                )
                reply_text = response.text
            except Exception as error:
                reply_text = "Sorry, my deep space communication link failed. Double-check your API key configurations!"
            
            st.write(reply_text)
            
    st.session_state.messages.append({"role": "assistant", "content": reply_text})

# 4. Sidebar Calculation Mechanics
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=50, max_value=3000, value=288)

if st.sidebar.button("🛰️ Scan Star"):
    st.sidebar.markdown("---")
    if 0.5 <= prad <= 2.0 and 180 <= teq <= 310:
        st.sidebar.success(f"🍀 **Match Found!** A rocky world at {teq-273}°C sitting in the habitable zone!")
    else:
        st.sidebar.error("❌ **False Positive:** Hostile environments detected. Life cannot form here.")
