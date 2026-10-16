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
            
            # Loads a stunning cosmic nebula image directly into the 3D space background canvas environment
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

            // Orbit controls handling smooth dragging
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.maxDistance = 1500;
            controls.minDistance = 50;

            // Generate cosmic star particle clusters layered over the space picture
            const geometry = new THREE.BufferGeometry();
            const vertices = [];
            const colors = [];

            for (let i = 0; i < 6000; i++) {
                vertices.push(THREE.MathUtils.randFloatSpread(2500));
                vertices.push(THREE.MathUtils.randFloatSpread(2500));
                vertices.push(THREE.MathUtils.randFloatSpread(2500));

                // Bright neon stars to stand out against the nebula image background
                const r = Math.random() * 0.4 + 0.6; // High red/white content
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
                starField.rotation.y += 0.00012; // Continuous elegant cosmic rotation drift
                starField.rotation.x += 0.00004;
                controls.update();
                renderer.render(scene, camera);
            }
            animateScene();

            // Handle browser changes smoothly inside Streamlit iframe windows
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
    
    # Render with explicit constraints to prevent window squishing
    components.html(threejs_universe_html, height=620, scrolling=False)
