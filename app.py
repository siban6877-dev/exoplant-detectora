import streamlit as st
import requests
import urllib.parse
import pandas as pd
import numpy as np
import plotly.express as px  # Upgrades our radar grid map dramatically!
import time

# Set up page configurations with a wide screen monitor profile
st.set_page_config(
    page_title="Kepler Exoplanet Detector AI - DeepSpace Platform", 
    page_icon="🌌", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
#                      COMPETITION-GRADE ULTRA COSMIC CSS STYLING
# ==============================================================================
st.markdown(
    """
    <style>
    /* Absolute target background injection using a premium, robust Wikipedia Hubble asset */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(4, 6, 14, 0.75), rgba(8, 10, 24, 0.88)), 
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
        background-color: rgba(6, 10, 26, 0.92) !important;
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

    /* Transform native chat input block interface to look like an operational space helmet HUD */
    div[data-testid="stChatInput"] {
        background-color: rgba(12, 19, 44, 0.95) !important;
        border: 2px solid rgba(0, 210, 255, 0.5) !important;
        border-radius: 12px !important;
        box-shadow: 0px 0px 15px rgba(0, 210, 255, 0.2);
    }

    /* Custom styles for metrics dashboards */
    div[data-testid="stMetricValue"] {
        color: #00ffcc !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }
    
    /* Custom spacing dividers */
    .cosmic-divider {
        height: 2px;
        background: linear-gradient(90deg, rgba(0,210,255,0), rgba(0,210,255,1), rgba(0,210,255,0));
        margin: 25px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
#                               MAIN HEADER INTERFACE
# ==============================================================================
st.title("🌌 Kepler Space Tech Intelligence Dashboard")
st.write("---")

# Layout distribution: Split screen for interactive analytics vs Chat Core interface
col_main, col_stats = st.columns([3, 2])

with col_main:
    st.subheader("🛰️ AI Deep-Space Telecom Communication Hub")
    st.caption("Live low-latency uplink channel connected directly to Kepler AI Engine cluster via Pollinations Framework.")

    # 1. Setup Conversational Memory State
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": "Awaiting commands, Commander. 👨‍🚀 I am Kepler, your live space tech assistant. Ask me absolutely anything about exoplanets, biosignatures, transit curves, or mission telemetry parameters!"
            }
        ]

    # Display historical chat archive directly inside the window
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # 2. Handle Live Dynamic Chat Input Streamer
    if user_input := st.chat_input("Transmit parameters or queries to Kepler Engine Core..."):
        # Render user prompt locally
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generate responsive text strings utilizing memory injections
        with st.chat_message("assistant"):
            with st.spinner("Decoding cosmic background radiation signals... 📡"):
                try:
                    # SYSTEM INSTRUCTION REFIX: Keep it single-lined without prompt breaks so the raw URL string passes cleanly
                    system_instruction = (
                        f"You are Kepler, a space expert panel AI assistant. Answer this query cleanly without using markdown symbols: {user_input}"
                    )
                    
                    # URL safe translation compilation layer
                    encoded_prompt = urllib.parse.quote(system_instruction)
                    url = f"https://pollinations.ai{encoded_prompt}"
                    
                    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
                    
                    if response.status_code == 200:
                        reply_text = response.text
                    else:
                        reply_text = "⚠️ Telemetry Alert: Main antenna array experiencing severe magnetic solar flare noise. Request re-transmission."
                except Exception as error:
                    reply_text = "💥 Strategic Disconnect: Connection link timeout with main Deep Space Mission Control relay."
                
                st.write(reply_text)
                
        st.session_state.messages.append({"role": "assistant", "content": reply_text})

with col_stats:
    st.subheader("📊 Sector Live Instrumentation")
    st.write("Real-time automated astrophysical diagnostic modeling output vectors:")
    
    # Fast telemetry overview window displays to add professional context
    st.info("🛰️ **Active Orbit Profile**: Kepler Deep Field Sector 4\n\n🛰️ **Array Core Integrity**: 98.4%\n\n🛰️ **AI System Load**: Operational")
    st.markdown("<div class='cosmic-divider'></div>", unsafe_allow_html=True)
    
    st.subheader("🧮 Secondary Analytical Derivatives")
    st.caption("AI-derived algorithmic space metrics deduced instantly from your sidebar active properties:")

# ==============================================================================
#                      SIDEBAR CONFIGURATION AND INSTRUMENTATION
# ==============================================================================
st.sidebar.header("🔬 Telescope Telemetry Input")
st.sidebar.write("Input raw deep-space telemetry datasets below:")

prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.2, step=0.05)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=10, max_value=4000, value=265, step=5)
esi_weight = st.sidebar.slider("AI ESI Classification Threshold", min_value=0.0, max_value=1.0, value=0.75, step=0.01)

# ==============================================================================
#          DYNAMIC FIXED LIVE HIGH-LIGHTING PLOTLY RADAR MAP GENERATOR 
# ==============================================================================
st.sidebar.markdown("---")
st.sidebar.subheader("🗺️ Galaxy Coordinates Radar Grid")

# Seed configuration tracking to generate steady starfields that remain rigid
np.random.seed(1337)
starfield_count = 45

# Create background environment stars data
x_coords = np.random.uniform(-10.0, 10.0, starfield_count)
y_coords = np.random.uniform(-10.0, 10.0, starfield_count)
types = ["Background Star"] * starfield_count

# Dynamic point positioning calculated directly via current inputs
user_planet_x = float((prad - 1.2) * 5.0)
user_planet_y = float(((teq - 265) / 100.0) * 4.0)

# Build unified visual dataset frame
map_df = pd.DataFrame({
    'Sector X': np.append(x_coords, user_planet_x),
    'Sector Y': np.append(y_coords, user_planet_y),
    'Object Type': types + ["🎯 Target Candidate"]
})

# Generate interactive glowing chart via Plotly
fig = px.scatter(
    map_df, x='Sector X', y='Sector Y', color='Object Type',
    color_discrete_map={"Background Star": "#556285", "🎯 Target Candidate": "#00ffcc"},
    template="plotly_dark"
)

# Custom thematic adjustments to map background to hide grids and look like tactical radar
fig.update_layout(
    margin=dict(l=10, r=10, t=10, b=10),
    height=280,
    showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False, zeroline=True, zerolinewidth=1, zerolinecolor="rgba(0, 150, 255, 0.4)", showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=True, zerolinewidth=1, zerolinecolor="rgba(0, 150, 255, 0.4)", showticklabels=False)
)
fig.update_traces(marker=dict(size=map_df['Object Type'].map({"Background Star": 6, "🎯 Target Candidate": 14})))

# Render into UI container view
st.sidebar.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
st.sidebar.caption(f"🎯 Locked Target Location Vector: [X: {user_planet_x:.2f} | Y: {user_planet_y:.2f}]")
st.sidebar.markdown("---")

# Calculate secondary variables based on physical telemetry variables
simulated_escape_velocity = round(float(11.2 * (prad ** 0.5)), 2)
simulated_solar_flux = round(float(((teq / 278.0) ** 4)), 3)

# Render auxiliary data into the secondary columns right on screen canvas layout
with col_stats:
    st.metric(label="Estimated Escape Velocity", value=f"{simulated_escape_velocity} km/s", delta="Earth Ref: 11.2 km/s")
