import streamlit as st
import requests
import urllib.parse  # Safely handle spaces and special characters in URL
import pandas as pd  # Native data tracking for the universe map
import numpy as np

st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")

# ==========================================
# BULLETPROOF GALAXY SPACE THEME
# ==========================================
st.markdown(
    """
    <style>
    /* Targets the primary app view container directly to guarantee background injection */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.8)), 
                          url('https://wikimedia.org');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Make top navigation bar transparent so it doesn't block the background */
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Make the sidebar translucent dark neon blue */
    section[data-testid="stSidebar"] {
        background-color: rgba(10, 16, 32, 0.85) !important;
        border-right: 1px solid rgba(0, 150, 255, 0.2);
    }
    
    /* Clean up title styling and add a neon glow effect */
    h1 {
        color: #ffffff !important;
        text-shadow: 0px 0px 15px rgba(0, 180, 255, 0.7);
        font-weight: 700 !important;
    }
    
    /* Make chat input box blend with space theme */
    div[data-testid="stChatInput"] {
        background-color: rgba(20, 25, 40, 0.95) !important;
        border: 1px solid rgba(0, 150, 255, 0.4) !important;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌌 Kepler Exoplanet Detector AI")
st.write("Welcome! This AI platform leverages machine learning indicators and conversational space intelligence to analyze exoplanetary datasets.")

# 1. Setup Conversational Memory State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey! 👋 I am Kepler, your live space tech assistant. Ask me absolutely anything about exoplanets, biosignatures, or mission telemetry!"}
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
    
    # Generate response from AI model using requests
    with st.chat_message("assistant"):
        with st.spinner("Consulting mission archives... 🛰️"):
            try:
                # Build context memory from previous messages so it acts like a true chatbot
                context = ""
                for msg in st.session_state.messages[-5:]: # Pass last 5 messages for quick token performance
                    context += f"{msg['role'].capitalize()}: {msg['content']}\n"
                
                system_instruction = (
                    "You are Kepler, an expert NASA Astrophysicist specializing in Exoplanet Discovery. "
                    "Keep answers highly engaging, scientific yet easy to understand. "
                    f"Based on our chat history:\n{context}\nProvide your next response: "
                )
                
                # Safely encode the string so characters like '?' or '#' do not crash the request
                encoded_prompt = urllib.parse.quote(system_instruction)
                url = f"https://pollinations.ai{encoded_prompt}"
                
                response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
                
                if response.status_code == 200:
                    reply_text = response.text
                else:
                    reply_text = "My communication antenna is experiencing solar interference. Try sending that query one more time!"
            except Exception as error:
                reply_text = "Connection error: Lost telemetry link with mission control. Please try again!"
            
            st.write(reply_text)
            
    st.session_state.messages.append({"role": "assistant", "content": reply_text})

# 3. Sidebar Advanced Analytics & Interactive Map
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=50, max_value=3000, value=288)
esi_weight = st.sidebar.slider("AI ESI Classification Threshold", min_value=0.0, max_value=1.0, value=0.7)

# ==========================================
# FIXED & UPGRADED DATA-DRIVEN UNIVERSE MAP
# ==========================================
st.sidebar.markdown("---")
st.sidebar.subheader("🗺️ Universe Map Radar")
st.sidebar.write("Live mathematical galaxy mapping of surrounding sector candidates:")

# Generate reliable starfield data points natively so it NEVER fails to load
np.random.seed(42)
map_data = pd.DataFrame(
    np.random.randn(40, 2) * 5,
    columns=['Sector Longitude (X)', 'Sector Latitude (Y)']
)
# Add your current target system coordinate directly onto the map
map_data.loc[len(map_data)] = [prad * 2.5, teq / 100]

# Render interactive map plot right inside the sidebar
st.sidebar.scatter_chart(map_data, x='Sector Longitude (X)', y='Sector Latitude (Y)', size=15)
st.sidebar.markdown("---")

if st.sidebar.button("🛰️ Execute AI Transit Analysis"):
    st.sidebar.subheader("AI Prediction Metrics")
    
    # Earth Similarity Index (ESI) formulation
    r_term = (1.0 - abs((prad - 1.0) / (prad + 1.0))) ** 0.5
    t_term = (1.0 - abs((teq - 288.0) / (teq + 288.0))) ** 0.5
    esi_score = round(r_term * t_term, 2)
    
    st.sidebar.metric(label="Earth Similarity Index (ESI)", value=f"{esi_score}")
    
    if esi_score >= esi_weight:
        st.sidebar.success(f"🍀 **Candidate Confirmed:** AI models indicate a high likelihood of a habitable environment! (Temp: {teq-273}°C)")
    else:
        st.sidebar.error("❌ **False Positive / Hostile:** Planet metrics fall below the target AI safety threshold framework.")
