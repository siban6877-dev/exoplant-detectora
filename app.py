import streamlit as st
import requests
import urllib.parse
import pandas as pd
import numpy as np
import plotly.graph_objects as go  # Delivers the high-end 3D map and 2D Orbit Tracker
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
        background-image: linear-gradient(rgba(4, 6, 14, 0.8), rgba(8, 10, 24, 0.9)), 
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

    /* Target the bottom-anchored chat input box wrapper specifically to fix styling layouts */
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

# Initialize Chat Messages State right at the top
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Awaiting commands, Commander. 👨‍🚀 I am Kepler, your live cosmic tech assistant. Ask me absolutely anything about exoplanets, biosignatures, or telemetry profiles!"
        }
    ]

# Layout distribution: Main Area holds header stats and your beautiful ORBIT MAP
col_main, col_stats = st.columns([2, 1.2])

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
#          HIGH-END 3D EXOPLANET VISITOR MAP WITH TEXTURE MESH SHADING
# ==============================================================================
st.sidebar.markdown("---")
st.sidebar.subheader("🔮 3D Exoplanet Tactical Surface Viewer")

u = np.linspace(0, 2 * np.pi, 60)
v = np.linspace(0, np.pi, 60)
u, v = np.meshgrid(u, v)

sphere_radius = float(prad * 0.8)
x_3d = sphere_radius * np.sin(v) * np.cos(u)
y_3d = sphere_radius * np.sin(v) * np.sin(u)
z_3d = sphere_radius * np.cos(v)

procedural_texture_map = np.sin(u * 5) * np.cos(v * 5) + np.sin(u * 2)

if teq < 200:
    planet_colorscale = "Ice"
elif teq <= 320:
    planet_colorscale = "YlGnBu"
else:
    planet_colorscale = "YlOrRd"

fig_3d = go.Figure(data=[go.Surface(
    x=x_3d, y=y_3d, z=z_3d, 
    surfacecolor=procedural_texture_map, 
    colorscale=planet_colorscale, 
    showscale=False,
    hoverinfo='none',
    lighting=dict(ambient=0.55, diffuse=0.8, roughness=0.4, specular=0.2)
)])

fig_3d.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    height=240,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(eye=dict(x=1.35, y=1.35, z=1.35))
    )
)

st.sidebar.plotly_chart(fig_3d, use_container_width=True, config={'displayModeBar': False})
st.sidebar.markdown("---")

# Calculate secondary variables based on physical telemetry variables
simulated_escape_velocity = round(float(11.2 * (prad ** 0.5)), 2)
simulated_solar_flux = round(float(((teq / 278.0) ** 4)), 3)

with col_stats:
    st.metric(label="Estimated Escape Velocity", value=f"{simulated_escape_velocity} km/s", delta="Earth Ref: 11.2 km/s")
    st.metric(label="Calculated Stellar Energy Flux", value=f"{simulated_solar_flux} x Earth", delta="-0.045 Flux Offset")

# ==============================================================================
#      NEW UPGRADE: EXPANDABLE 2D MISSION EXPLORER SYSTEM MAP (GOOGLY REPLICA)
# ==============================================================================
with col_main:
    st.subheader("🛰️ System Mission Explorer")
    st.caption("Live mathematical telemetry flight orbits showing targeted vector fields. Use the top-right button on the map to expand full-screen.")
    
    # Generate continuous circular track lines for the planets
    angles = np.linspace(0, 2 * np.pi, 200)
    
    fig_orbit = go.Figure()
    
    # Draw Orbit Rings (Gold tracks matching your reference image style)
    for r, name in zip([1.0, 1.8, 2.8], ["Venus Orbit", "Earth Orbit", "Exoplanet Orbit"]):
        fig_orbit.add_trace(go.Scatter(
            x=r * np.cos(angles), y=r * np.sin(angles),
            mode='lines', name=name,
            line=dict(color='rgba(212, 175, 55, 0.3)', width=1.5, dash='dash'),
            hoverinfo='skip'
        ))
        
    # Plot Space Objects (Sun, Venus, Earth, and Custom Target Candidate)
    # Exoplanet coordinates dynamically scale based on your user parameter sliders!
    exo_distance = 2.8 + (prad * 0.1)
    
    fig_orbit.add_trace(go.Scatter(x=[0], y=[0], mode='markers', name='Sun', marker=dict(color='#ff4500', size=24, shadow=dict(color='#ff8c00', blur=10))))
    fig_orbit.add_trace(go.Scatter(x=[0.7], y=[0.7], mode='markers+text', name='Venus', text=["Venus"], textposition="top center", marker=dict(color='#e3bb7b', size=10)))
    fig_orbit.add_trace(go.Scatter(x=[-1.3], y=[1.2], mode='markers+text', name='Earth', text=["Earth"], textposition="top center", marker=dict(color='#0096ff', size=12)))
    fig_orbit.add_trace(go.Scatter(
        x=[exo_distance * np.cos(1.2)], y=[exo_distance * np.sin(1.2)], 
        mode='markers+text', name='Target Candidate', text=["🎯 Kepler Target"], textposition="top center",
        marker=dict(color='#00ffcc', size=15)
    ))
    
    # Format map layout style to look identical to premium dark star system charts
    fig_orbit.update_layout(
        template="plotly_dark",
        margin=dict(l=10, r=10, t=10, b=10),
        height=380,
        paper_bgcolor="rgba(10, 16, 32, 0.75)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )
    
    # This enables the native interactive full-screen expandable bar buttons matching your screenshot!
    st.plotly_chart(fig_orbit, use_container_width=True, config={'displaylogo': False, 'modeBarButtonsWithText': ['toggleHover']})
    
    # Custom divider layout spacer
    st.markdown("<div class='cosmic-divider'></div>", unsafe_allow_html=True)
    
    # Chat History section sits cleanly directly below the main visual map panel area
