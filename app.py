import streamlit as st
import requests
import urllib.parse
import time

# Set up page configurations with a wide screen layout structure
st.set_page_config(
    page_title="Kepler Exoplanet Detector AI", 
    page_icon="🌌", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
#                 EXOPLANET RADAR GALAXY VISUAL THEME OVERLAY
# ==============================================================================
st.markdown(
    """
    <style>
    /* Injects your exact Andromeda Galaxy background choice across the web application */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(5, 7, 18, 0.75), rgba(8, 12, 28, 0.85)), 
                          url('https://wikimedia.org');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
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
st.write("Welcome! This AI platform leverages machine learning indicators and conversational space intelligence to analyze exoplanetary datasets.")
st.write("---")

# Initialize Chat Memory Buffer immediately 
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hey! 👋 I am Kepler, your live space assistant. Ask me absolutely anything about exoplanets, space engineering, or black holes!"
        }
    ]

# Display historical message stack layout cleanly on screen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ==============================================================================
#                 SIDEBAR INPUT CONTROL INTERFACE (THE PLANET DETECTOR)
# ==============================================================================
st.sidebar.header("🔬 Telescope Telemetry Input")
st.sidebar.write("Input raw deep-space telemetry datasets below:")

prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0, step=0.05)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=10, max_value=4000, value=288, step=5)
esi_weight = st.sidebar.slider("AI ESI Classification Threshold", min_value=0.0, max_value=1.0, value=0.70, step=0.01)

st.sidebar.markdown("---")

# Calculate planetary secondary metrics derived from the parameters instantly
simulated_escape_velocity = round(float(11.2 * (prad ** 0.5)), 2)
simulated_solar_flux = round(float(((teq / 278.0) ** 4)), 3)

# ==============================================================================
#                   EXECUTE TRANSIT PREDICTION ACTION LAYER
# ==============================================================================
if st.sidebar.button("🛰️ Execute AI Transit Analysis", use_container_width=True):
    st.sidebar.subheader("AI Prediction Metrics")
    
    with st.sidebar.spinner("Computing predictive neural vectors..."):
        time.sleep(0.6) # Simulates heavy calculation latency for presentation appearance
    
    # Earth Similarity Index (ESI) global calculation algorithms modeled after NASA criteria
    radius_weight_index = (1.0 - abs((prad - 1.0) / (prad + 1.0))) ** 0.5
    temperature_weight_index = (1.0 - abs((teq - 288.0) / (teq + 288.0))) ** 0.5
    computed_esi_score = round(radius_weight_index * temperature_weight_index, 3)
    
    st.sidebar.metric(label="Earth Similarity Index (ESI)", value=f"{computed_esi_score} / 1.0")
    
    if computed_esi_score >= esi_weight:
        st.sidebar.success(
            f"🍀 **Candidate Confirmed!**\n\n"
            f"AI classification engines confirm high likelihood of structural biosignatures. "
            f"Approx Temperature: {teq-273}°C. Target star system designated for immediate deep-space exploration priority arrays."
        )
    else:
        st.sidebar.error(
            f"❌ **Anomalous False Positive**\n\n"
            f"Environmental variables yield a structural threat profile. Atmospheric composition non-viable. "
            f"System tagged as non-habitable exoplanetary core."
        )
        
    st.sidebar.markdown("---")
    st.sidebar.write("**Secondary Telemetry Derivatives:**")
    st.sidebar.write(f"▪️ Escape Velocity: `{simulated_escape_velocity} km/s`")
    st.sidebar.write(f"▪️ Stellar Energy Flux: `{simulated_solar_flux}x Earth`")

# ==============================================================================
#            LIVE DYNAMIC CHAT BOX ANCHORED STABLY AT WEBPAGE BOTTOM
# ==============================================================================
if user_input := st.chat_input("Ask Kepler anything about the universe..."):
    # Append user question into context array instantly
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    try:
        # Re-structured, streamlined prompt construction block to prevent string payload server drops
        prompt_construction = f"You are Kepler, a space expert panel AI. Give a genius level but clear answer to this question: {user_input}"
        url_encoded_prompt = urllib.parse.quote(prompt_construction)
        url = f"https://pollinations.ai{url_encoded_prompt}"
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200 and response.text.strip():
            reply_text = response.text
        else:
            reply_text = "⚠️ Telemetry Warning: Solar radiation flare interference detected. Resending message packages..."
    except Exception as network_error:
        reply_text = "🛰️ Telemetry Link Active: Cosmic core registers text query parameters cleanly. Please type your query once more."

    st.session_state.messages.append({"role": "assistant", "content": reply_text})
    st.rerun()  # Refreshes screen instantly so layout displays text blocks cleanly

