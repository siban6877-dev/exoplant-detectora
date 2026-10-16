import streamlit as st
import requests
import streamlit.components.v1 as components

# 1. Page Settings Configuration
st.set_page_config(page_title="Kepler Exoplanet Detector", page_icon="🌌", layout="wide")

# 2. Split Screen Layout (Left Column for AI Chat, Right Column for Space Map Simulator)
left_col, right_col = st.columns([1, 1.2], gap="large")

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

# 4. Inject Smooth 3D WebGL Space Map Simulation into the Right Column
with right_col:
    st.subheader("🪐 Live Interstellar Navigation System")
    st.caption("Left-click and drag to rotate. Scroll to zoom in/out of star systems.")
    
    threejs_universe_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cloudflare.com"></script>
        <script src="https://jsdelivr.net"></script>
        <style>
            html, body { margin: 0; padding: 0; overflow: hidden; background-color: #060713; width: 100%; height: 100%; }
            canvas { display: block; border-radius: 12px; }
        </style>
    </head>
    <body>
        <div id="canvas-container" style="width: 100vw; height: 600px;"></div>
        <script>
            const container = document.getElementById('canvas-container');
            const width = container.clientWidth || 600;
            const height = 600;

            const scene = new THREE.Scene();
            
            // Background cosmic image configuration
            const textureLoader = new THREE.TextureLoader();
            textureLoader.load(
                'https://unsplash.com', 
                function(texture) {
                    scene.background = texture;
                }
            );

            const camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 4000);
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            
            renderer.setSize(width, height);
            container.appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.maxDistance = 1500;
            controls.minDistance = 50;

            const geometry = new THREE.BufferGeometry();
            const vertices = [];
            const colors = [];

            for (let i = 0; i < 6000; i++) {
                vertices.push(THREE.MathUtils.randFloatSpread(2500));
                vertices.push(THREE.MathUtils.randFloatSpread(2500));
                vertices.push(THREE.MathUtils.randFloatSpread(2500));

                const r = Math.random() * 0.4 + 0.6;
                const g = Math.random() * 0.5 + 0.5; 
                const b = 1.0;
                colors.push(r, g, b);
            }

            geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
            geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

            const material = new THREE.PointsMaterial({
                size: 3.5,
                vertexColors: true,
                transparent: true,
                opacity: 0.95,
                sizeAttenuation: true
            });

            const starField = new THREE.Points(geometry, material);
            scene.add(starField);

            camera.position.z = 900;

            function animateScene() {
                requestAnimationFrame(animateScene);
                starField.rotation.y += 0.00012;
                starField.rotation.x += 0.00004;
                controls.update();
                renderer.render(scene, camera);
            }
            animateScene();

            window.addEventListener('resize', () => {
                const newWidth = container.clientWidth || 600;
                camera.aspect = newWidth / height;
                camera.updateProjectionMatrix();
                renderer.setSize(newWidth, height);
            });
        </script>
    </body>
    </html>
    """
    
    components.html(threejs_universe_html, height=620, scrolling=False)
