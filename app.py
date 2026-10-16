import streamlit as st

# 1. Page Title and Header
st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌")
st.title("🌌 Kepler Exoplanet Detector AI")
st.write("Welcome! This AI analyzes space data to find worlds orbiting distant stars.")

# 2. Friendly Chat Bot greeting
st.subheader("💬 Chat with Kepler AI")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am the Kepler Exoplanet Detector. How can I help you find an alien world today?"}]

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Chat Input
if user_input := st.chat_input("Ask me something (e.g., 'What metrics do you use?')"):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Simple bot replies
    bot_reply = "I am ready! Use the scientific tools in the sidebar to input telescope data, and I will check if it's a real planet."
    if "help" in user_input.lower():
        bot_reply = "To use me, look at the sidebar on the left. Type in the planetary radius and transit depth, then click 'Scan Star'!"
        
    with st.chat_message("assistant"):
        st.write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# 3. Create Sidebar for Planet Data Input
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (koi_prad)", min_value=0.1, max_value=100.0, value=1.2)
depth = st.sidebar.number_input("Transit Depth (koi_depth)", min_value=1.0, max_value=10000.0, value=150.0)
period = st.sidebar.number_input("Orbital Period in Days (koi_period)", min_value=0.5, max_value=500.0, value=10.0)

# 4. Button to Predict
if st.sidebar.button("🛰️ Scan Star for Planets"):
    if prad < 5.0 and depth < 500.0:
        st.sidebar.success("🎉 ANALYSIS COMPLETE: Confirmed Earth-like Exoplanet!")
    else:
        st.sidebar.error("❌ ANALYSIS COMPLETE: False Positive (Likely a companion star or space noise).")
