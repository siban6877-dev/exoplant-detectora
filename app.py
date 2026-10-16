import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Kepler Universe Engine",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sidebar Filters (Emulating your original parameters cleanly)
st.sidebar.title("🛸 System Diagnostics")
st.sidebar.markdown("Use these parameters to tune the universe visualization matrix.")

radius = st.sidebar.slider("Planetary Radius (Earth Sizes)", 0.1, 10.0, 1.0)
temp = st.sidebar.slider("Planet Temperature (Kelvin)", 50, 2000, 288)

st.sidebar.info(f"Current Matrix Targets:\nRadius: {radius}x | Temp: {temp}K")

# 3. Main Interface Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.title("🪐 Kepler Detector AI")
    st.markdown("---")
    
    # Static mockup placeholder of your chatbot to avoid state interference
    st.chat_message("assistant").write("Hello! I am Kepler, your live space assistant. Ask me anything about the mapped particles!")
    user_query = st.text_input("Ask Kepler anything about the universe...", key="new_map_chat_input")
    
    if user_query:
        st.chat_message("user").write(user_query)
        st.chat_message("assistant").write(f"Analyzing cosmic map cluster nodes for query variables matching: '{user_query}'...")

with col2:
    st.subheader("🌌 Live 3D Interstellar Simulation")
    
    # Embedded interactive 3D container using hardware acceleration
    threejs_universe_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cloudflare.com"></script>
        <script src="https://jsdelivr.net"></script>
        <style>
            body { margin: 0; overflow: hidden; background-color: #0b0c10; }
            canvas { width: 100%; height: 100%; display: block; }
        </style>
    </head>
    <body>
        <script>
            // Setup scene elements
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(60, window.innerWidth / 650, 0.1, 3000);
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            
            renderer.setSize(window.innerWidth, 650);
            document.body.appendChild(renderer.domElement);

            // Camera interaction controls
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.maxDistance = 1200;
            controls.minDistance = 100;

            // Generate field of stars
            const geometry = new THREE.BufferGeometry();
            const vertices = [];
            const colors = [];

            for (let i = 0; i < 8000; i++) {
                // Random position vectors
                vertices.push(THREE.MathUtils.randFloatSpread(2000));
                vertices.push(THREE.MathUtils.randFloatSpread(2000));
                vertices.push(THREE.MathUtils.randFloatSpread(2000));

                // Vary color shifts between deep blues, cyans and purples
                colors.push(Math.random() * 0.3, Math.random() * 0.7 + 0.3, 1.0);
            }

            geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
            geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

            const material = new THREE.PointsMaterial({
                size: 2.5,
                vertexColors: true,
                transparent: true,
                opacity: 0.85,
                sizeAttenuation: true
            });

            const starField = new THREE.Points(geometry, material);
            scene.add(starField);

            camera.position.z = 800;

            // Smooth background continuous animation sequence loop
            function renderLoop() {
                requestAnimationFrame(renderLoop);
                starField.rotation.y += 0.0002;
                starField.rotation.x += 0.0001;
                controls.update();
                renderer.render(scene, camera);
            }
            renderLoop();

            // Screen sizing adaptive mechanics
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / 650;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, 650);
            });
        </script>
    </body>
    </html>
    """
    
    components.html(threejs_universe_html, height=660, scrolling=False)
