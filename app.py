import streamlit as st

st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")
st.title("🌌 Kepler Exoplanet Detector AI")
st.write("Welcome! Chat with Kepler, your conversational AI assistant, to discover and evaluate alien worlds.")

# 1. Initialize Memory for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey there! 👋 I am Kepler, your space exploration AI. I can analyze telescope data or just chat about space problems. What's on your mind?"}
    ]

# 2. Display Chat Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 3. Handle Conversational User Input
if user_input := st.chat_input("Ask Kepler anything... (e.g., 'How long would it take to fly to an exoplanet?')"):
    # Display user's text
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # AI Understanding Logic (Natural Language Responses)
    user_query = user_input.lower()
    
    if "how long" in user_query or "time" in user_query or "travel" in user_query:
        reply = "Great question! Even the closest exoplanet (Proxima Centauri b) is about 4.2 light-years away. If we traveled in our fastest current spacecraft (like the Voyager probe going 38,000 mph), it would take us roughly **73,000 years** to get there! This is why space travel is a massive problem we are trying to solve."
    
    elif "live" in user_query or "habitable" in user_query or "water" in user_query:
        reply = "To live on an exoplanet, it needs to be in the **Goldilocks Zone**—not too hot, and not too cold. It needs a rocky surface and a protective atmosphere to hold liquid water. Right now, we use AI data metrics like planetary radius (`koi_prad`) to narrow down which ones are safe to explore!"
        
    elif "what do you do" in user_query or "help" in user_query or "how to use" in user_query:
        reply = "I'm a smart filter! You can use the control panel in the left sidebar to input space numbers (like planet size and temperature). I'll calculate the telemetry and classify the world for you instantly!"
        
    elif "hello" in user_query or "hi" in user_query or "hey" in user_query:
        reply = "Hey! Ready to hunt for some alien worlds today? Ask me a space question or try scanning a star using the sidebar menu!"
        
    else:
        # Fallback response that shows the AI is engaged and listening
        reply = f"I hear you! You're asking about '{user_input}'. While I'm still learning down here at mission control, my core job is calculating stellar data. Try testing my scanning sensors in the left sidebar or asking me about travel times across galaxies!"

    # Display AI reply
    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

# 4. Sidebar Controls (Keeps your scanning tools active!)
st.sidebar.header("🔬 Telescope Telemetry Input")
prad = st.sidebar.number_input("Planetary Radius (Earth Sizes)", min_value=0.1, max_value=50.0, value=1.0)
teq = st.sidebar.number_input("Planet Temperature (Kelvin)", min_value=50, max_value=3000, value=288)

if st.sidebar.button("🛰️ Scan Star"):
    st.sidebar.markdown("---")
    if 0.5 <= prad <= 2.0 and 180 <= teq <= 310:
        st.sidebar.success(f"🍀 **Match Found!** A rocky world at {teq-273}°C. It can hold liquid water!")
    else:
        st.sidebar.error("❌ **False Positive:** This world's extreme environment cannot support life.")
