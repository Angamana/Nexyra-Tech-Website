// preloader.js

const initPreloader = () => {
    // Prevent layout shift from scrollbar disappearing
    const scrollbarWidth = window.innerWidth - document.documentElement.clientWidth;
    document.body.style.paddingRight = `${scrollbarWidth}px`;

    // Inject HTML
    const overlay = document.createElement('div');
    overlay.id = 'preloader-overlay';
    overlay.innerHTML = `
        <div id="preloader-bg"></div>
        <div id="preloader-canvas-container"></div>
        <div id="preloader-text">Nexyra Tech</div>
    `;
    document.body.appendChild(overlay);
    document.body.classList.add('preloader-active');

    const container = document.getElementById('preloader-canvas-container');
    const textEl = document.getElementById('preloader-text');
    
    // Split text into individual spans for letter animation
    const textString = "Nexyra Tech";
    textEl.innerHTML = textString.split('').map(char => `<span style="opacity: 0; display: inline-block;">${char === ' ' ? '&nbsp;' : char}</span>`).join('');
    const chars = textEl.querySelectorAll('span');
    gsap.set(textEl, { opacity: 1 }); // Container visible, spans hidden

    // 1. Setup Scene, Camera, Renderer
    const scene = new THREE.Scene();
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    const aspect = window.innerWidth / window.innerHeight;
    const isMobile = window.innerWidth < 768;
    const d = isMobile ? 24 : 12; // Increase view volume on mobile so object fits horizontally
    const camera = new THREE.OrthographicCamera(-d * aspect, d * aspect, d, -d, 0.1, 1000);
    camera.position.set(0, 0, 25);

    // 2. Geometries (from logo3d.js)
    const extrudeSettings = { depth: 2, bevelEnabled: true, bevelSegments: 4, steps: 2, bevelSize: 0.1, bevelThickness: 0.1 };
    const createShape = (vertices) => {
        const shape = new THREE.Shape();
        shape.moveTo(vertices[0][0], vertices[0][1]);
        for (let i = 1; i < vertices.length; i++) { shape.lineTo(vertices[i][0], vertices[i][1]); }
        shape.lineTo(vertices[0][0], vertices[0][1]);
        return shape;
    };

    const rightLegVerts = [[2, 6.73], [2, -6.73], [5, -5], [5, 5]];
    const diagonalVerts = [[-5, 0.77], [-5, -2.69], [2, -6.73], [5, -5]];
    const topPieceVerts = [[-1, 5.0], [2, 3.27], [5, 5], [2, 6.73]];

    const rightLegGeom = new THREE.ExtrudeGeometry(createShape(rightLegVerts), extrudeSettings);
    const diagonalGeom = new THREE.ExtrudeGeometry(createShape(diagonalVerts), extrudeSettings);
    const topPieceGeom = new THREE.ExtrudeGeometry(createShape(topPieceVerts), extrudeSettings);

    // Vertex colors for diagonal
    const count = diagonalGeom.attributes.position.count;
    const colors = new Float32Array(count * 3);
    const pos = diagonalGeom.attributes.position.array;
    const colorLeft = new THREE.Color(0x050a1f); 
    const colorRight = new THREE.Color(0xffffff); 
    const tempColor = new THREE.Color();
    for (let i = 0; i < count; i++) {
        let t = Math.max(0, Math.min(1, (pos[i * 3] - (-5)) / (2 - (-5))));
        t = Math.pow(t, 0.8);
        tempColor.lerpColors(colorLeft, colorRight, t);
        colors[i * 3] = tempColor.r; colors[i * 3 + 1] = tempColor.g; colors[i * 3 + 2] = tempColor.b;
    }
    diagonalGeom.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    // Vertex colors for topPiece
    const topCount = topPieceGeom.attributes.position.count;
    const topColors = new Float32Array(topCount * 3);
    const topPos = topPieceGeom.attributes.position.array;
    const topColorLeft = new THREE.Color(0x4a5460); 
    for (let i = 0; i < topCount; i++) {
        let t = Math.max(0, Math.min(1, (topPos[i * 3] - (-1)) / (2 - (-1))));
        t = Math.pow(t, 0.8);
        tempColor.lerpColors(topColorLeft, colorRight, t);
        topColors[i * 3] = tempColor.r; topColors[i * 3 + 1] = tempColor.g; topColors[i * 3 + 2] = tempColor.b;
    }
    topPieceGeom.setAttribute('color', new THREE.BufferAttribute(topColors, 3));

    // Materials
    const silverMaterial = new THREE.MeshStandardMaterial({ color: 0xdce0e5, metalness: 0.2, roughness: 0.4, transparent: true, opacity: 0 });
    const navyMaterial = new THREE.MeshStandardMaterial({ vertexColors: true, metalness: 0.6, roughness: 0.3, transparent: true, opacity: 0 });

    // Solid Meshes
    const rightHalf = new THREE.Group();
    const rightLeg = new THREE.Mesh(rightLegGeom, silverMaterial); rightLeg.position.z = 0; rightHalf.add(rightLeg);
    const diagonal = new THREE.Mesh(diagonalGeom, navyMaterial); diagonal.position.z = -2; rightHalf.add(diagonal);
    const topPiece = new THREE.Mesh(topPieceGeom, navyMaterial); topPiece.position.z = -2; rightHalf.add(topPiece);

    const leftHalf = rightHalf.clone();
    leftHalf.rotation.z = Math.PI;
    leftHalf.position.z = -0.01;

    const gapOffset = 2.0; 
    rightHalf.position.x = gapOffset;
    leftHalf.position.x = -gapOffset;

    const solidLogoGroup = new THREE.Group();
    solidLogoGroup.add(rightHalf);
    solidLogoGroup.add(leftHalf);
    
    // Start solid group at normal size
    solidLogoGroup.scale.set(1.0, 1.0, 1.0);
    solidLogoGroup.position.y = 0;

    scene.add(solidLogoGroup);

    // Particle System
    function createParticlesFromGeometry(meshGeom, baseColor, particleCount, zOffset) {
        const posAttribute = meshGeom.getAttribute('position');
        const indices = meshGeom.getIndex() ? meshGeom.getIndex().array : null;
        const pos = posAttribute.array;
        
        const points = [];
        const cols = [];
        const colObj = new THREE.Color(baseColor);
        const hasColors = meshGeom.getAttribute('color');
        let colArr = hasColors ? meshGeom.getAttribute('color').array : null;

        for(let i=0; i<particleCount; i++) {
            let vA, vB, vC;
            if (indices) {
                const triIndex = Math.floor(Math.random() * (indices.length / 3)) * 3;
                vA = indices[triIndex] * 3; vB = indices[triIndex+1] * 3; vC = indices[triIndex+2] * 3;
            } else {
                const triIndex = Math.floor(Math.random() * (pos.length / 9)) * 9;
                vA = triIndex; vB = triIndex+3; vC = triIndex+6;
            }
            
            let r1 = Math.random(), r2 = Math.random();
            if (r1 + r2 > 1) { r1 = 1 - r1; r2 = 1 - r2; }
            let r3 = 1 - r1 - r2;
            
            points.push(
                r1 * pos[vA] + r2 * pos[vB] + r3 * pos[vC],
                r1 * pos[vA+1] + r2 * pos[vB+1] + r3 * pos[vC+1],
                (r1 * pos[vA+2] + r2 * pos[vB+2] + r3 * pos[vC+2]) + zOffset
            );
            
            if (hasColors) {
                cols.push(
                    r1 * colArr[vA] + r2 * colArr[vB] + r3 * colArr[vC],
                    r1 * colArr[vA+1] + r2 * colArr[vB+1] + r3 * colArr[vC+1],
                    r1 * colArr[vA+2] + r2 * colArr[vB+2] + r3 * colArr[vC+2]
                );
            } else {
                cols.push(colObj.r, colObj.g, colObj.b);
            }
        }
        
        const geom = new THREE.BufferGeometry();
        const scrambled = new Float32Array(points.length);
        for(let i=0; i<points.length; i+=3) {
            scrambled[i] = points[i] + (Math.random() - 0.5) * 2;
            scrambled[i+1] = points[i+1] + (Math.random() - 0.5) * 2;
            scrambled[i+2] = points[i+2] + (Math.random() - 0.5) * 2;
        }
        geom.setAttribute('position', new THREE.BufferAttribute(scrambled, 3));
        geom.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3));
        geom.setAttribute('targetPosition', new THREE.Float32BufferAttribute(points, 3));
        geom.setAttribute('scrambledPosition', new THREE.Float32BufferAttribute(scrambled, 3));
        
        const mat = new THREE.PointsMaterial({ size: 0.15, vertexColors: true, transparent: true, opacity: 0 });
        return new THREE.Points(geom, mat);
    }

    const particlesGroup = new THREE.Group();
    const rightLegParticles = createParticlesFromGeometry(rightLegGeom, 0xdce0e5, 3000, 0);
    const diagParticles = createParticlesFromGeometry(diagonalGeom, 0x050a1f, 3000, -2);
    const topParticles = createParticlesFromGeometry(topPieceGeom, 0x4a5460, 1000, -2);
    
    const pRightHalf = new THREE.Group();
    pRightHalf.add(rightLegParticles); pRightHalf.add(diagParticles); pRightHalf.add(topParticles);
    
    const pLeftHalf = pRightHalf.clone();
    pLeftHalf.rotation.z = Math.PI;
    pLeftHalf.position.z = -0.01;
    
    pRightHalf.position.x = gapOffset;
    pLeftHalf.position.x = -gapOffset;

    particlesGroup.add(pRightHalf);
    particlesGroup.add(pLeftHalf);
    
    // Scale particles to match initial solid state
    particlesGroup.scale.set(1.0, 1.0, 1.0);
    particlesGroup.position.y = 0;

    scene.add(particlesGroup);

    // Lighting
    scene.add(new THREE.AmbientLight(0xffffff, 0.6));
    const dirLight1 = new THREE.DirectionalLight(0xffffff, 1.2); dirLight1.position.set(-10, 15, 10); scene.add(dirLight1);
    const dirLight2 = new THREE.DirectionalLight(0x4353ff, 0.8); dirLight2.position.set(10, -10, 5); scene.add(dirLight2);
    const backLight = new THREE.DirectionalLight(0xffffff, 0.5); backLight.position.set(0, 0, -10); scene.add(backLight);

    let renderActive = true;
    let time = 0;
    const animate = () => {
        if(!renderActive) return;
        requestAnimationFrame(animate);

        // Continuous subtle rotation
        solidLogoGroup.rotation.y = Math.sin(time * 1.5) * 0.25; 
        solidLogoGroup.rotation.x = Math.sin(time * 1.0) * 0.1;  
        // position.y is handled by GSAP initially, we add the hover effect to the GSAP object or inner group
        
        particlesGroup.rotation.copy(solidLogoGroup.rotation);

        time += 0.01;
        renderer.render(scene, camera);
    };
    animate();

    // Resize handler
    window.addEventListener('resize', () => {
        const aspect = window.innerWidth / window.innerHeight;
        camera.left = -d * aspect;
        camera.right = d * aspect;
        camera.top = d;
        camera.bottom = -d;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // --- GSAP TIMELINE (11 seconds total) ---
    const tl = gsap.timeline();

    // 0s - 3.5s: Particles morph in
    const morphProgress = { val: 0 };
    tl.to(morphProgress, {
        val: 1,
        duration: 3.5,
        ease: "power2.inOut",
        onUpdate: () => {
            [rightLegParticles, diagParticles, topParticles].forEach(p => {
                const geom = p.geometry;
                const pos = geom.attributes.position.array;
                const target = geom.attributes.targetPosition.array;
                const scrambled = geom.attributes.scrambledPosition.array;
                for(let i=0; i<pos.length; i++) {
                    pos[i] = scrambled[i] + (target[i] - scrambled[i]) * morphProgress.val;
                }
                geom.attributes.position.needsUpdate = true;
                p.material.opacity = morphProgress.val; // Fade in
            });
        }
    }, 0);

    // 3.5s: Particles fade out, Solid fade in
    tl.to([rightLegParticles.material, diagParticles.material, topParticles.material], { opacity: 0, duration: 0.5 }, 3.5);
    tl.to([silverMaterial, navyMaterial], { opacity: 1, duration: 0.5 }, 3.5);

    // 3.5s - 4s: Object rests

    // 4s - 8s: Object splits, Text appears
    tl.to(rightHalf.position, { x: gapOffset + 12, duration: 4, ease: "power2.inOut" }, 4);
    tl.to(leftHalf.position, { x: -(gapOffset + 12), duration: 4, ease: "power2.inOut" }, 4);

    tl.to(chars, { 
        opacity: 1, 
        duration: 0.8, 
        stagger: {
            from: "center",
            amount: 1.0
        },
        ease: "power2.out" 
    }, 5.5);
    tl.to(textEl, { color: "#ffffff", duration: 4, ease: "power1.inOut" }, 5.5);

    // 8s - 11s: Transition to final positions and fizzle out
    // Need to calculate target screen positions
    tl.add(() => {
        // Calculate Navbar text target precisely
        const navBrandText = document.querySelector('.brand-logo span');
        const navRect = navBrandText.getBoundingClientRect();
        
        // Calculate 3D Container target
        const heroContainer = document.getElementById('logo-3d-container');
        const heroRect = heroContainer.getBoundingClientRect();

        // Animate Text to Navbar
        gsap.to(textEl, {
            top: navRect.top + navRect.height/2 + 1,
            left: (navRect.left + navRect.width/2) - 7,
            fontSize: '18px',
            duration: 3,
            ease: "power3.inOut"
        });

        // Animate 3D Object to Hero Container
        const targetX = (heroRect.left + heroRect.width/2) / window.innerWidth * 2 - 1;
        const targetY = -(heroRect.top + heroRect.height/2) / window.innerHeight * 2 + 1;
        
        // Bring halves back together slightly while moving
        gsap.to(rightHalf.position, { x: gapOffset, duration: 3, ease: "power3.inOut" });
        gsap.to(leftHalf.position, { x: -gapOffset, duration: 3, ease: "power3.inOut" });

        // Move the whole group to the container screen position
        const worldX = targetX * (d * aspect);
        const worldY = targetY * d;
        const targetScale = heroRect.height / window.innerHeight; // approximate scaling

        gsap.to(solidLogoGroup.position, {
            x: worldX,
            y: worldY,
            duration: 3,
            ease: "power3.inOut"
        });
        
        gsap.to(solidLogoGroup.scale, {
            x: targetScale,
            y: targetScale,
            z: targetScale,
            duration: 3,
            ease: "power3.inOut"
        });

        // Fade out blurry background
        const bg = document.getElementById('preloader-bg');
        gsap.to(bg, {
            opacity: 0,
            duration: 3,
            delay: 3.0,
            ease: "power2.inOut",
            onComplete: () => {
                // Remove preloader, show real elements
                overlay.remove();
                document.body.classList.remove('preloader-active');
                document.body.style.paddingRight = '';
                renderActive = false;
                
                // Allow logo3d.js to take over, it's already running behind the scenes.
            }
        });
    }, 8);
};

// Wait for fonts and scripts to load, then initialize
window.addEventListener('load', () => {
    if (sessionStorage.getItem('preloaderPlayed')) {
        return;
    }
    sessionStorage.setItem('preloaderPlayed', 'true');
    if (window.gsap && window.THREE) {
        initPreloader();
    } else {
        console.error("GSAP or THREE not found");
    }
});