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
    
    // Replace Facebook Link
    content = content.replace(/href="https:\/\/www\.facebook\.com\/"/g, 'href="https://www.facebook.com/profile.php?id=61592497580105" target="_blank"');
    
    // Replace LinkedIn Link
    content = content.replace(/href="https:\/\/www\.linkedin\.com\/"/g, 'href="https://www.linkedin.com/in/nexyra-technologies-b47a8241a" target="_blank"');
    
    // Ensure target="_blank" is added to open in new tab if it doesn't already have it
    // Using simple replacement for the exact strings found in the footer
    
    fs.writeFileSync(file, content, 'utf-8');
    console.log(`Updated social links for ${file}`);
}
