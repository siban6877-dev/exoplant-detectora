import streamlit as st
import requests

# 1. Page Configurations & Title
st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🪐", layout="wide")

# 2. INJECT DEEP SPACE BACKGROUND AND GLASS UI STYLING (CSS)
space_background_url = "https://unsplash.com"

st.markdown(
    f"""
    <style>
    /* Background Image setup */
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.75)), url("{space_background_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Force texts to be bright white and glowy */
    h1, h2, h3, p, span, label, div {{
        color: #ffffff !important;
        text-shadow: 0px 0px 4px rgba(0, 210, 255, 0.3);
    }}
    
    /* Make the left sidebar a dark sci-fi glass console */
    [data-testid="stSidebar"] {{
        background-color: rgba(10, 15, 30, 0.85) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(0, 210, 255, 0.2);
    }}
    
    /* Style inputs for a neon laboratory vibe */
    input, .stNumberInput div {{
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid rgba(0, 210, 255, 0.4) !important;
    }}
    
    /* Style Chat Containers */
    [data-testid="stChatMessage"] {{
        background-color: rgba(20, 30, 55, 0.6) !important;
        border-radius: 12px;
        border: 1px solid rgba(0, 210, 255, 0.15);
        margin-bottom: 10px;
        backdrop-filter: blur(5px);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🪐 Kepler Exoplanet Detector AI")
st.write("Welcome! This chatbot uses an open-access AI brain to discuss anything about space, astronomy, and exoplanets.")

# 3. Setup Conversational Memory State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Greetings, Explorer! 🌌 I am Kepler, your live space mission assistant. Ask me absolutely anything about exoplanets, space engineering, or black holes, and let's explore!"}
    ]

# Display historical messages in UI
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 4. Handle Live Dynamic Chat Input
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
                reply_text = f"Connection error: Could not reach mission control. Please try again!"
            
            st.write(reply_text)
            
    st.session_state.messages.append({"role": "assistant", "content": reply_text})

# 5. Sidebar Calculation Mechanics
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=50, max_value=3000, value=288)

if st.sidebar.button("🛰️ Scan Star"):
    st.sidebar.markdown("---")
    if 0.5 <= prad <= 2.0 and 180 <= teq <= 310:
        st.sidebar.sidebar_success = st.sidebar.success(f"🍀 **Match Found!** A rocky world at {teq-273}°C sitting in the habitable zone!")
    else:
        st.sidebar.sidebar_error = st.sidebar.error("❌ **False Positive:** Hostile environments detected. Life cannot form here.")
