const fs = require('fs');
const path = require('path');

const rootDir = 'C:\\Users\\angam\\Downloads\\Nexyra Website';

function getFiles(dir, files = []) {
    const fileList = fs.readdirSync(dir);
    for (const file of fileList) {
        const name = `${dir}/${file}`;
        if (fs.statSync(name).isDirectory()) {
            getFiles(name, files);
        } else if (name.endsWith('.html')) {
            files.push(name);
        }
    }
    return files;
}

const htmlFiles = getFiles(rootDir);

for (const file of htmlFiles) {
    if(file.includes('Cookie System')) continue;

    let content = fs.readFileSync(file, 'utf-8');
    
    // Replace Instagram Link
    content = content.replace(/href="https:\/\/www\.instagram\.com\/flowcubdesign"/g, 'href="https://www.instagram.com/nexyratechnologies?igsh=ank4czlhd3d4cmUz&utm_source=qr" target="_blank"');
    
    fs.writeFileSync(file, content, 'utf-8');
    console.log(`Updated Instagram link for ${file}`);
}
