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
    
    // Replace X Link (usually just https://x.com/ in the current markup)
    content = content.replace(/href="https:\/\/x\.com\/"/g, 'href="https://x.com/nexyra_tech?s=11" target="_blank"');
    
    fs.writeFileSync(file, content, 'utf-8');
    console.log(`Updated Twitter link for ${file}`);
}
