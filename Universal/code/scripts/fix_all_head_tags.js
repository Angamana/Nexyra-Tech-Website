const fs = require('fs');
const path = require('path');

const rootDir = 'C:\\Users\\angam\\Downloads\\Nexyra Website';

function getFiles(dir, files = []) {
    const fileList = fs.readdirSync(dir);
    for (const file of fileList) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            if (file !== 'tools' && file !== '.git') {
                getFiles(fullPath, files);
            }
        } else if (file.endsWith('.html')) {
            files.push(fullPath);
        }
    }
    return files;
}

const htmlFiles = getFiles(rootDir);

for (const filePath of htmlFiles) {
    let content = fs.readFileSync(filePath, 'utf8');

    // 1. Remove literal "`n" or "\n" artifacts inserted by powershell
    content = content.replace(/`n/g, '\n');

    // 2. Fix cookie-policy.css link if broken
    // Ensure cookie-policy.css link is cleanly on its own line after webflow css
    content = content.replace(/<link href="([^"]*sentrixa-template.webflow.shared[^"]*)" rel="stylesheet" type="text\/css"\/>[\s]*<link href="([^"]*cookie-policy.css") rel="stylesheet" type="text\/css"\/>/gi, (match, p1, p2) => {
        return `<link href="${p1}" rel="stylesheet" type="text/css"/>\n<link href="${p2}" rel="stylesheet" type="text/css"/>`;
    });

    // 3. Fix Favicon tags with URL encoded %20 for spaces
    const relFromRoot = path.relative(rootDir, filePath);
    const depth = relFromRoot.split(path.sep).length - 1;
    let prefix = '';
    for (let i = 0; i < depth; i++) {
        prefix += '../';
    }

    const encodedLogoPath = `${prefix}Universal/images/Nexyra%20Logo.png`;

    // Remove existing favicon/apple-touch-icon tags
    content = content.replace(/<link rel="(icon|shortcut icon|apple-touch-icon)"[^>]*>/gi, '');

    // Insert clean favicon tags right before </head>
    const faviconBlock = `
<link rel="icon" type="image/png" href="${encodedLogoPath}"/>
<link rel="shortcut icon" type="image/png" href="${encodedLogoPath}"/>
<link rel="apple-touch-icon" href="${encodedLogoPath}"/>
</head>`;

    content = content.replace(/<\/head>/i, faviconBlock);

    // Clean up any double blank lines
    content = content.replace(/\n\s*\n\s*\n/g, '\n\n');

    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Cleaned & fixed: ${relFromRoot}`);
}
