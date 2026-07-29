// logo3d.js - The continuous 3D logo animation after the preloader finishes

document.addEventListener('DOMContentLoaded', () => {
    const heroContainer = document.getElementById('logo-3d-container');
    if(!heroContainer) return;

    const sceneLogo = new THREE.Scene();
    const cameraLogo = new THREE.PerspectiveCamera(45, heroContainer.clientWidth / heroContainer.clientHeight, 0.1, 100);
    cameraLogo.position.z = 12;

    const rendererLogo = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    rendererLogo.setSize(heroContainer.clientWidth, heroContainer.clientHeight);
    rendererLogo.setPixelRatio(window.devicePixelRatio);
    heroContainer.appendChild(rendererLogo.domElement);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6); 
    sceneLogo.add(ambientLight);
    const dirLight1 = new THREE.DirectionalLight(0xffffff, 1.2); 
    dirLight1.position.set(-10, 15, 10);
    sceneLogo.add(dirLight1);
    const dirLight2 = new THREE.DirectionalLight(0x4353ff, 0.8);
    dirLight2.position.set(10, -10, 5);
    sceneLogo.add(dirLight2);
    const backLight = new THREE.DirectionalLight(0xffffff, 0.5); 
    backLight.position.set(0, 0, -10); 
    sceneLogo.add(backLight);

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

    const silverMaterial = new THREE.MeshStandardMaterial({ color: 0xdce0e5, metalness: 0.2, roughness: 0.4 });
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
    const navyMaterial = new THREE.MeshStandardMaterial({ vertexColors: true, metalness: 0.6, roughness: 0.3 });

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

    // Responsive scale logic based on the perfected PC size (0.3921)
    function getScaleFactor() {
        const baseScale = 0.3921;
        if (window.innerWidth < 768) return baseScale * 0.65; // Mobile
        if (window.innerWidth < 1024) return baseScale * 0.85; // Tablet
        return baseScale; // PC
    }

    solidLogoGroup.scale.set(getScaleFactor(), getScaleFactor(), getScaleFactor());
    sceneLogo.add(solidLogoGroup);

    let mouseX = 0; let mouseY = 0;
    let isDragging = false;

    document.addEventListener('mousedown', () => {
        isDragging = true;
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
        // Snap back to center when released
        mouseX = 0;
        mouseY = 0;
    });

    document.addEventListener('mousemove', (e) => {
        if (isDragging) {
            mouseX = (e.clientX / window.innerWidth) * 2 - 1;
            mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
        }
    });

    const clockLogo = new THREE.Clock();
    function animateLogo() {
        requestAnimationFrame(animateLogo);
        const time = clockLogo.getElapsedTime();
        // Gentle wobble + mouse tracking
        const targetY = Math.sin(time * 1.5) * 0.15 + mouseX * 0.5;
        solidLogoGroup.rotation.y += (targetY - solidLogoGroup.rotation.y) * 0.05;
        solidLogoGroup.rotation.x += (mouseY * 0.5 - solidLogoGroup.rotation.x) * 0.05;
        
        // Idle floating animation
        solidLogoGroup.position.y = Math.sin(time * 2.5) * 0.05;
        
        rendererLogo.render(sceneLogo, cameraLogo);
    }
    animateLogo();

    window.addEventListener('resize', () => {
        cameraLogo.aspect = heroContainer.clientWidth / heroContainer.clientHeight;
        cameraLogo.updateProjectionMatrix();
        rendererLogo.setSize(heroContainer.clientWidth, heroContainer.clientHeight);
        
        // Update scale on resize
        const newScale = getScaleFactor();
        solidLogoGroup.scale.set(newScale, newScale, newScale);
    });
});
